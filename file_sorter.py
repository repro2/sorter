import os
from os.path import splitext, exists, join
from shutil import move
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import threading
from constants import file_extensions

# Directory settings (set by GUI)
source_dir = ""
dest_dirs = {
    "music": "Music",
    "video": "Videos",
    "image": "Images",
    "document": "Documents",
    "books": "Books",
    "executables": "Executables"
}

# Callback function for status updates
update_callback = None

def set_update_callback(callback):
    global update_callback
    update_callback = callback

def set_source_directory(dir_path):
    global source_dir
    source_dir = dir_path
    create_destination_directories()

def create_destination_directories():
    for folder in dest_dirs.values():
        path = join(source_dir, folder)
        if not exists(path):
            try:
                os.makedirs(path)
                logging.info(f"Created folder: {path}")
            except OSError as e:
                logging.error(f"Error creating folder {path}: {e}")

def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1
    while exists(join(dest, name)):
        name = f"{filename}({counter}){extension}"
        counter += 1
    return name

def move_file(dest, entry, name):
    if exists(join(dest, name)):
        unique_name = make_unique(dest, name)
        old_name = join(dest, name)
        new_name = join(dest, unique_name)
        os.rename(old_name, new_name)
        name = unique_name

    try:
        move(entry, join(dest, name))
        if update_callback:
            update_callback(f"Moved file to: {join(dest, name)}")
    except Exception as e:
        logging.error(f"Error moving file {name}: {e}")
        if update_callback:
            update_callback(f"Error moving file {name}: {e}")

class MoverHandler(FileSystemEventHandler):
    def on_modified(self, event):
        if not event.is_directory:
            try:
                with os.scandir(source_dir) as entries:
                    for entry in entries:
                        if entry.is_file():
                            self.sort_file(entry)
            except Exception as e:
                logging.error(f"Error scanning directory: {e}")

    def sort_file(self, entry):
        name = entry.name
        _, ext = splitext(name)
        ext = ext.lower()

        for category, extensions in file_extensions.items():
            if ext in extensions:
                move_file(join(source_dir, dest_dirs[category]), entry.path, name)
                break

def start_sorting():
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, source_dir, recursive=False)
    observer.start()
    logging.info("Started monitoring for file changes...")

    # Perform initial sorting of existing files in the source directory
    try:
        with os.scandir(source_dir) as entries:
            for entry in entries:
                if entry.is_file():
                    event_handler.sort_file(entry)
    except Exception as e:
        logging.error(f"Error scanning directory: {e}")

    try:
        while True:
            pass  # This will keep the thread alive
    except KeyboardInterrupt:
        observer.stop()
    observer.join()

def start_sorting_thread():
    sorting_thread = threading.Thread(target=start_sorting, daemon=True)
    sorting_thread.start()
    logging.info("File sorting thread started.")



