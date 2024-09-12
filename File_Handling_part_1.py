def file_operations():
  """Demonstrates file operations in Python."""

  # Open a file for writing
  with open("output.txt", "w") as file:
    file.write("Hello, world!\n")
    file.write("This is a sample text file.")

  # Open a file for reading
  with open("output.txt", "r") as file:
    content = file.read()
    print(content)

  # Append to a file
  with open("output.txt", "a") as file:
    file.write("\nAdditional content.")

if __name__ == "__main__":
  file_operations()