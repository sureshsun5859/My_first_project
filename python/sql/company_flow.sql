
--My Solution

select a.company_code, a.founder, count(distinct b.Lead_manager_code) ,
 count(distinct c.senior_Manager_code), count(distinct d.Manager_code),count(distinct e.Employee_code) 
from company a
inner join Lead_Manager b on a.company_code = b.company_code
inner join senior_Manager c on b.Lead_manager_code = c.Lead_manager_code
inner join Manager d on c.senior_Manager_code = d.senior_Manager_code
inner join Employee e on d.Manager_code = e.Manager_code
group by a.company_code, a.founder
order by a.company_code ;

--another people solution which is more simple and easy to understand, less join not traditional way
SELECT company_code, (SELECT founder FROM Company WHERE company_code = e.company_code), COUNT(DISTINCT(lead_manager_code)), COUNT(DISTINCT(senior_manager_code)), COUNT(DISTINCT(manager_code)), COUNT(DISTINCT(employee_code)) 
FROM Employee e
GROUP BY company_code
ORDER BY company_code;

--ther below is more effieciten just used the two tables, company and employee, and used the join to get the founder from company table
SELECT c.company_code, c.founder, COUNT(DISTINCT e.lead_manager_code), 
COUNT(DISTINCT e.senior_manager_code), COUNT(DISTINCT e.manager_code), 
COUNT(DISTINCT e.employee_code) FROM company c JOIN employee e 
ON c.company_code = e.company_code GROUP BY c.company_code, c.founder 
ORDER BY c.company_code ASC;