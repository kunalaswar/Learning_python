use office;

-- select * from employees 
-- where country = "India" order by ename desc;

-- select * from employees order by salary desc limit 2 offset 1;

-- create table students(rno int primary key auto_increment,
-- sname varchar(20) not null,
-- smarks int ,gender char(1));

-- insert into students values (12,"raj",55,"F");

/*INSERT INTO students VALUES
(1, "Aarav", 90, 'M'),
(2, "Anika", 85, 'F'),
(3, "Vivaan", 78, 'M'),
(4, "Adhira", 92, 'F'),
(5, "Ishaan", 65, 'M'),
(6, "Siya", 88, 'F'),
(7, "Reyansh", 72, 'M'),
(8, "Dhriti", 95, 'F'),
(9, "Kabir", 80, 'M'),
(10, "Avyaan", 75, 'M'),
(11, "Samaira", 89, 'F'),
(21, "Raj", 55, 'M'),
(13, "Diya", 91, 'F'),
(14, "Arjun", 68, 'M'),
(15, "Aanya", 82, 'F'),
(16, "Vihaan", 70, 'M'),
(17, "Navya", 93, 'F'),
(18, "Atharv", 77, 'M'),
(19, "Anaya", 87, 'F'),
(20, "Shaurya", 62, 'M');*/

-- select * from students;

-- select gender ,count(gender) from students group by gender;



-- write a query how many people from which country

-- select country ,count(country) from employees group by country;

-- select gender from students group by gender;

-- WAQ to print who many items sold per category


-- WAQ to print total marks achived by students for a perticular group 

-- select sum(smarks) from students group by gender;

-- select gender,sum(smarks) from students group by gender;

-- what is the average marks in the girls

-- select gender,avg(smarks) from students group by gender;
-- select 

-- write a query to print maximun marks of students basesonthe there score
-- select gender ,max(smarks) from students group by gender;

-- select min che query

-- select count(distinct gender) from students;

-- write a query print name of employees from different country along with different county count

-- select country,count(country) from employees group by country;

-- select country ,count(country), group_concat(ename) from employees 
-- group by country;




