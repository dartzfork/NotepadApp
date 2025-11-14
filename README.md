# NotepadApp

A modern, feature-rich notepad application built with Python and CustomTkinter. This lightweight text editor provides an intuitive user interface with essential text editing capabilities, perfect for quick note-taking and text file management.

![Python Version](https://img.shields.io/badge/python-3.7%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)
![CustomTkinter](https://img.shields.io/badge/UI-CustomTkinter-orange)

## Features

- **Modern UI**: Clean and intuitive interface built with CustomTkinter
- **Theme Support**: Automatic system theme detection (Light/Dark mode)
- **File Operations**: Create, open, and save text files
- **Text Editing**: Standard cut, copy, and paste functionality
- **Cross-platform**: Works on Windows, macOS, and Linux
- **Customizable Window**: Adjustable window size with centered display
- **File Type Support**: Compatible with .txt files and all file types

## Screenshots

The application features a clean, modern interface with:
- Large text editing area with word wrapping
- Command bar with all essential functions
- Customizable appearance based on system settings

## Prerequisites

Before running NotepadApp, ensure you have the following installed:

- **Python 3.7 or higher**: Download from [python.org](https://www.python.org/downloads/)
- **pip**: Python package manager (usually included with Python)

## Installation

### Method 1: Clone the Repository

```bash
# Clone the repository
git clone https://github.com/dartzfork/NotepadApp.git

# Navigate to the project directory
cd NotepadApp

# Install required dependencies
pip install -r requirements.txt
```

### Method 2: Download ZIP

1. Download the repository as a ZIP file from GitHub
2. Extract the ZIP file to your desired location
3. Open a terminal/command prompt in the extracted folder
4. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Dependencies

NotepadApp requires the following Python package:

- **customtkinter**: Modern and customizable tkinter widgets
  ```bash
  pip install customtkinter
  ```

All dependencies are listed in `requirements.txt` for easy installation.

## Usage

### Running the Application

To start NotepadApp, run the following command in the project directory:

```bash
python Notepad.py
```

Or on some systems:

```bash
python3 Notepad.py
```

### Basic Operations

#### Creating a New File
1. Click the **New** button in the command bar
2. The text area will be cleared and ready for new content

#### Opening an Existing File
1. Click the **Open** button
2. Select a file from the file dialog
3. The file content will be displayed in the text area

#### Saving a File
1. Click the **Save** button
2. If it's a new file, choose a location and filename
3. The file will be saved with your content

#### Text Editing
- **Cut**: Click the **Cut** button or use Ctrl+X (Cmd+X on macOS)
- **Copy**: Click the **Copy** button or use Ctrl+C (Cmd+C on macOS)
- **Paste**: Click the **Paste** button or use Ctrl+V (Cmd+V on macOS)

#### Exiting the Application
- Click the **Exit** button (red button in the command bar)
- Or close the window using the standard window controls

## Configuration

### Customizing Window Size

You can customize the initial window size by modifying the parameters when creating the Notepad instance:

```python
# Default size is 800x600
app = Notepad(width=1024, height=768)
```

### Changing Appearance

The application automatically adapts to your system theme. You can modify the appearance settings in the code:

```python
ctk.set_appearance_mode("System")  # Options: "System", "Dark", "Light"
ctk.set_default_color_theme("blue")  # Options: "blue", "green", "dark-blue"
```

## Project Structure

```
NotepadApp/
├── Notepad.py           # Main application file
├── README.md            # Project documentation
├── requirements.txt     # Python dependencies
├── CONTRIBUTING.md      # Contribution guidelines
├── .gitignore          # Git ignore file
└── Notepad.ico         # Application icon (optional)
```

## Technical Details

### Architecture

NotepadApp is built using object-oriented programming principles:

- **Notepad Class**: Encapsulates all functionality and UI components
- **CustomTkinter Integration**: Provides modern, customizable widgets
- **Event-Driven Design**: Responds to user interactions through callbacks

### Key Components

1. **Text Area**: CTkTextbox widget for text editing with word wrapping
2. **Scrollbar**: CTkScrollbar for navigating long documents
3. **Command Bar**: CTkFrame containing CTkButton widgets for all operations
4. **File Management**: Built-in file operations using Python's standard library

## Troubleshooting

### Application Won't Start

- **Issue**: `ModuleNotFoundError: No module named 'customtkinter'`
- **Solution**: Install CustomTkinter using `pip install customtkinter`

### Icon Not Displaying

- **Issue**: Icon warning or error on startup
- **Solution**: The icon file (Notepad.ico) is optional. The application will run without it.

### File Dialog Not Appearing

- **Issue**: File open/save dialogs don't show
- **Solution**: Ensure your Python installation includes tkinter (usually included by default)

## Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on how to contribute to this project.

### Quick Start for Contributors

1. Fork the repository
2. Create a feature branch: `git checkout -b feature/your-feature-name`
3. Make your changes and commit: `git commit -m "Add your feature"`
4. Push to your fork: `git push origin feature/your-feature-name`
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Author

**dartzfork**

Updated with CustomTkinter for modern UI/UX.

## Acknowledgments

- Built with [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) by Tom Schimansky
- Inspired by classic notepad applications with a modern twist

## Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/dartzfork/NotepadApp/issues) page
2. Open a new issue if your problem isn't already reported
3. Provide detailed information about your environment and the problem

## Roadmap

Potential future enhancements:

- [ ] Syntax highlighting for code files
- [ ] Find and replace functionality
- [ ] Line numbers display
- [ ] Multiple tabs for editing multiple files
- [ ] Keyboard shortcuts customization
- [ ] Recent files menu
- [ ] Auto-save functionality
- [ ] Font customization options

## Version History

- **v1.0.0** (Current): Initial release with core functionality
  - Basic text editing
  - File operations (New, Open, Save)
  - Cut, copy, paste operations
  - Modern CustomTkinter interface

---

Made with ❤️ using Python and CustomTkinter
