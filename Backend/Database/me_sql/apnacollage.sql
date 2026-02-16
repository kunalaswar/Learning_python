-- create database if not exists collage;

-- drop database if exists company;

-- show databases;



-- use collage;
-- show tables;

-- create database student;

use student;
-- create table students (rollno int primary key, name varchar(50));

-- insert into students 
-- values(101,"karan"),(102,"harsh");

--  primary key 


--  foreign key
create table tmep(cust_id int foreign key (cust_id) references customer (id))







