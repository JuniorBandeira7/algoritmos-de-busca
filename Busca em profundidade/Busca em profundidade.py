grafo = {
    (0,0,0,0,0,0,0,0,0): [(1,0,0,1,0,0,0,0,1), (0,0,0,0,0,0,1,1,1)],
    (1,0,0,1,0,0,0,0,1): [(0,0,0,0,0,0,0,0,0)],
    (0,0,0,0,0,0,1,1,1): [(0,0,0,0,0,0,0,0,0), (0,0,0,0,0,0,0,1,0)],
    (0,0,0,0,0,0,0,1,0): [(0,0,0,0,0,0,1,1,1), (0,1,0,0,0,0,1,1,1), (0,0,1,0,0,0,1,1,1), (0,0,0,0,1,0,1,1,1), (0,0,0,0,0,1,1,1,1)],
    (0,1,0,0,0,0,1,1,1): [(0,0,0,0,0,0,0,1,0), (0,1,0,0,0,0,0,0,0)],
    (0,0,1,0,0,0,1,1,1): [(0,0,0,0,0,0,0,1,0), (0,0,1,0,0,0,0,0,0)],
    (0,0,0,0,1,0,1,1,1): [(0,0,0,0,0,0,0,1,0), (0,0,0,0,1,0,0,0,0)],
    (0,0,0,0,1,0,0,0,0): [(1,0,0,1,1,0,0,0,1), (0,0,0,0,1,0,1,1,1), (0,0,0,1,1,0,0,0,1), (0,0,0,1,1,1,0,0,1)],
    (0,0,0,1,1,0,0,0,1): [(0,0,0,0,1,0,0,0,0), (0,0,0,0,0,0,0,0,0)],
    (0,0,0,0,0,1,1,1,1): [(0,0,0,0,0,0,0,1,0), (0,0,0,0,0,1,0,0,0)],
    (0,1,0,0,0,0,0,0,0): [(1,1,1,0,0,0,0,0,1), (0,1,0,0,0,0,1,1,1), (1,1,0,1,0,0,0,0,1)],
    (0,0,1,0,0,0,0,0,0): [(1,1,1,0,0,0,0,0,1), (0,0,1,0,0,0,1,1,1), (1,0,0,1,1,0,0,0,1)],
    (0,0,0,0,0,1,0,0,0): [(0,0,0,1,1,1,0,0,1), (0,0,0,0,0,1,1,1,1), (1,0,0,1,0,1,0,0,1)],
    (1,1,1,0,0,0,0,0,1): [(0,0,1,0,0,0,0,0,0), (0,1,0,0,0,0,0,0,0), (0,1,1,0,0,0,0,0,0)],
    (1,1,0,1,0,0,0,0,1): [(0,1,0,0,0,0,0,0,0)],
    (1,0,1,1,0,0,0,0,1): [(0,0,1,0,0,0,0,0,0)],
    (0,0,0,1,1,1,0,0,1): [(0,0,0,0,1,1,0,0,0), (0,0,0,0,0,1,0,0,0), (0,0,0,0,1,0,0,0,0)],
    (1,0,0,1,1,0,0,0,1): [(0,0,0,0,1,0,0,0,0)],
    (1,0,0,1,0,1,0,0,1): [(0,0,0,0,0,1,0,0,0)],
    (0,1,1,0,0,0,0,0,0): [(1,1,1,0,0,0,0,0,1), (1,1,1,1,0,0,0,0,1), (0,1,1,0,0,0,1,1,1)],
    (0,0,0,0,1,1,0,0,0): [(0,0,0,1,1,1,0,0,1), (1,0,0,1,1,1,0,0,1), (0,0,0,0,1,1,1,1,1)],
    (1,1,1,1,0,0,0,0,1): [(1,1,1,0,0,0,0,0,0), (0,1,1,0,0,0,0,0,0)],
    (0,1,1,0,0,0,1,1,1): [(0,1,1,0,0,0,0,0,0)],
    (1,0,0,1,1,1,0,0,1): [(0,0,0,1,1,1,0,0,0), (0,0,0,0,1,1,0,0,0)],
    (0,0,0,0,1,1,1,1,1): [(0,0,0,0,1,1,0,0,0)],
    (1,1,1,0,0,0,0,0,0): [(1,1,1,1,1,0,0,0,1), (1,1,1,1,0,1,0,0,1), (1,1,1,1,0,0,0,0,1), (1,1,1,0,0,0,1,1,1)],
    (0,0,0,1,1,1,0,0,0): [(1,1,0,1,1,1,0,0,1), (1,0,1,1,1,1,0,0,1), (1,0,0,1,1,1,0,0,1), (0,0,0,1,1,1,1,1,1)],
    (1,1,1,1,1,0,0,0,1): [(0,1,1,0,1,0,0,0,0), (1,1,1,0,0,0,0,0,0)],
    (1,1,1,1,0,1,0,0,1): [(0,1,1,0,0,1,0,0,0), (1,1,1,0,0,0,0,0,0)],
    (1,1,1,0,0,0,1,1,1): [(0,1,1,0,0,0,1,1,0), (0,0,1,0,0,0,1,1,0), (0,1,0,0,0,0,1,1,0), (1,1,1,0,0,0,0,0,0)],
    (1,1,0,1,1,1,0,0,1): [(0,0,0,1,1,1,0,0,0), (0,1,0,0,1,1,0,0,0)],
    (1,0,1,1,1,1,0,0,1): [(0,0,0,1,1,1,0,0,0), (0,0,1,0,1,1,0,0,0)],
    (0,0,0,1,1,1,1,1,1): [(0,0,0,0,1,1,1,1,0), (0,0,0,0,0,1,1,1,0), (0,0,0,0,1,0,1,1,0), (0,0,0,1,1,1,0,0,0)],
    (0,1,1,0,1,0,0,0,0): [(1,1,1,1,1,0,0,0,1), (0,1,1,0,1,0,1,1,1)],
    (0,1,1,0,0,1,0,0,0): [(1,1,1,1,0,1,0,0,1), (0,1,1,0,0,1,1,1,1)],
    (0,1,1,0,0,0,1,1,0): [(1,1,1,0,0,0,1,1,1), (1,1,1,1,0,0,1,1,1)],
    (0,0,1,0,0,0,1,1,0): [(1,1,1,0,0,0,1,1,1), (1,0,1,1,0,0,1,1,1)],
    (0,1,0,0,0,0,1,1,0): [(1,1,1,0,0,0,1,1,1), (1,1,0,1,0,0,1,1,1)],
    (0,1,0,0,1,1,0,0,0): [(1,1,0,1,1,1,0,0,1), (0,1,0,0,1,1,1,1,1)],
    (0,0,1,0,1,1,0,0,0): [(1,0,1,1,1,1,0,0,1), (0,0,1,0,1,1,1,1,1)],
    (0,0,0,0,1,1,1,1,0): [(1,0,0,1,1,1,1,1,1), (0,0,0,1,1,1,1,1,1)],
    (0,0,0,0,0,1,1,1,0): [(1,0,0,1,0,1,1,1,1), (0,0,0,1,1,1,1,1,1)],
    (0,0,0,0,1,0,1,1,0): [(1,0,0,1,1,0,1,1,1), (0,0,0,1,1,1,1,1,1)],
    (0,1,1,0,1,0,1,1,1): [(0,1,1,0,1,0,0,0,0)],
    (0,1,1,0,0,1,1,1,1): [(0,1,1,0,0,1,0,0,0)],
    (1,1,1,1,0,0,1,1,1): [(0,1,1,0,0,0,1,1,0), (1,1,1,0,0,0,1,1,0), (1,1,1,1,0,0,0,0,0)],
    (1,0,1,1,0,0,1,1,1): [(0,0,1,0,0,0,1,1,0), (1,0,1,1,0,0,0,0,0)],
    (1,1,0,1,0,0,1,1,1): [(0,1,0,0,0,0,1,1,0), (1,1,0,1,0,0,0,0,0)],
    (0,1,0,0,1,1,1,1,1): [(0,1,0,0,1,1,0,0,0)],
    (0,0,1,0,1,1,1,1,1): [(0,0,1,0,1,1,0,0,0)],
    (1,0,0,1,1,1,1,1,1): [(0,0,0,1,1,1,1,1,0), (1,0,0,1,1,1,0,0,0), (0,0,0,0,1,1,1,1,1)],
    (1,0,0,1,0,1,1,1,1): [(0,0,0,0,0,1,1,1,0), (1,0,0,1,0,1,0,0,0)],
    (1,0,0,1,1,0,1,1,1): [(0,0,0,0,1,0,1,1,0), (1,0,0,1,1,0,0,0,0)],
    (1,1,1,0,0,0,1,1,0): [(1,1,1,1,0,0,1,1,1), (1,1,1,1,1,0,1,1,1), (1,1,1,1,0,1,1,1,1),],
    (1,1,1,1,0,0,0,0,0): [(1,1,1,1,0,0,1,1,1)],
    (1,0,1,1,0,0,0,0,0): [(1,0,1,1,0,0,1,1,1)],
    (1,1,0,1,0,0,0,0,0): [(1,1,0,1,0,0,1,1,1)],
    (0,0,0,1,1,1,1,1,0): [(1,0,0,1,1,1,1,1,1), (1,1,0,1,1,1,1,1,1), (1,0,1,1,1,1,1,1,1)],
    (1,0,0,1,1,1,0,0,0): [(1,0,0,1,1,1,1,1,1)],
    (1,0,0,1,0,1,0,0,0): [(1,0,0,1,0,1,1,1,1)],
    (1,0,0,1,1,0,0,0,0): [(1,0,0,1,1,0,1,1,1)],
    (1,1,1,1,1,0,1,1,1): [(1,1,1,0,0,0,1,1,0), (1,1,1,1,1,0,0,0,0)],
    (1,1,1,1,0,1,1,1,1): [(1,1,1,0,0,0,1,1,0), (1,1,1,1,0,1,0,0,0)],
    (1,1,0,1,1,1,1,1,1): [(0,0,0,1,1,1,1,1,0), (1,1,0,1,1,1,0,0,0)],
    (1,0,1,1,1,1,1,1,1): [(0,0,0,1,1,1,1,1,0), (1,0,1,1,1,1,0,0,0)],
    (1,1,1,1,1,0,0,0,0): [(1,1,1,1,1,1,1,0,1), (1,1,1,1,1,0,1,1,1)],
    (1,1,1,1,0,1,0,0,0): [(1,1,1,1,1,1,1,0,1), (1,1,1,1,0,1,1,1,1)],
    (1,1,0,1,1,1,0,0,0): [(1,1,1,1,1,1,1,0,1), (1,1,0,1,1,1,1,1,1)],
    (1,0,1,1,1,1,0,0,0): [(1,1,1,1,1,1,1,0,1), (1,0,1,1,1,1,1,1,1)],
    (1,1,1,1,1,1,1,0,1): [(1,1,1,1,1,1,0,0,0), (1,0,1,1,1,1,0,0,0), (1,1,0,1,1,1,0,0,0), (1,1,1,1,0,1,0,0,0), (1,1,1,1,1,0,0,0,0)],
    (1,1,1,1,1,1,0,0,0): [(1,1,1,1,1,1,1,0,1), (1,1,1,1,1,1,1,1,1)]
}


resposta = None
pilhaDeAbertos = [[(0,0,0,0,0,0,0,0,0)]]#Armazena os caminhos em vez de apenas os nós
lista_de_caminhos_fechados = []
sucesso = False
while sucesso == False and pilhaDeAbertos != []:
    caminhoAtual = pilhaDeAbertos.pop()#Remover o primeiro caminho da lista
    noCandidato = caminhoAtual[-1]#Pegar o último nó do caminho atual
    lista_de_caminhos_fechados.append(noCandidato)
    for i in grafo[noCandidato]:
        if i == (1,1,1,1,1,1,1,1,1):
            sucesso = True
            caminhoAtual.append((1,1,1,1,1,1,1,1,1))#Adicionar o nó de destino ao caminho atual+
            resposta = caminhoAtual#Armazenar o caminho encontrado
            break
        else:
            if i not in lista_de_caminhos_fechados:
                novoCaminho = caminhoAtual.copy()#Criar uma cópia do caminho atual
                novoCaminho.append(i)#Adicionar o novo nó ao caminho
                pilhaDeAbertos.append(novoCaminho)
if sucesso == False:
    print("Não achou")
else:
    print("Caminho encontrado:", resposta)

