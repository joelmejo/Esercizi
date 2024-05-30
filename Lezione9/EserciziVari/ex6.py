# Data una lista di interi, chiamata tree, che rappresenta un albero binario, restituire True
# se l'albero è simmetrico; False altrimenti.

# La lista di interi è formata così:

#     L'elemento in posizione 0 corrisponde alla radice
#     Dato un nodo in posizione i, il suo figlio sinistro si trova in posizione 2*i + 1
#     Dato un nodo in posizione i, il suo figlio destro si trova in posizione 2*(i+1)
#     Se, dato un indice i si va fuori bound facendo almeno uno dei calcoli dei punti precedenti,
#        significa che il nodo che corrisponde a quell'indice è una foglia.
# Potete utilizzare la classe TreeNode per crearvi prima l'albero - anziché usare la lista tree -
#    e poi visitare l'albero sfruttando gli oggetti di tipo TreeNode.

def symmetric(tree: list[int]) -> bool:
    # scrivere qui la vostra funzione
    left_branch: list[int] = []
    right_branch: list[int] = []

    def get_left_child(i: int):
        if 2*i + 1 < len(tree):
            i = 2*i + 1
            return i
        else:
            return None
    
    def get_right_child(i: int):
        if 2*(i+1) < len(tree):
            i = 2*(i+1)
            return i
        else:
            return None
    i: int= 0
    while len(left_branch) != (len(tree) -1) // 2:
        if get_left_child(i) != None:
            i = get_left_child(i)
            left_branch.append(tree[i])
        else:
            i = (i - 1) // 2
            if get_right_child(i) != None:
                i = get_right_child(i)
                left_branch.append(tree[i])

    i: int= 0
    while len(right_branch) != (len(tree) -1) // 2:
        if get_right_child(i) != None:
            i = get_right_child(i)
            right_branch.append(tree[i])
        else:
            i = (i // 2) - 1
            if get_left_child(i) != None:
                i = get_left_child(i)
                right_branch.append(tree[i])
    print(left_branch)
    print(right_branch)
    return left_branch == right_branch

print(symmetric([1,2,2,3,4,4,3])) #True

print(symmetric([1,2,2,None,3,None,3])) #False

print(symmetric([1,2,2,None,3,3,None])) #True

print(symmetric([1,2,2,3,None,None,3])) #True