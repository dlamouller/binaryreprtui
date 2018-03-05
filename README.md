binaryrep is a utility to display position of the bits of a number.
Entries can be decimal, hexadecimal, binary or octal.
obviously with python, there is a basic command

    >>> bin(64)
    '0b1000000'

but if you want to know the position of MSB, it's not straightforward. That's the purpose of binaryrepr.
The output is formatted in GitHub Flavored Markdown GFM (optionally you can indicate left, right, or center).

### Installation Guide

> pip install binaryrepr

##### python dependencies

- click
- prettytable

### Take a look on some example.

- a simple example (less than 256)

	**_binaryrepr 64_**

	+---+---+---+---+---+---+---+---+---+
	| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	+---+---+---+---+---+---+---+---+---+
	| 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
	+---+---+---+---+---+---+---+---+---+

- another example (greater than 255)

	**_binaryrepr 1024_**
	
	+----+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
	| 16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	+----+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
	| 0  | 0  | 0  | 0  | 0  | 0  | 1  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
	+----+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+

- a short representation without leading zeros

	**_binaryrepr 1024 -s_**

	+----+---+---+---+---+---+---+---+---+---+---+
	| 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	+----+---+---+---+---+---+---+---+---+---+---+
	| 1  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
	+----+---+---+---+---+---+---+---+---+---+---+

- another representation: gmf gitHub markdown format

	**_binaryrepr 1024 -f gmf -s_**

	| 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	|----|---|---|---|---|---|---|---|---|---|---|
	| 1  | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |

- another representation: noline

	**_binaryrepr 1024 -f noline -s_**

	 10  9  8  7  6  5  4  3  2  1  0 
	 1   0  0  0  0  0  0  0  0  0  0

- verbose mode

  **_binaryrepr 255 -v_**

	representation of 255
	+-------+---+---+---+---+---+---+---+---+---+
	| value | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	+-------+---+---+---+---+---+---+---+---+---+
	|  255  | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
	+-------+---+---+---+---+---+---+---+---+---+

- input can be decimal, binary, hexa or octal

  **_binaryrepr 0xFF_**

	+---+---+---+---+---+---+---+---+---+
	| 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
	+---+---+---+---+---+---+---+---+---+
	| 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
	+---+---+---+---+---+---+---+---+---+

- input can be binary and output hexadecimal for example

  **_binaryrepr 0b100 -t hex_**

	+---+---+---+
	| 8 | 4 | 0 |
	+---+---+---+
	| 0 | 0 | 4 |
	+---+---+---+


