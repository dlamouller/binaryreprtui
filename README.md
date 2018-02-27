binaryrep is a utility to display position of the bits of a number.
Entries can be decimal, hexadecimal, binary or octal.
obviously with python, there is a basic command

    >>> bin(64)
    '0b1000000'

but if you want to know the position of MSB, it's not straightforward. That's the purpose of binaryrepr.
The output is formatted in GitHub Flavored Markdown GFM (optionally you can indicate left, right, or center).

### Installation Guide

> pip install binaryreprtui

##### python dependencies

- click

### Take a look on some example.

- a simple example (less than 256)

	**_binaryrepr 64_**
	
 | 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |--|--|--|--|--|--|--|--|--|
 | 0| 0| 1| 0| 0| 0| 0| 0| 0|

- another example (greater than 255)

	**_binaryrepr 1024_**
	
 | 16| 15| 14| 13| 12| 11| 10| 9| 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |---|---|---|---|---|---|---|--|--|--|--|--|--|--|--|--|--|
 | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0| 0| 0| 0| 0| 0| 0| 0| 0| 0|

- a short representation without leading zeros

	**_binaryrepr 1024 -s_**

 | 10| 9| 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |---|--|--|--|--|--|--|--|--|--|--|
 | 1 | 0| 0| 0| 0| 0| 0| 0| 0| 0| 0|

- a representation can be center using option format center

	**_binaryrepr 65535 -f center -s_**

 | 15| 14| 13| 12| 11| 10| 9| 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |:-:|:-:|:-:|:-:|:-:|:-:|--|--|--|--|--|--|--|--|--|--|
 | 1 | 1 | 1 | 1 | 1 | 1 | 1| 1| 1| 1| 1| 1| 1| 1| 1| 1|

- verbose mode

  **_binaryrepr 255 -v_**

 representation of 255

 endianness: little

 position bits | 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |---|--|--|--|--|--|--|--|--|--|
 value         | 0| 1| 1| 1| 1| 1| 1| 1| 1|

- input can be decimal, binary, hexa or octal

  **_binaryrepr 0xFF_**

 | 8| 7| 6| 5| 4| 3| 2| 1| 0|
 |--|--|--|--|--|--|--|--|--|
 | 0| 1| 1| 1| 1| 1| 1| 1| 1|

- input can be binary and output hexadecimal for example

  **_binaryrepr 0b100 -t hex_**

 | 8| 4| 0|
 |--|--|--|
 | 0| 0| 4|


