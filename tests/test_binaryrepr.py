#bug: input: 255 256. La valeur 255 n'est pas bonne
import pytest
from .. import binaryrepr

def test_basic():
    m = binaryrepr.getTable(('1',), 'bin', 'basic', True)
    assert len(m.x) == len(m.position)
    assert m.depth == 7
    assert m.power == 1
    m = binaryrepr.getTable(('255',), 'hex', 'basic', True)
    assert len(m.x) == len(m.position)
    assert m.depth == 7
    assert m.power == 4
    m = binaryrepr.getTable(('256',), 'oct', 'basic', True)
    assert len(m.x) == len(m.position)
    assert m.depth == 15
    assert m.power == 3
    for f in ['basic', 'gfm', 'noline', 'nohrules']:
        m = binaryrepr.getTable(('256',), 'oct', f, False)
        assert len(m.x) == len(m.position)
        assert m.depth == 15
        assert m.power == 3

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1',), 'bin', 'basic', 0, """+-------+--------+--------+---+---+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d1  |   0    |   7    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
+-------+--------+--------+---+---+---+---+---+---+---+---+"""),
        (('1',), 'bin', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
        (('1',), 'hex', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
        (('1',), 'oct', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""
)
    ]
    )
def test_Onebasic(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1',), 'bin', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
        (('1',), 'bin', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d1     0       7     1 """),
        (('1',), 'hex', 'gfm', 1, """| input | ffs_u8 | nlz_u8 | 0 |
|-------|--------|--------|---|
|   d1  |   0    |   7    | 1 |"""),
        (('1',), 'oct', 'nohrules', 1, """| input | ffs_u8 | nlz_u8 | 0 |
|   d1  |   0    |   7    | 1 |"""
)
    ]
    )
def test_Oneformat(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1',), 'bin', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
        (('1',), 'hex', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
        (('1',), 'oct', 'basic', 1, """+-------+--------+--------+---+
| input | ffs_u8 | nlz_u8 | 0 |
+-------+--------+--------+---+
|   d1  |   0    |   7    | 1 |
+-------+--------+--------+---+"""),
    ]
    )
def test_Onetyperepr(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('2',), 'bin', '', 1, """+-------+--------+--------+---+---+
| input | ffs_u8 | nlz_u8 | 1 | 0 |
+-------+--------+--------+---+---+
|   d2  |   1    |   6    | 1 | 0 |
+-------+--------+--------+---+---+"""),
        (('2',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+
| input | ffs_u8 | nlz_u8 | 1 | 0 |
+-------+--------+--------+---+---+
|   d2  |   1    |   6    | 1 | 0 |
+-------+--------+--------+---+---+"""),
        (('4',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+
| input | ffs_u8 | nlz_u8 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+
|   d4  |   2    |   5    | 1 | 0 | 0 |
+-------+--------+--------+---+---+---+"""),
        (('8',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+
|   d8  |   3    |   4    | 1 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+"""),
        (('16',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+
|  d16  |   4    |   3    | 1 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+"""),
        (('32',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+
|  d32  |   5    |   2    | 1 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+"""),
        (('64',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+
|  d64  |   6    |   1    | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+"""),
        (('128',), 'bin', 'basic', 1, """+-------+--------+--------+---+---+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d128 |   7    |   0    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+"""),
        (('256',), 'bin', 'basic', 1, """+-------+---------+---------+---+---+---+---+---+---+---+---+---+
| input | ffs_u16 | nlz_u16 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+---------+---------+---+---+---+---+---+---+---+---+---+
|  d256 |    8    |    7    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+---------+---------+---+---+---+---+---+---+---+---+---+"""),
        (('65535',), 'bin', 'basic', 1, """+--------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
| input  | ffs_u16 | nlz_u16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+--------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
| d65535 |    15   |    0    | 1  | 1  | 1  | 1  | 1  | 1  | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+--------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+"""),
    ]
    )
def test_power2_bin(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('2',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d2     1       6     2 """),
        (('4',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d4     2       5     4 """),
        (('8',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  3  0 
   d8     3       4     1  0 """),
        (('16',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  3  0 
  d16     4       3     2  0 """),
        (('32',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  3  0 
  d32     5       2     4  0 """),
        (('64',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  6  3  0 
  d64     6       1     1  0  0 """),
        (('128',), 'oct', 'noline', 1, """ input  ffs_u8  nlz_u8  6  3  0 
  d128    7       0     2  0  0 """),
        (('65535',), 'oct', 'noline', 1, """ input   ffs_u16  nlz_u16  15  12  9  6  3  0 
 d65535     15       0     1   7   7  7  7  7 """),
    ]
)
def test_power2_oct(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('2',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d2     1       6     2 """),
        (('4',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d4     2       5     4 """),
        (('8',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  0 
   d8     3       4     8 """),
        (('16',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  4  0 
  d16     4       3     1  0 """),
        (('32',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  4  0 
  d32     5       2     2  0 """),
        (('64',), 'hex', 'noline', 1, """ input  ffs_u8  nlz_u8  4  0 
  d64     6       1     4  0 """),
        (('256',), 'hex', 'noline', 1, """ input  ffs_u16  nlz_u16  8  4  0 
  d256     8        7     1  0  0 """),
        (('65536',), 'hex', 'noline', 1, """ input   ffs_u32  nlz_u32  16  12  8  4  0 
 d65536     16       15    1   0   0  0  0 """),
    ]
)
def test_power2_hex(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1', '2', '4', '8', '16', '32', '64', '128', '255'), 'bin', 'basic', 0, """+-------+--------+--------+---+---+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d1  |   0    |   7    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d2  |   1    |   6    | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d4  |   2    |   5    | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d8  |   3    |   4    | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d16  |   4    |   3    | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d32  |   5    |   2    | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d64  |   6    |   1    | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d128 |   7    |   0    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d255 |   7    |   0    | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+-------+--------+--------+---+---+---+---+---+---+---+---+"""),
        (('255', '128', '64', '32', '16', '8', '4', '2', '1'), 'bin', 'basic', 0, """+-------+--------+--------+---+---+---+---+---+---+---+---+
| input | ffs_u8 | nlz_u8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d255 |   7    |   0    | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d128 |   7    |   0    | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d64  |   6    |   1    | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d32  |   5    |   2    | 0 | 0 | 1 | 0 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|  d16  |   4    |   3    | 0 | 0 | 0 | 1 | 0 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d8  |   3    |   4    | 0 | 0 | 0 | 0 | 1 | 0 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d4  |   2    |   5    | 0 | 0 | 0 | 0 | 0 | 1 | 0 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d2  |   1    |   6    | 0 | 0 | 0 | 0 | 0 | 0 | 1 | 0 |
+-------+--------+--------+---+---+---+---+---+---+---+---+
|   d1  |   0    |   7    | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 1 |
+-------+--------+--------+---+---+---+---+---+---+---+---+"""),
    ]
)
def test_multi_bin(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected


@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1', '1<<4', '1<<8', '1<<16'), 'hex', 'basic', 0, """+--------+---------+---------+----+----+----+----+----+---+---+---+
| input  | ffs_u32 | nlz_u32 | 28 | 24 | 20 | 16 | 12 | 8 | 4 | 0 |
+--------+---------+---------+----+----+----+----+----+---+---+---+
|   d1   |    0    |    31   | 0  | 0  | 0  | 0  | 0  | 0 | 0 | 1 |
+--------+---------+---------+----+----+----+----+----+---+---+---+
|  d16   |    4    |    27   | 0  | 0  | 0  | 0  | 0  | 0 | 1 | 0 |
+--------+---------+---------+----+----+----+----+----+---+---+---+
|  d256  |    8    |    23   | 0  | 0  | 0  | 0  | 0  | 1 | 0 | 0 |
+--------+---------+---------+----+----+----+----+----+---+---+---+
| d65536 |    16   |    15   | 0  | 0  | 0  | 1  | 0  | 0 | 0 | 0 |
+--------+---------+---------+----+----+----+----+----+---+---+---+"""),
    ]
)
def test_multi_hex(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('1', '1<<16', '1<<8', '1<<4'), 'oct', 'basic', 0, """+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+
| input  | ffs_u32 | nlz_u32 | 30 | 27 | 24 | 21 | 18 | 15 | 12 | 9 | 6 | 3 | 0 |
+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+
|   d1   |    0    |    31   | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 0 | 0 | 1 |
+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+
| d65536 |    16   |    15   | 0  | 0  | 0  | 0  | 0  | 2  | 0  | 0 | 0 | 0 | 0 |
+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+
|  d256  |    8    |    23   | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 4 | 0 | 0 |
+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+
|  d16   |    4    |    27   | 0  | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 0 | 2 | 0 |
+--------+---------+---------+----+----+----+----+----+----+----+---+---+---+---+"""),
    ]
)
def test_multi_oct(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected

@pytest.mark.parametrize(
    'val, repr, format, short, expected',
    [
        (('255', '256'), 'bin', 'basic', 0, """+-------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
| input | ffs_u16 | nlz_u16 | 15 | 14 | 13 | 12 | 11 | 10 | 9 | 8 | 7 | 6 | 5 | 4 | 3 | 2 | 1 | 0 |
+-------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
|  d255 |    7    |    8    | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 0 | 1 | 1 | 1 | 1 | 1 | 1 | 1 | 1 |
+-------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+
|  d256 |    8    |    7    | 0  | 0  | 0  | 0  | 0  | 0  | 0 | 1 | 0 | 0 | 0 | 0 | 0 | 0 | 0 | 0 |
+-------+---------+---------+----+----+----+----+----+----+---+---+---+---+---+---+---+---+---+---+"""),
    ]
)
def test_multi_above8bits(val, repr, format, short, expected ):
    m = binaryrepr.getTable(val, repr, format, short)
    assert str(m) == expected
