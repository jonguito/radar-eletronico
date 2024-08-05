velocidade = int(input('Qual é a velocidade do carro? '))
atençao = ('Tenha um bom dia! Dirija com segurança!')
multa = (velocidade -80)*7
if velocidade <= 80:
    print(atençao)
if velocidade > 80:
    print(f'''MULTADO! Você excedeu o limite de velocidade permitido de 80km/h. 
você deve pagar uma multa de R${multa},00.
{atençao} ''')
