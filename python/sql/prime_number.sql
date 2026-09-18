-- the below in my sql 
with recursive number as (
    select 2 as num
    union
    select num + 1 
    from number
    where num < 1000
),
prime as (
    select n1.num
    from number as n1
    where not exists (
        select num from number as n2
        where n2.num < n1.num and n1.num % n2.num = 0
    )
)
select group_concat(num separator "&") from prime;

--same above code in oracle 
WITH numbers (num) AS (
    SELECT 2 FROM dual
    UNION ALL
    SELECT num + 1 
    FROM numbers
    WHERE num < 1000
),
prime AS (
    SELECT n1.num
    FROM numbers n1
    WHERE NOT EXISTS (
        SELECT 1 
        FROM numbers n2
        WHERE n2.num < n1.num 
          AND MOD(n1.num, n2.num) = 0
    )
)
SELECT LISTAGG(num, '&') WITHIN GROUP (ORDER BY num) AS prime_numbers 
FROM prime;
