documents = [  {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"}, {"type": "invoice", "number": "11-2", "name":"Геннадий Покемонов"},  {"type": "insurance", "number": "10006","name": "Аристарх Павлов"} ] 
directories = { '1': ['2207 876234', '11-2'],  '2': ['10006'],  '3': []  }

def num_to_name():
  any_num = str(input("Введите номер: "))
  for doc_dict in documents:
   if doc_dict["number"] == any_num:
     return doc_dict["name"]
  
def list_print():
  for doc_list in documents:
   print(doc_list['type'],doc_list['number'],doc_list['name'])
  
def num_to_shelf():
 any_num = str(input("Введите номер: "))
 for shelf, number_list in directories.items():
   for number in number_list:
     if number == any_num:
       return shelf

def add_new_doc():
  new_num = str(input("Введите номер: "))
  new_type = str(input("Введите тип: "))
  new_name = str(input("Введите имя: "))
  new_shelf = str(input("Введите полку: "))
  new_dict = dict(type = new_type, number = new_num, name = new_name)
  if new_shelf in directories:
    documents.append(new_dict)
    for shelf, number_list in directories.items():
      if shelf == new_shelf:
        number_list.append(new_num)
    print("Документ добавлен")
  else:
    print("Такой полки не существует!")


def all_names():
  try:
    for doc_dict in documents:
      print(doc_dict["name"])
  except KeyError:
    print("Имя не записано!")



command = str(input("Введите команду: "))
if command == "p":
  print(num_to_name())
if command == "l":
  print(list_print())
if command == "s":
  print(num_to_shelf())
if command == "a":
  print(add_new_doc())
if command == "n":
  print(all_names())
