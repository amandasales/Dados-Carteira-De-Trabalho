from datetime import datetime
dados = {}
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
idade = datetime.now().year - nasc
dados['idade'] = idade
dados['ctps'] = int(input('Carteira de trabalho: (0 caso não tenha)'))
if dados['ctps'] != 0:
    dados['ano de contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = dados['idade'] + ((dados['ano de contratação'] + 35) - datetime.now().year)
print(f'-=-' * 30)
for k, v in dados.items():
    print(f'{k} recebe {v}')
