I’ve been thinking about how to build simple models.

Suppose I write the equations:

    area = height * section.perimeter + 2 * section.area
    volume = height * section.area
    
These describe a cylinder or prism, and they imply some things about
`section`: it should have a property `area` that can be multiplied by
an integer or whatever `height` is, and a property `perimeter` that
can be multiplied by whatever `height` is and then added to an integer
times `area`.

My editor should offer to create `section` and `height`, and in
`section` it should offer to create `perimeter` and `area`.
