CREATE SCHEMA `mydb` ;
use mydb;
create table todo( 
id int auto_increment,
task char(100),
primary key(id)
);

select * from todo;

insert into todo (task) values ('buy fruits');

insert into todo (task) values ('buy books');