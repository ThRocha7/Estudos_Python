lista_id = [[123, 124], [125, 126]]
lista_mensagens = ['abacate', 'pera']
 

id_msg_alterada = 123
msg_editada = 'maçã'
 

for i in lista_id:
    if id_msg_alterada in i:
        print(lista_id.index(i))  

print(lista_id[0][1])

        # if id_msg_alterada == lista_id[i][0]:
        #     lista_mensagens[i] = msg_editada
        # else:
        #     print('não encontrei')
 
print(lista_mensagens)
 