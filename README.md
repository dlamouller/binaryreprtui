binaryrep is a utility to display position of the bits of a number.
Entries can be decimal, hexadecimal, binary or octal. Obviously with
python, there is a basic command

> &gt;&gt;&gt; bin(64) '0b1000000'

but if you want to know the position of MSB, it's not straightforward.
That's the purpose of binaryrepr. The output is formatted in
reStructuredText. Other shapes of output are available.

\#\#\# Installation Guide

&gt; pip install binaryrepr

\#\#\#\#\# python dependencies

-   click
-   prettytable

\#\#\# Take a look on some example.

-   a simple example (less than 256)

    > **binaryrepr 64**
    >
    >   ------- ------- ------- ------- ------- ------- ------- ------- -------
    >   8       7       6       5       4       3       2       1       0
    >   0       0       1       0       0       0       0       0       0
    >   ------- ------- ------- ------- ------- ------- ------- ------- -------
    >
-   another example (greater than 255)

    > **binaryrepr 1024**
    >
    >   ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    >   16   15   14   13   12   11   10   9    8    7    6    5    4    3    2    1    0
    >   0    0    0    0    0    0    1    0    0    0    0    0    0    0    0    0    0
    >   ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ---- ----
    >
-   a short representation without leading zeros

    > **binaryrepr 1024 -s**
    >
    >   ------- ------ ------ ------ ------ ------ ------ ------ ------ ------ ------
    >   10      9      8      7      6      5      4      3      2      1      0
    >   1       0      0      0      0      0      0      0      0      0      0
    >   ------- ------ ------ ------ ------ ------ ------ ------ ------ ------ ------
    >
-   another representation: noline (also gfm github format markdown)

    > **binaryrepr 1024 -f noline -s**
    >
    > > value 10 9 8 7 6 5 4 3 2 1 0
    > >
    > > :   1024 1 0 0 0 0 0 0 0 0 0 0
    > >
-   input can be decimal, binary, hexa or octal

    **binaryrepr 0xFF**

    >   ------- ------- ------- ------- ------- ------- ------- ------- -------
    >   8       7       6       5       4       3       2       1       0
    >   0       1       1       1       1       1       1       1       1
    >   ------- ------- ------- ------- ------- ------- ------- ------- -------
    >
-   input can be binary and output hexadecimal for example

    **binaryrepr 0b100 -t hex**

    > +-----------+-------+----+----+---+---+---+
    > | value dec | value | 16 | 12 | 8 | 4 | 0 |
    > +-----------+-------+----+----+---+---+---+
    > | > 45312   | > b10 | 0  | b  | 1 | 0 | 0 |
    > |           | 0     |    |    |   |   |   |
    > +-----------+-------+----+----+---+---+---+
    >
-   several input mixed

> **binaryrepr 2 4 8 16 32 64 128 0xFF**
>
> > +-------+---+---+---+---+---+---+---+---+---+
> > | value | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 64  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 32  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 16  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 12  | 0 | 0 | 0 | 0 | 0 | 1 | 1 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 8   | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 4   | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> > | > 2   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
> > +-------+---+---+---+---+---+---+---+---+---+
> >

