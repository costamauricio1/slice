lista = ["Python",30.61,"Java",51,["a","b",20],"maçã"]

print(f"Tamanho da lista = {len(lista)}") #função utilizada pra saber o tamanho da sequência.

for i,item in enumerate(lista):#enumera a lista
  print(f"Posição = {i},\t valor = {item} -----> tipo individual = {type(item)}")#enumera identificando algumas características, como posição na lista e seu tipo.

print("\nExemplos de Slice:\n")  #slice são fatiamentos da lista.

print("lista[1]=",lista[1])#pega a posição 1 na lista. No caso, começa a contar o 0, logo a posição 1 é a segunda, e assim por diante. 
print("lista[0:2]=", lista[0:2])#lembrando que não conta o valor superior, apenas o inferior. 
print("lista[:2]=", lista[:2])#mostrando que caso seja a posição 0, não precisa de colocar o 0. 
print("lista[3:5]=", lista[3:5])#basta subtrair para saber quais posições serão analisadas, no caso 5-3=2, duas posições começando da posição 3, ou seja, a quarta, sendo terceira e quarta.
print("lista[3:6]=", lista[3:6])
print("lista[3:]", lista[3:])#vai até o final das posições.
print("lista[-2]=", lista[-2])#vê as posições d regredindo do 0 ao -2.
print("lista[-1]=", lista[-1])#mesma coisa
print("lista[-3]=", lista[-3])
print("lista[4][1]=", lista[4][1])#vê a posição 1 da lista da posição 4.
