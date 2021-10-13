import constants as c #arquivo de valores padrão dos pesos
import random #biblioteca usada para gerar os valores de entrada

adj = [c.peso_e, c.peso_d, c.peso_c, c.peso_b, c.peso_a, c.peso_b, c.peso_c, c.peso_d, c.peso_e]#vetor com adjacencias, valores sao padrao para todos os canais
#a lógica é (peso menor --aumento gradual--> canal de referencia <--diminuicao gradual-- peso menor), sendo 5 pesos pra cada lado, e o canal de referencia no meio

#canais = random.sample(range(-80, -50),19) #alimentando todos os canais com valores aleatorios entre -50 e -80 (inclusive os que não são conectáveis)
canais = [-80, -54, -73, -66, -69, -68, -61, -62, -56, -58, -72, -57, -63, -53, -77, -70, -78, -55, -71] #testando os canais de entrada

soma = 0 #variavel temporaria para soma de pesos
total = [] #variavel principal que armazenara as somas totais dos 11 canais disponiveis pra conectar-se

arquivo = open(r"entradas_saidas.txt","a+")
for i in range(0,19):
    arquivo.write(str(canais[i]))
    arquivo.write(' ')

for i in range(4, 15): #começando do indice 4 do vetor, que equivale ao canal 1, o primeiro canal conectável, até o 15 onde está o canal 11
    print("Adjacencias do CANAL {:2}\t\t PESO {:.2f}\t\t VALOR {}:".format(i-3, adj[4], canais[i])) #print do canal de referencia nessa execuçao
    print()
    soma = 0
    if(canais[i] > -60): #se esse canal for maior que -60 dbm, não podemos considerar como uma possibilidade
        total.append(1000) #peso muito grande no vetor, para que o sistema nao o escolha
        print("Impossivel de conectar neste canal, valor ultrapassa -60 dbm")
        print("________________________________________________________________________________________\n")
        continue #voltamos ao laço principal, para o proximo canal de referência
    else:
        for j in range(-7, 2): #caso o canal seja viavel, comecamos a calcular os canais adjacentes com base nos pesos
            print("Canal {:2} ---- peso {:.2f} ---- valor {}".format(i+j, adj[j+7], canais[i+j+3]))
            soma = soma + (canais[i+j+3] * adj[j+7]) #adcionando a soma com o valor deste peso, a formula é soma + (canal * peso)
            print("---->soma: {:.2f}".format(soma))
            print("********************************************")
    print("SOMA TOTAL: {:.2f}".format(soma)) #soma total dos pesos nesse canal, o quanto sera "custoso" se conectar nele
    total.append(soma) #adcionando esse valor no vetor principal
    print("___________________________________________________________________________________________\n")
soma = 0
for i in range(0, 11): #usando o laço para dois fatores
    if(total[i] == 1000):
        soma+=1 # a variavel soma sera reutilizada para um controle com o proposito de evitar um bug
        print("| CANAL {:2} -> SOMA TOTAL: Inapto |".format(i+1, total[i])) #caso o total seja 1000, significa que é um canal inapto
    else:
        print("| CANAL {:2} -> SOMA TOTAL: {:.2f} |".format(i+1, total[i])) #print comum do valor no canal apto
print("\n")
if(soma == 11): #soma valendo 11 neste contexto, significa que todos os canais estao com valor > -60 dbm, todos sao inviaveis
    print("Impossivel conectar em todos os canais!") #sem esse controle, o programa escolheria o primeiro canal que viesse, mesmo sendo inapto
    arquivo.write("Inapto")
elif(canais[4] == min(total)):
    print("Canal escolhido {} com o valor de {:.2f} em sua soma".format(1, total[0])) #os tres elifs (contando com esse) servem para priorizar os canais 1, 6 e 11
    arquivo.write("1")
elif(canais[9] == min(total)):
    print("Canal escolhido {} com o valor de {:.2f} em sua soma".format(6, total[5])) #caso os canais 1, 6 e 11 tenham o valor minimo tambem, escolhemos eles
    arquivo.write("6")
elif(canais[14] == min(total)):
    print("Canal escolhido {} com o valor de {:.2f} em sua soma".format(11, total[10])) # para evitar que o programa pegue um outro canal com mesmo valor de peso
    arquivo.write("11")
else:
    print("Canal escolhido {} com o valor de {:.2f} em sua soma".format(total.index(min(total))+1, min(total))) #caso contrario, escolher o canal mais "barato"
    arquivo.write(str(total.index(min(total))+1))
arquivo.write('\n')
arquivo.close()

