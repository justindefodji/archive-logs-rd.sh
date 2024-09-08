import shutil
import os
import time
import sys


def archive_folder(source: str):
    destination = '/var/log'

    # Create the destination folder if it does not exist
    if not os.path.exists(destination):
        os.makedirs(destination)

    # Create a folder with the current date and time and the base name is logs_archive
    folder_name = time.strftime('logs_archive_%Y-%m-%d_%H-%M-%S')
    destination = destination + folder_name

    # Create the folder
    os.makedirs(destination)

    # Move all files from the source folder to the destination folder
    for file_name in os.listdir(source):
        shutil.move(os.path.join(source, file_name), destination)

    # Create a tar.gz file with the folder
    shutil.make_archive(destination, 'gztar', destination)

    # Remove the folder
    shutil.rmtree(destination)


if __name__ == '__main__':
    archive_folder(sys.argv[1])
