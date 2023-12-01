# aula4 Python Turma 21 - 29/11/2023
# programa para retornar uma lista de dados a partir de um dicionário

# Apresentação
print('\n\t\t\t -- Cadastro de Produtos --\n')

# Entrada de dados
nomeProduto = input("Digite o nome do produto: ")
quantidadeProduto = int(input("Digite a quantidade do produto: "))
valorProduto = float(input("Digite o preço unitário do produto: "))
disponivelProduto = input("Produto se encontra disponível? (S/N): ")

# Verificar a disponibilidade
if disponivelProduto.upper() == 'S':
    disponibilidade = True
else:
    disponibilidade = False

# Processamento e dicionário com os valores inseridos pelo usuário
dados_produto = {'nome': nomeProduto, 'quantidade': quantidadeProduto, 'preço': valorProduto, "disponibilidade": disponibilidade}

preco_total = dados_produto['quantidade'] * dados_produto['preço']

# Saída
print('\nCadastrado efetuado com sucesso',
      '\nProduto: ', dados_produto['nome'],
      '\nQuantidade: ', dados_produto['quantidade'],
      '\nPreço: R$ ', dados_produto['preço'],
      '\nDisponível: ', dados_produto['disponibilidade'],
      '\nPreço Total: R$ ', preco_total)
