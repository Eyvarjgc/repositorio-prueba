#eval()
class Persona:
    def __init__(self,nombre,edad) -> None:
        self.n = nombre
        self.e = edad

    def __str__(self) -> str:
        print(f"Nombre: {self.n}")
        return f"Edad: {self.e}"
        


p1 = Persona("Eyvar", "18")
print(str(p1))
