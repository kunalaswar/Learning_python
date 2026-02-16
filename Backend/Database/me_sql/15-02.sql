-- waq to print every cunstomer name with product they brought
use office;
-- select t1.first_name,t2.item 
-- from customers as t1 inner join
-- orders as t2 on   -- where pan lehala tar chalate vatate
-- t1.customer_id = t2.customer_id;


-- select t1.first_name ,t2.item 
-- from customers as t1 outer join
-- orders as t2 on
-- t1.customer_id = t2.customer_id;


-- give me the list of country who have only to people

-- insert into employees values(110,"john",25,"japan",54000)

-- INSERT INTO employees VALUES
-- (1, "Liam", 32, "USA", 62000),
-- (2, "Olivia", 28, "Canada", 58000),
-- (3, "Noah", 35, "UK", 70000),
-- (4, "Emma", 24, "Australia", 55000),
-- (5, "William", 40, "Germany", 80000),
-- (6, "Ava", 29, "France", 60000),
-- (7, "James", 31, "USA", 57000),
-- (8, "Isabella", 26, "Canada", 52000),
-- (9, "Ethan", 38, "UK", 75000),
-- (10, "Mia", 27, "Australia", 59000),
-- (11, "Alexander", 33, "Germany", 65000),
-- (12, "Charlotte", 25, "France", 50000),
-- (13, "Benjamin", 42, "USA", 85000),
-- (14, "Amelia", 30, "Canada", 63000),
-- (15, "Daniel", 36, "UK", 72000),
-- (16, "Harper", 23, "Australia", 48000),
-- (17, "Michael", 39, "Germany", 78000),
-- (18, "Abigail", 28, "France", 61000),
-- (19, "Jackson", 34, "USA", 68000),
-- (20, "Sofia", 27, "Canada", 56000);


-- select country from employees group by country;

-- divide stu based on gender avg their marks print only their averaage is greater than 85

-- select gender ,avg(smarks ) from students group by gender having avg(smarks)>85;


-- subqueries

-- select max(salary) from employees where country =	"india";

-- select ename salary from employees where salary(select )


-- print list of studetns sname marks hwhose matrk is greater 
-- than average male studetents name

select avg(marks) form studetns
group by gender having gender ="m";










