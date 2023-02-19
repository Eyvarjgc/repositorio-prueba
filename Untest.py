#eval()
import pickle
class Persona:
    def __init__(self,nombre,edad) -> None:
        self.n = nombre
        self.e = edad

    def __str__(self) -> str:
        print(f"Nombre: {self.n}")
        return f"Edad: {self.e}"
        

    def question(self):
        ask = input("Desea guardar sus datos en un documento??(S/N)").upper
        if ask == "s" or "S":
            file = open("data", "wb")
            pickle.dump(p1,file)
            file.close()
            del file
            print("-DATOS EXITOSAMENTE GUARDADOS-")

            ask_2 = input("Desea leer los datos ingresados?(S/N)").upper
            if ask_2 == "s" or "S":
                file = open("data", "rb")
                read = pickle.load(file)
                print(read)
            else:
                print("No desea leer sus datos")
        else:
            print("no desea guardar sus datos")



p1 = Persona("Eyvar", "18")
p1.question()

