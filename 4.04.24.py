while True:
    class Car:
        def menu(self):
            choice = input(" 1-Cоздать новые параметры ,2-Посмотреть параметры автомобиля- ,3-Выход -> ")
            if choice == "1":
                print("Вы выбрали создать новый автомобиль")
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
            self.model = input("Введите модель автомобиля: ")
            self.year = int(input("Введите год выпуска: "))
            self.manufacturer = input("Введите производителя: ")
            self.engine_volume = float(input("Введите объем двигателя: "))
            self.color = input("Введите цвет машины: ")
            self.price = float(input("Введите цену: "))
        def output_data(self):
            print("Модель:", self.model)
            print("Год выпуска:", self.year)
            print("Производитель:", self.manufacturer)
            print("Объем двигателя:", self.engine_volume)
            print("Цвет машины:", self.color)
            print("Цена:", self.price)


        def get(self):
            what = input("Введите информацию которую хотите узнать Модель,Год,Производитель,Обьем двигателя,Цвет,Цена -> ")
            if what == "Модель":
                print(self.model)
            elif what == "Год":
                print(self.year)
            elif what == "Производитель":
                print(self.manufacturer)
            elif what == "Обьем двигателя":
                print(self.engine_volume)
            elif what == "Цвет":
                print(self.color)
            elif what == "Цена":
                print(self.price)
            else:
                print("Не правильный ввод")


    car1 = Car()
    car1.menu()
    print("\nДанные об автомобиле:")
    car1.output_data()
    car1.get()


