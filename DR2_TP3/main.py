import math


# TP 3.1
def sliceString(str):
    str_len = len(str)
    half_str = math.ceil(str_len / 2)

    return str[0:half_str], str[half_str:str_len]

input_str = input("Olá, usuário! Digite uma string: ")
print(sliceString(input_str))

"""
#------------------------------------------------------------------------------------
# TP 3.2
def startsWithPrefix(first_str, second_str):
    prefix = first_str[:3]

    if second_str.startswith(prefix):
        print(f"A palavra {second_str} começa com o mesmo prefixo ({prefix}) da palavra {first_str}!")
    else:
        print(f"A palavra {second_str} NÃO começa com o mesmo prefixo ({prefix}) da palavra {first_str}!")

def getUserInput():
    strings = []

    for i in range(2):
        if i == 0:
            str_input = input("Olá usuário, digite a primeira palavra: ")
            strings.append(str_input)
        else:
            str_input = input("Olá usuário, digite a segunda palavra: ")
            strings.append(str_input)
        
    return strings


first_string, second_string = getUserInput()
startsWithPrefix(first_string, second_string)

#------------------------------------------------------------------------------------

# TP 3.3
def transformToList(str):
    char_list = []

    for i in range(len(str)):
        char_list.append(str[i])

    return char_list

input_str = input("Olá, usuário! Por favor, digite uma string: ")
print(transformToList(input_str))

#------------------------------------------------------------------------------------

# TP 3.4
def replaceStr(phrase, term_to_replace, new_word):
    return phrase.replace(term_to_replace, new_word)

def getUserInputs():
    print("Olá, usuário! Esse programa irá substituir trechos especifícos de uma frase por uma palavra da sua escolha.")

    phrase = input("Por favor, digite a frase: ")
    term_to_replace = input("Digite o trecho que deseja trocar: ") 
    new_word = input("Por favor, digite a palavra que entrará na frase: ")

    print(replaceStr(phrase, term_to_replace, new_word))

getUserInputs()


#------------------------------------------------------------------------------------
# TP 3.5
def verifyChars(str):
    return str.isdigit()

def printAnswer(is_digit):
    if is_digit:
        print("Todos os caracteres são numéricos.")
    else:
        print("Nem todos os caracteres são numéricos.")

input_str = input("Olá, usuário! Por favor, digite algo para verificar se existem somente caracteres numéricos: ")

is_digit = verifyChars(input_str)
printAnswer(is_digit)

#------------------------------------------------------------------------------------
# TP 3.6
def splitInteger(int_number):
    return list(str(int_number))[::-1]

input_int = int(input("Olá, usuário! Por favor, digite um número inteiro: "))
print(f"O inverso do número {input_int} é {splitInteger(input_int)}.")

#------------------------------------------------------------------------------------
# TP 3.7
def getPortugueseName(num):
    if num == 0:
        return "Zero"   
    elif num == 1:
        return "Um"
    elif num == 2:
        return "Dois"
    elif num == 3:
        return "Três"
    elif num == 4:
        return "Quatro"
    elif num == 5:
        return "Cinco"
    elif num == 6:
        return "Seis"
    elif num == 7:
        return "Sete"
    elif num == 8:
        return "Oito"
    else:
        return "Nove"
    
def printNumberNames(str):
    print("Nomes em Português: ")
    print()

    for digit in str:
        int_digit = int(digit)

        print(f"{int_digit} - {getPortugueseName(int_digit)}")

input_string = input("Olá, usuário! Por favor, digite números de 0 a 9: ")
printNumberNames(input_string)

#------------------------------------------------------------------------------------
# TP 3.8
def convertToList(str):
    return str.split()

def removeDuplicateWords(str):
    str_list = convertToList(str)

    unique_words = []
    for word in str_list:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)

input_string = input("Olá, usuário! Entre com uma string: ")
print(f"String sem duplicatas - {removeDuplicateWords(input_string)}")

#------------------------------------------------------------------------------------
# TP 3.9
def convertToList(number):
    return [int(digit) for digit in str(number)]

def printResult(number):
    num_list = convertToList(number)
    sum_result = sum(num_list)

    print(f"A soma dos números {num_list} é igual a {sum_result}.")

input_number = int(input("Olá, usuário! Digite um número inteiro: "))
printResult(input_number)

#------------------------------------------------------------------------------------
# TP 3.10
def printCommonChars(first_str, second_str):
    common_chars = []

    for char in first_str:
        if char in second_str and char not in common_chars:
            common_chars.append(char)

    if not common_chars:
        print(f"As palavras {first_str} e {second_str} não possuem caracteres em comum.")
    else:
        print(f"Os caracteres comuns entre {first_str} e {second_str} são {common_chars}.")

first_str = input("Olá, usuário! Digite a palavra um: ")
second_str = input("Digite a palavra dois: ")

printCommonChars(first_str, second_str)

#------------------------------------------------------------------------------------
# TP 3.11
def strToList(str):
    return str.split()

def printStrList(str_list):
    if not str_list:
        return

    print("Lista de palavras: ")
    for i, word in enumerate(str_list):
        print(f"{i} - {word}")



def insert_word():
    str = input("Olá, usuário! Por favor, digite palavras separadas por um espaço em branco: ")

    str_list = strToList(str)
    printStrList(str_list)

    print()
    if len(str_list) < 3:
        str_input = input("Digite a nova palavra: ")
        str_list.append(str_input)

        print() 
        print(f"Palavra '{str_input}' adicionada com sucesso!")
    else:
        word_position = int(input("Digite a posição que deseja inserir a nova palavra: "))
        new_word = input("Digite a palavra nova: ")
        str_list.insert(word_position, new_word)

        print()
        print(f"Palavra '{new_word}' adicionada com sucesso!")
    
    print()
    printStrList(str_list)

insert_word()

#------------------------------------------------------------------------------------
# TP 3.12
def combineLists(list1, list2):
    list1.extend(list2)

    return list1

def getUserInput():
    first_input = input("Olá, usuário! Digite números separados por vírgula (ex: 1,2,3): ")
    second_input = input("Digite mais números separados por vírgula (ex: 4,5,6): ")

    list1 = first_input.split(",")
    list2 = second_input.split(",")

    return list1, list2

def printCombinedLists():
    list1, list2 = getUserInput()

    print("Listas combinadas:", combineLists(list1, list2))

printCombinedLists()

#------------------------------------------------------------------------------------
# TP 3.13
def convertToList(str):
    return str.split()

def removeDuplicates(str):
    str_list = convertToList(str)

    unique_words = []
    for word in str_list:
        if word not in unique_words:
            unique_words.append(word)

    return " ".join(unique_words)

input_string = input("Olá, usuário! Entre com uma string: ")
print(f"String sem duplicatas - {removeDuplicates(input_string)}")

#------------------------------------------------------------------------------------
# TP 3.14
def getShopList():
    shop_list = input("Olá, usuário, digite sua lista de compras, com cada item sendo separado por um espaço em branco: ")

    return shop_list.split()

def printShopList(shop_list):
    for i, item in enumerate(shop_list):
        print(f"{i} - {item}")

def organizePurchases(shop_list):
    last_item_idx = len(shop_list) - 1
    last_item = shop_list[last_item_idx]

    shop_list.pop()
    print()
    print(f"O item '{last_item}' foi removido com sucesso!")
    print()

    print("Lista de compras atualizada: ")
    printShopList(shop_list)

shop_list = getShopList()
printShopList(shop_list)
organizePurchases(shop_list)
"""