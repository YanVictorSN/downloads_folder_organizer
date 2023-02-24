from pathlib import Path
import shutil
from typing import List, Tuple, Dict

categories_and_extension_types = {
    "Images": [".svg", ".jpeg", ".jpg", ".mpeg", ".png"],
    "Scanning": [".tif", ".woff", ".jfif", ".woff2"],
    "Documents": [
        ".xlsx",
        ".pptx",
        ".epub",
        ".docx",
        ".doc",
        ".excalidraw",
        ".drawio",
        ".txt",
        ".odt",
        ".csv",
    ],
    "Audios": [".mp3", ".wav"],
    "Kindle_books": [".mobi"],
    "Videos": [".mp4", ".ts", ".ogg"],
    "Pdfs": [".pdf"],
    "Executables": [".exe", ".msi"],
    "Compressed_Files": [".zip", ".rar", ".gz", ".xz", ".bz2"],
    "Program_files": [".py", ".md", ".sql", ".npy", ".json", ".html", ".js", ".nb"],
    "Folders": [""],
}


def list_directory_categories(
    categories_and_extension_types: Dict[str, List[str]]
) -> List[str]:
    """
    Transforms a ready-made dictionary into categories by taking only the keys

    Arg:
    `list_extensions`: Dictionary with categories and extension types

    Return:

    List of categories

    """
    categories = [category for category in categories_and_extension_types.keys()]
    return categories


def create_directories(categories: List[str]) -> None:
    """
    Create folders for each category

    Arg:
    `categories`: List of categories

    Return:
    None

    """
    downloads_path = Path.home() / "Downloads"
    for category in categories:
        category_path = downloads_path / category
        if category_path.exists():
            print(f"Diretório {category_path} já foi criado.")
        else:
            category_path.mkdir(parents=True)
            print(f"Criando diretório: '{category_path}'")


def list_download_files() -> List[str]:
    """
    Creates a list iterating through all the files in the downloads folder.

    Return:
    List of file names.

    """

    downloads_path = Path.home() / "Downloads"
    downloads_files = [str(file.name) for file in downloads_path.iterdir()]
    return downloads_files


def get_file_name_and_extension(
    names_in_download_folder: List[str],
) -> List[Tuple[str, str]]:
    """
    Iterate through the list of download folder names and return a list of names and extensions in a tuple

    Arg:
    `names_in_download_folder`: List of names in download folder

    Return:
    Names and corresponding extensions in a tuple

    """

    files_with_extensions = [
        (Path(file).name, Path(file).suffix) for file in names_in_download_folder
    ]
    return files_with_extensions


def move_files_into_directory(download_files, files_names_and_extensions):
    """
    Interact through each file in the download list by checking the extension and moving to the corresponding folder category.

    Arg:
    `download_files`: List of names in download folder

    Return:
    Names and corresponding extensions in a tuple

    """
    downloads_path = Path.home() / "Downloads"
    for file in download_files:
        name_file = file[0]
        extension_file = file[1]
        for folder_categories, extensions in files_names_and_extensions.items():
            source_file = downloads_path / name_file
            destination_path = downloads_path / folder_categories / name_file
            try:
                if extension_file != "" and extension_file in extensions:
                    shutil.move(str(source_file), str(destination_path))
                    break
                elif (
                    name_file not in files_names_and_extensions.keys()
                    and extension_file == ""
                ):
                    destination_path = downloads_path / str("Folders") / name_file
                    shutil.move(str(source_file), str(destination_path))
                    break
                else:
                    pass
            except Exception as error:
                print(error)


def main():
    """
    Function: list_directory_categories(categories_and_extension_types)

    This function lists the categories and their associated extension types.

    Function: create_directories(list_categories)

    This function creates a directory for each category in the list of categories provided.

    Function: list_download_files()

    This function lists all files in the downloads folder.

    Function: get_file_name_and_extension(download_files)

    This function separates the file names and extensions from the list of downloaded files.

    Function: move_files_into_directory(file_name_and_extension, categories_and_extension_types)

    This function iterates over each downloaded file and then iterates over each extension, moving the file to the specific category based on the extension type.
    """
    list_categories = list_directory_categories(categories_and_extension_types)
    create_directories(list_categories)
    download_files = list_download_files()
    file_name_and_extension = get_file_name_and_extension(download_files)
    move_files_into_directory(file_name_and_extension, categories_and_extension_types)


main()
