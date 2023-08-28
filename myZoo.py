class Lion:
    counter = 0
    age = 0
    gender = "male"
    name = "Mufasa"
#rerwe
    def __init__(self,age,gender,name) -> None:
        Lion.counter = Lion.counter + 1
        self.age = age
        self.gender = "female"
        self.name = "yossi"

    def __str__(self) -> str:
        return str(Lion.counter)







if __name__== "__main__":
    L1 = Lion(15,"male","momo")
    L2 = Lion(3,"male","koko")
    L3 = Lion(7,"female","lolo")

    print(L1)
    print(L2)
    print(L3)