from time import sleep as s
print("Olá, vou te auxiliar no cáculo de ROI")
print("-------------------------------------")

lReceita = []
periodo = 1
receita = input("Digite o valor da receita de seu projeto: \n0- se não tiver a receita\n")

receitaTotal = 0
while float(receita) == 0:
    adicionando = input("Vou te ajudar! Caso queira o resultado diga: R\nPara adicionar o período diga: P\n- Diga um gasto: ")
    if adicionando == "R":
        receita = receitaTotal * float(periodo)
        print("RECEITA: {}".format(receita))
        break

    elif adicionando == "P":
        periodo = input("Insira o período de tempo: ")

    else:
        lReceita.append(float(adicionando))
        receitaTotal = sum(lReceita)

print("Receita: {}\nCerto, Agora que sabemos sua receita vamos começar".format(receita))
valor = float(input("Diga o valor investido analisado: "))

#tempo = float(input("Agora diga o período de tempo do projeto "))

#valor = valor * tempo

ROI = float(receita) - valor
ROI = ROI / valor
ROI = ROI * 100
print("\n\nCalculando tudo, definimos que o ROI vale: {0:.1f}".format(ROI))


s(10)