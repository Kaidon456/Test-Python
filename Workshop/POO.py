
class alumno:
    def __init__(self,nombre, matricula,materia):
        self.nom = nombre
        self.matricula = matricula
        self.materia = materia

    def materias(self):
        print(f'El alumno esta registrado en la materia{self.materia}')
        return self.materia

    def nombre(self):
        print(f'el alumno se llama {self.nom}')
        return self.nom

marco = alumno('marco',24400234,'ing de software')
nombre = marco.nombre()
materia = marco.materias()