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
    
    def registrar_partida(self, gols_feitos: int, gols_tomados: int, cartoes_a: int, cartoes_v: int):
        self.gols_pro += gols_feitos
        self.gols_sofridos += gols_tomados
        self.amarelo += cartoes_a
        self.vermelho += cartoes_v

        self.saldo = self.gols_pro - self.gols_sofridos

        if gols_feitos > gols_tomados:
           self.pontos += 3
           self.vitorias += 1
        elif gols_feitos == gols_tomados:
            self.pontos += 1
            self.empates += 1
        else:
            self.derrotas += 1