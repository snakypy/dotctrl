from os import walk
from os.path import join


def listing_files(directory: str) -> list:
    """Lists files from a specific directory."""
    objects: list = list()

    for root, _, files in walk(directory):
        for file in files:
            elem = join(root, file)
            elem = elem.replace(f"{directory}/", "")
            objects.append(elem)

    return objects
