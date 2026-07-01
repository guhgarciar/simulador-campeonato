import random

class Time:
    def __init__ (self, nome_do_time: str):
        self.nome: str = nome_do_time
        self.vitorias: int = 0
        self.empates: int = 0
        self.derrotas: int = 0
        self.gols_pro: int = 0
        self.gols_sofridos: int = 0
        self.saldo: int = 0
        self.amarelo: int = 0
        self.vermelho: int = 0

times_campeonato = ["Athletico-PR", "Atlético-MG", "Bahia", "Botafogo", "Chapecoense", "Corinthians", "Coritiba", "Cruzeiro", "Flamengo", "Fluminense", "Grêmio", "Internacional", "Mirassol", "Palmeiras", "Red Bull Bragantino", "Remo", "Santos", "São Paulo", "Vasco", "Vitória"]
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
