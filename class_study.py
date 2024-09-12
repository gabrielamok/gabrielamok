class Person:
  """Represents a person."""

  def __init__(self, name, age):
    """Constructor for the Person class.

    Args:
      name: The person's name.
      age: The person's age.
    """

    self.name = name
    self.age = age

  def greet(self):
    """Greets the person."""

    print("Hello, my name is", self.name, "and I am", self.age, "years old.")

# Create objects of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Access attributes and call methods
print(person1.name)
print(person2.age)
person1.greet()
person2.greet()