from pathlib import Path
from app.const import ALLOWED_EXTENSIONS
from flask_sqlalchemy import SQLAlchemy

def is_allowed_extension(file_name, allowed_extensions: tuple):
    """
    Checks if the file name has an allowed extension.

    Args:
        file_name (str): The file name.
        allowed_extensions (tuple): A tuple of allowed extensions.

    Returns:
        bool: True if the file name has an allowed extension, False otherwise.
    """

    return file_name.endswith(allowed_extensions)

def list_files(path:Path, allowed_extensions:tuple = None) -> list:
    """
    Lists all videos in the specified path.

    Args:
        path (Path): The path to the directory containing the videos.
        allowed_extensions (tuple): A tuple of allowed extensions.

    Returns:
        list: A list of the various files

    """

    if not allowed_extensions:
        allowed_extensions = ALLOWED_EXTENSIONS

    videos = []
    for file in Path(path).glob('*'):
        """
        why am not using the os.listdir function:
            The os.listdir() function is not very efficient, as it has to read the entire contents of the directory into memory. The Path.glob() function is a more efficient way to iterate over the files in a directory, as it only reads the file names.
        """
        if is_allowed_extension(file.name, allowed_extensions):
            videos.append(file)
    return videos



def list_folders(path: Path):
    if not type(path) == Path:
        path = Path(path)
    
    folders = []
    for item in path.glob("*"):
        if item.is_dir():
            folders.append(item)
    return folders



def add_folder(path: str, database: SQLAlchemy):
    # check if path exist
    folder = Path(path)

    if not folder.is_dir():
        raise ValueError("The path passed is not a directory please input a valid directory path")
    elif not folder.exists:
        raise FileExistsError("The path dose not exist")
    else:
        files = list_files(folder)
        folders = list_folders(folder)

        print(files)
        print()
        print(folders)

        
    

