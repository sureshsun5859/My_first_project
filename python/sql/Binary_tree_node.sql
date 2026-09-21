-- problem statement , table name BST have two columns N and P , column N have the node values and column P has the parent value for Node.
-- wrtie sql code to display leaf and inner and root values.
/*
input:
  Table : BST 
  N  P
  1  2
  3  2
  6  8
  9  8
  2  5
  8  5
  5  Null
  
expected out put :
1 Leaf
2 Inner
3 Leaf
5 Root
6 Leaf
8 Inner
9 Leaf
*/

select --*
t1.n as node ,
case when t1.p is null then 'Root'
     when t2.n is null then 'Leaf'
     when t1.N = t2.P then 'Inner'
     else 'None' end parent
 from BST t1
left join BST t2
on t1.N = t2.P
group by t1.n,
case when t1.p is null then 'Root'
     when t2.n is null then 'Leaf'
     when t1.N = t2.P then 'Inner'
     else 'None' end
order by t1.n
;


/*
Result:
1 Leaf
2 Inner
3 Leaf
4 Inner
5 Leaf
6 Inner
7 Leaf
8 Leaf
9 Inner
10 Leaf
11 Inner
12 Leaf
13 Inner
14 Leaf
15 Root
*/
