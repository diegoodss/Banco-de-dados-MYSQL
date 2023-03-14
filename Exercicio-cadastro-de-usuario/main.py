import os
import mysql.connector

con = mysql.connector.connect(host = '',
                              database = 'marina',
                              user = 'root',
                              password = '')


if con.is_connected():
    bd_info = con.get_server_info()
    print('Banco de dados esta conectando = ', bd_info)

def cadastrar_aluno():
    cpf = input('CPF: ')
    nome = input('Nome: ')
    nascimento = input('Data de nascimento: ')
    fone = input('Telefone do responsável: ')
    nomeResp= input('Nome do Responsável: ')
    comandoCadAluno = f'''insert into cadastrar_aluno(cpf,nome,nascimento,fone,nomeResp) values ('{cpf}','{nome}','{nascimento}','{fone}','{nomeResp}')'''
    cursor = con.cursor ()
    cursor.execute(comandoCadAluno)
    con.commit()

def cadastrar_funcionario():
    cpf_func = input('CPF: ')
    nome_func = input('Nome: ')
    nascimento = input('Data de nascimento: ')
    fone = input('Telefone: ')
    cargo= input('Cargo: ')
    comandoCadFuncionario = f'''insert into cadastrar_funcionario(cpf,nome,nascimento,fone,cargo) values ('{cpf_func}','{nome_func}','{nascimento}','{fone}','{cargo}')'''
    cursor = con.cursor ()
    cursor.execute(comandoCadFuncionario)
    con.commit()

def cadastrar_curso():
    nome_curso = input('Nome do curso: ')
    vagas = input('Vagas: ')
    carga_horaria = input('Carga Horária: ')
    periodo = input('Período: ')
    comandoCadCurso = f'''insert into cadastrar_curso(nome_curso,vagas,carga_horaria,periodo) values ('{nome_curso}','{vagas}','{carga_horaria}','{periodo}')'''
    cursor = con.cursor ()
    cursor.execute(comandoCadCurso)
    con.commit()

def relatorio_aluno():
    consulta_sql = 'select * from cadastrar_aluno'
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print('Numero total de registros retornados: ',cursor.rowcount)
    print('Mostrando os Registros')
    for linha in linhas:
        print('ID  = ',linha[0])
        print('Nome = ',linha[1])
        print('CPF = ',linha[2])
        print('Data de Nascimento = ',linha[3])
        print('Nome do responsável = ',linha[4])
        print('Telefone = ',linha[5])
        os.system('pause')
        os.system('cls')

def relatorio_funcionario():
    consulta_sql = 'select * from cadastrar_funcionario'
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print('Número total de registros retornados: ',cursor.rowcount)
    print('Mostrando os Registros')
    for linha in linhas:
        print('ID  = ',linha[0])
        print('Nome = ',linha[1])
        print('CPF = ',linha[2])
        print('Data de nascimento = ',linha[3])
        print('Cargo = ',linha[4])
        print('Telefone = ',linha[5])
        os.system('pause')
        os.system('cls')
        voltar = int(input(':'))

def relatorio_curso():
    consulta_sql = 'select * from cadastrar_curso'
    cursor = con.cursor()
    cursor.execute(consulta_sql)
    linhas = cursor.fetchall()
    print('Número total de registros retornados: ',cursor.rowcount)
    print('Mostrando os Registros')
    for linha in linhas:
        print('ID  = ',linha[0])
        print('Nome = ',linha[1])
        print('Vagas = ',linha[2])
        print('Carga Horaria = ',linha[3])
        print('Período = ',linha[4])
        os.system('pause')
        os.system('cls')

def main():
    escolhas = 1
    op = 0
    while escolhas !=5:
        print('1- Opções para Aluno')
        print('2- Opções para Funcionário')
        print('3- Opções para Curso')
        print('4- Encerrar')
        escolhas = int(input(':'))
        os.system('cls')
        if escolhas == 1:
            while op !=6 :
                print('1- Incluir Aluno: ')
                print('2- Editar: ')
                print('3- Relatório: ')
                print('4- Voltar: ')
                op = int(input(':'))
                os.system('cls')
                if op == 1:
                    cadastrar_aluno()
                    os.system('cls')
                while op == 2:
                    consulta_sql = 'select * from cadastrar_aluno'
                    cursor = con.cursor()
                    cursor.execute(consulta_sql)
                    linhas = cursor.fetchall()
                    print('Número total de registros retornados: ',cursor.rowcount)
                    print('Mostrando os Registros')
                    for linha in linhas:
                        print('ID  = ',linha[0])
                        print('Nome = ',linha[1])
                        print('CPF = ',linha[2])
                        print('Data de nascimento = ',linha[3])
                        print('Responsável = ',linha[4])
                        print('Fone responsável = ',linha[5],'\n')
                    
                    escID = int(input("Qual o ID do aluno que deseja realizar as mudanças? "))
                    os.system('cls')
                    print('\n1- Nome')
                    print('2- CPF')
                    print('3- Data de nascimento')
                    print('4- Responsável')
                    print('5- Fone responsável')
                    print('6- Deletar''\n')
                    esc = int(input("Qual é a informação que gostaria de alterar? "))
                    
                    if esc == 1:
                        
                        mudNome = input("Qual nome deseja colocar? ")
                        comandoEditAluno = f'update cadastrar_aluno set nome = "{mudNome}" where id_aluno = {escID}'
                        cursor = con.cursor ()
                        cursor.execute(comandoEditAluno)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 2:
                        
                        mudCPF = input("Qual CPF deseja colocar? ")
                        comandoEditAluno = f'update cadastrar_aluno set cpf = "{mudCPF}" where id_aluno = {escID}'
                        cursor = con.cursor ()
                        cursor.execute(comandoEditAluno)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 3:
                        
                        mudDataNasc = input("Qual a data de nascimento que deseja colocar? ")
                        comandoEditAluno = f'update cadastrar_aluno set nascimento = "{mudDataNasc}" where id_aluno = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditAluno)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 4:
                        
                        mudNomeResp = input("Qual nome de responsável deseja colocar? ")
                        comandoEditAluno = f'update cadastrar_aluno set nomeResp = "{mudNomeResp}" where id_aluno = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditAluno)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 5:
                        
                        mudFone = input("Qual o número de telefone deseja colocar?")
                        comandoEditAluno = f'update cadastrar_aluno set fone = "{mudFone}" where id_aluno = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditAluno)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 6:
                        fechaDelete = int(input("Deseja mesmo deletar esse usuário? Se sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaDelete !=1:
                            break
                        comandoDelAluno = f'delete from cadastrar_aluno where id_aluno = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoDelAluno)
                        con.commit()
 
                if op == 3:
                    relatorio_aluno()
                if op == 4:
                    break
                
        elif escolhas == 2:
            while op!=6:
                print('1- Incluir Funcionário: ')
                print('2- Editar: ')
                print('3- Relatório: ')
                print('4- Voltar: ')
                op = int(input(':'))
                os.system('cls')
                if op ==1:
                    cadastrar_funcionario()
                    os.system('cls')
                while op == 2:
                    consulta_sql = 'select * from cadastrar_funcionario'
                    cursor = con.cursor()
                    cursor.execute(consulta_sql)
                    linhas = cursor.fetchall()
                    print('Número total de registros retornados: ',cursor.rowcount)
                    print('Mostrando os Registros')
                    for linha in linhas:
                        print('ID  = ',linha[0])
                        print('Nome = ',linha[1])
                        print('CPF = ',linha[2])
                        print('Data de nascimento = ',linha[3])
                        print('Cargo = ',linha[4])
                        print('Telefone = ',linha[5], '\n')
                    
                    escID = int(input("Qual o ID do funcionário que deseja realizar mudanças? "))
                    os.system('cls')
                    print('\n1- Nome')
                    print('2- CPF')
                    print('3- Data de nascimento')
                    print('4- Cargo')
                    print('5- Telefone')
                    print('6- Deletar''\n')
                    esc = int(input("Qual é a informação que gostaria de alterar? "))
                    
                    if esc == 1:
                        
                        mudNome = input("Qual nome deseja colocar?")
                        comandoEditFunc = f'update cadastrar_funcionario set nome = "{mudNome}" where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditFunc)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 2:
                        
                        mudCPF = input("Qual CPF deseja colocar? ")
                        comandoEditFunc = f'update cadastrar_funcionario set cpf = "{mudCPF}" where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditFunc)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 3:
                        
                        mudDataNasc = input("Qual data de nascimento deseja colocar? ")
                        comandoEditFunc = f'update cadastrar_funcionario set nascimento = "{mudDataNasc}" where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditFunc)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 4:
                        
                        mudCargo = input("Qual cargo deseja colocar? ")
                        comandoEditFunc = f'update cadastrar_funcionario set cargo = "{mudCargo}" where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditFunc)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 5:
                        
                        mudFone = input("Qual número de telefone deseja colocar? ")
                        comandoEditFunc = f'update cadastrar_funcionario set fone = "{mudFone}" where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditFunc)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break
                    
                    elif esc == 6:
                        fechaDelete = int(input("Deseja mesmo deletar funcionário? Se sim, digite 1: "))
                        if fechaDelete !=1:
                            break
                        comandoDelFunc = f'delete from cadastrar_funcionario where id_funcionario = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoDelFunc)
                        con.commit()
                
                if op ==3:
                    relatorio_aluno()
                if op ==4:
                    break
                          
        elif escolhas == 3:
            while op !=6:
                print('1- Incluir Curso: ')
                print('2- Editar: ')
                print('3- Relatório: ')
                print('4- Voltar: ')
                op = int(input(':'))
                os.system('cls')
                if op == 1:
                    cadastrar_curso()
                    os.system('cls')
                while op == 2:
                    consulta_sql = 'select * from cadastrar_curso'
                    cursor = con.cursor()
                    cursor.execute(consulta_sql)
                    linhas = cursor.fetchall()
                    print('Número total de registros retornados: ',cursor.rowcount)
                    print('Mostrando os Registros')
                    for linha in linhas:
                        print('ID  = ',linha[0])
                        print('Nome do curso = ',linha[1])
                        print('Vagas = ',linha[2])
                        print('Carga Horaria = ',linha[3])
                        print('Período = ',linha[4],'\n')
                    
                    escID = int(input("Qual o ID do curso que deseja realizar mudanças? "))
                    os.system('cls')
                    print('\n1- Nome do curso')
                    print('2- Vagas')
                    print('3- Carga Horária')
                    print('4- Período')
                    print('5- Deletar''\n')
                    esc = int(input("Qual é a informação que gostaria de alterar? "))
                    
                    if esc == 1:
                        
                        mudNome = input("Qual nome deseja colocar? ")
                        comandoEditCurso = f'update cadastrar_curso set nome_curso = "{mudNome}" where id_curso = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditCurso)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 2:
                        
                        mudVagas = input("Quantas vagas deseja colocar? ")
                        comandoEditCurso = f'update cadastrar_curso set vagas = "{mudVagas}" where id_curso = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditCurso)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 3:
                        
                        mudDataNasc = input("Qual a carga horária deseja colocar? ")
                        comandoEditCurso = f'update cadastrar_curso set carga_horaria = "{mudDataNasc}" where id_curso = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditCurso)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 4:
                        
                        mudCargo = input("Qual o período que deseja colocar? ")
                        comandoEditCurso = f'update cadastrar_curso set periodo = "{mudCargo}" where id_curso = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoEditCurso)
                        con.commit()
                        fechaWhileUpdate = int(input("Deseja continuar realizando mudanças? Caso sim, digite 1, caso contrário, digite qualquer outro número: "))
                        if fechaWhileUpdate !=1:
                            break

                    elif esc == 5:
                        fechaDelete = int(input("Deseja mesmo deletar esse curso? Se sim, digite 1: "))
                        if fechaDelete !=1:
                            break
                        comandoDelCurso = f'delete from cadastrar_curso where id_curso = {escID} '
                        cursor = con.cursor ()
                        cursor.execute(comandoDelCurso)
                        con.commit()
                if op == 3:
                    relatorio_curso()
                if op == 4:
                    break
        else:
            break

main()
        
if con.is_connected():
    bd_info = con.get_server_info()
    print('Banco de dados está conectando = ', bd_info)