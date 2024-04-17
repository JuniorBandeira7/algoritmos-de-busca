actions = { 
    (0,0,0,0,0,0,0,0,0): [(1,0,0,1,0,0,0,0,1), (0,0,0,0,0,0,1,1,1)],
    (1,0,0,0,1,0,0,0,1): [(0,0,0,0,0,0,0,0,0)],
    (0,0,0,0,0,0,1,1,1): [(0,0,0,0,0,0,0,1,0), (0,0,0,0,0,0,0,0,0)],
    (0,0,0,0,0,0,0,1,0): [(0,0,1,0,0,0,1,1,1), (0,0,1,0,0,0,1,1,1), (0,0,0,0,1,0,1,1,1), (0,0,0,0,0,1,1,1,1)],##precisa terminar
}
#print(actions[(0,0,0,0,0,0,0,0,0)])

resposta = None
pilhaDeAbertos = [[(0,0,0,0,0,0,0,0,0)]]#Armazena os caminhos em vez de apenas os nós
listaDeFechados = []
sucesso = False
while sucesso == False and pilhaDeAbertos != []:
    caminhoAtual = pilhaDeAbertos.pop(0)#Remover o primeiro caminho da lista
    noCandidato = caminhoAtual[-1]#Pegar o último nó do caminho atual
    listaDeFechados.append(noCandidato)
    for i in actions[noCandidato]:
        if i == (0,0,0,0,0,1,1,1,1):
            sucesso = True
            caminhoAtual.append(17)#Adicionar o nó de destino ao caminho atual
            resposta = caminhoAtual#Armazenar o caminho encontrado
            break
        else:
            if i not in listaDeFechados:
                novoCaminho = caminhoAtual.copy()#Criar uma cópia do caminho atual
                novoCaminho.append(i)#Adicionar o novo nó ao caminho
                pilhaDeAbertos.append(novoCaminho)
if sucesso == False:
    print("Não achou")
else:
    print("Caminho encontrado:", resposta)

