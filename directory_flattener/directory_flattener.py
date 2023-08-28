import os

def print_directory_structure(path, level=0, file=None, excluded_folders=[]):
    for child in sorted(os.listdir(path)):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            if child in excluded_folders:
                continue
            if file:
                file.write('    ' * level + '|--' + child + '\n')
            else:
                print('    ' * level + '|--' + child)
            print_directory_structure(child_path, level + 1, file, excluded_folders)
            
    for child in sorted(os.listdir(path)):
        child_path = os.path.join(path, child)
        if os.path.isfile(child_path):
            if child_path == file_name:
                continue
            if file:
                file.write('    ' * level + '|--' + child + '\n')
            else:
                print('    ' * level + '|--' + child)


def print_directory_contents(path, level=0, file=None, current_path="", excluded_folders=[]):
    for child in sorted(os.listdir(path)):
        child_path = os.path.join(path, child)
        if os.path.isdir(child_path):
            if child in excluded_folders:
                continue
            current_path = os.path.join(current_path, child)
            print_directory_contents(child_path, level + 1, file, current_path, excluded_folders)
            current_path = os.path.dirname(current_path)
    for child in sorted(os.listdir(path)):
        child_path = os.path.join(path, child)
        if os.path.isfile(child_path):
            parent_folder = os.path.basename(os.path.dirname(child_path))
            if child_path == file_name:
                continue
            if parent_folder in excluded_folders:
                continue
            if file:
                file.write(f"###FILESEPERATION### {current_path}/{child}\n\n")
                with open(child_path, "rb") as f:
                    content = f.read()
                    content = content.decode("utf-8", errors='replace')
                    file.write(content+'\n\n\n\n\n')
            else:
                with open(child_path, "rb") as f:
                    content = f.read()
                    content = content.decode("utf-8", errors='replace')
                    print(f"###FILESEPERATION### {current_path}/{child} \n")
                    file.write(content+'\n\n\n\n\n')




input_folder = input("Enter the path of the folder: ")
folders = input_folder.split('/')
file_location = input("Enter 'i' if you want to store the file inside the last folder or 'o' if you want to store the file outside the last folder: ")

file_name = folders[-1]+"_RecursiveDirectoryTraversing.txt"
if file_location.lower() == 'i':
    file_name = os.path.join(input_folder, file_name)
else:
    file_name = os.path.join(os.path.dirname(input_folder), file_name)

excluded_folders = []
while True:
    excluded_folder = input("Enter the name of the folder you want to exclude (or !?none to stop inputting): ")
    if excluded_folder.lower() == "!?none":
        break
    excluded_folders.append(excluded_folder)

with open(file_name,'w') as file:
    print_directory_structure(input_folder, file=file, excluded_folders=excluded_folders)
    file.write('\n\n\n\n\n')
    print_directory_contents(input_folder, file=file, excluded_folders=excluded_folders)

print(f"Output file name is: {file_name}")
