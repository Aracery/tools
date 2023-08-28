import os



def delete_all_files_recursively(directory_path):
  """Deletes all files recursively in a directory, but not the directory itself.

  Args:
    directory_path: The path to the directory to delete the files from.
  """
  for file_name in os.listdir(directory_path):
    file_path = os.path.join(directory_path, file_name)
    if os.path.isfile(file_path):
      os.remove(file_path)

    # Recursively delete subdirectories.
    elif os.path.isdir(file_path):
      delete_all_files_recursively(file_path)



def main():
  directory = os.path.dirname(__file__) + '/data/'
  delete_all_files_recursively(directory)




if __name__ == "__main__":
  main()
