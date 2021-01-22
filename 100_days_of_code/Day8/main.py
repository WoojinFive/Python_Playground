def greet(name):
    print(f"Hello, {name}")
    print(f"How do yo do {name}?")
    print("Isn't the weather nice today?")

greet("Angela")

#Functions with more than 1 input
def greet2(name, location):
    print(f"Hello {name}")
    print(f"What is it like in {location}")

# greet2("Angela", "London")
greet2(location="Seoul", name="Angela")