class Lion:
    age =""
    gender = ""

    def __init__(self,age,gender):
        self.age = age
        self.gender = gender

    def move(self) -> str:
        return f'age : {self.age}, gender : {self.gender}'

    def eat(self) -> str:
        pass

    def __str__(self) -> str:
        return f'age : {self.age}, gender : {self.gender}'

class Fish:
    age =""
    gender = ""

    def __init__(self,age,gender):
        self.age = age
        self.gender = gender

    def move(self) -> str:
        return f'age : {self.age}, gender : {self.gender}'

    def eat(self) -> str:
        pass

    def __str__(self) -> str:
        return f'age : {self.age}, gender : {self.gender}'




    def __str__(self) -> str:
        pass

    def __init__(self) -> None:
        pass



if __name__ == "__main__":
    Lion1 = Lion(5,"male")
    Lion2 = Lion(11,"male")
    Lion3 = Lion(3,"female")

    print(Lion1)
    print(Lion2)
    print(Lion3)