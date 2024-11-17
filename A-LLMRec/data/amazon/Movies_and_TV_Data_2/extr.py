def extract_top_n_lines(file_path, n):
    # Read the top n lines from the file
    with open(file_path, 'r') as file:
        lines = file.readlines()[:n]

    # Overwrite the file with the top n lines
    with open(file_path, 'w') as file:
        file.writelines(lines)

# Example usage
file_path = 'Movies_and_TV.json'
n=30000# Change this to the number of lines you want to keep
extract_top_n_lines(file_path, n)
