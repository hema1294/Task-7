#Python program using a function to do the following
# a. create a text file with current timestamp 

import datetime

def create_text_file_with_timestamp():
    # Get current timestamp
    current_time = datetime.datetime.now()
    
    # Format timestamp as string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create file name with timestamp
    file_name = f"text_file_{timestamp_str}.txt"
    
    # Write timestamp to text file
    with open(file_name, 'w') as file:
        file.write(f"Timestamp: {current_time}")

# Call the function to create the text file
create_text_file_with_timestamp()

# b. file content should have the content of the current timestamp

import datetime

def create_text_file_with_timestamp_content():
    # Get current timestamp
    current_time = datetime.datetime.now()
    
    # Format timestamp as string
    timestamp_str = current_time.strftime("%Y-%m-%d_%H-%M-%S")
    
    # Create file name with timestamp
    file_name = f"text_file_{timestamp_str}.txt"
    
    # Write timestamp content to text file
    with open(file_name, 'w') as file:
        file.write(f"Timestamp: {current_time}\n")
        file.write("This is the content of the file.")

# Call the function to create the text file
create_text_file_with_timestamp_content()