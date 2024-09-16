class Person:
    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"My name is {self.name} and {self.age} years old."


person = Person("Tom", 12)
print(person)
