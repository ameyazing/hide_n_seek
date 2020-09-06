# hide_n_seek
Python solution for Hide N Seek game
(https://www.amazon.in/METRO-TOYS-GIFT-%E0%A4%B9%E0%A4%BE%E0%A4%88%E0%A4%A1-%E0%A4%9C%E0%A4%82%E0%A4%97%E0%A4%B2/dp/B082XG436C/ref=sr_1_1?dchild=1&keywords=hide+n+seek+game&qid=1599403886&sr=8-1)

How to run the program?
python3 hide_n_seek.py

How to interpret the output?
+----+----+
| Q1 | Q2 |
+----+----+
| Q4 | Q3 |
+----+----+

Piece1, Piece2, Piece3, Piece4 map to Q1, Q2, Q3, Q4 respectively
Within each quadrant, positions are considered as follows:
+---------+
| 1     2 |
|    0    |
| 4     3 |
+---------+
Place pieces which only uncover 1 in respective piece arrays.
