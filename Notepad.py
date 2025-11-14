"""
NotepadApp - A Modern Text Editor

This module provides a simple yet feature-rich notepad application built with
Python and CustomTkinter. It offers essential text editing capabilities with
a modern, user-friendly interface that adapts to system themes.

Features:
    - Create, open, and save text files
    - Cut, copy, and paste text
    - Modern CustomTkinter interface with theme support
    - Cross-platform compatibility (Windows, macOS, Linux)

Author: Mrinal Verma
Updated: with CustomTkinter for modern UI/UX
License: MIT
"""

import os
import customtkinter as ctk
from tkinter import filedialog, messagebox


class Notepad:
    """
    A modern notepad application with CustomTkinter GUI.
    
    This class encapsulates all functionality for a simple text editor including
    file operations (new, open, save), text editing operations (cut, copy, paste),
    and a clean, modern user interface.
    
    Attributes:
        root (ctk.CTk): The main application window
        text_area (ctk.CTkTextbox): The text editing widget
        scrollbar (ctk.CTkScrollbar): Vertical scrollbar for text area
        command_bar (ctk.CTkFrame): Frame containing command buttons
        file (str): Path to the currently opened file, None if no file is open
    
    Example:
        >>> app = Notepad(width=800, height=600)
        >>> app.run()
    """
    
    def __init__(self, width=600, height=400):
        """
        Initialize the Notepad application.
        
        Sets up the main window, configures the UI theme, creates all widgets,
        and centers the window on the screen.
        
        Args:
            width (int, optional): Width of the application window in pixels. 
                                  Defaults to 600.
            height (int, optional): Height of the application window in pixels. 
                                   Defaults to 400.
        """
        # Configure CustomTkinter appearance
        ctk.set_appearance_mode("System")  # Adapt to system theme (Light/Dark)
        ctk.set_default_color_theme("blue")  # Color scheme for widgets
        
        # Initialize main window
        self.root = ctk.CTk()
        self.root.title("Untitled - Notepad")
        
        # Set application icon (optional - continues if icon file not found)
        try:
            self.root.iconbitmap("Notepad.ico")
        except:
            pass  # Icon is optional, application works without it
        
        # Center the window on screen
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x = int((screen_width / 2) - (width / 2))
        y = int((screen_height / 2) - (height / 2))
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        
        # Configure grid layout - make text area expandable
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        
        # Create text editing area with word wrapping
        self.text_area = ctk.CTkTextbox(
            self.root, 
            wrap="word",  # Wrap text at word boundaries
            font=("Segoe UI", 13)
        )
        self.text_area.grid(row=0, column=0, sticky="nsew", padx=(0, 0), pady=(0, 0))
        
        # Create and configure scrollbar
        self.scrollbar = ctk.CTkScrollbar(self.root, command=self.text_area.yview)
        self.text_area.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.grid(row=0, column=1, sticky="ns")
        
        # Initialize file path tracking
        self.file = None  # Stores path to currently opened file
        
        # Create command bar with action buttons
        self.command_bar = ctk.CTkFrame(self.root)
        self.command_bar.grid(row=1, column=0, columnspan=2, sticky="ew")
        self.command_bar.grid_columnconfigure((0, 1, 2, 3, 4, 5), weight=1)
        
        # File operation buttons
        ctk.CTkButton(
            self.command_bar, 
            text="New", 
            command=self.new_file
        ).grid(row=0, column=0, padx=4, pady=6)
        
        ctk.CTkButton(
            self.command_bar, 
            text="Open", 
            command=self.open_file
        ).grid(row=0, column=1, padx=4, pady=6)
        
        ctk.CTkButton(
            self.command_bar, 
            text="Save", 
            command=self.save_file
        ).grid(row=0, column=2, padx=4, pady=6)
        
        # Text editing operation buttons
        ctk.CTkButton(
            self.command_bar, 
            text="Cut", 
            command=self.cut
        ).grid(row=0, column=3, padx=4, pady=6)
        
        ctk.CTkButton(
            self.command_bar, 
            text="Copy", 
            command=self.copy
        ).grid(row=0, column=4, padx=4, pady=6)
        
        ctk.CTkButton(
            self.command_bar, 
            text="Paste", 
            command=self.paste
        ).grid(row=0, column=5, padx=4, pady=6)
        
        # Utility buttons
        ctk.CTkButton(
            self.command_bar, 
            text="About", 
            command=self.show_about
        ).grid(row=0, column=6, padx=4, pady=6)
        
        ctk.CTkButton(
            self.command_bar, 
            text="Exit", 
            command=self.quit_application,
            fg_color="red",
            hover_color="#bb2222"
        ).grid(row=0, column=7, padx=4, pady=6)
    
    def quit_application(self):
        """
        Close the application.
        
        Terminates the main window and exits the application. This method is
        called when the user clicks the Exit button.
        """
        self.root.destroy()
    
    def show_about(self):
        """
        Display the About dialog.
        
        Shows a message box with information about the application, including
        author credits and framework information.
        """
        messagebox.showinfo(
            "About Notepad",
            "Modern Notepad Example\nAuthor: Mrinal Verma\nUpdated: with CustomTkinter"
        )
    
    def new_file(self):
        """
        Create a new file.
        
        Clears the text area and resets the window title to "Untitled". This
        allows the user to start working on a new document. Any unsaved changes
        will be lost without warning.
        """
        self.text_area.delete("1.0", "end")
        self.root.title("Untitled - Notepad")
        self.file = None
    
    def open_file(self):
        """
        Open an existing file.
        
        Displays a file dialog allowing the user to select a file to open. The
        file's contents are read and displayed in the text area. The window title
        is updated to show the filename.
        
        Supported file types:
            - All files (*.*)
            - Text documents (*.txt)
        
        Error Handling:
            Displays an error dialog if the file cannot be opened (e.g., due to
            permissions or if the file doesn't exist).
        """
        filename = filedialog.askopenfilename(
            defaultextension=".txt",
            filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
        )
        
        if filename:
            try:
                # Read file contents
                with open(filename, "r") as file:
                    content = file.read()
                
                # Display content in text area
                self.text_area.delete("1.0", "end")
                self.text_area.insert("1.0", content)
                
                # Update window title and track file path
                self.root.title(f"{os.path.basename(filename)} - Notepad")
                self.file = filename
                
            except Exception as e:
                messagebox.showerror("Open File", f"Failed to open file:\n{e}")
    
    def save_file(self):
        """
        Save the current content to a file.
        
        If a file is already open, saves to that file. Otherwise, displays a
        save dialog to let the user choose a location and filename. The window
        title is updated to reflect the saved filename.
        
        Default settings:
            - Default filename: Untitled.txt
            - Default extension: .txt
            - Supported file types: All files and text documents
        
        Error Handling:
            Displays an error dialog if the file cannot be saved (e.g., due to
            permissions or disk space issues).
        """
        if self.file is None:
            # Show save dialog for new files
            filename = filedialog.asksaveasfilename(
                initialfile="Untitled.txt",
                defaultextension=".txt",
                filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")]
            )
            
            if not filename:
                return  # User cancelled the dialog
            
            self.file = filename
        
        try:
            # Write text area content to file (excluding trailing newline)
            with open(self.file, "w") as file:
                file.write(self.text_area.get("1.0", "end-1c"))
            
            # Update window title with saved filename
            self.root.title(f"{os.path.basename(self.file)} - Notepad")
            
        except Exception as e:
            messagebox.showerror("Save File", f"Failed to save file:\n{e}")
    
    def cut(self):
        """
        Cut selected text to clipboard.
        
        Removes the currently selected text from the text area and copies it to
        the system clipboard. Uses the standard Tkinter event system for
        clipboard operations.
        """
        self.text_area.event_generate("<<Cut>>")
    
    def copy(self):
        """
        Copy selected text to clipboard.
        
        Copies the currently selected text to the system clipboard without
        removing it from the text area. Uses the standard Tkinter event system
        for clipboard operations.
        """
        self.text_area.event_generate("<<Copy>>")
    
    def paste(self):
        """
        Paste text from clipboard.
        
        Inserts text from the system clipboard at the current cursor position
        in the text area. If text is selected, it will be replaced. Uses the
        standard Tkinter event system for clipboard operations.
        """
        self.text_area.event_generate("<<Paste>>")
    
    def run(self):
        """
        Start the application main loop.
        
        Enters the Tkinter event loop, which handles user interactions and keeps
        the application running until the user closes the window or clicks Exit.
        This method should be called after creating the Notepad instance.
        
        Example:
            >>> app = Notepad()
            >>> app.run()  # Application runs until closed
        """
        self.root.mainloop()


# Entry point for the application
if __name__ == "__main__":
    # Create and run the application with custom window size
    app = Notepad(width=800, height=600)
    app.run()
