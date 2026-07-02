import random
from models.time import Time

# --- CONFIGURAÇÃO INICIAL DO CAMPEONATO ---
times_campeonato = ["Athletico-PR", "Atlético-MG"]
times_cadastro = []

for i in times_campeonato:
    novo_time = Time(nome_do_time=i)
    times_cadastro.append(novo_time)

# --- MOTOR DE SIMULAÇÃO DOS CONFRONTOS ---
for i in range(len(times_cadastro)):
    for j in range(len(times_cadastro)):
        if i != j:
            time_casa = times_cadastro[i]
            time_visitante = times_cadastro[j]

            # Entrada de dados do placar
            gols_time_casa = int(input(f"Gols do time {time_casa.nome}: "))
            gols_time_visitante = int(input(f"Gols do time {time_visitante.nome}: "))
            
            # Sorteio de cartões do time mandante
            amarelos_casa = 0
            if random.choice([True, False]):
                amarelos_casa = random.randint(1, 5)

            vermelhos_casa = 0    
            if random.randint(1, 10) == 1:
                vermelhos_casa = random.choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 3])

            # Sorteio de cartões do time visitante
            amarelos_visitante = 0
            if random.choice([True, False]):
                amarelos_visitante += random.randint(1, 5)

            vermelhos_visitante = 0
            if random.randint(1, 10) == 1:
                vermelhos_visitante = random.choice([1, 1, 1, 1, 1, 1, 1, 2, 2, 3])

            # Atualiza os dados de cada clube usando a classe Time    
            time_casa.registrar_partida(gols_time_casa, gols_time_visitante, amarelos_casa, vermelhos_casa)
            time_visitante.registrar_partida(gols_time_visitante, gols_time_casa, amarelos_visitante, vermelhos_visitante)

# --- ORGANIZAÇÃO E IMPRESSÃO DA TABELA ---
tabela_organizada = sorted(times_cadastro, key = lambda time: time.pontos, reverse=True)

print("\n=== TABELA DE CLASSIFICAÇÃO ===")
print(f"{'Pos':<4} | {'Time':<15} | {'P':>3} | {'V':>2} | {'E':>2} | {'D':>2} | {'GP':>3} | {'GS':>3} | {'SG':>3} | {'A':>3} | {'V':>2}")
print("-" * 75)

for posicao, time in enumerate(tabela_organizada):
    # Alinhamento no terminal
    print(f"{posicao + 1:>2}º  | {time.nome:<15} | {time.pontos:>3} | {time.vitorias:>2} | {time.empates:>2} | {time.derrotas:>2} | {time.gols_pro:>3} | {time.gols_sofridos:>3} | {time.saldo:>3} | {time.amarelo:>3} | {time.vermelho:>2}")