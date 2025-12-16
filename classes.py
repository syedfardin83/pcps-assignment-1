class Player:
    def __init__(self,name,type):
        self.name=name
        self.type=type

    def show_info(self):
        print(f'Name:{self.name}, type:{self.type}')

p1=Player("Joihn","hero")
p1.show_info()

p2=Player("Rob","Villan")
p2.show_info()