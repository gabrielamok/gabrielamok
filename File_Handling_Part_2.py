def read_and_write_file(filename):
  """Reads the contents of a text file and appends some text.

  Args:
    filename: The name of the file.
  """

  try:
    with open(filename, "r") as file:
      content = file.read()
      print("Original content:")
      print(content)

    with open(filename, "a") as file:
      file.write("\nThis is some appended text.")

    print("Modified content:")
    with open(filename, "r") as file:
      content = file.read()
      print(content)
  except FileNotFoundError:
    print(f"Error: File '{filename}' not found.")

if __name__ == "__main__":
  filename = input("Enter the filename: ")
  read_and_write_file(filename)