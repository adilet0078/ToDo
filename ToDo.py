# Напишите простое приложение Todo, целью которого является ведение списка дел. Приложение должен состоять из двух классов: Todo и TodoItem:

# Инициализатор Todo ничего не принимает. В классе должен быть метод add_todo, который принимает экземпляр класса TodoItem, и добавляет в список todo_items. Метод list_items должен показывать все элементы в списке todo_items. Метод find должен принимать слово в качестве аргумента и выводить список экземпляров TodoItem, которые содержат это слово в виде кортежа, который будет иметь формат (индекс, экземпляр).

# Инициализатор TodoItem принимает строковое значение. В нем должна быть переменная, сохраняющая состояние is_done. Также в классе должен быть методы check и uncheck, которые меняют состояние is_done.

# Создайте экземпляр Todo, создайте несколько TodoItem, вызовите их методы.

# Сделайте так, чтобы приложение работало с командой строки. Подсказка: в качестве меню может выступать словарь, в котором ключем будет номер, значением -- метод. Для этого можете добавить метод run, в котором будет цикл while принимающий input.


# - Добавить БД в виде файла 
# - Добавить БД в виде PostgreSQL 
# - Добавить в гит

class TodoItem:
    def __init__(self, description):
        self.description = description
        self.is_done = False

    def check(self):
        self.is_done = True

    def uncheck(self):
        self.is_done = False

    def __str__(self):
        status = "[x]" if self.is_done else "[ ]"
        return f"{status} {self.description}"


class Todo:
    def __init__(self):
        self.todo_items = []

    def add_todo(self, todo_item):
        self.todo_items.append(todo_item)

    def list_items(self):
        if self.todo_items:
            for index, item in enumerate(self.todo_items, start=1):
                print(f"{index}. {item}")
        else:
            print("No items in the list!")

    def find(self, word):
        found_items = [(index, item) for index, item in enumerate(self.todo_items) if word in item.description]
        if found_items:
            for index, item in found_items:
                print(f"{index}. {item}")
        else:
            print("No items found with that word.")

    def run(self):
        menu = {
            "1": self.add_todo,
            "2": self.list_items,
            "3": self.find,
            "q": exit
        }

        while True:
            print("\n=== ToDo App ===")
            print("1. Add ToDo")
            print("2. List Todos")
            print("3. Find Todos")
            print("q. Quit")

            choice = input("Enter your choice: ")

            if choice in menu:
                if choice == "1":
                    description = input("Enter description: ")
                    todo_item = TodoItem(description)
                    menu[choice](todo_item)
                elif choice == "3":
                    word = input("Enter a word to find: ")
                    menu[choice](word)
                else:
                    menu[choice]()
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_app = Todo()
    todo_app.run()
