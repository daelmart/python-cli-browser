import socket #importar a biblioteca para operações de rede

#loop infinito na consola
# O utilizador tem a opção de:
# 1 - aceder a uma página
# 2 - sair da aplicação
# qualquer opção diferente de 1 e 2, leva ao programa exibir "Opção não disponível" e retornar a "Tela inicial"
aux = True
while aux == True:
    print("Bem vindo ao browser em linha de comando\n1 - acessar uma página\n2 - sair")
    
    #recebe a opção dada pelo utilizador e faz uma conversão para inteiro
    try:
        option = int(input())
    except ValueError:
        print("Valor inválido\n")
        option = False
    if(option != 1 and option != 2):
        print("Valor inválido\n")
        option = False

    while(option != False): 
        if option == 1:
            url = input("URL?\n")
            #formatação do requisição do cliente, no caso um GET, para obter a página
            request = "GET / HTTP/1.1\r\nHost:" + url+ "\r\n\r\n"
            #formatação do socket para enviar a requisição
            #a constante socket.AF_INET informa que será utilizado IPV4 para conexão
            #a constante socket.SOCK_STREAM define o tipo de socket que será utilizado (no caso, TCP)
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            #a conexão é inicializada com a URL que o utilizador inseriu, utilizando a porta 80
            s.connect((url, 80))
            #é feito o envio da requisição, convertendo em bytes e em padrão UTF-8
            s.send(bytes(request,'utf8'))
            #o resultado é defindo com o limite de 10.000 bytes
            result = s.recv(10000)
            # http = "charset=UTF-8"
            
            #formatar a resposta do servidor de bytes para string, para manipulação
            result_decoded = result.decode("utf-8")
            result_formated = result_decoded.partition("<")
            #Exibe o cabeçalho e em seguida o conteúdo HTML da página
            print("Este é o cabeçalho HTTP:\n")
            print(result_formated[0])
            print("Este é o conteúdo da página:\n\n")
            print(result_formated[1] + result_formated[2])
            
            #define a variável auxiliar "option" com o valor lógico "False" para sair do loop da requisição
            option = False
            
#       Caso a opção seja para sair, a variável auxiliar "aux" recebe o valor lógico "False" para sair do loop (e da aplicação)
        if option == 2:
            print("Bye")
            aux = False
            break
    