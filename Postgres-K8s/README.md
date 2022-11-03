This is a Postgres database project that is using AWS RDS. So first of all you should create database and tables on RDS Postgres DB. For this, you can use another EC2 instances that is installed postgres client. And to database connection, you should import SQLAlchemy lib. 

This is a first step of project. We can only add data. After finishing project, we will run CRUD operations. And then project will be run on the Kubernetes Cluster. 

Usable commands

# psql -p 5432 -h db.c4qk1p7b0x.us-east-1.rds.amazonaws.com -U postgres dbname    // to connect RDS DB
# \l+    show all database
# \dt    show tables
# create table employees (id serial PRIMARY KEY, name  VARCHAR ( 50 ) , surname VARCHAR ( 50 ) ,  age VARCHAR ( 50 ) , email VARCHAR ( 50 ) UNIQUE NOT NULL );
# SELECT name FROM employees;
# SELECT surname FROM employees;
# SELECT age  FROM employees;
# SELECT email  FROM employees;


