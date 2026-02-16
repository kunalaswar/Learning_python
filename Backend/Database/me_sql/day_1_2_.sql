-- 06 -02-2025

-- create database collage;
use collage;
-- create table teachers(tid int,tname varchar(100),gender char(1),doj date);
-- 
-- change the table name from this Query
-- rename table teachers to faculty;

-- Add the column name to table
-- alter table faculty add tsalary decimal(10,2);

-- Add the column name tage to table
-- alter table faculty add (tage int);

-- change the column name to that table
-- alter table faculty change tsalary sal decimal(10.2);

--  drop the column name from table 
-- alter table faculty drop column sal;

-- add the column after specific column 
-- alter table faculty add tsalary decimal(10,2) after tname;

-- alter table faculty drop tsalary;

-- 07-02-2025 -----------------------------------------------------------------
-- drop database school;

-- create database school;
use school;

-- create table students(sid int,sname varchar(30),email varchar(50),phoneno int);

-- add column students
-- alter table students add gender char(1);

-- add phno after sname
-- alter table students add phno int after sname;

-- rename column name 
-- alter table students change phno phoneno int;

-- drop table faculty;
use collage;
-- drop table faculty;

use school;
-- drop the database
-- drop database school;

-- create database	 school;
use school;
-- create table students(sid int,sname varchar(100),phno int,email varchar(30));

--  Add the data to the students table
-- insert into students values (10,'karna',9988,'kr@gamil.com');

-- truncate table students;

-- insert into students values(10,'karna',9988,'kr@gamil.com'),(20,"jay",4444,"jay@gamilcom"),
-- (30,"hanuman",5555,"htmope@gmail.com");

-- 09-02-2025-----------------------------------------------------------------
-- drop VS truncate
-- PRIMARY KEY AND FOREIGN KEY
-- unique one null values

-- create database office;
use office;

-- create table employees(eid int,ename varchar(30),gender char(1),
-- salary decimal(10,2),doj date);

-- insert into employees values(101,"karan","M",50000,"2025-01-15");
-- drop table employees;


-- create table employees(eid int primary key,ename varchar(30)not null,age int check (age>=18),
-- country varchar(30) default "India",salary decimal(10,2));

-- insert into employees values (101,"rexon",18,"India",20000);

-- alter table employees change eid eid int auto_increment;

-- insert a perticular column of the table
-- insert into employees (ename,age,salary ) values ('jay',20,3000);

use school;

-- create table teacher (tid int auto_increment primary key ,tname varchar(30) not null,
-- phno bigint not null,
-- country varchar(30) default "India",salary int check (salary >=20000));

-- insert into teacher values(101,"ankit",99123456,"India",30000);

























