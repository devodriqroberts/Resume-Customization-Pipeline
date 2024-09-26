import os

def save_output(content, output_path):
    """Save the tailored resume content to a specified output file."""
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    with open(output_path, "w") as file:
        file.write(content)

def remove_first_line(file_path):
    """Remove the first line that contains only 'latex 'from a file."""
    # Read all lines of the file
    with open(file_path, "r") as file:
        lines = file.readlines()
    
    if lines[0].strip() == "latex":
        # Remove the first line
        lines = lines[1:]
    
    # Write the remaining lines back to the file
    with open(file_path, "w") as file:
        file.writelines(lines)
    
    print(f"The first line has been removed from: {file_path}")