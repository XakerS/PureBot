# coding: utf-8
# Импортирование модулей

from random import randint
from random import choice

# Глобальные переменные

global not_found
global prefix
global inp

not_found = "Команда не найдена, введите «/help» для просмотра доступных комманд."
prefix = "[PureBot]"

# Начало программы

print("Запуск программы...\nПрограмма «PureBot» предназначена для лиц старше 14+  :D")
print("Разработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99\n\nВерсия: 0.2")
print("-"*50,"\n")
inp = str(input("Введите комманду: "))

# Command «/help»

def helps(commandsend):
 if commandsend == "/help":
  print("\n Список комманд:\n/help - Помощь по боту\n/random - Случайное число от 0 до 100\n/tf - Мини игра «True or False»")

# Command «/random»
  
def random(commandsend):
 if commandsend == "/random":
  random = randint(0,100)
  print("\n Случайное число: ",random)

# Мини игра True or False

def trueorfalse(commandsend):
 if commandsend == "/tf":
  words = {
  	1:"Россия - Это молодая страна?",
  	1:"Test aaaaaaa?",
  	2:"Тестовый текст?"
  	} 
  ri = randint(1,2)
  randwords = choice([words[ri]]) 
  print("\n",randwords)
  Да = "1"
  да = "1"
  Нет = "2"
  нет = "2"
  result = input("Выберите ответ «Да» или «Нет»?\nОтвет: ")
  if result == "1":
   print("\nИ это...\nПравильный ответ!")
   #print("\nВаша награда: ",randmoney)
  else:
   print("Неверный ответ!")
   
# commands = helps,random,trueorfalse
# Функция ввода и вывода

def entry(inp):
 if inp == "/help":
  helps(inp)
 elif inp == "/random":
  random(inp)
 elif inp == "/tf":
  trueorfalse(inp)
 else:
  print(not_found)
 
entry(inp)

# Конец программы

print("\n\n©DevCorp")
