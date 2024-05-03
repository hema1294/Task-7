#Python program using a function to read from a text file and  the function will take the name of the text file and display the content of the file into the console 

def read_text_file(file_name):
    try:
        # Open the text file for reading
        with open(file_name, 'r') as file:
            # Read the content of the file
            file_content = file.read()
            # Display the content in the console
            print("Content of", file_name, ":\n", file_content)
    except FileNotFoundError:
        print("File not found.")

# Example usage:
file_name = "example.txt"  # Provide the name of the text file
read_text_file(file_name)