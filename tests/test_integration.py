from unittest import mock
from pathlib import Path

from downloads_folder_organizer.organization_folder import (
    list_directory_categories,
    list_download_files,
    get_file_name_and_extension,
    move_files_into_directory,
)


def test_list_directory_categories():
    list_extensions = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".doc", ".pdf", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
    }

    assert list_directory_categories(list_extensions) == [
        "Images",
        "Documents",
        "Videos",
    ]


def test_list_download_files():
    with mock.patch("pathlib.Path.home", return_value=Path("/yanvi/Downloads")):
        with mock.patch(
            "pathlib.Path.iterdir",
            return_value=[
                Path("/yanvi/Downloads/file1.txt"),
                Path("/yanvi/Downloads/file2.jpg"),
                Path("/yanvi/Downloads/file3.pdf"),
            ],
        ):
            assert list_download_files() == [
                "file1.txt",
                "file2.jpg",
                "file3.pdf",
            ]


def test_get_file_name_and_extension():
    files_list = [
        "file1.txt",
        "file2.jpg",
        "file3.pdf",
    ]

    files_with_extensions = [
        (Path(file).name, Path(file).suffix) for file in files_list
    ]
    assert get_file_name_and_extension(files_list) == [
        ("file1.txt", ".txt"),
        ("file2.jpg", ".jpg"),
        ("file3.pdf", ".pdf"),
    ]


@mock.patch("shutil.move")
def test_move_files_into_directory(mock_move):
    download_files = [
        ("file1.txt", ".txt"),
        ("file2.jpg", ".jpg"),
        ("file3.pdf", ".pdf"),
    ]

    files_names_and_extensions = {
        "Images": [".jpg", ".png", ".gif"],
        "Documents": [".doc", ".pdf", ".txt"],
        "Videos": [".mp4", ".mov", ".avi"],
    }

    move_files_into_directory(download_files, files_names_and_extensions)

    expected_calls = [
        mock.call(
            "C:\\Users\\yanvi\\Downloads\\file1.txt",
            "C:\\Users\\yanvi\\Downloads\\Documents\\file1.txt",
        ),
        mock.call(
            "C:\\Users\\yanvi\\Downloads\\file2.jpg",
            "C:\\Users\\yanvi\\Downloads\\Images\\file2.jpg",
        ),
        mock.call(
            "C:\\Users\\yanvi\\Downloads\\file3.pdf",
            "C:\\Users\\yanvi\\Downloads\\Documents\\file3.pdf",
        ),
    ]
    mock_move.assert_has_calls(expected_calls)
