while True:
    class Car:
        def menu(self):
            choice = input(" 1-Cоздать стадион ,2-Посмотреть параметры стадиона- ,3-Выход -> ")
            if choice == "1":
                print("Вы выбрали создать ввести стадион")
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
            self.model = input("Название стадиона: ")
            self.year = int(input("Введите дату открытия: "))
            self.manufacturer = input("Введите страну: ")
            self.engine_volume = input("Введите город: ")
            self.price = int(input("Введите вместимость: "))
        def output_data(self):
            print("Название:", self.model)
            print("Дата открытия:", self.year)
            print("Страна:", self.manufacturer)
            print("Город:", self.engine_volume)
            print("Вместимость:", self.price)


        def get(self):
            what = input("Введите информацию которую хотите узнать Название,Дата,Страна,Город,Вместимость -> ")
            if what == "Название":
                print(self.model)
            elif what == "Дата":
                print(self.year)
            elif what == "Страна":
                print(self.manufacturer)
            elif what == "Город":
                print(self.engine_volume)
            elif what == "Вместимость":
                print(self.price)
            else:
                print("Не правильный ввод")


    car1 = Car()
    car1.menu()
    print("\nДанные об стадионе:")
    car1.output_data()
    car1.get()