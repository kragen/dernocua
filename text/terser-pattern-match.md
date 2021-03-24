Reading EOPL I enountered their `variant-case` structure.  The idea is
that if you have, say, a tree made out of `interior` records and
`leaf` records defined as (p. 80, §3.4.1)

    (define-record interior (symbol left-tree right-tree))
    (define-record leaf (number))

then you can define, say (p. 81, §3.4.2, slightly tweaked):

    (define (leaf-sum tree)
      (variant-case tree
         (leaf (number) number)
         (interior (left-tree right-tree)
           (+ (leaf-sum left-tree) (leaf-sum right-tree)))
         (else (error "leaf-sum: Invalid tree" tree))))

This is pretty closely analogous to polymorphic variants in OCaml,
except that the fields are named; in the last case, the `symbol` field
is unused and so not mentioned.  In OCaml we can define this without
defining the record types first, but the fields are named only
positionally:

    # let rec leaf_sum = function `Leaf n -> n | `Interior (_, left, right) -> leaf_sum left + leaf_sum right ;;
    val leaf_sum : ([< `Interior of 'b * 'a * 'a | `Leaf of int ] as 'a) -> int =
      <fun>
    # leaf_sum (`Interior (`Leaf 4, `Interior (`Leaf 5, `Leaf 6)));;
    Characters 9-60:
      leaf_sum (`Interior (`Leaf 4, `Interior (`Leaf 5, `Leaf 6)));;
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Error: This expression has type
             [> `Interior of
                  [> `Leaf of int ] *
                  [> `Interior of [> `Leaf of int ] * [> `Leaf of int ] ] ]
           but an expression was expected of type
             [< `Interior of 'b * 'a * 'a | `Leaf of int ] as 'a
           Types for tag `Interior are incompatible
    # leaf_sum (`Interior ("foo", `Leaf 4, `Interior ("bar", `Leaf 5, `Leaf 6)));;
    - : int = 15

The type inferred is not actually fully general, because it requires
the type for a given tag to be consistent:

    # leaf_sum (`Interior ("foo", `Leaf 4, `Interior (3.14, `Leaf 5, `Leaf 6)));;
    Characters 9-73:
      leaf_sum (`Interior ("foo", `Leaf 4, `Interior (3.14, `Leaf 5, `Leaf 6)));;
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    Error: This expression has type
             [> `Interior of
                  string *
                  ([< `Interior of string * 'a * 'a | `Leaf of int > `Leaf ]
                   as 'a) *
                  [> `Interior of float * [> `Leaf of int ] * [> `Leaf of int ] ] ]
           but an expression was expected of type 'a
           Types for tag `Interior are incompatible

Usually you have more than one function operating on a given type, so
it occurred to me that the Scheme code is somewhat redundant; as long
as it’s only dispatching on record types, it could be written as follows:

    (define (leaf-sum tree)
      (variant-case tree
         (leaf number)
         (interior (+ (leaf-sum left-tree) (leaf-sum right-tree)))
         (else (error "leaf-sum: Invalid tree" tree))))

Moreover the `error` could be implicit as it is in OCaml.

This way of doing things requires you to name your fields in a type
declaration, and only accommodates the simplest pattern-matches, but
those are nevertheless the most commonly used ones.  (It also has the
disadvantage that adding fields to a record type could silently change
the meaning of existing code, instead of just breaking it as it
normally does.)  So you could imagine saying, for example:

    a tree:
        a leaf:
            n: int
        a interior:
            sym: symbol
            left-tree: tree
            right-tree: tree

    to leaf-sum:
        on leaf:
            n
        on interior:
            leaf-sum left-tree + leaf-sum right-tree

Pointer-bit variant discrimination
----------------------------------

Another vaguely related pattern-matching note is that if your record
types are all non-polymorphic sum types like the above, and you do
full type erasure, as is normal in ML, then in most cases you can get
away with discriminating them entirely with pointer tag bits, avoiding
embedding a tag field in the record itself.  `tree` above, for
example, needs only one tag bit, to distinguish `leaf` from
`interior`; very many such sum types need only 2–4.  You could provide
an “overflow tag”, say, when all the pointer-tag bits are 1, which
indicates that the record does indeed contain a tag field further
discriminates the record type, but only types with 8 or more variants
will need it if your pointers are 64-bit aligned.

Here are the last few sum types I defined.  These are from porting
μKanren to OCaml:

    type var = Var of Index.t (* the index is a counter typically from call_fresh *)
    type term = Vart of var | Const of int | Pair of term * term
    type 'a stream = Cons of 'a * 'a stream | Thunk of (unit -> 'a stream) | Mzero
    type state = State of env * Index.t (* index of the next variable to create *)

This is from an incomplete port of COMFY-65 to OCaml; the real type
would have about five more variants:

    type ast = If of ast * ast * ast | Not of ast | Seq of ast list | Const of int

This is also sort of an example:

    type num = Int of int | Float of float
    type expr = Sum of expr * expr | Product of expr * expr | Const of num

This was also sort of an example:

    type test_item = Hematocrit of int | Creatinine of float | Glucose of int
    type test_items = EmptyTest | TestCons of test_item * test_items
    type test = Test of (int * float * test_items)
    type int_tag = HematocritT | GlucoseT
    type float_tag = CreatinineT
    type by_type_tag = EmptyBTT
                     | BTTConsInt of (int_tag * int * by_type_tag)
                     | BTTConsFloat of (float_tag * float * by_type_tag)
    type int_item = HematocritI | GlucoseI
    type float_item = CreatinineI
    type item = IntItem of int_item * int | FloatItem of float_item * float
    type maps_test = MTest of (int IntMap.t * float FloatMap.t)
      type item = Int of K.int_key * int
                | Float of K.float_key * float
      type int_key = Hematocrit | Glucose
      type float_key = Creatinine

This was from Neel Krishnaswami:

    type 'a exp =
      | Var of string
      | App of 'a exp * 'a exp
      | Lam of string * 'a 

This is a regular expression engine, based on a remark by Dave Long,
which I cut down to use polymorphic variants in order to minimize the
amount of code:

    let rec any = function `N -> false | `C (h, t) -> h || any (t ())
    and map f = function `N -> `N | `C (a, b) -> `C (f a, fun () -> map f (b ()))
    and iota m n = if m = n then `N else `C (m, fun () -> iota (m+1) n)
    let rec splits s = let n = String.length s in
                    map (fun i -> String.sub s 0 i, String.sub s i (n-i))
                      (iota 0 (n+1))
    and matches s = function `Lit t -> s = t
                           | `Cat (h, t) -> any (map (fun (a, b) ->
                             matches a h && matches b t) (splits s))
                           | `Alt (a, b) -> matches s a || matches s b
                           | `Star r -> s = "" || matches s (`Cat (r, `Star r))

This uses two types, which could be defined in the conventional way as

    type stream = Cons of bool * (unit -> stream) | Nil
    type regex = Alt of regex * regex | Cat of regex * regex | Star of regex | Lit of string

And here are some types from Bicicleta:

    type methods = NoDefs
                               (* name, body, is_positional ... *)
                   | Definition of string * bicexpr * bool * methods
    and bicexpr = Name of string
                  | Call of bicexpr * string
                  | Literal of string option * methods
                  | Derivation of bicexpr * string option * methods
                  | StringConstant of string
                  | Integer of int
                  | Float of float
                  | NativeMethod of (lookup -> bicobj)
    and userdata = UserString of string
                  | UserInteger of int 
                  | UserFloat of float
                      (* name, selfname, body, env *)
    and bicmethod = string * string option * bicexpr * lookup
    and bicobj = ProtoObject 
                 | BaseObject of lookup
                (* Derive of positional method names, methods, parent, cache *)
                 | Derive of string list * bicmethod list * bicobj
                     * (string, bicobj) Hashtbl.t option ref
                 | UserData of userdata
                 | Error of string * string
    and lookup = Phi | Add of string * bicobj * lookup ;;

So, in reverse order, these types have 2, 5, 1, 3, 8, 2, 4, 2, 3, 1,
2, 2, 1, 2, 1, 2, 3, 1, 2, 1, 2, 3, 3, 2, 4, 1, 3, 3, and 1 variant.
So in most cases you could distinguish them entirely with pointer
bits, even if you only had two pointer bits to play with.
