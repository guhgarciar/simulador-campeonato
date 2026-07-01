import random #biblioteca que gera os dados randômicos

class Time:
    # O __init__ é o construtor. É ele que prepara a "caixinha" do time na memória.
    # O 'nome_do_time' é a única coisa que vamos passar de fora.
    def __init__ (self, nome_do_time: str):
        self.nome: str = nome_do_time

        # Todos os outros atributos começam zerados porque o campeonato não começou!
        self.pontos: int = 0
        self.vitorias: int = 0
        self.empates: int = 0
        self.derrotas: int = 0
        self.gols_pro: int = 0
        self.gols_contra: int = 0
        self.saldo: int = 0
        self.cartoes_amarelos: int = 0
        self.cartoes_vermelhos: int = 0

nomes_dos_times = ["São Paulo", "Flamengo", "Palmeiras", "Santos", "Corinthians"]

campeonato = []

for i in nomes_dos_times:
    # 1. Criamos o objeto 'Time' na memória usando o texto da vez (i)
    novo_time = Time(nome_do_time=i)
    # 2. Guardamos esse objeto completo dentro da nossa lista do campeonato
    campeonato.append(novo_time)

for i in campeonato:
    print(i.nome)