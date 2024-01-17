import tkinter
import tkinter.filedialog as filedialog
import customtkinter
import file_sorter  # This module contains the sorting logic

class FileSorterApp(customtkinter.CTk):
    def __init__(self):
        super().__init__()

        # Configure window
        self.title("File Sorter")
        self.geometry("800x600")

        # Source Directory Selection
        self.btn_select_source = customtkinter.CTkButton(self, text="Select Source Directory", command=self.select_source)
        self.btn_select_source.pack(pady=10)

        # Start Sorting Button
        self.btn_start_sorting = customtkinter.CTkButton(self, text="Start Sorting", command=self.start_sorting)
        self.btn_start_sorting.pack(pady=10)

        # Status Display
        self.status_text = customtkinter.CTkTextbox(self, width=250, height=10)
        self.status_text.pack(pady=10)

    def select_source(self):
        source_dir = filedialog.askdirectory()
        if source_dir:
            self.status_text.insert(tkinter.END, f"Selected Source Directory: {source_dir}\n")
            file_sorter.set_source_directory(source_dir)
            self.status_text.insert(tkinter.END, "Destination folders will be created in the source directory if they don't exist.\n")

    def start_sorting(self):
        self.status_text.insert(tkinter.END, "Starting file sorting...\n")
        file_sorter.set_update_callback(self.update_status)
        file_sorter.start_sorting_thread()

    def update_status(self, message):
        self.status_text.insert(tkinter.END, message + "\n")

if __name__ == "__main__":
    app = FileSorterApp()
    app.mainloop()
