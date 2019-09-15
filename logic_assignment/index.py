import json
from datetime import datetime

arquivo_json = open('U1ZQR43RB.json')
dados_json    = json.load(arquivo_json) # 214 objetos ...

###################  LISTAS E VARIAVEIS  #################################
##########################################################################

dados_organizados = [] # lista com os dados organizados conforme a questão pediu.

lista_de_usuarios = [] # lista com os usuários encontrados ...
lista_mensagens  = [] # lista com todas as mensagens dos usuarios ...
dados_usuario = {}  # dicionario com os atributos nome, mensagens e mensagens respondidas antes de dois minutos


lista_sub_mensagens = [] #lista com as mensagens respondidas antes de dois minutos

###########################################################################
###########################################################################


for usuario in dados_json:


    if usuario['user'] not in lista_de_usuarios:

        # Adicionando os usuários encontrados no .json ...
        lista_de_usuarios.append(usuario['user'])

        # lista_de_usuários = ['U0MFNAG05', 'U0KK0T3CG', 'U1ZQR43RB', 'USLACKBOT']


        lista_mensagens = []

        for mensagem in dados_json:

            if (usuario['user'] == mensagem['user']):

                # Adicionando mensagens enviadas por cada usuário encontrado ...
                lista_mensagens.append(mensagem['text'])


        # criando um objeto com as informações de usuário e mensagens encontradas ...

        dados_usuario['username'] = usuario['user']
        dados_usuario['mensagens']= lista_mensagens


        for sub_mensagens in dados_json:

            dic_sub_msg = {} # dicionário auxiliar para as sub_mensagens ...
            lista_aux_sub_msg   = [] # lista auxiliar para as sub mensagens ...

            if sub_mensagens['text'] in lista_mensagens:

                # tempo que a mensagem foi enviada
                tempo_sub_msg = float(sub_mensagens['ts'])
                tempo_sub_msg = datetime.fromtimestamp(tempo_sub_msg)

                for mensagens_respondidas_rapidamente in dados_json:

                    # verifica se as mensagens são diferentes para evitar redundância ...
                    if sub_mensagens['text'] != mensagens_respondidas_rapidamente['text']:

                        # tempo mensagens de resposta da mensagem enviada
                        tempo_resposta = float(mensagens_respondidas_rapidamente['ts'])
                        tempo_resposta = datetime.fromtimestamp(tempo_resposta)

                        # condição comparando o tempo entre uma mensagem e suas respostas ...
                        if (tempo_resposta.hour == tempo_sub_msg.hour) and (tempo_resposta.minute - tempo_sub_msg.minute) <= 2 :

                            lista_aux_sub_msg.append(mensagens_respondidas_rapidamente['text'])


                dic_sub_msg[tempo_sub_msg] = lista_aux_sub_msg
                lista_sub_mensagens.append(dic_sub_msg)


        dados_usuario['mensagens_rapidas'] = lista_sub_mensagens #adicionando msg respondidas antes de dois minutos ...

        dados_organizados.append(dados_usuario) # adicionando os objetos a uma lista ...

        dados_usuario = {}

################################################################################
################################################################################

converter_json = json.dumps(str(dados_organizados), indent= 2, separators = (',',':'))

print(converter_json)

