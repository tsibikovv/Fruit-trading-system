import csv
from datetime import datetime


def readFromCSV(massive):
  new = []
  with open('fruits.csv', 'r', encoding = 'iso-8859-1', newline = "") as file :
    csv_reader = csv.DictReader(file, delimiter=',')
    next(csv_reader)
    for row in csv_reader :
      fruit = row["Fruit"]
      cost = row["Cost"]
      nali = row["Nali"]
      country = row["Country"]
      massive.append(fruit, cost, nali, country)
  print(massive)
  return massive
  

def main():
  fruits = []
  
  readFromCSV(fruits)

  print(fruits)
  while True : 
    print(f"Добро пожаловать в систему торговли фруктами!\n {"-" * 90}\nМеню авторизации :")

    adm = False
    
    user = input("Введите логин : ")
    password = input("Введите пароль : ")
    print("-" * 90, f"\n")

    if adm == False :
      print(f"Вы зарегистрировались как Пользователь системы!\n{"-" * 90}")
      print(f"Доступные команды :\n 1. Посмотреть каталог\n 2. Фильтровать по наличию\n 3. Фильтровать по стране\n 4. Филтровать по цене\n 5. Сортировать\n 6. Поиск по названию\n 7. Выход\n {"-" * 90}\n")
      userChoice = int(input("Ввод : "))
      print("-" * 90, f"\n")
      if userChoice == 1 : 
        for i in range(len(fruits)) :
          for x in fruits[i] :
            print(f"Фрукт №{i} - {fruits[i][0]}\n Стоимость - {fruits[i][1]}\n Наличие - {fruits[i][2]}\n Страна - {fruits[i][3]}\n {"-" * 90}")
      elif userChoice == 2 :
        pass
      elif userChoice == 3 :
        pass
      elif userChoice == 4 :
        pass
      elif userChoice == 5 :
        print(f"Доступные команды : \n 1. По названию\n 2. По цене\n {"-" * 90}\n")
      elif userChoice == 6 :
        pass
      elif userChoice == 7 :
        continue












if __name__ == "__main__" :
  main()



















