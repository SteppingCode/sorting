import os
import shutil


path_to_folder: str = os.path.join(input("Enter the absolute path to your folder: "))
EXTENSIONS: dict = {
    "image": ["png", "jpg", "jpeg"],
    "video": ["mp4", "avi", "mkv"],
    "audio": ["mp3"],
    "gif": ["gif"],
    "icon": ["ico"],
}


def sorting_function(directory: str) -> None:
    """
    :param directory:
    :return:
    """
    try:
        folder = os.listdir(path=directory)
        try:
            for extension in EXTENSIONS:
                os.mkdir(path=f"{directory}/{extension}")
        except FileExistsError:
            pass
        finally:
            for file in folder:
                if len(file.split(".")) >= 2:
                    for name, ex in EXTENSIONS.items():
                        if file.split(".")[-1] in ex:
                            shutil.move(f"{directory}/{file}", f"{directory}/{name}/{file}")
    except NotADirectoryError as e:
        print(f"Sorry, the file could not be found.\n{e}")
    finally:
        for dirname in os.listdir(path=directory):
            if len(os.listdir(path=os.path.join(directory, dirname))) == 0:
                os.rmdir(path=os.path.join(directory, dirname))
        print("Done")


def main():
    sorting_function(directory=path_to_folder)


if __name__ == "__main__":
    main()
