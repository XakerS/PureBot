# Импортирование модулей

from random import randint

# Глобальные переменные

global not_found
global prefix

not_found = "Команда не найдена"
prefix = "[PureBot]"

# Начало программы

print("Запуск программы...\nПрограмма «PureBot» предназначена для лиц старше 14+  :D")
print("Разработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99\n\nВерсия: 0.1")
print("-"*50,"\n")

# Command «/help»

def helps(commandsend):
 if commandsend == "/help":
  print("\n Список комманд:\n/help - Помощь по боту\n/random - Случайное число от 0 до 100")

# Command «/random»
  
def random(commandsend):
 if commandsend == "/random":
  random = randint(0,100)
  print("\n Случайное число: ",random)

# Мини игра Ture or False

def trueorfalse(commandsend):
 if commandsend == "/trueorfalse":
  words = {True:"Твоя мамка бухала?"}
  randwords = choice([words[key]])
   
#commands = helps,random,trueorfalse

inp = str(input("Введите комманду: "))
if inp == "/help":
 helps("/help")
elif inp == "/random":
 random("/random")
elif inp == "/trueorfalse":
 random("/trueorfalse")
else:
 print(not_found)

# Конец программы

print("\n\n©DevCorp")
