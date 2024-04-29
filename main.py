import os
import shutil

path: str = input("Please input absolute path to your folder: ")

try:
    list_files = os.listdir(path=path)
    list_files.remove('desktop.ini')

    print(f"Folder located in '{path}' contains:")
    for i in range(len(list_files)):
        print(f"{i+1}. {list_files[i]}")

    answer: str = input("Are you sure? (y/n): ")

    match answer:
        case "Y" | "y":
            try:
                extensions_list = []
                for file in list_files:
                    if len(file.split(".")) >= 2:
                        if file.split(".")[-1] not in extensions_list:
                            extensions_list.append(file.split(".")[-1])
                for ext in extensions_list:
                    try:
                        os.mkdir(path=os.path.join(path, ext))
                    except FileExistsError:
                        pass
                for file in list_files:
                    if len(file.split(".")) >= 2:
                        ext = file.split(".")[-1]
                        shutil.move(os.path.join(path, file), os.path.join(path, ext, file))
            except Exception as e:
                print(f"Something went wrong. {e}")
            else:
                print("All done")
        case "N" | "n":
            print("Okay")
        case _:
            print("Incorrect input")
except FileNotFoundError:
    print("Oops! Something went wrong.")
    print("Please try again.")
