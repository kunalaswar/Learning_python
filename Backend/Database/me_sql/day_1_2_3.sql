-- create database school;
use school;

-- create table student (sid int,sname varchar(50),sfee decimal(10,2));

-- add  column gerder into the table 

-- this command only for alter 

-- add students 	email column
-- alter table students add gender char(1);

-- 
-- alter table students add column phno char(10) after sname

-- rename a column 
-- alter table students change sfee fee int;

-- delete a column
-- alter table students drop gender 

-- Delete hole the database 
-- drop database school

-- Delete the table 
-- drop table student;

-- truncate table students

-- DML COMMAND 
-- insert the data into the table
-- insert into students values(23,"raj",525525,25.23)


-- insert nultiple data into the table
-- insert into students values
-- (22,"aaa",545526,26.23),
-- (23,"bbb",545527,27.23),
-- (24,"ccc",545528,28.23);

-- insert into students values(6,"raj7",9012345678,90.90)

-- 10 - 02 - 2025 ---------------------------------------------------------------------


-- 11 -02 -2025 --------------------------------------------------------------------

use office;
-- select * from employees;
-- insert into employees(ename,age,salary )values("shekar",18,12000);

-- update che query

-- update employees set salary  = 15000
-- where ename = 'shekar';

-- change eid 107 's country as united states 

-- update employees set country = 'united states' 
-- where eid = 107;

-- DELETE :commands

-- delete from employees where ename = 'jay'; -- purna jay delete karate 
-- delete from employees where eid = 103;

-- delete from employees where eid = 108;
-- delete from employees where eid = 109;

-- 

-- select * from employees ;
-- select ename,age from employees;

-- select age from employees;
-- select eid from employees;


-- select specific data by using clauses
-- select ename,age from employees where age>17;
-- 
-- write a SQL query to print names of employees from India
-- select ename from employees where country ="India";


-- 
use office;
-- opeartor
-- select 2%3

-- select * from employees where age is null;
-- select * from employees where age is not null;

-- waq to show all people whose name staart with "p"

-- select * from employees where ename like 'p%';

-- select * from employees where ename like '%r';

-- WAQ to show all people whose second letter is a 

-- select * from employees where ename like '_a%'
-- select * from employees where ename like '%k__';




























