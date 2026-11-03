
Q1: please parse the given string into rows using sql query, dont use build in functions liek regular expressions or string splitting functions. You can achieve this by using a recursive common table expression (CTE) to split the string into rows based on a delimiter..

ANS: 
WITH RECURSIVE split_string AS (
    -- Anchor member: Start with the first character and the rest of the string
    SELECT 
        SUBSTRING('suresh', 1, 1) AS character, 
        SUBSTRING('suresh', 2) AS remaining_string
    
    UNION ALL
    
    -- Recursive member: Pull the next character from the remaining string
    SELECT 
        SUBSTRING(remaining_string, 1, 1), 
        SUBSTRING(remaining_string, 2)
    FROM 
        split_string
    WHERE 
        remaining_string <> '' AND remaining_string IS NOT NULL
)
SELECT character FROM split_string;

