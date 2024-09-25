# Crie um programa que receba uma quantidade indefinida de números do usuário. O programa deve calcular a média desses números e parar quando o usuário digitar -1.

soma = 0
contador = 0

while True:
    numero = float(input("Digite um número (-1 para parar): "))
    
    if numero == -1:
        break  # Sai do loop se o usuário digitar -1
    
    soma += numero  # Adiciona o número à soma
    contador += 1   # Incrementa o contador

# Verifica se o contador é maior que 0 para evitar divisão por zero
if contador > 0:
    media = soma / contador
    print(f"A média dos números informados é: {media:.2f}")
else:
    print("Nenhum número foi informado.")
    