
-- 12-02-2025
-- print all the emoloyee from emoployee table
use office;
-- select * from employees;

-- select ename,age from employees;
-- print all emoloyees whose salary is greater than 20k
-- select * from employees where salary >= 20000;

-- print all employees whose age not null
-- select * from employees where age!=null;
-- select * from employees where age!='null';
-- select * from employees where age is not null;
-- print all employee 
-- select * from employees where ename like '_a%';

-- select * from employees where 	salary between 20000 and 30000;
	
-- print all employee details whose 
-- select * from employees where ename in ('jay','shekar');    

-- print all employees from "India" alphabetically 
-- select * from employees where country = "India" order by ename;

-- select * from employees where country = "India"order by ename desc;


-- print all employees whose salary is getater then 25k

-- select * from employees where salary>20000 order by salary desc;

-- print name ,age of Highest salary employees

-- select ename ,age from employees order by salary desc
-- limit 1;

-- INSERT INTO employees (eid, ename, salary, age, country) VALUES
-- (1, 'Alice', 55000.00, 30, 'USA'),
-- (2, 'Bob', 60000.00, 35, 'india'),
-- (3, 'Charlie', 50000.00, 28, 'india'),
-- (4, 'David', 70000.00, 40, 'Australia'),
-- (5, 'Eve', 65000.00, 32, 'India');


-- print second highest salary employees details
-- select * from employees 
-- order by salary desc limit 2 offset 1; 

-- select * from employees 
-- order by salary desc limit 1 offset 1;


-- count number of people Based on there country
-- select country,count(country) from employees group by country ;


-- select * from Employees;
-- rename table employees to employee;
-- rename table employee to employees;

-- alter table employees add mno bigint;









