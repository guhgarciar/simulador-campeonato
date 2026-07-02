import random
from models.time import Time

times_campeonato = ["Athletico-PR", "Atlético-MG"]
times_cadastro = []

for i in times_campeonato:
    novo_time = Time(nome_do_time=i)
    times_cadastro.append(novo_time)

for i in range(len(times_cadastro)):
    for j in range(len(times_cadastro)):
        if i != j:
            time_casa = times_cadastro[i]
            time_visitante = times_cadastro[j]
            gols_time_casa = int(input(f"Gols do time {time_casa.nome}: "))
            gols_time_visitante = int(input(f"Gols do time {time_visitante.nome}: "))
            if gols_time_casa > gols_time_visitante:
                time_casa.pontos += 3
                time_casa.vitorias += 1
                time_visitante.derrotas += 1
            elif gols_time_casa == gols_time_visitante:
                time_casa.pontos += 1
                time_casa.empates += 1
                time_visitante.pontos += 1
                time_visitante.empates += 1
            else:
                time_visitante.pontos += 3
                time_casa.derrotas += 1
                time_visitante.vitorias += 1
            time_casa.gols_pro += gols_time_casa
            time_casa.gols_sofridos += gols_time_visitante
            time_casa.saldo = (time_casa.gols_pro - time_casa.gols_sofridos)
            time_visitante.gols_pro += gols_time_visitante
            time_visitante.gols_sofridos += gols_time_casa
            time_visitante.saldo = (time_visitante.gols_pro - time_visitante.gols_sofridos)
            teve_amarelo_casa = random.choice([True, False])
            if teve_amarelo_casa == True:
                time_casa.amarelo += random.randint(1, 5)
            teve_vermelho_casa = random.randint(1, 10)
            if teve_vermelho_casa == 1:
                opcoes_vermelho = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
                time_casa.vermelho += random.choice(opcoes_vermelho)
            teve_amarelo_visitante = random.choice([True, False])
            if teve_amarelo_visitante == True:
                time_visitante.amarelo += random.randint(1, 5)
            teve_vermelho_visitante = random.randint(1, 10)
            if teve_vermelho_visitante == 1:
                opcoes_vermelho = [1, 1, 1, 1, 1, 1, 1, 2, 2, 3]
                time_visitante.vermelho += random.choice(opcoes_vermelho)

tabela_organizada = sorted(times_cadastro, key = lambda time: time.pontos, reverse=True)

print("\n=== TABELA DE CLASSIFICAÇÃO ===")
# Deixamos o cabeçalho com larguras fixas batendo com o laço de baixo
print(f"{'Pos':<4} | {'Time':<15} | {'P':>3} | {'V':>2} | {'E':>2} | {'D':>2} | {'GP':>3} | {'GS':>3} | {'SG':>3} | {'A':>3} | {'V':>2}")
print("-" * 75)

for posicao, time in enumerate(tabela_organizada):
    # Formatando cada coluna com tamanho fixo e alinhamento perfeito
    print(f"{posicao + 1:>2}º  | {time.nome:<15} | {time.pontos:>3} | {time.vitorias:>2} | {time.empates:>2} | {time.derrotas:>2} | {time.gols_pro:>3} | {time.gols_sofridos:>3} | {time.saldo:>3} | {time.amarelo:>3} | {time.vermelho:>2}")