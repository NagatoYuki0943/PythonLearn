with open("exec_run_python_file_.py") as f:
    data = f.read()

print(data)
# class Person():
#     def __init__(self, name: str, age: int) -> None:
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return f"My name is {self.name} and {self.age} years old."

# person = Person('Tom', 12)
# print(person)

exec(data)
# My name is Tom and 12 years old.

person = Person('Jerry', 11)
print(person)
# My name is Jerry and 11 years old.
