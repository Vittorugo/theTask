import json
from datetime import datetime

file_json = open('U1ZQR43RB.json','r')
dados_json = json.load(file_json)


list_json = []  # lista com os objetos.
lista_de_usuarios = [] # lista com o nome dos participantes da conversa.
fast_msg = [] # lista para adicionar msg respondidas rapidamente.


class user():

    def __init__(self, nome, mensage):

        self.username = nome
        self.mensages = mensage


def user_msg( username, msg ):



    obj_user_msg = user(username, msg)
    list_json.append(obj_user_msg)
    #lista de usuários ...





obj_msg = {}

for usuario in dados_json:

    fast_msg = []
    tempo_msg_vez = float(usuario['ts'])
    ts_primeira_msg = datetime.fromtimestamp(tempo_msg_vez)


    usuario_msg = []
    usuario_consultado = usuario['user']

    if usuario_consultado not in lista_de_usuarios:

        lista_de_usuarios.append(usuario_consultado)

        # timestamp da primeira msg ...
        timestamp_first_msg = float(usuario['ts'])
        ts_first = datetime.fromtimestamp(timestamp_first_msg)

        for nome in dados_json:


            timestamp_last_msg =  float(nome['ts'])  #tempo da última msg ...
            ts_last = datetime.fromtimestamp(timestamp_last_msg)


            if (ts_last.minute - ts_first.minute) < 2 :

                fast_msg.append(nome['text'])  # adicionado msgs respondidas em menos de 2 minutos ...

            if  usuario_consultado == nome['user']:

                usuario_msg.append(nome['text']) # separando as msgs do usuario...


        obj_msg[usuario['ts']] = fast_msg #objeto com chave = horário da mensagem e valor = mensagens respondidas antes de 2 minutos.

        user_msg(usuario_consultado, usuario_msg)


for i in list_json:
    print(i.mensages)
