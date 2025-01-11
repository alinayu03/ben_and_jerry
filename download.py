import os
import subprocess

# Clone a GitHub repository
def clone_repo(repo_url, clone_path):
    if not os.path.exists(clone_path):
        subprocess.run(["git", "clone", "--depth", "1", repo_url, clone_path], check=True)
    else:
        print(f"Repository already cloned at {clone_path}")

# Get all code files from the repository
def get_code_files(repo_path, extensions):
    code_files = []
    for root, dirs, files in os.walk(repo_path):
        for file in files:
            if file.endswith(tuple(extensions)):
                code_files.append(os.path.join(root, file))
    return code_files

# Read and preprocess the content of a code file
def preprocess_code_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        code = file.read()
    # Preprocessing steps can be added here if necessary
    return code

# Save all preprocessed code into one file
def save_all_preprocessed_code(files, output_file):
    with open(output_file, 'w', encoding='utf-8') as output:
        for file_path in files:
            preprocessed_code = preprocess_code_file(file_path)
            output.write(preprocessed_code)
            output.write("\n\n")  # Add spacing between files for readability

# Main function
def main():
    # Parameters
    repo_url = "https://github.com/alinayu03/cat.git"  # Replace with your repo
    clone_path = "./new_repo"
    output_file = "all_code.txt"
    extensions = [".py", ".js", ".java", ".cpp", ".cs", ".swift"]  # Add extensions as needed

    # Clone repository
    print("Cloning repository...")
    clone_repo(repo_url, clone_path)

    # Get code files
    print("Extracting code files...")
    code_files = get_code_files(clone_path, extensions)
    print(f"Found {len(code_files)} code files.")

    # Save all preprocessed code into one file
    print("Preprocessing and saving all code into one file...")
    save_all_preprocessed_code(code_files, output_file)
    print(f"All preprocessed code saved to {output_file}.")

if __name__ == "__main__":
    main()
