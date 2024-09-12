def dictionary_basics():
  """Demonstrates dictionary basics in Python."""
##Dictionary is Like an array
  # Create a dictionary
  my_dict = {"name": "Alice", "age": 30, "city": "New York"}

  # Access values by keys
  print("Name:", my_dict["name"])
  print("Age:", my_dict["age"])
  print("City:", my_dict["city"])

  # Modify values
  my_dict["age"] = 31
  print("Updated age:", my_dict["age"])

  # Add a new key-value pair
  my_dict["occupation"] = "Engineer"
  print("Dictionary after adding:", my_dict)

  # Get all keys and values
  keys = my_dict.keys()
  values = my_dict.values()
  print("Keys:", keys)
  print("Values:", values)

if __name__ == "__main__":
  dictionary_basics()