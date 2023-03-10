create database cadastroExercicio;
use cadastroExercicio;
show tables;

create table Funcionario(
	id int not null,
    nome varchar(45) not null,
    idade int,
    cpf char(15),
    endereco varchar(50),
    telefone varchar(15),
    DataNascimento varchar(45),
    cidade varchar(45),
    nacionalidade varchar(45),
    DataAdm varchar(45),
    salario varchar (45),
    
    
    constraint primary key (id)
);
drop table Funcionario;
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (1,'Diego Santos Silva',19,'071.749.431-44','Rua Eurendina Mendes Titara','(67) 99352-2608','Campo grande','Brasileiro','05/12/2002','10/03/2019','7.000');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (2,'Nathan Pizolito',19,'857.104.620-47','Rua joao de paulo','(67) 2977-8661','Sao paulo','Brasileiro','05/09/2003','10/02/2020','1.500');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (3,'Marina sophia','17','326.697.458-33','Rua jorge leopoldo','(67) 97663-7672','Sao Paulo','Brasileiro','13/06/2005',06/12/2020,'3.000');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (4,'João Vitor',19,'300.922.940-22','Rau doutor jivago','(67) 99146-5109','Costa Rica','Brasileiro','19/07/2003','18/07/2016','2.500');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (5,'Thiago Sandre',17,'482.483.620-43','Beco Santa Clara','(67) 97438-7452','Campo grande','Brasileiro','06/06/2005','25/01/2020','2.000');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (6,'Luan victor',18,'774.414.300-03','Rua Flamengo','(67) 97573-8522','Sao Paulo','Brasileiro','06/05/2004','26/08/2021','3.500');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (7,'Julia Ajpert',18,'804.086.640-53','Rua J','(67) 99286-1543','Costa Rica','Brasileiro','15/10/2004','18/09/2020','4.000');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (9,'Surle Martins',44,'807.209.300-22','Rua Barão do Rio Branco 8','(67) 97510-8651','Campo Grande','Brasileiro','16/03/1972','02/11/1992','2.200');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (10,'José Fernandes',35,'935.932.820-03','Rua Kelly','(67) 97439-6875','Costa Rica','Brasileiro','06/05/1987','15/04/2006','1.400');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (11,'Nathan Henrique',25,'314.742.530-40','Alameda José Orlando','(67) 97432-3272','Sao paulo','Brasileiro','06/05/1997','25/05/2010','3.200');
insert into Funcionario (id,nome,idade,cpf,endereco,telefone,cidade,nacionalidade,DataNascimento,DataAdm,salario)
values (12,'Erik Silva',30,'831.731.640-83','Rua Peroba','(67) 99468-1358','Campo grande','Brasileiro','06/05/1992','16/08/2007','1.900');

select * from Funcionario;

create table Departamento(
	id int not null,
    nomeDepartamento varchar (45),
    
    constraint primary key (id)
);

insert into Departamento(id,nomeDepartamento)
values (10,'RH');
insert into Departamento(id,nomeDepartamento)
values (20,'Arquivo');
insert into Departamento(id,nomeDepartamento)
values (30,'Almoxerifado');
insert into Departamento(id,nomeDepartamento)
values (40,'Copa');
insert into Departamento(id,nomeDepartamento)
values (50,'Protocolo');

select * from Departamento;

create table Dependentes(
	id int not null,
    nome varchar (45),
    datanascimento varchar (45),
	localnascimento varchar(45),
    idempregado varchar (45),
    numerocertidao varchar (45),
    idade varchar (45),
   
    constraint primary key (id)
);
drop table Dependentes;

insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('1','Murilo Lorenzo Fernandes','08/03/2010','12','Campo Grande','1','180081 01 55 2019 1 29475 320 8630579-54');
insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('2','Gustavo Kaique Peixoto','10/06/2009','11','São Paulo','11','104079 01 55 2011 1 29284 810 6145992-95');
insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('3','Alexandre Pietro das Neves','12/10/2005','17','Costa Rica','10','218774 01 55 2016 1 26157 651 8089068-17');
insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('4','Guilherme Matheus Márcio Barbosa','18/05/2012','10','Sao Paulo','12','245610 01 55 2018 1 06438 671 6190287-19');
insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('5','João Francisco Freitas','18/05/2002','20','Campo Grande','9','126270 01 55 2022 1 20754 102 116382-82');
insert into Dependentes(id,nome,datanascimento,idade,localnascimento,idempregado,numerocertidao)
values('6','Gustavo Guilherme Gonçalves','20/09/2020','2','Campo Grande','3','221283 01 55 2011 1 87022 265 5742288-35');

select * from  dependentes;


create table Cargos(
	id int not null,
    NomeCargo varchar (45),
    idDepartamento varchar (45),
    nomeDepartamento varchar (45),
    
    constraint primary key (id)
);
drop table Cargos;

insert into Cargos (id,NomeCargo,idDepartamento,nomeDepartamento)
values (1,'Psicologa','20','RH');
insert into Cargos (id,NomeCargo,idDepartamento,nomeDepartamento)
values (2,'Auxiliar Administrativo','10','Arquivo');
insert into Cargos (id,NomeCargo,idDepartamento,nomeDepartamento)
values (3,'Auxiliar de almoxerifado','30','Almoxerifado');
insert into Cargos (id,NomeCargo,idDepartamento,nomeDepartamento)
values (4,'Cozinheira','40','Copa');
insert into Cargos (id,NomeCargo,idDepartamento,nomeDepartamento)
values (5,'Atendente','50','Protocolo');

select * from Cargos;

-- 1 – Selecione todos os registros da tabela funcionários. 
select * from Funcionario;

-- 2 – Selecione todos os registros da tabela departamentos. 
select * from Departamento;

-- 3 – Selecione todos os registros da tabela cargos. 
select * from Cargos;

-- 4 – Selecione todos os registros da tabela dependentes. 
select * from Dependetes;

-- 5 – Atualize o salário para 6500,00 do funcionário que tiver id = 3. 
update Funcionario set salario = '6.500' where id = 3;

-- 6 – Atualize o endereço para Av. Afonso Pena, 5432 dos funcionários com id menor que 5. 
update Funcionario set endereco = 'Afonso Pena' where id < 5;

-- 7 – Selecione o nome e idade de todos os funcionários e exiba por ordem de idade decrescente. 
select nome,idade from Funcionario order by idade desc;

-- 8 – Selecione todos os registros dos funcionários e exiba por ordem de nome decrescente. 
select * from Funcionario order by nome desc;

-- 9 – Selecione todos os registros dos funcionários que tenha id seja maior que 8 e menor que 18. 
select * from Funcionario where id > 8 and id < 18;

-- 10 – Selecione todos os registros dos funcionários que tenha id seja equivalente a (1,2,8,18,21). 
select * from Funcionario where id in (1,2,8,18,21);

-- 12 – Selecione o nome e salario de todos os funcionários que o nome comece com J. 
select nome,salario from Funcionario where nome like 'j%';

-- 13 – Selecione o nome e salario de todos os funcionários que o nome termine com A.
select nome,salario from Funcionario where nome like '%a';

-- 14 – Selecione contagem de registros na tabela funcionários. 
select count(*) as contador from Funcionario;

-- 15 – Selecione o salário mínimo da tabela funcionários.
select min(salario) from Funcionario;

-- 16 – Selecione o dependente com maior idade na tabela dependentes. 
select max(idade) from Dependentes;

-- 17 – Faça a média salarial da tabela funcionários.
select sum(salario) as soma,avg(salario) as media from Funcionario;

-- 18 – Exiba a quantidade de ids dos funcionários que tem a mesma idade.​
select id from Funcionario where idade = 17;
select id from Funcionario where idade = 18;
select id from Funcionario where idade = 19;