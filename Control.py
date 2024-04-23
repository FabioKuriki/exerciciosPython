from Exercicios import Exercicios

class Control:
    def __init__(self):
        self.exer = Exercicios()
        self.opcao = -1
        self.opcao2 = -1
        self.opcao3 = -1

    def coletar(self):
        self.exer.num1 = int(input("Informe o primeiro número: "))
        self.exer.num2 = int(input("Informe o segundo número: "))

    def coletar1num(self):
        self.exer.num1 = int(input("Informe um número: "))
        while (self.exer.num1 < 1):
            self.exer.num1 = int(input("Informe um número maior ou igual a 1\n\nInforme um número: "))

    def coletarTexto(self):
        self.exer.num1 = int(input("Informe um número: "))
        while (self.exer.num1 < 1):
            self.exer.num1 = int(input("Informe um número maior ou igual a 1\n\nInforme um número: "))

        self.exer.numTexto = str(self.exer.num1)

    def menu(self):
        self.opcao2 = int(input("-------- Menu ---------\n\n" +
                           "\n0. Voltar" +
                           "\n1. Somar" +
                           "\n2. Subtrair" +
                           "\n3. Dividir" +
                           "\n4. Multiplicar" +
                           "\nEscolha uma das opções acima: "))

    def menuExericios(self):
        self.opcao3 = int(input("-------- Menu ---------\n\n" +
                               "\n0. Voltar" +
                               "\n1. Exercício 01" +
                               "\n2. Exercício 02" +
                               "\n3. Exercício 03" +
                               "\n4. Exercício 04" +
                               "\n5. Exercício 05" +
                               "\n6. Exercício 06" +
                               "\n7. Exercício 07" +
                               "\n8. Exercício 08" +
                               "\n9. Exercício 09" +
                               "\n10. Exercício 10" +
                               "\n11. Exercício 11" +
                               "\n12. Exercício 12" +
                               "\n13. Exercício 13" +
                               "\n14. Exercício 14" +
                               "\n15. Exercício 15" +
                               "\n16. Exercício 16" +
                               "\n17. Exercício 17" +
                               "\n18. Exercício 18" +
                               "\n19. Exercício 19" +
                               "\n20. Exercício 20" +
                               "\nEscolha uma das opções acima: "))

    def menuSelecionar(self):
        self.opcao = int(input("-------- Menu ---------\n\n" +
                               "\n0. Sair" +
                               "\n1. Operações" +
                               "\n2. Exercícios" +
                               "\nEscolha uma das opções acima: "))

    def menuSelecionarCompleto(self):
        while(self.opcao != 0):
            self.menuSelecionar()
            if(self.opcao == 0):
                print("Obrigado")
            elif(self.opcao == 1):
                self.operacao()
            elif(self.opcao == 2):
                self.menuExerciciosCompleto()
            else:
                print("Selecione uma opção válida!")

    def operacao(self):
        while(self.opcao2 != 0):
            self.menu()
            if(self.opcao2 == 0):
                print("Voltando")
            elif(self.opcao2 == 1):
                self.coletar()
                print(self.exer.somar())
            elif(self.opcao2 == 2):
                self.coletar()
                print(self.exer.subtrair())
            elif (self.opcao2 == 3):
                self.coletar()
                print(self.exer.dividir())
            elif (self.opcao2 == 4):
                self.coletar()
                print(self.exer.multiplicar())
            else:
                print("Erro! Opção inválida!")

    def menuExerciciosCompleto(self):
        while(self.opcao3 != 0):
            self.menuExericios()
            if(self.opcao3 == 0):
                print("Obrigado")
            elif(self.opcao3 == 1):
                print(self.exer.exercicio01())
            elif(self.opcao3 == 2):
                print(self.exer.exercicio02())
            elif(self.opcao3 == 3):
                print(self.exer.exercicio03())
            elif(self.opcao3 == 4):
                print(self.exer.exercicio04())
            elif(self.opcao3 == 5):
                self.coletar1num()
                print(self.exer.exercicio05())
            elif(self.opcao3 == 6):
                self.coletar1num()
                print(self.exer.exercicio06())
            elif(self.opcao3 == 7):
                self.coletar1num()
                print(self.exer.exercicio07())
            elif(self.opcao3 == 8):
                self.coletar1num()
                print(self.exer.exercicio08())
            elif(self.opcao3 == 9):
                self.coletar1num()
                print(self.exer.exercicio09())
            elif(self.opcao3 == 10):
                self.coletar1num()
                print(self.exer.exercicio10())
            elif(self.opcao3 == 11):
                self.coletar1num()
                print(self.exer.exercicio11())
            elif(self.opcao3 == 12):
                self.coletar1num()
                print(self.exer.exercicio12())
            elif(self.opcao3 == 13):
                print(self.exer.exercicio13())
            elif(self.opcao3 == 14):
                self.coletar1num()
                print(self.exer.exercicio14())
            elif(self.opcao3 == 15):
                self.coletarTexto()
                print(self.exer.exercicio15())
            elif(self.opcao3 == 16):
                self.coletar1num()
                print(self.exer.exercicio16())
            elif(self.opcao3 == 17):
                self.coletar1num()
                print(self.exer.exercicio17())
            elif(self.opcao3 == 18):
                self.coletar1num()
                print(self.exer.exercicio18())
            elif(self.opcao3 == 19):
                self.coletar1num()
                print(self.exer.exercicio19())
            elif(self.opcao3 == 20):
                self.coletar1num()
                print(self.exer.exercicio20())
            else:
                print("Selecione uma opção válida!")
