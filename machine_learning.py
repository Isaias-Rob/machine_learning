import math
import statistics as s
arquivo = open('entradas_saidas.txt', 'r') #abrir arquivo de amostra
temp = [] #armazenar vetor temporario
soma_temp = 0 #soma temporaria para distancia euclidiana
valores = [] #valores armazenados dos vetores de entrada
canais = [] #canais armazenados no arquivo (saida)
entrada = [-80, -54, -73, -66, -69, -68, -61, -62, -56, -58, -72, -57, -63, -53, -77, -70, -78, -55, -71] #entrada de dados para decisao
euclidiana = [] #armazenamento das euclidianas
count = 0 #variavel de contagem
for i in arquivo.readlines(): #ler linha por linha
    linha = i.split(' ') #caractere separado por espacos
    #print('linha', linha)
    #input()
    for j in linha: #pegando caractere por caractere da linha (i) na variavel (j)
        #print(int(j))
        count+=1
        if(count<20):
            temp.append(int(j)) #adcionando caracteres no vetor temporario
            #print('temp', temp)
        else:
            canais.append(int(j)) #terminado valores, armazenar a saida para aqueles valores
            #print('canal', canais)
            count = 0 #zerar contagem
            #input()
            for k in range(0,len(temp)): #para cada elemento do vetor temporario
                soma_temp = soma_temp + ((entrada[k] - temp[k])**2) #soma da formula euclidiana
                #print('soma_temp', soma_temp)
                #input()
            if(soma_temp < 0):
                euclidiana.append(math.sqrt((soma_temp*-1))) #raiz quadrada da formula euclidiana, condicao caso a soma seja negativa para evitar erros
                #print('euclidiana', euclidiana)
                soma_temp = 0
                temp.clear()
            else:
                euclidiana.append(math.sqrt(soma_temp)) #condicao positiva
                #print('euclidiana', euclidiana)
                soma_temp = 0
                temp.clear()
    #input()
print("Canal {}, euclidiana {}".format(canais[euclidiana.index(min(euclidiana))], min(euclidiana))) #resultado







