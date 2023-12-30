# Download Sorter
This simple Python script helps you organize files in a given directory by sorting them based on their file types into a destination directory. Additionally, the script provides functionality to delete all files (excluding folders) from a specified directory.

## Features
### copy_by_type(src, loc)
This function copies files in a given source directory (src) and organizes them based on file types in the specified destination directory (loc). It ignores directories (folders) during the process.
Parameters:
src (str): Source directory path.
loc (str): Destination directory path.

### delete_files(src)
This function deletes all files (excluding folders) from the specified directory (src).
Parameters:
src (str): Directory path from which files will be deleted.
## Usage Example:
```bash
import os
import shutil

downloads = "C:\\Users\\vedak_7jcynkb\\Downloads"
destination = "D:\\SortedDownloads"

# Organize files in the Downloads directory and move them to the destination directory
copy_by_type(downloads, destination)

# Delete all files (excluding folders) from the Downloads directory
delete_files(downloads)
```

## Important Note
The script assumes that the files in the source directory are not currently in use or locked by other processes.
Ensure that you have the necessary permissions to read from the source directory and write to the destination directory.

## Make sure to replace the downloads and destination paths with your actual source and destination directory paths.
