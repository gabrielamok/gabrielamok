class Car:
  """Represents a car."""

  def __init__(self, make, model, year):
    """Constructor for the Car class.

    Args:
      make: The car's make.
      model: The car's model.
      year: The car's year.
    """

    self.make = make
    self.model = model
    self.year = year

  def print_details(self):
    """Prints the car's details."""

    print(f"Make: {self.make}")
    print(f"Model: {self.model}")
    print(f"Year: {self.year}")

# Create a car object
my_car = Car("Toyota", "Corolla", 2023)

# Print the car's details
my_car.print_details()