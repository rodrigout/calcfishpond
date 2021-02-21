#App  para saber quantos peixes para um viveiro
# tilapias por metros cubicos = 20 cada 1 quilo
#cada metro quadrado 1.6 tilapias

larg = float(input("largura do viveiro:")) # largura do viveiro
comp = float(input("comprimento do viveiro:")) #comprimento do viveiro

tilapia = 1.6

peixes = (larg * comp)*tilapia #calculo de tamanho do viveiro
print("O numero de tilapias é:", peixes) #resultados