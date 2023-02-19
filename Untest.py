#eval()

import pickle
class Persona:
    def __init__(self,nombre,edad) -> None:
        self.n = nombre
        self.e = edad

    def __str__(self) -> str:
        print(f"Nombre: {self.n}")
        return f"Edad: {self.e}"
        
    def add(self):
        file = open("data" "wb")
        pickle.dump("p1", "file")
        file.close()
        del file

    def question(self):
        ask = input("Desea guardar sus datos en un documento??(S/N)")
        if ask.upper == "s":
            p1.add()
        else:
            print("no desea guardar sus datos")

p1 = Persona("Eyvar", "18")
print(str(p1))
p1.question()
