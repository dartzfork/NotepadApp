import os
import customtkinter as ctk
from tkinter import filedialog, messagebox

class Notepad:
    def __init__(self, width=600, height=400):
        ctk.set_appearance_mode("System")  # Modes: "System" (default), "Dark", "Light"
        ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

        self.root = ctk.CTk()
        self.root.title("Untitled - Notepad")
        # Set icon (optional)
        try:
            self.root.iconbitmap("Notepad.ico")
        except:
            pass

        # Center the window
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")

        # Configure grid to expand Textbox
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        # Textbox and Scrollbar
        self.text_area = ctk.CTkTextbox(self.root, wrap="word", font=("Segoe UI", 13))
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=(0,0), pady=(0,0))

        self.scrollbar = ctk.CTkScrollbar(self.root, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns")

        self.file = None

        # Modern top menu with CTkSegmentedButton as a command bar
        self.command_bar = ctk.CTkFrame(self.root)
        self.command_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.command_bar.grid_columnconfigure((0,1,2,3,4,5), weight=1)

        ctk.CTkButton(self.command_bar, text="New", command=self.new_file).grid(row=0, column=0, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Open", command=self.open_file).grid(row=0, column=1, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Save", command=self.save_file).grid(row=0, column=2, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Cut", command=self.cut).grid(row=0, column=3, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Copy", command=self.copy).grid(row=0, column=4, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Paste", command=self.paste).grid(row=0, column=5, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="About", command=self.show_about).grid(row=0, column=6, padx=4, pady=6)
        ctk.CTkButton(self.command_bar, text="Exit", command=self.quit_application, fg_color="red", hover_color="#bb2222").grid(row=0, column=7, padx=4, pady=6)

    def quit_application(self):
        self.root.destroy()

    def show_about(self):
        messagebox.showinfo("About Notepad", "Modern Notepad Example\nAuthor: Mrinal Verma\nUpdated: with CustomTkinter")

    def new_file(self):
        self.text_area.delete("1.0", "end")
        self.root.title("Untitled - Notepad")
        self.file = None

    def open_file(self):
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        if filename:
            try:
                with open(filename, "r") as file:
                    content = file.read()
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", content)
                self.root.title(f"{os.path.basename(filename)} - Notepad")
                self.file = filename
            except Exception as e:
                messagebox.showerror("Open File", f"Failed to open file:\n{e}")

    def save_file(self):
        if self.file is None:
            filename = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
            )
            if not filename:
                return
            self.file = filename
        try:
            with open(self.file, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            self.root.title(f"{os.path.basename(self.file)} - Notepad")
        except Exception as e:
            messagebox.showerror("Save File", f"Failed to save file:\n{e}")

    def cut(self):
        self.text_area.event_generate("<<Cut>>")

    def copy(self):
        self.text_area.event_generate("<<Copy>>")

    def paste(self):
        self.text_area.event_generate("<<Paste>>")

    def run(self):
        self.root.mainloop()

# Entry point
if __name__ == "__main__":
    app = Notepad(width=800, height=600)
    app.run()
