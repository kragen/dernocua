I was thinking about the transaction-per-call notes in Derctuo, and it
occurred to me that an Emacs clone might be a fun testbed for some of
the ideas in there, in particular the use of transactions to guarantee
UI responsiveness without presenting a complicated programming model
to ad-hoc editing scripts, and providing easier error recovery.  If
updating the screen, syntax-highlighting text, auto-indenting, and
handling keystroke commands are each done in separate transactions, it
should be easy to guarantee rapid screen updates, and even in some
cases rapid keystroke commands.

The transaction write logging can maybe also be repurposed for undo,
which is a pretty essential feature.  Emacs’s local undo is one of the
nicest things about Emacs.

What would I actually need to implement to get an editor I’d use?
-----------------------------------------------------------------

Here is some of my view-lossage from Emacs while writing this note, to
try to get a handle on which commands I use most and would therefore
miss most if they were missing:

    r e p a i n t i n g SPC t h e SPC s c r e e n M-q SPC
    a n d SPC C-a M-d u p d a t i n g M-f M-f , SPC s y
    <backspace> n <backspace> y n t a x - h i g h l i t
    h <backspace> <backspace> g h t i n g SPC t e x t ,
    C-x C-s C-e h a n d l i n g SPC k e y s t r o k e s
    SPC a r e SPC d o n e SPC i n SPC s e p a r a t e M-q
    SPC t r a n s a c t i o n s , SPC C-x C-s C-p C-e <backspace>
    SPC c o m m n d s <backspace> <backspace> <backspace>
    a n d s M-q M-f SPC e a c h C-x C-s C-e SPC t h e n
    SPC C-x C-s <M-backspace> i t SPC s h o u l d SPC b
    e SPC e a s y SPC t o SPC g u a r a n t e e M-q SPC
    r a p i d SPC s c r e e n SPC u p d a t e s , SPC a
    n d SPC p o s s i b l y SPC e v e n SPC r a p i d SPC
    k e y s t r o k e SPC c o m m a n d M-b M-b M-b M-b
    <M-backspace> M-f SPC i n SPC s o m e SPC c a s e s
    C-e s . M-q C-x C-s M-> <return> <return> C-x C-s C-h
    l  C-x o C-SPC
    M-< M-w C-x o C-y C-x C-x C-> C-g C-l C-o C-o C-x 1
    H e r e SPC i s SPC s o m e SPC o f SPC m y SPC v i
    e w - l o s s a g e SPC f r o m SPC E m a c s SPC w
    h i l e SPC r u n <M-backspace> w r i t i n g SPC t
    h i s SPC d o c u m e n <M-backspace> p a g e <M-backspace>
    n o t e : C-x C-s C-h l C-x o C-p
    C-M-v C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p
    C-p C-s c - h SPC l C-r M-f C-f C-f C-f C-f C-SPC C-n
    C-n C-n C-n C-n C-n M-w C-x o M-> SPC C-y M-^ M-^ M-^
    M-^ M-^ M-^ C-/ C-/ C-/ C-/ C-/ C-/ C-f <return> C-x
    C-x C-e C-f C-> C-x C-s C-x 1 M-v C-g M-{ M-{ C-n C-p
    C-o <return> C-x C-s T h e SPC t r a n s a c t i o
    n SPC w r i t e SPC l o g g i n g SPC c a n SPC a l
    s o SPC b e SPC r e p u r p o s e d SPC t <backspace>
    f o r SPC C-x C-s C-x b s h <return> C-d g r e p SPC
    - i SPC q e m a c s SPC . . / d e r c u <tab> m a r
    <tab> * <return> C-x C-f M-p M-p M-n <M-backspace>
    <M-backspace> <M-backspace> <M-backspace> <M-backspace>
    d e r c u <tab> m a r <tab> q e <tab> m <backspace>
    a <tab> <return> C-x 3 C-x b C-s <return> C-h l
    p e n d i n g SPC p r o p e r l y , SPC M - q SPC l
    e a v i n g SPC y o u SPC i n p <backspace> SPC p l
    a c e , M-q SPC r e i <backspace> d i s p l a y SPC
    t h a t SPC i s n ' t SPC v i s i l <backspace> b l
    y SPC s l o w SPC ( ! ) , SPC M - / , SPC c o n t r
    l - b a c k s p a c e , M-q SPC M-b M-b M-f <backspace>
    o l C-e c o m m a n d SPC <backspace> - g r a n u l
    a r i t y SPC u n d o , M-q SPC p r e f i x SPC a r
    g u m e n t s , SPC a n d SPC <M-backspace> <backspace>
    <backspace> . M-b M-b a n d SPC C-e SPC S-SPC l s <backspace>
    <backspace> A l s o SPC s o m e SPC t h i n g s SPC
    I S-SPC u s e d SPC t h a t SPC d i c SPC <backspace>
    <backspace> d SPC w o r k : M-q SPC C C-h k C-x C-e
    C-x o q C-x o C-x o <backspace> g o t o - l i n e ,
    SPC y a n k - p o p . M-b M-b <backspace> <backspace>
    SPC a n d SPC C-e <backspace> SPC , s a y <M-backspace>
    <backspace> , <backspace> <backspace> , SPC s a y .
    M-q C-x C-s C-x 1 C-h l
    C-x o C-x o C-x o M-< C-s C - h SPC l C-SPC
    M-< M-w C-x o M-{ C-y C-x C-x C-> C-x C-s C-x 1 C-x
    C-x C-o C-x C-s M-v M-{ M-{ M-{ M-{ M-{ M-} M-} C-p
    M-f M-f M-f M-f M-f SPC m a y b e C-e u n d o , SPC
    w h i c h SPC i s SPC p a <backspace> <backspace> a
    SPC p r e t t y SPC e s s e n t i a l SPC f e a t u
    r e . M-q SPC S-SPC E m a c ' <backspace> s ' s SPC
    l o c a l SPC u n d o SPC i s SPC o n e SPC o f SPC
    t h e SPC n e <backspace> i c e s t SPC t h i n g s
    SPC a b o u t SPC E m a c s . M-' M-q C-x C-s <next>
    <next> <prior> <prior> <prior> M-{ M-{ M-{ M-{ M-}
    C-p C-x b t r a n C-g C-x C-f <M-backspace> <M-backspace>
    d e r t <backspace> c t u <tab> m a r <tab> r a n <M-backspace>
    t r a n s <tab> <return> C-x C-= C-= C-= <next> M-x
    M-p <return> c d SPC . . / d e r c t u <tab> <return>
    l s <return> f i r e f o <tab> SPC d e r c t <tab>
    - 0 2 <tab> <tab> 1 / n o t <tab> t r a n s <tab> &
    <return> C-x 1 C-x b <return> C-x b C-s <return> C-h
    l
    C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n
    M-w C-x o M-> M-{ M-{ M-} C-y C-x C-x C-> C-g C-d C-x
    C-s C-x 1 C-v M-} M-{ M-} C-p C-p C-p C-p C-p C-o M-{
    C-p C-e <backspace> , SPC t o SPC t r y SPC t o SPC
    g e t SPC a SPC h a n d l e SPC o n SPC w h i c h SPC
    c o m m a n d SPC <backspace> s SPC I S-SPC u s e M-q
    SPC m o s t SPC a n d SPC w o u l d SPC t h e r e f
    o r e SPC m i s s SPC m o s t SPC i f SPC t h e y SPC
    w e r e SPC m i s s i n g : M-q C-x C-s C-x 2 C-x C-f
    <M-backspace> <M-backspace> d e v 3 / d e c o d e -
    l <backspace> <backspace> l o s s a g e . p y <return>
    # ! / u s r / b i n / p y t h o n 3 <return> " " <backspace>
    <backspace> " " " D e c o d e SPC e m a c s SPC C-x
    C-s C-h k C-h l C-x o v i e w - l o s s a g e . C-x
    o C-x o C-n C-n C-n C-n C-n C-n C-n C-n C-e C-b C-b
    C-b <return> C-x o C-x o C-v C-v C-v C-v M-x o p e
    n - d r i <tab> <return> l o s s a g e . <backspace>
    M-b t m p . <return> C-h l
    C-x o C-r C-r C-r M-f M-f C-f C-f C-SPC C-n C-n C-g
    C-r C-r C-r M-< C-SPC M-> C-p C-p M-w C-x o C-x o M->
    M-{ C-y C-x C-x C-> C-x C-x C-g C-x C-f t m p . l <tab>
    <return> C-n C-n C-x k <return> C-x o q C-x o <backspace>
    SPC o u t p u t . " " " <return> C-x C-s M-b M-b M-f
    M-f SPC w i t h SPC a n SPC a s s u m e d SPC k e y
    m a p C-x C-s M-x d e s c r i b - e <backspace> <backspace>
    e - k e y <tab> m <tab> <backspace> <backspace> <backspace>
    <backspace> c u r <tab> k e y <tab> m <backspace> <backspace>
    <backspace> <backspace> m <M-backspace> <M-backspace>
    m <tab> o d <tab> <return> C-x o C-x o C-x o C-v C-v
    C-v M-v C-v C-v C-v C-v M-v M-v M-v q C-h l
    M-< C-s C - h SPC l C-s C-x C-x C-g
    C-x C-x C-g C-r C - h SPC <backspace> C-p C-p C-p C-p
    C-p C-p C-p C-p C-p C-a C-p C-p C-f C-f C-SPC C-n C-n
    C-n C-n C-n C-n C-n C-n C-n C-n C-n C-e C-f M-w C-x
    o C-x o C-y C-x C-x C-> C-x C-s C-x o q C-x o C-x o
    C-x o C-g M-v M-v M-v M-v M-v M-v C-x o C-e <return>
    <return> w o r <M-backspace> d e f SPC w o r d s M-(
    i n f i l e C-e : <return> <tab> f o r SPC l i n e
    SPC i n SPC i n f M-/ : <return> <tab> f o r SPC w
    o r d SPC i n SPC l i n e . s p l i t ( ) : <return>
    <tab> y i e l d SPC w o r d <return> C-x C-s <return>
    <return> i f SPC _ _ n a m e _ _ SPC = = SPC ' _ _
    m a i n _ _ ' : <return> <tab> p r i n t ( l i s t
    ( w o r d s ( s y s . s t d i n ) ) ) M-< M-} C-o C-o
    i m p r o <backspace> <backspace> o r t SPC s y s C-x
    C-s C-h l
    C-x o C-x o C-r C-e C-g C-x o C-r
    C - h SPC l C-r M-f M-f C-f C-f C-SPC M-> C-p C-p M-w
    C-x o C-x o M-} C-y C-x C-x C-> C-g C-x C-s C-d C-x
    C-s C-x o q C-x o C-x b C-g M-x M-p C-g M-o C-g M-x
    s h e l l <return> c d SPC . . / d e v 3 <return> p
    y t h o n SPC d e c o d e l <tab> <return> C-x o C-x
    b <return> M-{ C-SPC M-} M-w C-x o C-y C-d <return>
    C-d <return> C-c C-d <return> C-d C-d C-c C-p C-v C-v
    C-v C-v C-v C-v M-v C-h l
    C-x o
    C-x o C-x o C-r C-r C-r M-f M-f M-f M-f M-b C-SPC C-n
    C-n C-n C-e C-n C-n C-n C-n C-n M-w C-x o C-p C-n C-y
    C-x C-x C-> C-l C-x C-s C-x 1 C-x C-x C-o C-f C-x C-s
    C-x 2 C-x b C-s C-s <return> M-} M-} C-o <return> p
    r e f i x e s SPC = SPC ( ' C - x ' M-b C-b C-b C-b
    ( C-e , ) M-b C-b C-b C-b C-b <backspace> [ C-e SPC
    ( ' C - c ' , ) , SPC C-x C-s C-x o M-v <prior> <prior>
    <prior> <prior> <prior> <prior> <prior> <prior> <next>
    <next> C-x o ( ' E S S <S-backspace> C ' ) <backspace>
    , ' <backspace> ) ) <backspace> ] C-f C-s C-g C-x C-s
    C-n C-n C-n C-o C-k C-o <tab> m a i n ( s y s s <backspace>
    . s t d i n ) C-f C-k C-k C-p C-p C-p C-o C-o d e f
    SPC m a i n ( i n p u t ) <backspace> <backspace> <backspace>
    <backspace> f i l e ) : <return> C-y C-k C-x C-s M-x
    c o m p C-g C-x o M-v M-v C-v C-n C-SPC C-v C-n C-n
    C-n C-n C-n M-w C-x o M-x M-p <return> M-> C-p M->
    M-p M-p <return> C-y C-/ C-x b <return> C-r ) SPC C-f
    , C-x C-s C-x g q C-h l
    C-r C-r <return> M-> C-r C
    - h SPC l C-r C-f M-f M-f C-SPC M-> C-p C-e C-p C-e
    C-p C-e M-w C-x o C-x o M-} C-y C-x C-x C-> C-d C-x
    C-x C-o C-x C-s C-x o q C-x b <return> M-p <return>
    C-x o C-f C-SPC M-2 M-0 C-p M-w C-x o C-y <return>
    C-d C-d C-x o C-h l
    C-x o C-x o C-x o C-r
    C-r C-r M-f M-f M-f M-b M-f C-SPC C-n C-n C-n C-n C-n
    M-w C-x o C-x o M-} C-y C-x C-x C-> C-d C-x C-s C-x
    o C-x o C-x o C-x b C-g C-n C-n C-n C-n C-n C-n C-o
    C-x C-s C-x o C-x o C-x 3 C-x b <return> C-n C-n <return>
    w <backspace> <tab> f o r SPC w o r d SPC i n SPC M-d
    M-d C-d C-e <backspace> <backspace> : <return> C-p
    C-o <tab> p r e f i x SPC = SPC ( ) C-n C-n C-e <tab>
    C-x C-s p r e f i x SPC = SPC p r f <backspace> e f
    i x SPC + S-SPC <M-backspace> <backspace> <backspace>
    + = SPC ( w o r d , ) <return> <tab> i f SPC p r e
    f i x SPC n o t SPC i n SPC p r e f i x e : <backspace>
    s : <return> <tab> p r i n t ( p r e f i x ) M-b '
    SPC ' . j o i n ( C-e ) <return> <tab> p r e f i x
    SPC = SPC ( ) C-x C-s C-h l
    C-x o C-x o C-x o C-r C-r C-r M-f M-f
    M-f C-SPC M-} M-w C-x o C-x o C-x o C-y C-x C-x C->
    C-d C-x C-s C-v C-x o C-x o C-f C-p C-p C-p C-n C-n
    C-n C-o <tab> <backspace> <backspace> p r i n t ( '
    SPC ' . j o i n ( p r e f i x ) ) C-a C-o C-x C-s C-x
    o M-p M-p <return> M-p M-p <return> C-d C-d M-v M-v
    M-v M-v M-v M-v M-v M-v M-v C-x o C-x o C-x o C-r [
    C-d { C-e <backspace> } C-x C-s <return> <return> c
    m d s SPC = SPC { <backspace> <backspace> <backspace>
    <backspace> t r SPC SPC <backspace> = SPC ' ' ' <return>
    C - v SPC C-h k C-v s c r o l l - u p <return> M -
    v SPC s c r o l l - d o w n C-h f <return> C-p C-p
    C-p C-p C-e C-b , SPC ( ' C - h , <backspace> ' , )
    C-x C-s C-x o C-x o C-x o C-x o C-n C-n C-n C-n <return>
    C - h SPC l SPC v i e w - l o s s a g e <return> C-x
    C-s C - x SPC o SPC o t h e r - w i n d o w C-h f <return>
    <return> C - r SPC i s e a r c - b a <backspace> <backspace>
    <backspace> h - b a c k w a r d C-h f <return> <return>
    ' ' ' C-x C-s C-h l
    C-h f <return> C-h k M-w <M-backspace> <M-backspace>
    <M-backspace> <M-backspace> k i l l - r i n g - s a
    v e C-x C-s <return> C - p SPC p r e v i o u s - l
    n e C-x C-s <backspace> <backspace> i n e C-x C-s <return>
    C - y SPC y a n k C-h f <return> <return> C - x SPC
    C - x SPC C-h k C-x C-x e x c h a M-/ C-x C-s C-h k
    C-x 1 <return> d e <backspace> <backspace> C - x SPC
    1 SPC d e l e t e - o t M-/ - w M-/ <M-backspace> w
    i n d o w s C-x C-s C-n <return> c m d s SPC = SPC
    { w o r d [ <backspace> s [ M-b ' SPC ' . j o i n (
    C-e : - 1 ] ) : S-SPC w o r d s [ - 1 ] <return> <tab>
    f o r SPC l i n e SPC i n SPC C-p C-a C-o C-n C-n C-e
    c m d s M-/ . s p l i t ( \ <backspace> ' \ n ' ( <backspace>
    ) <return> <tab> f o r SPC w o r d s SPC 9 <backspace>
    i n SPC [ l i n e . s p l i t ( ) ] <return> <tab>
    f o r SPC <M-backspace> i f SPC C-x o M-> p y t h o
    n 3 <return> ' \ n ' . s p l i t ( ) <return> M-p M-b
    M-b C-b SPC <return> C-x o w C-g C-/ C-x o C-x o w
    o r d s } C-x C-s C-h l
    C-x o C-x
    o C-x o C-r C-r C-r M-< C-f C-f C-SPC M-> C-p C-p M-w
    C-x o C-x o C-x o C-y C-x C-x C-> C-g C-x C-s C-x C-x
    C-g C-x o C-x o C-f C-v C-n C-l C-n C-n C-o <tab> c
    m d SPC = SPC M-d C-d C-e <backspace> <return> C-k
    C-n C-o <tab> i f SPC <M-backspace> p r i n t ( p r
    e f i x , SPC c m d s . g e t ( p r e f i x , SPC '
    s e l f - i n s e r t - c o m m a n d ) <backspace>
    ' ) ) C-x C-s C-x o C-d M-p M-p M-p M-p M-p <return>
    M-p M-p M-p M-p M-p <return> C-d C-c C-p C-v C-x o
    C-x o C-x o C-a M-f M-f <M-backspace> c m d M-f M-f
    M-f <M-backspace> c m d s <backspace> C-x C-s C-x o
    M-> C-d M-p M-p <return> M-p M-p <return> C-d C-c C-c
    C-c C-p C-v <next> <down> <down> <down> <down> <down>
    <down> <down> <down> <down> <down> <down> <down> <down>
    <down> <down> <down> <down> <down> <down> C-x o C-x
    o C-h l
    C-r C-r C-r M-f M-f M-f C-SPC M-> C-p
    C-p M-w C-x o C-x o C-x o C-y C-x C-x C-> C-d C-x C-s
    C-x o C-x o M-{ C-x C-s C-p C-p C-p C-p C-n C-n C-n
    C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-p C-p
    C-e M-b M-b M-b M-d M-d M-d ? ? ? C-x C-s C-x o M->
    M-p M-p <return> M-p M-p <return> C-d C-d C-c C-p C-v
    C-v C-v C-l C-x o C-x o C-x o C-h k C-> M-v C-l C-n
    C-n C-n C-o C - > SPC i n d e n t i <backspace> - r
    i g i d l y - 4 <return> C - l SPC C-h k C-l r e c
    e n t e r - t o p - b o t t o m C-x C-s <return> C
    - x SPC C s - <backspace> <backspace> - s SPC C-h k
    C-x C-s s a v e - b u f f e r C-x C-s <return> C -
    o SPC C-h k C-o o p e n - l i n e <return> C - f SPC
    C-h k C-f f o r w a r d - c h a r C-x C-s C-h k C-x
    2 <return> C - x SPC 2 SPC s p l i t - w i n d M-/
    <backspace> - M-/ M-/ <M-backspace> v e r M-/ <backspace>
    t i c a l l y C-x C-s C-h l
    C-x o C-x
    o C-x o C-r C-r C-r M-f M-f M-f C-SPC M-> M-p C-p C-p
    M-w C-x o C-x o C-x o M-} C-y C-x C-x C-> C-d C-x C-s
    C-x o C-x o <return> C - s SPC i e <backspace> s e
    a r c h - f o r w a r d C-h k C-s C-h k <return> <return>
    < r e t u r n > S-SPC n e w l i n e C-x C-s C-h k M-}
    <return> f o r w a r d - p a r a g r a p h C-a M -
    } S-SPC C-x C-s C-M-v C-v C-n C-n C-n C-n C-n C-n C-n
    C-o <return> f o r SPC c h r SPC i n SPC <backspace>
    <backspace> <backspace> <backspace> <backspace> <backspace>
    <backspace> _ c SPC i n SPC r a n g e ( 3 3 , SPC 1
    2 7 ) : <return> <tab> c m d s [ c ] SPC = SPC ' s
    e l f - i n s e r t - c o m m a n d ' C-x C-s C-h 
    l C-x o C-x o C-x o C-r C-r M-f
    M-f M-f C-SPC M-} M-w C-x o C-x o C-x o M-} C-y C-x
    C-x C-d C-x C-x C-> C-f C-g C-x C-s C-x o C-x o C-x
    o M-> M-p M-p <return> M-p C-x o C-x o C-x o C-a M-f
    C-f _ C-x C-s C-x o <return> M-p M-p M-p <return> C-d
    C-c C-c C-x o C-x o C-x o C-b c h r ( C-f C-f ) C-x
    C-s C-x o M-p M-p <return> M-p M-p <return> C-d C-c
    C-c C-c C-p C-v C-v <next> C-h k C-x b C-x o C-x o
    C-x o M-< C-v M-} C-p C-o C - x SPC b SPC i s w i t
    c h - b u <backspace> <backspace> <backspace> b - b
    u f f e r C-x C-s <return> S P C SPC C-h k SPC s e
    l f - i n s e r t - c o m m a n d C-x C-s C-M-v <return>
    C - b SPC b a c k w a r d - c h a r C-x C-s C-h k C-v
    C-h k C-b C-h l C-x
    o C-x o C-x o C-r C-r C-r M-f M-f M-f C-SPC M-> C-p
    C-p M-w C-x o C-x o C-x o C-p C-y C-x C-x C-d M-^ C-n
    C-a C-SPC M-} C-> C-g C-x C-s M-v C-x o C-x o C-M-v
    <return> < p r i o r > S-SPC s c r o l l - u p C-h
    k <prior> <backspace> <backspace> d o w n C-x C-s <return>
    < n e x t > S-SPC s c r o l l - u p C-h k <next> C-M-v
    C-h k <S-backspace> <return> < S - b a k c p s <backspace>
    <backspace> <backspace> <backspace> c k s p a c e >
    SPC p <backspace> C-x o C-h k <S-backspace> C-x o C-h
    k <S-backspace> C-x o C-x o d e l e t e - b a c k w
    a r d - c h a r C-x C-s <return> C - g SPC q u i t
    C-h k C-g M-b k e y b o a d <backspace> r d - C-x C-s
    C-e <return> H <backspace> C-h k C-k C - k SPC k i
    l l - l i n e C-x C-s <return> C-h k <tab> < t a b
    > S-SPC i n d e n t - f o r - t a b - c o m m a n C-h
    C-g d C-x C-s C-h l C-x o C-x o C-x o C-r C-r C-r M-f M-f M-f C-SPC
    M-} M-w C-x o C-x o C-x o M-} C-p C-e SPC C-y C-x C-x
    C-d C-x C-x C-x C-x C-n C-e C-a C-> C-x C-s C-v M-}
    C-x o C-x o C-M-v C-h k <backspace> C-x o C-h k <backspace>
    C-x o C-x o C-x o C-p C-p C-p C-a C-k C-k C-y C-y C-p
    M-f M-f M-b <M-backspace> C-x C-s C-h l C-x o C-x o C-x o C-r C-r C-r M-f M-f M-f C-SPC
    C-SPC M-} C-x C-x M-w C-x o C-x o C-x o C-p C-e C-y
    C-x C-x C-n C-a C-n C-> C-x C-s C-n C-g C-x o C-x o
    C-M-v C-M-v C-h k M-x C-n C-n C-n C-e <return> M -
    x SPC e x e c u t e - e x t e n d e d - c o m m a n
    d C-x C-s C-M-v C-h k M-p C-x o C-h k M-p C-x o C-x
    o C-x o <return> M - p SPC c o m i n t - p r e v i
    o u s - i n p u t C-x C-s <return> C - / SPC u n d
    o C-h l C-h k M-/ C-h k C-/ <return> M - / SPC d a
    b b r e v - e x p a n d C-x C-s C-h l
    C-x o C-x o C-x o C-r C-r C-r C-r M-f C-f C-f C-f C-f
    C-SPC M-} M-w C-x o C-x o C-x o C-n C-n C-n C-n C-n
    C-e C-y C-x C-x C-x C-x C-x C-x C-n C-f C-> C-g C-x
    C-s C-x C-x C-x C-x C-g C-u C-SPC C-u C-SPC C-u C-SPC
    C-u C-SPC C-x o C-x o C-h k C-x g <return> C - x SPC
    g SPC m a g i t - s t a t u s C-x C-s C-M-v C-x o M->
    M-p M-p <return> M-p M-p <return> C-d C-c C-c C-h k
    M-> C-x o C-x o C-x o <return> M - > S-SPC e n d -
    o f - b u f f e r C-x C-s C-x o C-r ? ? C-r C-r M->
    C-x o C-x o C-h l
    C-r C-r <return> C-r c - h SPC l C-r C-n
    C-a C-SPC M-} M-w C-x o C-x o C-x o M-} C-y C-x C-x
    C-> C-g C-x C-s C-x o C-x o C-v C-n C-n C-n C-n C-n
    C-n C-n C-n C-n C-p C-p C-p C-p C-p C-o <tab> f r e
    q s SPC = SPC { } C-f C-n C-x C-s C-n C-p C-p C-o C-n
    C-x C-s C-n C-n C-n C-p C-n C-n C-n C-n C-o <tab> M-{
    C-o <tab> u n k o n w n s <backspace> <M-backspace>
    u n k n o w n s SPC = SPC s e t ( ) M-} M-} C-p C-o
    <tab> C-a C-k C-n C-o <tab> i f SPC c m d SPC i n SPC
    c m d s : <return> <tab> f r e q <M-backspace> n a
    m e SPC = SPC c m d C-p C-p C-p C-n C-n C-n C-p C-p
    M-b C-M-S-SPC C-M-S-SPC C-M-S-SPC C-w n a m e C-p <return>
    <tab> n a m e SPC = SPC C-y C-n C-n C-a k <tab> i M-b
    C-k i f SPC n a m e SPC n o t SPC i n SPC f r e q s
    : <return> <tab> f r e q s [ n a m e ] SPC = SPC 0
    <return> <tab> <backspace> f r e q s [ n a m e ] S-SPC
    + = SPC 1 C-f C-k <return> <tab> i f SPC n a m e SPC
    = <M-backspace> c m d SPC n o t SPC i n SPC c m d s
    : <return> <tab> u n k n o w n s . a d d ( c m d )
    C-h l
    C-x o C-x o C-x o C-r C-r C-r M-f M-f
    M-f C-SPC M-> C-p C-p M-w C-x o C-x o C-x o M-} C-y
    C-x C-x C-> C-d C-x C-s C-x o C-x o C-f C-k C-x C-s
    C-n C-n C-o <return> <tab> f o r SPC n a m e SPC i
    n SPC s o r t e d ( f r e q s . k e y s ( ) , SPC k
    e y = f r e q s . g e t M-b C-e , SPC r e v e r s e
    = T r e u e ) <backspace> <backspace> <backspace> <backspace>
    u e ) : <return> <tab> p r i n t ( n a m e M-b ' %
    8 d SPC % s ' SPC % S-SPC ( f r e q s [ n a m e , SPC
    <backspace> <backspace> ] , SPC C-e ) ) <return> <return>
    <tab> p <backspace> <backspace> p r i n t ( " u n k
    n o w n s : " " <backspace> , SPC " , SPC " , <backspace>
    . j o i n ( u n k M-/ ) ) C-x C-s C-h l
     C-x o C-x o C-x o C-r C-r C-r M-f M-f M-f
    C-SPC M-} M-w C-x o C-x o C-x o M-} C-y C-x C-x C->
    C-d C-x C-s C-x o C-x o C-x o M-p M-p <return> M-p
    M-p <return> C-d C-d M-v C-x o C-x o C-x o C-r r e
    v M-d M-d <backspace> <backspace> C-x C-s C-x o C-x
    o M-} C-SPC M-{ M-w C-x o C-x o C-x o M-> M-p M-n C-x
    o C-x o C-x M-< C-g C-x o M-< C-n C-n C-o f r o m SPC
    _ - f u t u r <M-backspace> <backspace> _ f u r u t
    <backspace> <backspace> <backspace> t u r e _ _ S-SPC
    i m p o r t SPC p r i n t _ f u n c t i o n C-x C-s
    C-x o M-p M-p <return> C-x o C-SPC M-} M-w C-x o C-x
    o C-x o C-y <return> C-d C-d M-v C-v C-h l
    k C-d C-x o C-x o C-x o C-x o C-x o C-x o C - d SPC
    d e l e t e - c h a r C-h k C-a <return> C - a SPC
    m o v e - b e g M-/ - M-/ o f - l i n e C-x C-s C-h
    k S-SPC <return> S - S P C SPC s e l f M-/ <return>
    C - w SPC k i l l - r e g i o n C-h f <return> C-x
    C-s <return> C-h k C-x C-f C - x SPC C - f SPC f i
    n d - f i l e <return> C - x SPC C - e SPC C-h k C-z
    C-h k C-x C-r C-h k C-x C-e e v a l - l a s t - s e
    x p <return> C-x C-s C - u SPC C-h k C-u u n i v e
    f s <backspace> <backspace> r s a l - a r g u m e n
    t C-x C-s C-h k C-c C-d C-x o C-h k C-c C-d C-x o C-x
    o C-x o <return> C - c SPC C - d SPC c o m i n t -
    s e n d - e o f <return> C-x C-s M - < S-SPC C-h k
    M-< b e g i n M-/ - f M-/ <M-backspace> o M-/ - M-/
    M-/ C-x C-s <return> C-h k C-c C-c C-x o C-h k C-c
    C-c C-x o C-x o C-x o C - c SPC C - c SPC c o m i n
    t - i n t e r r u p t - s u b j o b C-h l
    C-x C-s C-x o C-x o C-r C-r C-r M-< C-SPC M-} M-w C-x
    o M-} C-y C-x C-x C-> C-g C-x C-s C-x o <return> C-h
    k M-0 M - 0 SPC d i g i t - a r g u m e n t <return>
    <f3> M - <f4> <backspace> <backspace> <backspace> <f3>
    <return> M - <f3> SPC d i g i t - a r g u m e n t <f4>
    <f4> <f4> <f4> <f4> <f4> <f4> <f4> <f4> <f4> C-a C-p
    C-p C-p C-p C-p C-p C-p C-p C-p C-p C-k C-k C-SPC M-}
    C-p M-w C-y C-x C-x M-% M - <return> C - <return> !
    C-x C-s C-h l
    s - p r o m p t <return> C-x C-s C-h k M-( M - ( SPC
    i n s e r t - p a r e n t h e s e s C-x C-s <return>
    C - x SPC k C-h k C-x k SPC k i l l - b u f f e C-x
    C-s <return> <backspace> r <return> C - x SPC C = <backspace>
    - = SPC C-h k C-x C-= t e x t - s c a l e - a d j u
    s t C-x C-s <return> M - ^ SPC C-h k M-^ d e l e t
    e - i n d e n t a t i o n C-x C-s C-h k <down> <return>
    < d o w n > S-SPC n e x t - l i n e C-x C-s <return>
    C-h k C-x 3 C - x SPC 3 SPC s p l i t - w i n d M-/
    - h o r i z o n t a l l y C-x C-s C-h k C-= C-x o C-x
    o C-x o M-} C-r C - = C-h k C-M-v C-g C-h k C-M-v C-x
    o <return> C - M - v SPC s c r o l l - o t h e r -
    w i n d o w C-x C-s C-h k M-' <return> M - ' SPC s
    m a r t - a p o s t r o p h e C-x C-s <return> < M
    - B <backspace> b a c k s p a c e S-SPC <backspace>
    > S-SPC C-h k <M-backspace> b a c k w M-/ - M-/ M-/
    M-/ <return> C-h k M-{ C-h l
    C-M-v C-g C-h k C-M-v C-x o <return> C - M - v SPC
    s c r o l l - o t h e r - w i n d o w C-x C-s C-h k
    M-' <return> M - ' SPC s m a r t - a p o s t r o p
    h e C-x C-s <return> < M - B <backspace> b a c k s
    p a c e S-SPC <backspace> > S-SPC C-h k <M-backspace>
    b a c k w M-/ - M-/ M-/ M-/ <return> C-h k M-{ C-h
    l C-x o C-x o C-SPC C-r C-r C-g C-SPC C-g C-r c - h
    SPC l C-r M-{ C-SPC M-} M-w C-x o C-y C-x C-x C-> C-g
    C-x o C-h k M-{ M - { S-SPC b a c k w a r d - p a r
    a g r a p h C-x C-s <return> C - h SPC f SPC d e s
    c r i b e - f u n c t i o n <return> C - h SPC k SPC
    d e s c r i b e - k e y <return> M - q SPC f i l l
    - p a r a g r a p h C-h k M-q C-x C-s <return> M -
    o SPC C-h k M-o C-g C-g s h e l l C-x C-s <return>
    C-h k M-n C-x o C-h k M-n C-x o C-x o C-x o M - n SPC
    c o m i n t - n e x t - i n p u t <return> M - d C-h
    k M-d SPC k i l l - w o r d C-x C-s C-h k C-g C-h 
    l
    C-x o C-x o C-r C-r <return> C-r c - SPC h <backspace>
    <backspace> h SPC l l l <backspace> <backspace> M-<
    C-SPC M-} M-w C-x o M-} C-y C-x C-x C-> C-g C-x C-s
    C-x o C-x o C-x o C-x o M-} C-SPC M-{ M-w C-x o C-x
    o M-> M-p M-p <return> C-y <return> C-d C-d C-x o C-x
    o C-x o C-h k C-h C-g C-h k C-x M-< C-h k C-x C-r C-h
    k <f3> <return> < f 3 > S-SPC k m a c r o - s t a r
    M-/ <backspace> <backspace> - M-/ m a c r o - o r -
    i n s e r t - c o u n t e r <return> M - S-SPC <backspace>
    % C-h k M-% SPC q u e r y - r e p l a c e <return>
    < f 4 > S-SPC C-h k <f4> k m a c r o - e n d - o r
    - c a l l - m a c r o C-x C-s C-h l
    t a l , SPC C-x C-s M-x M-p <return> M-> M-p M-p <return>
    M-p M-p <return> C-d C-d M-v C-x 2 C-x b C-s <return>
    M-} <return> S o m e SPC n o t e s SPC o n SPC f r
    e q u e n c i e s SPC o f SPC c o m m a M-b M-b M-b
    m o s t SPC c o m m o n C-k SPC c o m m a n d SPC f
    r e q u e n c i e s : <return> <return> C-x C-s C-x
    o M-v C-p C-p C-p C-SPC C-n C-n C-n C-n C-n C-n C-n
    C-n C-n C-n C-v C-v C-v M-v M-v C-p M-v C-n C-n C-n
    C-n C-n C-n C-n M-w C-x o C-y C-x C-x C-> C-g C-x C-s
    C-v C-x 1 C-l M-{ C-p C-e <backspace> . SPC S-SPC O
    u t SPC o f SPC C-x C-s C-x b <return> M-> C-x b <return>
    5 8 8 2 SPC c o m a <backspace> m a n d s SPC r e c
    o r d e d SPC a b o v e SPC a n d SPC <backspace> SPC
    s u c c s s <backspace> <backspace> e s s f u l l y
    M-q d e c o d <backspace> <backspace> <backspace> <backspace>
    <backspace> SPC d e o c <backspace> <backspace> c o
    d e d , SPC t h e s e SPC C-f C-n C-SPC M-} M-= C-g
    M-{ C-p C-e 2 4 SPC c a <backspace> <backspace> a c
    c o u n t SPC f o r SPC C-v C-l M-( M-: M-( * S-SPC
    5 8 8 2 SPC . 9 <return> C-/ C-h l
    s SPC o b v i o u s l y SPC i s n ' t SPC e v e r y
    t h i n g SPC e s s e n t i a l ; SPC M-' C-x C-s i
    t ' s SPC m i s s i n g , SPC a m o n g SPC t h e r
    SPC t h i n g M-b M-b o C-e s , SPC f i n d - f i l
    e SPC a n d M-q SPC C-x C-s <M-backspace> <backspace>
    , SPC C-r k i l l C-g C-x b C-s <return> M-v C-l C-x
    b <return> y a n k , SPC k i l l - r i n g - s a v
    e SPC M-( t h e SPC n e w SPC c o p y - r e g M-/ i
    o n - a s k <backspace> - k i l l C-e . C-x C-s C-x
    b <return> C-x b <return> <backspace> , SPC C-h k M-:
    e v a l - e x p r e s s i o n , M-q SPC C-x C-s C-x
    1 M-v <down> <down> C-n C-n C-n C-n C-n C-l C-n C-n
    C-n C-n C-n C-n C-n C-n C-n C-e M-{ M-{ M-{ C-n C-n
    M-f M-f M-f M-f M-b ( <backspace> M-f M-f M-f SPC b
    y SPC a SPC j a n k y SPC e r r o <M-backspace> u n
    r e l i a b l e SPC c <backspace> s c r i p t M-q M-f
    <backspace> <backspace> SPC f l l o w i n g <M-backspace>
    f l <M-backspace> <backspace> s e C-x C-s C-h l
    C-x o C-r C - h SPC l
    M-< C-SPC M-} M-w C-x o M-{ C-y C-x C-x C-> C-g C-v
    M-} C-n C-n M-b M-d C-d M-f SPC o f SPC t h e M-q C-x
    C-s C-x 1 C-v C-l C-x b C-s <return> <down> <up> <up>
    <up> <up> C-x b <return> C-x b <return> <down> <down>
    <down> <down> <down> <down> <S-down> <S-down> <S-up>
    C-g C-x 2 C-x b <return> M-} C-n C-p C-n M-f M-f M-f
    M-f M-f M-f M-f M-f M-f C-o C-o SPC s u c h SPC b a
    s i c s SPC a s SPC f o r w a r d - c h a r , M-d M-d
    M-d C-d M-q C-n C-x o C-s e x t C-g C-x o C-e SPC n
    d SPC e M-b M-b a C-e x e c u t e - e x t e n d e d
    - c o m m a n d . C-r M - n C-r C-r C-r C-x C-f C-h
    k M-n q C-g C-x b <return> M-v M-v C-r M - n M-f C-f
    C-f C-f C-k n e x t - h i s t o r y - e l e m e n t
    C-r M - p M-f C-f C-f C-f C-k C-x C-f C-h k M-p q C-g
    p r e v i o u s - h i s t o r y - e l e m e n t C-x
    C-s C-x b <return> C-x 1 C-v C-v C-v C-h l
    C-x o C-r C-r M-> C-r c - h SPC l C-r M-f M-f
    M-f C-SPC M-} M-w C-x o M-} C-y C-x C-x C-> C-d C-l
    C-v C-x C-s M-} M-} M-} C-x C-x C-g C-x o C-x b <return>
    C-u C-SPC C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n
    C-n C-v C-l C-p C-p C-p C-p C-p C-p C-o <tab> u s e
    d _ k e y s SPC = SPC { } <return> <tab> C-a C-k C-x
    C-s C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n
    C-n C-n C-o C-o <tab> <backspace> C-a C-k C-o <tab>
    <backspace> i f SPC c h d <backspace> <backspace> m
    d SPC n o t SPC i n SPC u s M-/ : C-a C-o C-n C-e <return>
    <tab> C-p M-b M-d n a m e C-n <tab> u s e M-/ [ n a
    m e ] S-SPC = SPC c m d C-f C-k C-x C-s C-n C-n C-n
    C-n C-n C-n C-e C-a M-f M-f M-f M-f SPC ( e . g . ,
    SPC % s ) C-e C-b C-b , SPC u s M-/ [ n a m e ] C-e
    C-x C-s C-h l
    C-x o C-r C-r C-r
    M-f M-f C-f C-f C-SPC M-} M-w C-x b <return> C-y C-x
    C-x C-d C-x C-x C-> C-g C-x C-s C-SPC M-{ M-w M-x M-p
    <return> M-> M-p M-p <return> C-y <return> C-d C-d
    C-h k <S-up> C-x o C-x b C-s <return> M-v C-l C-n C-n
    C-n C-n C-n C-n C-n C-o M - : S-SPC e v a l C-h k M-:
    - e x p r e s s i o n C-x o C-x 2 C-x b C-s <return>
    C-x o C-x o <return> < S - d o w n > S-SPC C-a C-k
    C-k C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p
    C-p C-p C-p C-p C-y C-p C-p C-e C-n n e x t - l n e
    <backspace> <backspace> i n e C-x C-s C-r u p C-a C-r
    C-r C-v C-s C-s C-n C-n C-n C-n C-n C-y C-p C-e <M-backspace>
    u p S-SPC <S-backspace> > SPC p r e v M-/ - M-/ M-/
    <M-backspace> <M-backspace> C-h k <up> p r e v i o
    u s - l i n e <return> < u p > SPC p r e v M-/ - M-/
    C-x C-s C-h l
    t SPC C-x C-s i f SPC y o u SPC h a v e SPC C-a C-k
    T h i s SPC i s SPC p r o b a b l y SPC m o s t SPC
    o f SPC w h a t SPC C-a C-k S o SPC w i t h SPC t h
    o s e SPC c o m m a n d s , SPC y o u ' d SPC h a v
    e SPC <M-backspace> <M-backspace> <M-backspace> i f
    SPC m y SPC c u r r e n t SPC e d i t i n g SPC s e
    s s i o n SPC w e r e SPC t y p i c a l SPC M-( w h
    i c h SPC i t SPC p r o b a b l y SPC i s n ' t M-'
    C-e , SPC M-q SPC y o u ' d SPC <M-backspace> <M-backspace>
    I ' d SPC r u n SPC M-' i n t o SPC a C-p C-a M-f M-d
    SPC i f SPC y o u SPC h a d M-f M-f SPC i m p l e m
    e n t e d C-a M-f M-f M-d SPC I M-q C-n C-e C-x s SPC
    C-p M-b C-n C-e SPC m i s s i n g SPC s t a i r SPC
    o <backspace> a b o u t SPC o n c e SPC o u t SPC o
    f SPC e v e r y SPC 1 0 0 SPC c h a r a c t e r <M-backspace>
    k e y s t r o k e s . M-q C-x C-s C-h l
    m a j o r i t y SPC o f SPC m y SPC k y <backspace>
    e y s t r o k e s , SPC M-l M-q C-x C-s C-l C-l C-l
    <next> <prior> <down> C-e M-b M-b M-b M-b a n d SPC
    h a v i n g SPC h <backspace> j u s t SPC t h e s e
    SPC i m p l e m e n t e d SPC o u <M-backspace> w o
    u l d SPC m a k e SPC s o m e t h i n g SPC " f e e
    l SPC l i k e SPC a n SPC E m a c s " , SPC M-" M-"
    M-q C-x C-s <next> <next> <up> <next> <prior> <prior>
    <prior> M-> <backspace> , SPC b u t SPC i t SPC s e
    e m s SPC l i k e SPC i f SPC I S-SPC i m p l e m e
    n t e d SPC * m y * S-SPC M-q SPC i <backspace> s t
    a n <M-backspace> m o s t SPC u s e d SPC E m a c s
    SPC c o m m a n d s SPC i n s t e a d SPC o f SPC B
    e l l a r d ' s , SPC M-' t h e SPC s e t SPC w o u
    l d SPC b e SPC e v e n SPC s m a l l e r . M-b M-b
    M-b M-b t o SPC g e t SPC t o SPC c o m f o r t SPC
    M-q C-x C-s <next> <prior> <prior> <prior> C-h l
    C-n C-h f <return> C-n C-h f <return> C-n C-n C-n C-n
    M-f M-f M-f C-h f <return> C-n C-h f <return> C-n C-h
    f <return> C-p C-h f <return> C-n C-h f <return> C-x
    0 a n d SPC d o d <backspace> w n c a s e - w o r d
    SPC ( ! ? ) . M-q C-x C-s C-x 1 C-l C-p C-p C-p C-p
    C-p M-b M-b <M-backspace> <M-backspace> m o s t SPC
    M-q C-x C-s <prior> <next> C-n C-n C-n C-n C-n C-n
    C-n C-n C-n C-n C-n C-n M-f M-f M-f M-f SPC E m a <M-backspace>
    G N U S-SPC E m a c s SPC i m p l e m e n t s SPC m
    o s t M-f M-f M-f M-d M-d M-d C-e M-f M-f C-a M-d M-d
    M-d <backspace> M-q M-> C-x C-s C-h f r e c e n t e
    r <return> C-x 1 <backspace> S-SPC S-SPC S o m e SPC
    o f SPC t h e m SPC <backspace> , SPC l i k e SPC r
    e c e n M-/ , M-q SPC a r e SPC t h i n SPC L i s p
    SPC v e n e e r s SPC o n SPC t o p SPC o f SPC b u
    i l t - <M-backspace> p r i m i t i v e SPC f u n c
    t i o n s SPC l i k e SPC r e c e n t e r . M-b M-b
    M-d s u c h SPC a s M-q M-> C-x C-s <prior> <prior>
    <prior> <prior> <prior> <prior> <prior> <prior> <prior>
    <prior> <prior> <prior> <prior> <prior> <prior> C-h
    l C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-n C-a M-f
    , SPC c o n f l i c t i n g SPC w i t h SPC C-x b <return>
    M-> <return> | a <tab> b <M-right> <M-S-right> x <S-up>
    <S-right> <S-left> <S-up> C-a C-p C-p C-k C-k C-k C-k
    C-k C-x C-s C-x b <return> s h i f t - s e l e c t
    i o n SPC a n d SPC s o m e SPC o r g - m o d e SPC
    b i n d i n g s M-q C-x C-s C-x C-s C-n C-n C-n C-n
    C-n M-} C-o <return> T h e r e ' s SPC a SPC t h i
    n g SPC c a l l e d SPC [ A c e SPC J u m p ] [ 2 ]
    <return> <return> [ 2 ] : SPC C-y C-p C-p C-e SPC w
    h i c h SPC l e t s SPC y o u SPC j u m p SPC t o SPC
    t e x t SPC b y SPC s e a <M-backspace> t y p i n g
    SPC i t , SPC e v e n SPC i f SPC i t ' s SPC i n SPC
    a n o t h e r SPC w i n d o w M-' . M-q C-x C-s <backspace>
    , SPC s i m M-' <M-backspace> s o r t SPC o f SPC l
    i k e SPC m o v i n g SPC b y SPC i n c r e m e n t
    a l SPC s e a r c h . M-q C-x C-s C-h l
    i g n SPC w i t h SPC <M-backspace> w i t h SPC t h
    e SPC d i s p l a y SPC d i v i d e d SPC i n t o M-q
    SPC v e r t i c a l SPC " t r a c k " S-SPC e a c <M-backspace>
    <backspace> <backspace> s " S-SPC e a c h SPC d i v
    i d e d SPC i n t o SPC h o r i z o n t a l SPC " w
    i n d o w s " M-q M-" M-" M-" M-" SPC m i <backspace>
    <backspace> <backspace> C-e SPC m i g h t SPC b e SPC
    a SPC C-x C-s <M-backspace> <M-backspace> p r o v i
    d e SPC s i m p l e r SPC a n d SPC m o r e SPC p r
    e d i c t a b l e SPC b e a v <backspace> <backspace>
    h a v i o r . M-q C-x C-s <backspace> SPC t h a n SPC
    t h e SPC t r a d <M-backspace> m <backspace> S m t
    a l l t <M-backspace> S m a l l t a l k - s t y l e
    SPC o v e r a l <backspace> <backspace> l a p p i n
    g SPC w i n d o w s . C-x C-s M-> C-p C-p C-p M-b M-b
    <M-backspace> <M-backspace> w o n d e r SPC i f SPC
    M-q M-> C-x C-s M-v M-v M-v M-v M-v M-v M-v M-v M-v
    M-v M-v <next> <next> <next> <next> <next> <next> <next>
    <next> <prior> <prior> <down> C-h l C-x
    o C-r C - h SPC l M-> C-SPC C-p C-p C-SPC M-< M-w C-x
    o M-{ M-{ C-y C-x C-x C-> C-g C-x C-s M-{ C-x 1 M-{
    M-{ M-{ M-{ M-{ M-{ <next> <next> <next> <next> <next>
    <next> <next> <next> <next> <next> <next> <next> <next>
    <next> <next> <next> <next> <next> <next> <next> <next>
    <next> <prior> <prior> <next> <next> <next> <next>
    <prior> <prior> <prior> <prior> <next> C-x b p y <return>
    C-f C-SPC M-v M-v M-{ C-n C-n M-= C-g C-x 2 C-x b <return>
    M-> M-v M-v C-v M-v M-v M-v M-} C-o <return> I SPC
    u s e d SPC t h i s SPC t a b l e SPC t o SPC g e n
    e r a t e SPC t h e SPC b o <M-backspace> <M-backspace>
    t h e SPC a b o v e : M-b M-b M-b M-b o f SPC 9 9 SPC
    k e y b i n d i n g s SPC C-x C-s C-x o C-SPC C-v C-v
    C-v C-v C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n
    C-n M-w C-x o C-e <return> <return> C-y C-x C-x C->
    C-g C-x C-s C-x C-x C-k C-x C-x M-| s o r t <return>
    C-x C-x C-u M-| M-p <return> C-h l
    C-x C-> C-x C-x C-o C-r C - h SPC l C-l C-l C-l C-x
    C-x C-r C-r C-p C-p C-p C-p C-p C-p C-p C-p C-g C-p
    C-p C-p C-p C-p C-p C-p C-p C-p M-f M-f C-f C-f C-SPC
    C-p C-p C-p C-p C-p C-p M-b M-b M-b C-w C-x C-s C-h
    k M-| M-} C-x o C-x b C-s <return> C-o M - | SPC s
    h e l l - c o m M-/ <backspace> <backspace> <backspace>
    m M-/ - M-/ <M-backspace> o n - r e g i n <backspace>
    o n C-h f <return> C-x o C-x b <return> C-SPC M-{ C-n
    M-| ~ / d e v e l / d e v 3 / d e c o d e l <tab> <return>
    C-x b C-s <return> C-x C-s C-x b <return> C-x C-x M-|
    M-p <return> C-x o M-> C-x o C-x b <return> <return>
    C - x SPC 0 SPC C-h C-g C-x 2 C-h k C-x 0 C-x o C-x
    o d e l e t e - i <backspace> w i n d o w C-x C-s C-h
    k C-x M-< C-h k C-x s C-h k <M-right> <return> < M
    - R i g h t > S-SPC f o r w r <backspace> a r d - w
    o r d <return> < M - S - R i g h t > C-h k <M-S-right>
    SPC f o r w a r d - w o r d C-x C-s C-x b C-g C-x o
    C-x o C-r C-g C-p C-p C-p C-p C-p C-SPC C-p C-SPC C-p
    M-w C-x o C-x o C-x b <return> C-v C-v C-v C-v C-v
    C-v C-v C-v C-v M-v C-p C-p C-y C-p C-> C-x C-s C-h
    l
    <down> <right> <down> <down> <down> <down> <down> <down>
    <down> <down> <down> <down> <down> <down> <down> <down>
    <down> <down> <down> <down> <down> <down> <down> <down>
    <down> <down> <down> <down> <down> <down> <down> <down>
    <down> C-p M-v C-v C-n C-n C-n C-n C-n C-n C-n C-n
    C-n C-n C-n C-n C-n C-n C-n C-n C-n C-p C-SPC C-n C-n
    C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n C-n
    C-n C-n C-n C-n C-n C-n C-e C-x r k C-p C-p C-p C-p
    C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p
    C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p C-p
    C-p C-l C-p M-{ C-n C-e SPC SPC SPC SPC SPC SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC C-x r y C-x C--
    M-{ C-l C-n C-n C-n C-n C-n C-n C-l C-/ C-p SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC
    SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC SPC C-x r y
    M-b M-b M-b M-b M-b M-b M-b C-s C-w C-w M-b M-b C-b
    C-b C-b C-b C-b C-b C-b C-b C-b C-b C-b C-b C-b C-b
    C-b C-b C-b C-b C-b C-b C-b C-b C-b C-b C-k C-p C-k
    C-p C-k C-p C-k C-p C-k C-p C-k C-p C-k C-p C-k C-/
    C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/ C-/
    C-/ C-/ C-/ C-/ C-p C-/ C-v C-n C-n C-n C-n C-n C-n
    M-} C-SPC M-} C-w C-h l

Some notes on most common command frequencies.  Out of 9014 of the
commands recorded above and successfully decoded by a janky unreliable
script, these 21 account for 90% of the commands:

        5632     5632 self-insert-command (e.g., d)
         321     5953 next-line (e.g., C-n)
         297     6250 other-window (e.g., C-x o)
         242     6492 newline (e.g., <return>)
         216     6708 delete-backward-char (e.g., <backspace>)
         210     6918 previous-line (e.g., C-p)
         162     7080 save-buffer (e.g., C-x C-s)
         112     7192 scroll-up (e.g., C-v)
         112     7304 forward-word (e.g., M-f)
         101     7405 scroll-down (e.g., M-v)
          98     7503 isearch-backward (e.g., C-r)
          90     7593 describe-key (e.g., C-h k)
          71     7664 backward-kill-word (e.g., <M-backspace>)
          68     7732 previous-history-element (e.g., M-p)
          67     7799 indent-for-tab-command (e.g., <tab>)
          62     7861 backward-word (e.g., M-b)
          59     7920 end-of-line (e.g., C-e)
          56     7976 forward-paragraph (e.g., M-})
          56     8032 exchange-point-and-mark (e.g., C-x C-x)
          55     8087 set-mark-command (e.g., C-SPC)
          54     8141 keyboard-quit (e.g., C-g)

Although this is the majority of my keystrokes, and having just these
implemented would make something “feel like an Emacs”, this obviously
isn’t everything essential; it's missing such basics as forward-char,
find-file, yank, kill-ring-save (the new copy-region-as-kill),
eval-expression, and execute-extended-command.  The next 9% (90% of
the remainder) are accounted for by the following 29 commands:

          49     8190 forward-char (e.g., C-f)
          48     8238 delete-char (e.g., C-d)
          46     8284 yank (e.g., C-y)
          45     8329 open-line (e.g., C-o)
          45     8374 view-lossage (e.g., C-h l)
          44     8418 backward-paragraph (e.g., M-{)
          43     8461 dabbrev-expand (e.g., M-/)
          41     8502 iswitchb-buffer (e.g., C-x b)
          41     8543 kill-ring-save (e.g., M-w)
          40     8583 fill-paragraph (e.g., M-q)
          37     8620 end-of-buffer (e.g., M->)
          33     8653 indent-rigidly-4 (e.g., C->)
          30     8683 kill-line (e.g., C-k)
          29     8712 move-beginning-of-line (e.g., C-a)
          24     8736 kill-word (e.g., M-d)
          21     8757 ??? (e.g., <M-S-right>)
          21     8778 recenter-top-bottom (e.g., C-l)
          20     8798 isearch-forward (e.g., C-s)
          16     8814 backward-char (e.g., C-b)
          15     8829 describe-function (e.g., C-h f)
          15     8844 delete-other-windows (e.g., C-x 1)
          14     8858 scroll-other-window (e.g., C-M-v)
          14     8872 beginning-of-buffer (e.g., M-<)
          12     8884 kmacro-end-or-call-macro (e.g., <f4>)
          10     8894 execute-extended-command (e.g., M-x)
          10     8904 undo (e.g., C-/)
           9     8913 smart-apostrophe (e.g., M-')
           8     8921 split-window-vertically (e.g., C-x 2)
           8     8929 delete-indentation (e.g., M-^)

So if I had those commands implemented, if my current editing session
were typical (which it probably isn’t), I would run into a missing
stair about once out of every 100 keystrokes, probably a couple of
times a minute; still enough to break the spell of suspension of
disbelief, but close to usable.  The remaining 24 commands, though,
include some very significant ones:

           7     8936 universal-argument (e.g., C-u)
           7     8943 find-file (e.g., C-x C-f)
           6     8949 comint-interrupt-subjob (e.g., C-c C-c)
           6     8955 smartquote (e.g., M-")
           6     8961 insert-parentheses (e.g., M-()
           5     8966 comint-previous-prompt (e.g., C-c C-p)
           5     8971 shell-command-on-region (e.g., M-|)
           5     8976 next-history-element (e.g., M-n)
           4     8980 kmacro-start-macro-or-insert-counter (e.g., <f3>)
           3     8983 eval-expression (e.g., M-:)
           3     8986 comint-send-eof (e.g., C-c C-d)
           3     8989 mark-sexp (e.g., C-M-S-SPC)
           3     8992 digit-argument (e.g., M-0)
           3     8995 split-window-horizontally (e.g., C-x 3)
           2     8997 magit-status (e.g., C-x g)
           2     8999 delete-window (e.g., C-x 0)
           2     9001 query-replace (e.g., M-%)
           2     9003 eval-last-sexp (e.g., C-x C-e)
           2     9005 kill-buffer (e.g., C-x k)
           2     9007 kill-region (e.g., C-w)
           2     9009 shell (e.g., M-o)
           2     9011 text-scale-adjust (e.g., C-x C-=)
           2     9013 count-lines-region (e.g., M-=)
           1     9014 downcase-word (e.g., M-l)

My notes on QEmacs from Dercuano noted the things I missed from Emacs
in QEmacs: M-^, M-;, C-k appending properly, M-q leaving you in place,
redisplay that isn’t visibly slow (!), M-/, control-backspace,
command-granularity undo, and prefix arguments.  Also some things I
used that did work: goto-line and yank-pop, say.  I was astonished
that with only 88 commands it managed to be pretty usable, but it
seems like if I implemented *my* most used Emacs commands instead of
Bellard’s, the set to get to comfort would be even smaller, less than
75.

I used this table of 99 keybindings to generate the above:

    <M-Right> forward-word
    <M-S-Right> forward-word
    <M-backspace> backward-kill-word
    <S-backspace> delete-backward-char
    <S-down> next-line
    <S-up> previous-line
    <backspace> delete-backward-char
    <down> next-line
    <f3> kmacro-start-macro-or-insert-counter
    <f4> kmacro-end-or-call-macro
    <next> scroll-up
    <prior> scroll-down
    <return> newline
    <tab> indent-for-tab-command
    <up> previous-line
    C-/ undo
    C-0 digit-argument
    C-1 digit-argument
    C-2 digit-argument
    C-3 digit-argument
    C-4 digit-argument
    C-5 digit-argument
    C-6 digit-argument
    C-7 digit-argument
    C-8 digit-argument
    C-9 digit-argument
    C-> indent-rigidly-4
    C-M-S-SPC mark-sexp
    C-M-SPC mark-sexp
    C-M-v scroll-other-window
    C-SPC set-mark-command
    C-a move-beginning-of-line
    C-b backward-char
    C-c C-c comint-interrupt-subjob
    C-c C-d comint-send-eof
    C-c C-p comint-previous-prompt
    C-d delete-char
    C-e end-of-line
    C-f forward-char
    C-g keyboard-quit
    C-h f describe-function
    C-h k describe-key
    C-h l view-lossage
    C-k kill-line
    C-l recenter-top-bottom
    C-n next-line
    C-o open-line
    C-p previous-line
    C-r isearch-backward
    C-s isearch-forward
    C-u universal-argument
    C-v scroll-up
    C-w kill-region
    C-x 0 delete-window
    C-x 1 delete-other-windows
    C-x 2 split-window-vertically
    C-x 3 split-window-horizontally
    C-x C-= text-scale-adjust
    C-x C-e eval-last-sexp
    C-x C-f find-file
    C-x C-s save-buffer
    C-x C-x exchange-point-and-mark
    C-x b iswitchb-buffer
    C-x g magit-status
    C-x k kill-buffer
    C-x o other-window
    C-y yank
    M-" smartquote
    M-% query-replace
    M-' smart-apostrophe
    M-( insert-parentheses
    M-/ dabbrev-expand
    M-0 digit-argument
    M-1 digit-argument
    M-2 digit-argument
    M-3 digit-argument
    M-4 digit-argument
    M-5 digit-argument
    M-6 digit-argument
    M-7 digit-argument
    M-8 digit-argument
    M-9 digit-argument
    M-: eval-expression
    M-< beginning-of-buffer
    M-= count-lines-region
    M-> end-of-buffer
    M-^ delete-indentation
    M-b backward-word
    M-d kill-word
    M-f forward-word
    M-l downcase-word
    M-n next-history-element
    M-o shell
    M-p previous-history-element
    M-q fill-paragraph
    M-v scroll-down
    M-w kill-ring-save
    M-x execute-extended-command
    M-{ backward-paragraph
    M-| shell-command-on-region
    M-} forward-paragraph
    S-SPC self-insert-command
    SPC self-insert-command

Notice that 20 of these 99 are just digit-argument.  I supplemented
these with self-insert-command bindings for printable ASCII.

indent-rigidly-4, smartquote, and smart-apostrophe are little commands
I wrote that I often find useful.

Worth noting is that GNU Emacs implements most of these commands in
Elisp, with a few exceptions: self-insert-command, other-window,
delete-backward-char, forward-word, scroll-up, end-of-line,
scroll-down, delete-char, forward-char, backward-char,
scroll-other-window (!?), delete-other-windows,
execute-exptended-command, kill-buffer, and downcase-word (!?).  Some
of them, like recenter-top-bottom, are thin Lisp veneers on top of
primitive functions such as recenter.

Window management
-----------------

The Emacs way of handling windows from the keyboard is totally broken.
With two windows on the screen it’s fine.  Three is awkward.  Four is
unusable.  In the above lossage there are strings of up to six
other-window commands in a row.  Any number of better alternatives for
window *switching* have been invented: Win16 LRU alt-tab; screen/tmux
numbering of windows; irssi numbering of windows with
alt-1/alt-2/alt-3 etc. to switch between them and alt-a to jump to the
window that’s demanding attention; modifier keys which make the arrow
keys move you between windows (Hovav Shacham’s windmove from 1998,
inspired by Julian Assange’s change-windows-intuitively, uses shift by
default, conflicting with cua-mode shift-selection and some org-mode
bindings); iswitchb’s/icomplete’s/ido’s LRU list of buffers with
typeahead filtering; Win16 MDI ctrl-tab/ctrl-f4; etc.  Emacs itself
has accreted ace-window (apparently this involves assigning numbers to
all the windows so you can type C-x o 3, and there are other
characters for things like deleting windows, splitting windows,
maximizing windows, etc.), dimitri/switch-window (same), etc.

[Spacemacs][3] uses SPC 1, SPC 2, etc., to switch to windows 1, 2,
etc, and has window-manipulation commands on SPC w.

[3]: https://github.com/syl20bnr/spacemacs/blob/master/doc/DOCUMENTATION.org#window-manipulation-key-bindings

There’s a thing called [Ace Jump][2] which lets you jump to text by
typing it, even if it’s in another window, sort of like moving by
incremental search.

[2]: https://www.emacswiki.org/emacs/AceJump

A different problem is that many built-in Emacs commands, being
designed for two windows or less, [happily replace your window
contents with their own][0], although [in some cases you can appease
them by offering them a sacrificial window][1].  There’s a whole
ecosystem around the `display-buffer` command that attempts to make
this less frequently annoying.

[0]: http://ergoemacs.org/emacs/emacs_effective_windows_management.html
[1]: https://stackoverflow.com/questions/21761971/prevent-emacs-commands-from-showing-new-buffers-in-other-windows

I think this is a symptom of a broken user interface design.  I’m not
sure what the right design is; maybe something where opening new
things opens new windows by default, which you can then maximize and
unmaximize, or close, or resize.  I wonder if the Cedar/Oberon design
with the display divided into vertical “tracks” each divided into
horizontal “windows” might provide simpler and more predictable
behavior than the Smalltalk-style overlapping windows.