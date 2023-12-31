"""crear una clase Fraccion, que cuente con dos atributos: dividendo y divisor, que se asignan en el constructor,
y se imprimen como x/y en el método __str__."""

class Fraccion:
    
    def __init__(self, dividendo, divisor):
        self.dividendo = dividendo
        self.divisor = divisor
    
    def __str__(self):
        return f"{self.dividendo}/{self.divisor}"

fraccion1 = Fraccion(3, 4)
fraccion2 = Fraccion(2, 5)

print(f"Fracción 1: {fraccion1}")
print(f"Fracción 2: {fraccion2}")
