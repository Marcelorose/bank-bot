from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer
from chatterbot.trainers import ListTrainer
import os

bot = ChatBot('Teste')
trainer = ListTrainer(bot) # definir o "treinador"

for arq in os.listdir('arq'): # procurar na pasta dos arquivos
    chats = open('arq/' + arq, 'r').readlines() # ler os ficheiros
    print(chats)
    # trainer.train(chats) # treinar os ficheiros
while True:
    resq = input('Eu: ')
    resp = bot.get_response(resq)
    print(resp)