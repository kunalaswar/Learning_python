use office;

-- create table customers(customer_id int primary key auto_increment,
-- first_name varchar(20) not null,
-- last_name varchar(20) not null ,
-- age int not null,
-- country varchar(20) not null);

-- insert into customers(first_name,last_name,age,country) values
-- ('John', 'Doe', 25, 'USA'),
-- ('Alice', 'Smith', 30, 'UK'),
-- ('Bob', 'Johnson', 22, 'Canada'),
-- ('Mary', 'Williams', 28, 'Australia'),
-- ('James', 'Brown', 35, 'India');

-- create table orders(order_id int primary key ,
-- item varchar(20) not null,
-- amount int not null,
-- Customer_id int not null, 
-- foreign key (customer_id) references,
-- customers(customer_id));

-- sir 
-- create table Orders(
-- order_id int primary key,
-- item varchar(20) not null,
-- amount int not null,
-- customer_id int not null,
-- foreign key (customer_id) references 
-- customers(customer_id)
-- );

-- sir data

-- insert into orders values
-- (1,'Laptop', 1000, 3),
-- (2,'Smartphone', 500, 2),
-- (3,'Headphones', 150, 3),
-- (4,'Tablet', 300, 4),
-- (5,'Monitor', 400, 5);

-- waq to retrive first_name and item they brought
-- select t1.first_name ,t2.item
-- from customers as t1
-- inner join
-- orders as t2 on
-- t1.customer_id = t2.customer_id;


--  WAQ to print customer 

-- select t1.first_name, sum(t2.amount) from customers as t1
-- inner join orders as t2 on t1.customer_id = t2.customer_id group by t1.first_name;	


-- select t1.first_name, sum(t2.amount) from customers as t1
-- left join orders as t2 on t1.customer_id = t2.customer_id group by t1.first_name;	

select t1.first_name, sum(t2.amount) from customers as t1
right join orders as t2 on t1.customer_id = t2.customer_id group by t1.first_name;	




