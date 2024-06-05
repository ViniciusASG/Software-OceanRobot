print('Ola Bem-Vindo ao nosso software OceanRobot, um jogo onde voce aprende e se diverte!!! ')
nomeUsuario = input('Vamos Começar o jogo, Qual o seu nome: ')
print(f'Ola {nomeUsuario}, Estamos Felizes em ter voce no nosso jogo')
pontos = 0
oceanos = ['ATLANTICO', 'PACIFICO', 'INDICO', 'ARTICO']
oceanosUsuario = ['']
professores = ['DANILO RODRIGUES', 'JONES EGYDIO', 'LUCAS DEMETRIUS AUGUSTO', 'LUCAS SILVA DE SOUSA', 'JOSÉ HENRIQUE', 'ANA CLAUDIA', 'CAIO VINÍCIUS ']
materias = ['COMPUTATIONAL THINKING WITH PYTHON', 'DIFFERENTIATED PROBLEM SOLVING', 'EDGE COMPUTING & COMPUTER SYSTEMS', 'FRONT-END DESIGN', 'SOFTWARE & TOTAL EXPERIENCE DESIGN',
            'STORYTELLING E INSPIRAÇÃO EMPREENDEDORA', 'WEB DEVELOPMENT']
def oceanosfunc(msgOceanos):
    ponto = 0
    while True:
        escolhaUsuario = input('Diga os oceanos que voce conhece um de cada vez, nao use acentos ').upper()
        if escolhaUsuario in oceanosUsuario:
            print('Voce ja digitou esse oceano')
        elif escolhaUsuario in oceanos:
            print(f'Parabens! Voce acertou: {escolhaUsuario}')
            ponto += 1
            oceanosUsuario.append(escolhaUsuario)
            oceanos.remove(escolhaUsuario)  # Remove o oceano acertado da lista
        elif escolhaJogosUsuario in oceanosUsuario:
            print('Voce ja acertou essa opção, esse oceano existe ')
        else:
            print('Esse oceano nao existe, lembre de nao usar acentos')
        if ponto == 4:
            return ponto
'''pontos = oceanosfunc('Vamos Começar o jogo')'''
print(f'Muito Bem {nomeUsuario} voce esta com {pontos} pontos')

def maiorOceano(msgMaiorOceano):
    maiorUsuario = input('Qual o maior oceano do mundo?, nao use acentos ').upper()
    if maiorUsuario == 'PACIFICO':
        print('Parabens! Voce acertou, o maior oceano do mundo e o Pacifico.')
        ponto = 1
    else:
        print('Voce errou, o maior oceano do mundo era o Pacifico.')
        ponto = 0
    return ponto

'''pontos += maiorOceano('Vamos Começar o jogo do maior oceano')'''

def menorOceano(msgMenorOceano):
    maiorUsuario = input('Qual o menor oceano do mundo?, nao use acentos ').upper()
    if maiorUsuario == 'ARTICO':
        print('Parabens! Voce acertou, o maior oceano do mundo e o Artico.')
        ponto = 1
    else:
        print('Voce errou, o maior oceano do mundo era o Artico.')
        ponto = 0
    return ponto
'''pontos += menorOceano('Vamos Jogar o jogo do menor oceano')'''

def brasilOceano(msgbrasilOceano):
    brasilOceanoUsuario = input('Qual o oceano faz fronteira com o brasil? , nao use acentos ').upper()
    if brasilOceanoUsuario == 'ATLANTICO':
        print('Parabens voce acertou o oceano que faz fronteira com o brasil e o ATLANTICO')
        ponto = 1
    else:
        print('Voce errou, o oceano que faz fronteira com o brasil e o Atlantico')
        ponto = 0
    return ponto
'''pontos += brasilOceano('Vamos jogar o jogo do oceano no em volta do brasil')'''

def regrasJogos():
    print('Unica regra do jogo e se divertir muito ')
    return None

def infTodosOsOceanos():
    print(f'Todos os oceanos do planeta são {oceanos}')
    return None

def infmaiorOceano():
    print('''O maior oceano do mundo e O Oceano Pacífico é o maior oceano da Terra, situado entre a América,
           a leste, a Ásia e a Austrália, a oeste, e a Antártida, ao sul. Com 180 milhões de km² de área superficial,
           o Pacífico cobre quase um terço da superfície do planeta e corresponde a quase metade da superfície e do volume 
           dos oceanos. ''')
    return None

def infMenorOceano():
    print(f'''O Oceano Ártico ou Oceano Glacial Ártico está situado no Polo Norte e é o menor de todos, ocupa uma área de 14 milhões
           de quilômetros quadrados e possui uma característica particular, permanece praticamente congelado durante todo o ano.''')
    return None

def infBrasilOceano():
    print(f'oceano Atlântico, Banhado a leste pelo oceano Atlântico, o Brasil possui 23.102 km de fronteiras, sendo 15.735 km terrestres e 7.367 km marítimas.')
    return None

def infNossoProjeto():
    print(f'''A nossa solução seria um robo de coleta de dados para remoção dos lixos. Ele utilizaria um sistema de geolocalização por arduino
           e um sistema de ondas sonoras para caso haja perca de sinal. O robo teria placas de energia solar para recarga de energia de maneira
           sustentável.A partir de coordenadas e locais provaveis de haver lixo, o robo iria verificar se ha a presença de lixo na localização,
           e enviaria as informações se ha lixo ou nao. Fariamos um site compartilhando essas informações, e alguns sistemas adicionais, como por
           exemplo, a comparação de lugares e suas respectivas quantidades de lixos.''')
    return None

def infOceans20():
    print(f'''Oceans 20 (O20) é um grupo de engajamento lançado sob a presidência brasileira do G20 para destacar questões oceânicas nas agendas globais
           de clima, energia e meio ambiente. O grupo promove o uso sustentável dos recursos marinhos, envolvendo a sociedade civil, incluindo ONGs,
            setor privado, povos indígenas, comunidades tradicionais e cientistas (G20 Brasil 2024 - Português (Brasil)(o20brasil)
            O O20 é coordenado pela Cátedra UNESCO para a Sustentabilidade do Oceano da Universidade de São Paulo, em parceria com o Fórum Econômico Mundial,
           o Pacto Global da ONU - Rede Brasil, o Fundo Brasileiro para a Biodiversidade (FUNBIO) e o Instituto Nacional de Pesquisas Oceânicas (INPO)
           (o20brasil) (G20 Brasil 2024 - Português (Brasil)).''')
    return None

def infProfessores():
    print(f'Esses sao nossos professores {professores}')
    return None

def infMaterias():
    print(f'Essas são nossas materias {materias}')
    return None

def consultarProfessorMaterias():
    print(f'Professores: {professores}')
    consultaUsuarioMateria = input('Qual professor você quer saber a matéria que ele leciona? ').upper()
    for i in range(len(professores)):
        if professores[i] == consultaUsuarioMateria:
            print(f'O professor {professores[i]} leciona {materias[i]}')
            return
    print('Professor não encontrado.')

'''consultarProfessorMaterias()'''

while True:
    print(f'Essas são nossas paginas qual voce deseja acessar? ')
    primeiraOpcaoUsuario = input('''para acessar nossos jogos aperte o numero 1, para acessar nosso menu de informações aperte o numero 2,
                                    para acessar e saber mais sobre nossos professores aperte a tecla 3 ''')
    while True:
        if not primeiraOpcaoUsuario.isnumeric():
            primeiraOpcaoUsuario = input('''para acessar nossos jogos aperte o numero 1, para acessar nosso menu de informações aperte o numero 2,
                                        para acessar e saber mais sobre nossos professores aperte a tecla 3 ''')
        else:
            break
    primeiraOpcaoUsuario = int(primeiraOpcaoUsuario)    
    if primeiraOpcaoUsuario == 1:
        while True:
            print(f'Bem vindo aos jogos vamos começar atualmente voce esta com {pontos} pontos, jogue para conseguir mais pontos ')
            escolhaJogosUsuario = input('''Para entrar no jogo dos Oceanos Gerais aperte o 1,Para entrar no jogo do maior oceano aperte
                                            a tecla 2, Para entrar no jogo do menor oceano aperte o 3, Para entrar no jogo do oceano em volta
                                            do brasil aperte 4,para saber as regras do jogo aperte 5, para voltar ao menu anterior aperte 6 ''')
            while True:
                if not escolhaJogosUsuario.isnumeric():
                    escolhaJogosUsuario = input('''Para entrar no jogo dos Oceanos Gerais aperte o 1,Para entrar no jogo do maior oceano aperte
                                            a tecla 2, Para entrar no jogo do menor oceano aperte o 3, Para entrar no jogo do oceano em volta
                                            do brasil aperte 4,para saber as regras do jogo aperte 5, para voltar ao menu anterior aperte 6 ''')
                else:   
                    break
            escolhaJogosUsuario = int(escolhaJogosUsuario)   
            if escolhaJogosUsuario == 1:
                pontos += oceanosfunc('Vamos Começar o jogo dos oceanos gerais ')
                print(f'O jogador {nomeUsuario} tem {pontos} pontos')
                break
            elif escolhaJogosUsuario == 2:
                pontos += maiorOceano('Vamos Começar o jogo do maior oceano ')
                print(f'O jogador {nomeUsuario} tem {pontos} pontos')
                break
            elif escolhaJogosUsuario == 3:
                pontos += menorOceano('Vamos Jogar o jogo do menor oceano')
                print(f'O jogador {nomeUsuario} tem {pontos} pontos')
                break
            elif escolhaJogosUsuario == 4:
                pontos += brasilOceano('Vamos jogar o jogo do oceano no em volta do brasil')
                print(f'O jogador {nomeUsuario} tem {pontos} pontos')
                break
            elif escolhaJogosUsuario == 5:
                regrasJogos()
            elif escolhaJogosUsuario == 6:
                continue
            else:
                print('Voce digitou uma opção invalida, escolha uma opção valida')
    elif primeiraOpcaoUsuario == 2:
        print('Ola estamos felizes em saber que voce quer saber mais sobre o projeto Ocean Robot ')
        while True:
            escolhaInfosUsuarios = input('''Para saber sobre todos os oceanos aperte o 1, para saber sobre o maior oceano aperte 2,
                                            para saber sobre o menor oceano aperte 3, para saber sobre o oceano que banha o brasil aperte 4, 
                                            para saber sobre o nosso projeto aperte 5, para saber sobre o oceans20 aperte 6, para voltar ao menu anterior aperte 7 ''')
            while True:
                if not escolhaInfosUsuarios.isnumeric():
                    escolhaInfosUsuarios = input('''Para saber sobre todos os oceanos aperte o 1, para saber sobre o maior oceano aperte 2,
                                            para saber sobre o menor oceano aperte 3, para saber sobre o oceano que banha o brasil aperte 4, 
                                            para saber sobre o nosso projeto aperte 5, para saber sobre o oceans20 aperte 6, para voltar ao menu anterior aperte 7 ''')
                else:   
                    break
            escolhaInfosUsuarios = int(escolhaInfosUsuarios)    
            if escolhaInfosUsuarios == 1:
                infTodosOsOceanos()
                break
            elif escolhaInfosUsuarios == 2:
                infmaiorOceano()
                break
            elif escolhaInfosUsuarios == 3:
                infMenorOceano()
                break
            elif escolhaInfosUsuarios == 4:
                infBrasilOceano()
                break
            elif escolhaInfosUsuarios == 5:
                infNossoProjeto()
                break
            elif escolhaInfosUsuarios == 6:
                infOceans20()
                break
            elif escolhaInfosUsuarios == 7:
                continue
            else:
                print('Voce digitou uma opção invalida, escolha uma opção valida')
    elif primeiraOpcaoUsuario == 3:
        ('Ola então voce quer saber mais sobre nossos professores')
        while True:
            escolhaProfessoresUsuario = input('''Para saber quais sao nossos professores aperte o 1, Para saber qual são as nossas materias aperte o 2
                                                para realizar uma consulta de qual professor leciona qual materia aperte o 3, para voltar ao menu anterior aperte o 4 ''')
            while True:
                if not escolhaProfessoresUsuario.isnumeric():
                    escolhaProfessoresUsuario = input('''Para saber quais sao nossos professores aperte o 1, Para saber qual são as nossas materias aperte o 2
                                                para realizar uma consulta de qual professor leciona qual materia aperte o 3, para voltar ao menu anterior aperte o 4 ''')
                else:   
                    break
            escolhaProfessoresUsuario = int(escolhaProfessoresUsuario)
            if escolhaProfessoresUsuario == 1:
                infProfessores()
                break
            elif escolhaProfessoresUsuario == 2:
                infMaterias()
                break
            elif escolhaProfessoresUsuario == 3:
                consultarProfessorMaterias()
                break
            elif escolhaProfessoresUsuario == 4:
                continue
            else:
                print('Voce digitou uma opção invalida, escolha uma opção valida')
    else:
        print('Voce digitou uma opção invalida, escolha uma opção valida')