while True:
    class Car:
        def menu(self):
            choice = input(" 1-Cоздать новую книгу ,2-Посмотреть параметры книги- ,3-Выход -> ")
            if choice == "1":
                print("Вы выбрали создать новую книгу")
                self.input_data()
            elif choice == "2":
                self.get()
            elif choice == "3":
                exit(print("Вы вышли!"))
            else:
                print("Не правильный ввод")
        def __init__(self):
            self.model = ""
            self.year = 0
            self.manufacturer = ""
            self.engine_volume = 0.0
            self.color = ""
            self.price = 0.0

        def input_data(self):
            self.model = input("Название книги: ")
            self.year = int(input("Введите год выпуска: "))
            self.manufacturer = input("Введите издателя: ")
            self.engine_volume = input("Введите жанр: ")
            self.color = input("Введите автора: ")
            self.price = float(input("Введите цену: "))
        def output_data(self):
            print("Название:", self.model)
            print("Год выпуска:", self.year)
            print("Издатель:", self.manufacturer)
            print("Жанр:", self.engine_volume)
            print("Автор:", self.color)
            print("Цена:", self.price)


        def get(self):
            what = input("Введите информацию которую хотите узнать Название,Год,Издатель,Жанр,Автор,Цена -> ")
            if what == "Название":
                print(self.model)
            elif what == "Год":
                print(self.year)
            elif what == "Издатель":
                print(self.manufacturer)
            elif what == "Жанр":
                print(self.engine_volume)
            elif what == "Автор":
                print(self.color)
            elif what == "Цена":
                print(self.price)
            else:
                print("Не правильный ввод")


    car1 = Car()
    car1.menu()
    print("\nДанные об книге:")
    car1.output_data()
    car1.get()