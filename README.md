binaryrep is a utility to display position of the bits of a number.
Entries can be decimal, hexadecimal, binary or octal. Obviously with
python, there is a basic command

> &gt;&gt;&gt; bin(64) '0b1000000'

but if you want to know the position of MSB, it's not straightforward.
That's the purpose of binaryrepr. The output is formatted in
reStructuredText by default. Other shapes of output are available.

## Installation Guide

> &gt;&gt;&gt; pip install binaryrepr

#### python dependencies

-   click
-   prettytable

##### Take a look on some example.

-   a simple example (less than 256)

    **binaryrepr 64**
    
    | value | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    |-------|---|---|---|---|---|---|---|---|---|
    |   64  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

    
-   a short representation without leading zeros

    **binaryrepr 64 -s**

    | value | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    |-------|---|---|---|---|---|---|---|
    |   64  | 1 | 0 | 0 | 0 | 0 | 0 | 0 |

-   input can be hexadecimal
    
    **binaryrepr 0xFF**

    | value dec | value | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    |-----------|-------|---|---|---|---|---|---|---|---|---|
    |    255    |   ff  | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |

-   input can be binary and output hexadecimal for example

    **binaryrepr 0b100 -t hex**

    | value dec | value | 8 | 4 | 0 |
    |-----------|-------|---|---|---|
    |     4     |  100  | 0 | 0 | 4 |
    
-   several input mixed

    **binaryrepr 2 4 8 16 32 64 128 0x100**
    
    | value dec | value | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    |-----------|-------|---|---|---|---|---|---|---|---|---|
    |    256    |  100  | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    |    128    |  128  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
    |     64    |   64  | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
    |     32    |   32  | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
    |     16    |   16  | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
    |     8     |   8   | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
    |     4     |   4   | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
    |     2     |   2   | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |

-   with operator surrounded by quote
    **binaryrepr '170^85' 170 85
    | input | ffs_u8 | nlz_u8 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
    |-------|--------|--------|---|---|---|---|---|---|---|---|---|
    |  d255 |   7    |   0    | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
    |  d170 |   7    |   0    | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 | 0 |
    |  d85  |   6    |   1    | 0 | 0 | 1 | 0 | 1 | 0 | 1 | 0 | 1 |



