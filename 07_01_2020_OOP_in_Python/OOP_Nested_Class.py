# class Human:
#
#     def __init__(self):
#         self.name = 'Guido'
#         self.head = self.Head()
#
#
#     class Head:
#         def talk(self):
#             return 'talking...'
#
#
# if __name__ == '__main__':
#     guido = Human()
#     print(guido.name)
#     print(guido.head.talk())

class car:

    def __init__(self):
        self.name = 'Audi'
        self.engine = self.engine()


    class engine:

        def __init__(self):
            self.engine_model = "5.2 L V10"

        def start(self):
            print("Vroom...Vroom...")


if __name__ == '__main__':
    mycar = car()
    print(mycar.name)
    print(mycar.engine.engine_model)
    mycar.engine.start()

