create database marina;
use marina;
select * from cadastrar_aluno;
select * from cadastrar_funcionario;
select * from cadastrar_curso;




create table cadastrar_aluno(
	id_aluno int not null auto_increment,
    nome varchar (100),
    cpf char (15),
    nascimento char (15),
    nomeResp varchar (100),
    fone varchar (20),
    
    constraint primary key (id_aluno)
);

create table cadastrar_funcionario(
	id_funcionario int not null auto_increment,
    nome varchar (100),
    cpf char (15),
    nascimento char (15),
    cargo varchar (100),
    fone varchar(20),
    
    constraint primary key (id_funcionario)
);

create table cadastrar_curso(
	id_curso int not null auto_increment,
    nome_curso varchar (100),
    vagas varchar (20),
    carga_horaria varchar(20),
    periodo varchar (50),
    
    constraint primary key (id_curso)
);
