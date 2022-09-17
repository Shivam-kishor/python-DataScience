class Fruits:
    def __init__(self,name,color):
        self.name=name
        self.color=color
 
    def info(self):
        print("Fruits")
        print(f"{self.name}")
        print(f"{self.color}")


    class Mango(Fruit):
        def __init__(self,name,color,size,taste):
            super().__init__(self,name,color,taste,size):
            self.taste=taste
            self.size=size 



    f=Fruits("orange","orange")
    m=Mango("Daseri mango","greenish yellow",'sweet')


    f.info()
    m.info()