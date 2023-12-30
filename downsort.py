import os
import shutil

def copy_by_type(src,loc):
    """
    copies files in a given directory and sorts them according to file type in destination.
    It ignores directories(folders)

    takes 2 arguements, source directory and destination directory
    """
    os.chdir(src)
    dir_items=os.listdir()
    for file in dir_items:
        if os.path.isdir(file):
            continue
        file_type=file.split('.')[-1].upper()
        if file_type in os.listdir(loc):
            shutil.copy2(src+'\\'+file,loc+'\\'+file_type)
        else:
            os.mkdir(loc+'\\'+file_type)
            shutil.copy2(src+'\\'+file,loc+'\\'+file_type)
            
def delete_files(src):
    """
    deletes all files from a directory except for folders
    """
    os.chdir(src)
    dir_items=os.listdir()
    for file in dir_items:
        if os.path.isdir(file):
            continue
        else:
            os.remove(file)

downloads = "C:\\Users\\sv\\Downloads"
file_names = os.listdir()
destination = "D:\\SortedDownloads"

copy_by_type(downloads,destination)
delete_files(downloads)
