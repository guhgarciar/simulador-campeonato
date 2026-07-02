class Time:
    def __init__ (self, nome_do_time: str):
        self.nome: str = nome_do_time
        self.pontos: int = 0
        self.vitorias: int = 0
        self.empates: int = 0
        self.derrotas: int = 0
        self.gols_pro: int = 0
        self.gols_sofridos: int = 0
        self.saldo: int = 0
        self.amarelo: int = 0
        self.vermelho: int = 0