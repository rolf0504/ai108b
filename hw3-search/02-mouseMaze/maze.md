# Find a route using dfs
Executed result:
```
Map:
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ 
                  ■
■ ■ ■ ■ ■ ■ ■   ■ ■
■                 ■
■   ■ ■   ■ ■ ■ ■ ■
■     ■   ■       ■
■   ■ ■   ■   ■   ■
■   ■ ■ ■ ■   ■   ■
■             ■   ■
■ ■ ■ ■ ■ ■ ■ ■   ■
=============START=============
Step:  1
■■■■■■■■■■
0        ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  2
■■■■■■■■■■
00       ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  3
■■■■■■■■■■
000      ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  4
■■■■■■■■■■
0000     ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  5
■■■■■■■■■■
00000    ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  6
■■■■■■■■■■
000000   ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  7
■■■■■■■■■■
0000000  ■
■■■■■■■ ■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  8
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■        ■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  9
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■       0■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  10
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■      00■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  11
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■     000■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  12
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■    0000■
■ ■■ ■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  13
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■    0000■
■ ■■0■■■■■
■  ■ ■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  14
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■    0000■
■ ■■0■■■■■
■  ■0■   ■
■ ■■ ■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  15
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■    0000■
■ ■■0■■■■■
■  ■0■   ■
■ ■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  16
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■  0 0000■
■ ■■0■■■■■
■  ■0■   ■
■ ■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  17
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■ ■■0■■■■■
■  ■0■   ■
■ ■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  18
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■  ■0■   ■
■ ■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  19
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■ ■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  20
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■ ■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  21
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■      ■ ■
■■■■■■■■ ■

Step:  22
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■ 0    ■ ■
■■■■■■■■ ■

Step:  23
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■00    ■ ■
■■■■■■■■ ■

Step:  24
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■000   ■ ■
■■■■■■■■ ■

Step:  25
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■0000  ■ ■
■■■■■■■■ ■

Step:  26
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■ ■ ■
■00000 ■ ■
■■■■■■■■ ■

Step:  27
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■0■ ■
■00000 ■ ■
■■■■■■■■ ■

Step:  28
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■ ■ ■
■0■■■■0■ ■
■000000■ ■
■■■■■■■■ ■

Step:  29
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■   ■
■0■■0■0■ ■
■0■■■■0■ ■
■000000■ ■
■■■■■■■■ ■

Step:  30
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■0  ■
■0■■0■0■ ■
■0■■■■0■ ■
■000000■ ■
■■■■■■■■ ■

Step:  31
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■00 ■
■0■■0■0■ ■
■0■■■■0■ ■
■000000■ ■
■■■■■■■■ ■

Step:  32
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■00 ■
■0■■0■0■0■
■0■■■■0■ ■
■000000■ ■
■■■■■■■■ ■

Step:  33
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■00 ■
■0■■0■0■0■
■0■■■■0■0■
■000000■ ■
■■■■■■■■ ■

Step:  34
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■00 ■
■0■■0■0■0■
■0■■■■0■0■
■000000■0■
■■■■■■■■ ■

Step:  35
■■■■■■■■■■
0000000  ■
■■■■■■■0■■
■ 00 0000■
■0■■0■■■■■
■ 0■0■00 ■
■0■■0■0■0■
■0■■■■0■0■
■000000■0■
■■■■■■■■0■
```