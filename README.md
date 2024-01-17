# File Sorter Application

The File Sorter Application is a Python program that helps you organize your files by automatically categorizing and sorting them into different folders based on their file types. It provides a user-friendly GUI for selecting a source directory, and then it continuously monitors the directory for new and modified files, sorting them into predefined destination folders.

## Features

- Automatically sorts files into categories like Music, Videos, Images, Documents, Books, and Executables.
- Provides a graphical user interface (GUI) for selecting the source directory.
- Creates destination folders in the source directory if they don't already exist.
- Handles both new files and existing files in the source directory.
- Logs status updates for file sorting activities.

## Prerequisites

Before running the File Sorter Application, make sure you have the following installed:

- Python 3.x
- Required Python packages (install them using `pip install`):
  - `tkinter`
  - `watchdog`

## How to Use

1. Clone this repository to your local machine.

2. Open a terminal/command prompt and navigate to the project directory.

3. Run the application by executing the `gui.py` script:

   ```bash
   python gui.py

1. The GUI window will appear. Use the "Select Source Directory" button to choose the directory you want to monitor and sort files from.

2. Once you've selected the source directory, click the "Start Sorting" button to begin the automatic file sorting process.

3. The application will continuously monitor the source directory for file changes. Any new or modified files will be sorted into appropriate destination folders based on their file types.

4. You can monitor the sorting progress and see status updates in the GUI's status text box.

5. To stop the application, simply close the GUI window.

## Configuration
You can customize the destination folders for different file types by modifying the dest_dirs dictionary in the file_sorter.py module.

## Known Issues
None reported at the moment.

## Contribution
If you would like to contribute to this project or report issues, please feel free to create a GitHub issue or submit a pull request.

