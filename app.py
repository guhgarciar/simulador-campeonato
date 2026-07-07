from fastapi import FastAPI
from models.time import Time

app = FastAPI()

times_campeonato = ["Athletico-PR", "Atlético-MG"]
times_cadastro = []

for i in times_campeonato:
    novo_time = Time(nome_do_time=i)
    times_cadastro.append(novo_time)