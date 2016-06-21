# coding: utf-8
# Импортирование модулей

from random import randint
from random import choice as randstr
import sl4a

# Вывод на экран!

droid = sl4a.Android().makeToast
echo = droid
words = ["Привет, добро пожаловать в «PureBot»", "Если найдете баги, то пишите нам", "Приятной игры"]
for word in words:
 echo(word + "!")
 
# Глобальные переменные

global not_found
global prefix
global inp
global version

not_found = "Команда не найдена, введите «/help» для просмотра доступных комманд."
prefix = "[PureBot]"
version = "Версия: 0.4 - Бета"

# Начало программы

print("Запуск программы...\nПрограмма «PureBot» предназначена для лиц старше 14+  :D")
print("Разработчики:\n Xaker Su - mcg76\n Максим Удачин - Bruno99\n\n",version)
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
  true = {0:"В Армении есть интернет?",1:"У русских «Медведь», а у амереканцев «Ястреб»?",2:"Питон - Так называют какой-то язык программирования?",
  3:"Существует ли такой сериал «ZKD»?",4:"Python - Это язык программирования, который назван в честь цирка Пайтона?"}
  false = {0:"Обама черный?",1:"ЯП - Это язык педиков? ",2:"Вафля - это еда и имя?",
  3:"ПК - Это пистолетная кончина?",4:"Создатель minecraft - Шоги?"}
  keys = {"true":true,"false":false}
  rint = randint(0,4)
  rstr1 = randstr([true,false])
  rstr2 = randstr([rstr1[rint]])
  print("\n",rstr2)
  result = input("\n«true» или «false»?\nВаш ответ: ")
  if true == keys[result]:
   if rstr2 == true[rint]:
    print("Правильный ответ и это - ПРАВДА")
   else:
    print("Неверно, ответ: ЛОЖ")
  elif false == keys[result]:
   if rstr2 == false[rint]:
    print("Правильный ответ и это - ЛОЖ")
   else:
    print("Неверно, ответ: ПРАВДА")
  else:
   print("Вы ввели другой сивмвол в ответе!") 
   
# TODO:
# Правила и информация об игре!
# Система случайного получения денег:  
# print("\nВаша награда: ",randmoney)
# Возможно экономика "БОТовая".
   
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
