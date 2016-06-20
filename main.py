
# Импортирование модулей

from random import randint

# Глобальные переменные

global not_found
global prefix

not_found = "Команда не найдена"
prefix = "[PureBot]"

# Command «/help»

def help(commandsend):
 if commandsend == "/help":
  print("Список комманд:\n/help - Помощь по боту\n/random - Случайное число от 0 до 100")
 else:
  print(not_found)
  
# Command «/random»
  
def random(commandsend):
 if commandsend == "/random":
  random = randint(0,100)
  print("\nСлучайное число: ",random)
 else:
  print(not_found)
   
commands = help,random

# Код сырой, не рекомендуется что-либо делать дальше...!!!
