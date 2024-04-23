class Exercicios: # Classe começa em maiusculo, metodo não
    # Método Construtor
    def __init__(self):
        self.num1 = 0
        self.num2 = 0
        self.numTexto = ""

    # Self é utilizado para informar que faz parte dessa classe

    def somar(self):
        return f"{self.num1} + {self.num2} = {self.num1 + self.num2}"

    def subtrair(self):
        return f"{self.num1} - {self.num2} = {self.num1 - self.num2}"

    def dividir(self):
        if(self.num2 == 0):
            return "Impossível dividir por 0"
        else:
            return f"{self.num1} / {self.num2} = {self.num1 / self.num2}"

    def multiplicar(self):
        return f"{self.num1} * {self.num2} = {self.num1 * self.num2}"

    # Exercício 1: Faça um programa que imprima os números de 1 a 10.
    def exercicio01(self):
        for i in range(1, 11, 1):
            self.numTexto += f"{i},"

        return self.numTexto

    # Exercício 2: Faça um programa que imprima os números pares de 1 a 20.
    def exercicio02(self):

        for i in range(2, 21, 2):
            self.numTexto += f"{i},"

        return self.numTexto

    # Exercício 3: Faça um programa que calcule a soma dos números de 1 a 100.
    def exercicio03(self):
        for i in range(1, 101, 1):
            self.num1 += i

        return self.num1

    # Exercício 4: Faça um programa que imprima os múltiplos de 5 de 1 a 50.
    def exercicio04(self):
        for i in range(1, 51, 1):
            if (i % 5 == 0):
                self.numTexto += f"{i},"

        return self.numTexto

    # Exercício 5: Faça um programa que peça um usuário um número e imprima se é par ou ímpar.
    def exercicio05(self):
        if (self.num1 % 2 == 0):
            return "Par"
        else:
            return "Ímpar"

    # Exercício 6: Faça um programa que peça um usuário um número e imprima se é positivo,
    #              negativo ou zero.
    def exercicio06(self):
        if (self.num1 > 0):
            return "Positivo"
        elif (self.num1 < 0):
            return "Negativo"
        else:
            return "Zero"

    # Exercício 7: Faça um programa que peça ao usuário um número e imprima a tabuada
    #              desse número.
    def exercicio07(self):
        self.numTexto = ""

        for i in range(0, 11, 1):
            self.numTexto += f"{self.num1} * {i} = {self.num1 * i}\n"
        return f"Tabuada do {self.num1}: \n{self.numTexto}"

    # Exercício 8: Faça um programa que peça ao usuário um número e imprima os números
    #              de 1 até esse número.
    def exercicio08(self):
        self.numTexto = ""

        for i in range(1, self.num1 + 1, 1):
            self.numTexto += f"{i}, "

        return self.numTexto

    # Exercício 9: Faça um programa que peça ao usuário e imprima a soma dos números de 1
    #              até esse número.
    def exercicio09(self):
        self.num2 = 0

        for i in range(1, self.num1 + 1, 1):
            self.num2 += i

        return self.num2

    # Exercício 10: Faça um programa que imprima os números primos de 1 a 20.
    def exercicio10(self):
        self.numTexto = ""

        for i in range(1, 21, 1):
            if (i == 2 or i == 3 or i == 5 or i == 7):
                self.numTexto += f"{i}, "
            elif (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
                self.numTexto += f"{i}, "
            else:
                continue

        return self.numTexto

    # Exercício 11: Faça um programa que peça ao usuário um número e verifique se é primo.
    def exercicio11(self):
        if (self.num1 < 2):
            return "Não é primo"
        elif (self.num1 == 2 or self.num1 == 3 or self.num1 == 5 or self.num1 == 7):
            return "Primo"
        elif (self.num1 % 2 != 0 and self.num1 % 3 != 0 and self.num1 % 5 != 0 and self.num1 % 7 != 0):
            return "Primo"
        else:
            return "Não é primo"

    # Exercício 12: Faça um programa que calcule o fatorial de um número.
    def exercicio12(self):
        self.num2 = self.num1

        while (self.num1 > 1):
            self.num2 = self.num2 * (self.num1 - 1)
            self.num1 -= 1

        return self.num2

    # Exercício 13: Faça um programa que imprima a sequência de Fibonacci até o décimo termo.
    def exercicio13(self):
        self.num1 = 1
        self.num2 = 1
        self.termoAuxiliar = 0
        self.numTexto = "1, 1, "

        for i in range(3, 11, 1):
            self.termoAuxiliar = self.num1 + self.num2
            self.num1 = self.num2
            self.num2 = self.termoAuxiliar
            self.numTexto += f"{self.num2}, "

        return self.numTexto

    # Exercício 14: Faça um programa que peça ao usuário um número e imprima se é um número de Fibonacci.
    def exercicio14(self):
        self.num2 = 1
        self.num3 = 1
        self.termoAuxiliar = 0

        while (self.num1 > self.num2):
            self.termoAuxiliar = self.num2 + self.num3
            self.num2 = self.num3
            self.num3 = self.termoAuxiliar

            if (self.num1 == self.num2):
                return "É um número Fibonacci"

        return "Não é um número Fibonacci"

    # Exercício 15: Faça um programa que peça ao usuário um número e calcule a soma dos seus digitos.
    def exercicio15(self):
        self.num2 = 0

        for i in self.numTexto:
            self.num2 += int(i)

        return self.num2

    # Exercício 16: Faça um programa que peça ao usuário um número e imprima os números pares e
    #               ímpares de 1 até esse número.
    def exercicio16(self):
        self.tabPar = ""
        self.tabImpar = ""


        for i in range(1, self.num1 + 1, 1):
            if (i % 2 == 0):
                self.tabPar += f"{i}, "
            else:
                self.tabImpar += f"{i}, "

        return f"Número pares:\n{self.tabPar}\n\nNúmeros ímpares:\n{self.tabImpar}"

    # Exercício 17: Faça um programa que peça ao usuário um número e imprima os números primos de
    #               1 até esse número.
    def exercicio17(self):
        self.numTexto = ""

        for i in range(2, self.num1 + 1, 1):
            if (self.num1 < 2):
                return "Informe um número maior que 1"
            elif (i == 2 or i == 3 or i == 5 or i == 7):
                self.numTexto += f"{i}, "
            elif (i % 2 != 0 and i % 3 != 0 and i % 5 != 0 and i % 7 != 0):
                self.numTexto += f"{i}, "
            else:
                continue
        return self.numTexto

    # Exercício 18: Faça um programa que peça ao usuário um número e imprima a sequência de Collatz
    #               desse número.
    def exercicio18(self):
        self.collatz = f"{self.num1}"

        while (self.num1 != 1):
            if (self.num1 % 2 == 0):
                self.num1 = self.num1 // 2
                self.collatz += f", {self.num1}"
            else:
                self.num1 = (self.num1 * 3) + 1
                self.collatz += f", {self.num1}"

        return self.collatz

    # Exercício 19: Faça um programa que peça ao usuário um número e imprima a soma dos números
    #               pares e ímpares de 1 até esse número.
    def exercicio19(self):
        self.somaPar = 0
        self.somaImpar = 0

        for i in range(1, self.num1 + 1, 1):
            if (i % 2 == 0):
                self.somaPar += i
            else:
                self.somaImpar += i

        return f"Soma dos números pares:\n{self.somaPar}\nSoma dos número ímpares:\n{self.somaImpar}"

    # Exercício 20: Faça um programa que peça ao usuário um número e imprima se é um número perfeito
    #               (a soma de seus divisores, excluindo ele mesmo, é igual ao próprio número).
    def exercicio20(self):
        self.divisores = 0

        for i in range(1, self.num1, 1):
            if (self.num1 % i == 0):
                self.divisores += i

        if (self.divisores == self.num1):
            return "Número Perfeito"
        else:
            return "Não é número perfeito"