def tuple_immutability():
  """Demonstrates tuple immutability in Python."""

  # Create a tuple
  my_tuple = (10, "hello", 3.14)

  # Attempt to modify an element (will raise an error)
  try:
    my_tuple[1] = "world"
  except TypeError as e:
    print(f"Error: {e}")

  # Create a new tuple with modified elements
  new_tuple = my_tuple + ("goodbye",)

  print("Original tuple:", my_tuple)
  print("New tuple:", new_tuple)

if __name__ == "__main__":
  tuple_immutability()