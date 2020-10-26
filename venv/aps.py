# Importanto modulos
import interface
import os

# Lista com caracteres usados na criptografia.
abcdario = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
            'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X',
            'Y', 'Z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# Laço para o texto sempre ficar repetindo
sair = 'n'
while sair != 's':
    texto_final = ''
    # Chamando a função do topo
    interface.topo()
    # Comando para sempre que for chamado, limpar as mensagens
    clear = lambda: os.system('cls')
    clear()

    # Chamando a função barra
    interface.barrinha()
    # Chamando a função menu
    # Onde o usuário irá escolher a opção desejada
    opcao = interface.menu()
    clear()

    interface.barrinha()
    # Input que recebe a mensagem, onde depois que receber irá colocar tudo em caixa alta e retira os espaços
    texto = ''.join(input('Digite sua mensagem: ').upper().split())
    # Input para receber a senha
    chave = input('Digite sua chave: ').upper()
    texto_cripto = ''
    clear()

    # Nesse if ele irá verificar se o texto é menor que a chave, caso seja aparecerá a mensagem avisando.
    # E volta para o inicio.
    if (len(chave)) > (len(texto)):
        clear()
        print('Opção invalida, chave maior que a frase')
        input()
        clear()
    # Caso o contrario, ele irá executar o código
    else:
        # contador
        i = int(0)
        # Processo para repetir a chave varias vezes até ter o mesmo número de caracteres que o texto
        while (len(texto_cripto) < len(texto)):
            texto_cripto += chave[i]
            i += 1
            if( i == len(chave)):
                i=0
        for i in range(len(texto)):
            # O texto[i] precisa ser diferente de vazio
            if(texto[i]) != ' ':
                # Então a variavel posicao_letra_texto irá receber o index do texto dentro do abcdario
                posicao_letra_texto = int(abcdario.index(texto[i]))
                # posicao_letra_chave fará o mesmo, porem com o texto_cripto gerado na linha 46
                posicao_letra_chave = int(abcdario.index(texto_cripto[i]))
                # caso a opçõa seja 1, a mensagem será criptografiada
                if(opcao == 1):
                    # A mensagem é criptografada, fazendo a soma do index da palavra mais o index da chave,
                    # e dividindo tudo isso pelo modo do abcdario usado
                    texto_final += str(abcdario[(posicao_letra_texto + posicao_letra_chave) % len(abcdario)])
                else:
                    # Caso a opção foi a 2, então a mensagem será descriptografada. Usando mesma operação de cima,
                    # Porem ao inves de somar, ele ira subtrair. E depois disso deixará a mensagem toda em minúscula
                    texto_final += str(abcdario[(posicao_letra_texto - posicao_letra_chave) % len(abcdario)].lower())
            else:
                texto_final += ' '

        # Então com a opção 1 marcada, ele apresentará a mensagem criptografada e com a opção de sair do código
        if(opcao == 1):
            interface.barrinha()
            print(f'Mensagem criptografada: {texto_final}')
            sair = input('DESEJA SAIR? (s/n)')
            clear()
        # Caso contrário, será mostrado a mensagem descriptografada
        else:
            interface.barrinha()
            print(f'Mensagem descriptografada: {texto_final}')
            sair = input('DESEJA SAIR? (s/n)')
            clear()