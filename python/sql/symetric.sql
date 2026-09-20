
--to print the symetric number from table with two columns x, y
select 
    t1.x , t1.y 
       from Functions t1, Functions t2
where 
t1.x = t2.y
and t1.y = t2.x
group by t1.x, t1.y
having t1.x < t1.y or  count(*) > 1
order by t1.x 
;
