def list_operations():
  """Demonstrates list operations in Python."""

  # Create an empty list
  my_list = []

  # Append elements to the list
  my_list.append(10)
  my_list.append("hello")
  my_list.append(3.14)

  print("List after appending:", my_list)

  # Remove elements from the list
  my_list.remove("hello")
  del my_list[1]  # Remove element at index 1

  print("List after removing:", my_list)

  # Slice the list
  sublist = my_list[1:3]  # Create a sublist from index 1 to 2 (exclusive)

  print("Sublist:", sublist)

if __name__ == "__main__":
  list_operations()