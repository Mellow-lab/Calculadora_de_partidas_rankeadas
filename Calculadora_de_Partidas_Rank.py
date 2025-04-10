def calcular_rank(vitorias, derrotas):
    saldo = vitorias - derrotas

    if saldo < 0:
        nivel = "Madeira 🪵"

    elif saldo < 10:
        nivel = "Ferro ⚙️"

    elif 10 <= saldo <= 20:
        nivel = "Bronze 🥉"

    elif 21 <= saldo <= 50:
        nivel = "Prata 🥈"

    elif 51 <= saldo <= 80:
        nivel = "Ouro 🥇"

    elif 81 <= saldo <= 90:
        nivel = "Diamante 💎"

    elif 91 <= saldo <= 100:
        nivel = "Lendário 🧙"

    else:
        nivel = "Imortal 🐉"

    return saldo, nivel

while True:

    try:
        vitorias = int(input("Digite o número de vitórias: "))
        derrotas = int(input("Digite o número de derrotas: "))
        
        saldo, nivel = calcular_rank(vitorias, derrotas)

        print(f"O Herói tem de saldo de {saldo} está no nível de {nivel}")
        
        continuar = input("Deseja verificar outro jogador? (s/n): ")
        if continuar.lower() != 's':
            print("Encerrando a calculadora de partidas rankeadas.")
            break
    except ValueError:
        print("Por favor, digite apenas números inteiros.")