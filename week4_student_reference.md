# Week 4 Student Reference Guide
**CSC 242 - Object-Oriented Programming**  
**Topic:** GUI Programming with Tkinter, File I/O, and Event-Driven Programming

---

## 📚 Table of Contents
1. [GUI Programming Fundamentals](#1-gui-programming-fundamentals)
2. [Tkinter Basics](#2-tkinter-basics)
3. [Widgets and Layout Management](#3-widgets-and-layout-management)
4. [Event-Driven Programming](#4-event-driven-programming)
5. [File Input/Output Operations](#5-file-inputoutput-operations)
6. [Exception Handling with File Operations](#6-exception-handling-with-file-operations)
7. [Advanced GUI Patterns](#7-advanced-gui-patterns)
8. [Model-View-Controller Architecture](#8-model-view-controller-architecture)
9. [Best Practices](#9-best-practices)
10. [Practice Problems](#10-practice-problems)

---

## 1. GUI Programming Fundamentals

### What is a Graphical User Interface?
A GUI provides a visual way for users to interact with programs through:
- **Windows** - Main application containers
- **Widgets** - Interactive elements (buttons, text fields, etc.)
- **Events** - User actions (clicks, key presses, etc.)
- **Event Handlers** - Functions that respond to events

### Event-Driven Programming Model
```python
# Simplified event loop concept
def main_loop():
    while window_is_open:
        event = get_next_event()
        if event:
            handler = find_handler(event)
            handler(event)
        update_display()
```

### Key GUI Concepts
- **Parent-Child Relationships**: Widgets contain other widgets
- **Geometry Management**: How widgets are positioned and sized
- **Event Binding**: Connecting user actions to program responses
- **State Management**: Keeping track of application data

---

## 2. Tkinter Basics

### Introduction to Tkinter
Tkinter (Tk interface) is Python's standard GUI toolkit, built on the Tcl/Tk framework.

#### Basic Tkinter Setup
```python
import tkinter as tk
from tkinter import ttk  # Themed widgets

# Create main window
root = tk.Tk()
root.title("My Application")
root.geometry("400x300")  # Width x Height

# Start event loop
root.mainloop()
```

#### Alternative Import Styles
```python
# Method 1: Import whole module
import tkinter as tk
button = tk.Button(root, text="Click Me")

# Method 2: Import specific classes
from tkinter import Button, Label, Entry
button = Button(root, text="Click Me")

# Method 3: Import everything (not recommended)
from tkinter import *
button = Button(root, text="Click Me")
```

### First GUI Application
```python
import tkinter as tk

class HelloApp:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Hello World GUI")
        self.setup_widgets()
    
    def setup_widgets(self):
        # Create and pack a label
        label = tk.Label(self.root, 
                        text="Hello, GUI World!",
                        font=("Arial", 16),
                        fg="blue")
        label.pack(pady=20)
        
        # Create and pack a button
        button = tk.Button(self.root,
                          text="Click Me!",
                          command=self.button_clicked,
                          bg="lightblue")
        button.pack(pady=10)
    
    def button_clicked(self):
        print("Button was clicked!")
    
    def run(self):
        self.root.mainloop()

# Usage
if __name__ == "__main__":
    app = HelloApp()
    app.run()
```

---

## 3. Widgets and Layout Management

### Common Tkinter Widgets

#### Label Widget
```python
label = tk.Label(root,
                text="Display text here",
                font=("Arial", 12),
                fg="black",        # Foreground color
                bg="white",        # Background color
                width=20,          # Width in characters
                height=2,          # Height in lines
                anchor="center",   # Text alignment
                relief="raised",   # Border style
                borderwidth=2)
```

#### Button Widget
```python
def button_handler():
    print("Button pressed!")

button = tk.Button(root,
                  text="Press Me",
                  command=button_handler,
                  font=("Arial", 10, "bold"),
                  fg="white",
                  bg="blue",
                  width=15,
                  height=2,
                  state="normal")  # or "disabled"
```

#### Entry Widget (Text Input)
```python
entry = tk.Entry(root,
                width=30,
                font=("Arial", 12),
                justify="left",    # Text alignment
                show="*")          # For password fields

# Getting and setting text
def get_text():
    user_input = entry.get()
    print(f"User entered: {user_input}")

def set_text():
    entry.delete(0, tk.END)      # Clear existing text
    entry.insert(0, "New text")  # Insert new text
```

#### Text Widget (Multi-line Text)
```python
text_widget = tk.Text(root,
                     width=50,
                     height=10,
                     font=("Courier", 10),
                     wrap="word",     # Word wrapping
                     undo=True)       # Enable undo/redo

# Working with text content
def text_operations():
    # Insert text
    text_widget.insert("1.0", "Hello\n")  # Line 1, character 0
    text_widget.insert(tk.END, "World!")  # At the end
    
    # Get text
    content = text_widget.get("1.0", tk.END)
    
    # Delete text
    text_widget.delete("1.0", "1.5")  # Delete first 5 characters
    
    # Clear all text
    text_widget.delete("1.0", tk.END)
```

#### Checkbutton and Radiobutton
```python
# Checkbutton
check_var = tk.BooleanVar()
checkbutton = tk.Checkbutton(root,
                           text="Enable feature",
                           variable=check_var,
                           command=lambda: print(f"Checked: {check_var.get()}"))

# Radiobuttons
radio_var = tk.StringVar(value="option1")

radio1 = tk.Radiobutton(root,
                       text="Option 1",
                       variable=radio_var,
                       value="option1")

radio2 = tk.Radiobutton(root,
                       text="Option 2", 
                       variable=radio_var,
                       value="option2")
```

#### Listbox and Combobox
```python
# Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)
items = ["Item 1", "Item 2", "Item 3"]
for item in items:
    listbox.insert(tk.END, item)

def get_selection():
    selection = listbox.curselection()
    if selection:
        item = listbox.get(selection[0])
        print(f"Selected: {item}")

# Combobox (requires ttk)
from tkinter import ttk
combo = ttk.Combobox(root,
                    values=["Choice 1", "Choice 2", "Choice 3"],
                    state="readonly")
combo.set("Choice 1")  # Set default value
```

### Layout Management

#### Pack Geometry Manager
```python
# Pack arranges widgets in blocks before placing them in parent
widget1.pack(side="top", fill="x", expand=True, padx=10, pady=5)
widget2.pack(side="left", fill="y")
widget3.pack(side="bottom", fill="both", expand=True)

# Pack options:
# side: "top", "bottom", "left", "right"
# fill: "x", "y", "both", "none"
# expand: True/False - expand when window resizes
# padx/pady: external padding
# ipadx/ipady: internal padding
```

#### Grid Geometry Manager
```python
# Grid arranges widgets in a table-like structure
label.grid(row=0, column=0, sticky="w", padx=5, pady=5)
entry.grid(row=0, column=1, sticky="ew", padx=5, pady=5)
button.grid(row=1, column=0, columnspan=2, sticky="ew", pady=10)

# Grid options:
# row/column: position in grid (0-based)
# rowspan/columnspan: span multiple cells
# sticky: "n", "s", "e", "w" or combinations ("ew", "nsew")
# padx/pady: padding around widget
# ipadx/ipady: internal padding

# Configure grid weights for resizing
root.grid_columnconfigure(1, weight=1)  # Column 1 expands
root.grid_rowconfigure(0, weight=1)     # Row 0 expands
```

#### Place Geometry Manager
```python
# Place gives precise control over widget positioning
widget.place(x=50, y=100)                    # Absolute positioning
widget.place(relx=0.5, rely=0.5, anchor="center")  # Relative positioning
widget.place(relwidth=0.8, relheight=0.6)    # Relative sizing

# Place options:
# x/y: absolute position in pixels
# relx/rely: relative position (0.0 to 1.0)
# width/height: absolute size in pixels
# relwidth/relheight: relative size (0.0 to 1.0)
# anchor: positioning reference point
```

---

## 4. Event-Driven Programming

### Understanding Events
Events are generated by user interactions or system occurrences:
- **Mouse events**: clicks, movement, wheel scrolling
- **Keyboard events**: key presses, releases
- **Window events**: resize, close, focus changes
- **Widget events**: selection changes, text modifications

### Event Binding
```python
# Method 1: Command parameter (for buttons)
button = tk.Button(root, text="Click", command=handle_click)

# Method 2: Bind method (for any widget and event)
widget.bind("<Button-1>", handle_left_click)  # Left mouse click
widget.bind("<KeyPress>", handle_key_press)   # Any key press
widget.bind("<Return>", handle_enter_key)     # Enter key specifically

# Method 3: Protocol handler (for window events)
root.protocol("WM_DELETE_WINDOW", handle_window_close)
```

### Common Event Types
```python
# Mouse events
"<Button-1>"        # Left mouse button click
"<Button-2>"        # Middle mouse button
"<Button-3>"        # Right mouse button
"<Double-Button-1>" # Double left click
"<Motion>"          # Mouse movement
"<Enter>"           # Mouse enters widget
"<Leave>"           # Mouse leaves widget

# Keyboard events
"<KeyPress>"        # Any key pressed
"<Key-Return>"      # Enter key
"<Key-Escape>"      # Escape key
"<Control-c>"       # Ctrl+C
"<Alt-F4>"          # Alt+F4

# Window events
"<Configure>"       # Window resized
"<FocusIn>"         # Widget gains focus
"<FocusOut>"        # Widget loses focus
"<Destroy>"         # Widget destroyed
```

### Event Handler Functions
```python
# Event handlers receive an Event object
def handle_click(event):
    print(f"Clicked at ({event.x}, {event.y})")
    print(f"Widget: {event.widget}")
    print(f"Event type: {event.type}")

def handle_key_press(event):
    print(f"Key pressed: {event.keysym}")
    print(f"Key code: {event.keycode}")
    print(f"Character: {event.char}")

# Command handlers don't receive event object
def handle_button_click():
    print("Button was clicked!")

# Binding examples
canvas.bind("<Button-1>", handle_click)
entry.bind("<KeyPress>", handle_key_press)
button.config(command=handle_button_click)
```

### Advanced Event Handling
```python
class EventDemo:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_widgets()
        self.bind_events()
    
    def setup_widgets(self):
        self.canvas = tk.Canvas(self.root, width=400, height=300, bg="white")
        self.canvas.pack()
        
        self.status_label = tk.Label(self.root, text="Ready")
        self.status_label.pack()
    
    def bind_events(self):
        # Multiple events on same widget
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<KeyPress>", self.on_key_press)
        
        # Make canvas focusable for keyboard events
        self.canvas.focus_set()
    
    def on_left_click(self, event):
        # Draw circle at click location
        x, y = event.x, event.y
        self.canvas.create_oval(x-5, y-5, x+5, y+5, fill="red")
        self.status_label.config(text=f"Left click at ({x}, {y})")
    
    def on_right_click(self, event):
        # Clear canvas
        self.canvas.delete("all")
        self.status_label.config(text="Canvas cleared")
    
    def on_mouse_move(self, event):
        self.status_label.config(text=f"Mouse at ({event.x}, {event.y})")
    
    def on_key_press(self, event):
        if event.keysym == "Escape":
            self.root.quit()
```

---

## 5. File Input/Output Operations

### Basic File Operations
```python
# Writing to files
def write_file(filename, content):
    try:
        with open(filename, 'w') as file:
            file.write(content)
        print(f"Successfully wrote to {filename}")
    except IOError as e:
        print(f"Error writing file: {e}")

# Reading from files
def read_file(filename):
    try:
        with open(filename, 'r') as file:
            content = file.read()
        return content
    except FileNotFoundError:
        print(f"File {filename} not found")
        return None
    except IOError as e:
        print(f"Error reading file: {e}")
        return None

# Reading lines
def read_lines(filename):
    try:
        with open(filename, 'r') as file:
            lines = file.readlines()
        return [line.strip() for line in lines]  # Remove newlines
    except IOError as e:
        print(f"Error reading file: {e}")
        return []
```

### File Modes and Options
```python
# File modes
'r'   # Read only (default)
'w'   # Write only (overwrites existing file)
'a'   # Append only
'r+'  # Read and write
'w+'  # Write and read (overwrites existing)
'a+'  # Append and read

# Binary modes
'rb'  # Read binary
'wb'  # Write binary
'ab'  # Append binary

# Text encoding
with open('file.txt', 'r', encoding='utf-8') as file:
    content = file.read()
```

### Working with Different File Formats

#### CSV Files
```python
import csv

# Writing CSV
def write_csv(filename, data):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Age', 'City'])  # Header
        for row in data:
            writer.writerow(row)

# Reading CSV
def read_csv(filename):
    data = []
    try:
        with open(filename, 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)  # Skip header row
            for row in reader:
                data.append(row)
    except IOError as e:
        print(f"Error reading CSV: {e}")
    return data

# Using DictReader/DictWriter
def read_csv_dict(filename):
    try:
        with open(filename, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)
    except IOError as e:
        print(f"Error reading CSV: {e}")
        return []
```

#### JSON Files
```python
import json

# Writing JSON
def write_json(filename, data):
    try:
        with open(filename, 'w') as file:
            json.dump(data, file, indent=2)
    except IOError as e:
        print(f"Error writing JSON: {e}")

# Reading JSON
def read_json(filename):
    try:
        with open(filename, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"JSON file {filename} not found")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON: {e}")
        return None

# Example usage
data = {
    "users": [
        {"name": "Alice", "age": 30},
        {"name": "Bob", "age": 25}
    ],
    "settings": {
        "theme": "dark",
        "notifications": True
    }
}

write_json("config.json", data)
loaded_data = read_json("config.json")
```

### File Dialog Integration with Tkinter
```python
from tkinter import filedialog, messagebox

class FileDialogApp:
    def __init__(self):
        self.root = tk.Tk()
        self.setup_widgets()
    
    def setup_widgets(self):
        # File operation buttons
        tk.Button(self.root, text="Open File", 
                 command=self.open_file).pack(pady=5)
        tk.Button(self.root, text="Save File", 
                 command=self.save_file).pack(pady=5)
        tk.Button(self.root, text="Choose Directory", 
                 command=self.choose_directory).pack(pady=5)
        
        # Text area for file content
        self.text_area = tk.Text(self.root, width=60, height=20)
        self.text_area.pack(pady=10)
    
    def open_file(self):
        filename = filedialog.askopenfilename(
            title="Select a file",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                with open(filename, 'r') as file:
                    content = file.read()
                    self.text_area.delete("1.0", tk.END)
                    self.text_area.insert("1.0", content)
            except IOError as e:
                messagebox.showerror("Error", f"Could not open file: {e}")
    
    def save_file(self):
        filename = filedialog.asksaveasfilename(
            title="Save file",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                content = self.text_area.get("1.0", tk.END)
                with open(filename, 'w') as file:
                    file.write(content)
                messagebox.showinfo("Success", "File saved successfully!")
            except IOError as e:
                messagebox.showerror("Error", f"Could not save file: {e}")
    
    def choose_directory(self):
        directory = filedialog.askdirectory(title="Select a directory")
        if directory:
            messagebox.showinfo("Directory Selected", f"Selected: {directory}")
```

---

## 6. Exception Handling with File Operations

### Common File Exceptions
```python
try:
    with open("data.txt", "r") as file:
        content = file.read()
        
except FileNotFoundError:
    print("File does not exist")
    
except PermissionError:
    print("Permission denied to access file")
    
except IsADirectoryError:
    print("Expected file but found directory")
    
except OSError as e:
    print(f"Operating system error: {e}")
    
except Exception as e:
    print(f"Unexpected error: {e}")
```

### Robust File Handling Class
```python
import os
import json
from pathlib import Path

class FileManager:
    """Robust file management with comprehensive error handling"""
    
    def __init__(self, base_directory="."):
        self.base_directory = Path(base_directory)
        self.ensure_directory_exists()
    
    def ensure_directory_exists(self):
        """Create base directory if it doesn't exist"""
        try:
            self.base_directory.mkdir(parents=True, exist_ok=True)
        except OSError as e:
            raise RuntimeError(f"Cannot create directory {self.base_directory}: {e}")
    
    def read_text_file(self, filename):
        """Read text file with error handling"""
        filepath = self.base_directory / filename
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return file.read()
                
        except FileNotFoundError:
            raise FileNotFoundError(f"File not found: {filepath}")
        except PermissionError:
            raise PermissionError(f"Permission denied: {filepath}")
        except UnicodeDecodeError as e:
            raise ValueError(f"Cannot decode file {filepath}: {e}")
    
    def write_text_file(self, filename, content):
        """Write text file with error handling"""
        filepath = self.base_directory / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                file.write(content)
                
        except PermissionError:
            raise PermissionError(f"Permission denied: {filepath}")
        except OSError as e:
            raise OSError(f"Cannot write to {filepath}: {e}")
    
    def read_json_file(self, filename):
        """Read JSON file with error handling"""
        filepath = self.base_directory / filename
        
        try:
            with open(filepath, 'r', encoding='utf-8') as file:
                return json.load(file)
                
        except FileNotFoundError:
            raise FileNotFoundError(f"JSON file not found: {filepath}")
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON in {filepath}: {e}")
        except Exception as e:
            raise RuntimeError(f"Error reading JSON file {filepath}: {e}")
    
    def write_json_file(self, filename, data):
        """Write JSON file with error handling"""
        filepath = self.base_directory / filename
        
        try:
            with open(filepath, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
                
        except TypeError as e:
            raise TypeError(f"Data not JSON serializable: {e}")
        except OSError as e:
            raise OSError(f"Cannot write JSON to {filepath}: {e}")
    
    def file_exists(self, filename):
        """Check if file exists"""
        return (self.base_directory / filename).exists()
    
    def list_files(self, pattern="*"):
        """List files matching pattern"""
        try:
            return list(self.base_directory.glob(pattern))
        except OSError as e:
            raise OSError(f"Cannot list files: {e}")
    
    def delete_file(self, filename):
        """Delete file with error handling"""
        filepath = self.base_directory / filename
        
        try:
            filepath.unlink()
        except FileNotFoundError:
            raise FileNotFoundError(f"Cannot delete, file not found: {filepath}")
        except PermissionError:
            raise PermissionError(f"Permission denied to delete: {filepath}")
        except OSError as e:
            raise OSError(f"Cannot delete file {filepath}: {e}")
```

---

## 7. Advanced GUI Patterns

### MVC (Model-View-Controller) Pattern
```python
class Model:
    """Data and business logic"""
    
    def __init__(self):
        self.data = []
        self.observers = []
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()
    
    def add_item(self, item):
        self.data.append(item)
        self.notify_observers()
    
    def remove_item(self, index):
        if 0 <= index < len(self.data):
            del self.data[index]
            self.notify_observers()
    
    def get_items(self):
        return self.data.copy()


class View:
    """User interface"""
    
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.setup_widgets()
    
    def setup_widgets(self):
        # Entry for new items
        self.entry = tk.Entry(self.root, width=30)
        self.entry.pack(pady=5)
        self.entry.bind("<Return>", self.on_add_item)
        
        # Add button
        tk.Button(self.root, text="Add Item", 
                 command=self.on_add_item).pack(pady=5)
        
        # Listbox for items
        self.listbox = tk.Listbox(self.root, width=40, height=10)
        self.listbox.pack(pady=10)
        
        # Remove button
        tk.Button(self.root, text="Remove Selected", 
                 command=self.on_remove_item).pack(pady=5)
    
    def on_add_item(self, event=None):
        item = self.entry.get().strip()
        if item:
            self.controller.add_item(item)
            self.entry.delete(0, tk.END)
    
    def on_remove_item(self):
        selection = self.listbox.curselection()
        if selection:
            self.controller.remove_item(selection[0])
    
    def update(self):
        """Update view when model changes"""
        self.listbox.delete(0, tk.END)
        for item in self.controller.get_items():
            self.listbox.insert(tk.END, item)
    
    def run(self):
        self.root.mainloop()


class Controller:
    """Mediates between Model and View"""
    
    def __init__(self):
        self.model = Model()
        self.view = View(self)
        self.model.add_observer(self.view)
    
    def add_item(self, item):
        self.model.add_item(item)
    
    def remove_item(self, index):
        self.model.remove_item(index)
    
    def get_items(self):
        return self.model.get_items()
    
    def run(self):
        self.view.run()


# Usage
app = Controller()
app.run()
```

### Custom Widget Creation
```python
class CounterWidget(tk.Frame):
    """Custom widget combining multiple Tkinter widgets"""
    
    def __init__(self, parent, initial_value=0, min_value=None, max_value=None):
        super().__init__(parent)
        
        self.value = initial_value
        self.min_value = min_value
        self.max_value = max_value
        self.callbacks = []
        
        self.setup_widgets()
        self.update_display()
    
    def setup_widgets(self):
        # Decrease button
        self.decrease_btn = tk.Button(self, text="-", 
                                    command=self.decrease,
                                    width=3)
        self.decrease_btn.pack(side="left")
        
        # Value display
        self.value_label = tk.Label(self, text="0", 
                                  width=10, 
                                  relief="sunken",
                                  borderwidth=1)
        self.value_label.pack(side="left", padx=5)
        
        # Increase button
        self.increase_btn = tk.Button(self, text="+", 
                                    command=self.increase,
                                    width=3)
        self.increase_btn.pack(side="left")
    
    def increase(self):
        if self.max_value is None or self.value < self.max_value:
            self.value += 1
            self.update_display()
            self.notify_callbacks()
    
    def decrease(self):
        if self.min_value is None or self.value > self.min_value:
            self.value -= 1
            self.update_display()
            self.notify_callbacks()
    
    def set_value(self, value):
        if (self.min_value is None or value >= self.min_value) and \
           (self.max_value is None or value <= self.max_value):
            self.value = value
            self.update_display()
            self.notify_callbacks()
    
    def get_value(self):
        return self.value
    
    def add_callback(self, callback):
        self.callbacks.append(callback)
    
    def notify_callbacks(self):
        for callback in self.callbacks:
            callback(self.value)
    
    def update_display(self):
        self.value_label.config(text=str(self.value))
        
        # Update button states
        self.decrease_btn.config(
            state="normal" if (self.min_value is None or self.value > self.min_value) 
                  else "disabled"
        )
        self.increase_btn.config(
            state="normal" if (self.max_value is None or self.value < self.max_value) 
                  else "disabled"
        )


# Using the custom widget
root = tk.Tk()
root.title("Custom Counter Widget Demo")

def on_value_changed(value):
    print(f"Counter value changed to: {value}")

counter1 = CounterWidget(root, initial_value=5, min_value=0, max_value=10)
counter1.add_callback(on_value_changed)
counter1.pack(pady=10)

counter2 = CounterWidget(root, initial_value=0)
counter2.pack(pady=10)

root.mainloop()
```

---

## 8. Model-View-Controller Architecture

### Complete MVC Application Example
```python
import tkinter as tk
from tkinter import messagebox, filedialog
import json

class TaskModel:
    """Model for task management application"""
    
    def __init__(self):
        self.tasks = []
        self.observers = []
        self.next_id = 1
    
    def add_observer(self, observer):
        self.observers.append(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.model_changed()
    
    def add_task(self, title, description="", priority="Medium"):
        task = {
            'id': self.next_id,
            'title': title,
            'description': description,
            'priority': priority,
            'completed': False
        }
        self.tasks.append(task)
        self.next_id += 1
        self.notify_observers()
        return task['id']
    
    def update_task(self, task_id, **kwargs):
        task = self.find_task(task_id)
        if task:
            task.update(kwargs)
            self.notify_observers()
            return True
        return False
    
    def delete_task(self, task_id):
        task = self.find_task(task_id)
        if task:
            self.tasks.remove(task)
            self.notify_observers()
            return True
        return False
    
    def find_task(self, task_id):
        for task in self.tasks:
            if task['id'] == task_id:
                return task
        return None
    
    def get_tasks(self, filter_completed=None):
        if filter_completed is None:
            return self.tasks.copy()
        return [task for task in self.tasks 
                if task['completed'] == filter_completed]
    
    def save_to_file(self, filename):
        try:
            with open(filename, 'w') as file:
                json.dump(self.tasks, file, indent=2)
            return True
        except Exception as e:
            print(f"Error saving to file: {e}")
            return False
    
    def load_from_file(self, filename):
        try:
            with open(filename, 'r') as file:
                self.tasks = json.load(file)
            
            # Update next_id
            if self.tasks:
                self.next_id = max(task['id'] for task in self.tasks) + 1
            else:
                self.next_id = 1
            
            self.notify_observers()
            return True
        except Exception as e:
            print(f"Error loading from file: {e}")
            return False


class TaskView:
    """View for task management application"""
    
    def __init__(self, controller):
        self.controller = controller
        self.root = tk.Tk()
        self.setup_window()
        self.setup_widgets()
    
    def setup_window(self):
        self.root.title("Task Manager")
        self.root.geometry("600x500")
        self.root.protocol("WM_DELETE_WINDOW", self.on_closing)
    
    def setup_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Load", command=self.load_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.on_closing)
        
        # Task input frame
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Label(input_frame, text="Task Title:").pack(anchor="w")
        self.title_entry = tk.Entry(input_frame, width=50)
        self.title_entry.pack(fill="x", pady=(0, 5))
        self.title_entry.bind("<Return>", self.add_task)
        
        tk.Label(input_frame, text="Description:").pack(anchor="w")
        self.desc_entry = tk.Entry(input_frame, width=50)
        self.desc_entry.pack(fill="x", pady=(0, 5))
        
        # Priority and Add button
        button_frame = tk.Frame(input_frame)
        button_frame.pack(fill="x", pady=5)
        
        tk.Label(button_frame, text="Priority:").pack(side="left")
        self.priority_var = tk.StringVar(value="Medium")
        priority_menu = tk.OptionMenu(button_frame, self.priority_var, 
                                    "Low", "Medium", "High")
        priority_menu.pack(side="left", padx=5)
        
        tk.Button(button_frame, text="Add Task", 
                 command=self.add_task).pack(side="right")
        
        # Task list
        list_frame = tk.Frame(self.root)
        list_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(list_frame, text="Tasks:").pack(anchor="w")
        
        # Listbox with scrollbar
        list_container = tk.Frame(list_frame)
        list_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(list_container)
        scrollbar.pack(side="right", fill="y")
        
        self.task_listbox = tk.Listbox(list_container, 
                                      yscrollcommand=scrollbar.set)
        self.task_listbox.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.task_listbox.yview)
        
        # Task control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(control_frame, text="Mark Complete", 
                 command=self.toggle_complete).pack(side="left", padx=5)
        tk.Button(control_frame, text="Delete Task", 
                 command=self.delete_task).pack(side="left", padx=5)
        
        # Filter buttons
        filter_frame = tk.Frame(self.root)
        filter_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(filter_frame, text="Show All", 
                 command=self.show_all_tasks).pack(side="left", padx=5)
        tk.Button(filter_frame, text="Show Pending", 
                 command=self.show_pending_tasks).pack(side="left", padx=5)
        tk.Button(filter_frame, text="Show Completed", 
                 command=self.show_completed_tasks).pack(side="left", padx=5)
        
        self.filter_mode = None
    
    def add_task(self, event=None):
        title = self.title_entry.get().strip()
        if not title:
            messagebox.showwarning("Invalid Input", "Please enter a task title")
            return
        
        description = self.desc_entry.get().strip()
        priority = self.priority_var.get()
        
        self.controller.add_task(title, description, priority)
        
        # Clear input fields
        self.title_entry.delete(0, tk.END)
        self.desc_entry.delete(0, tk.END)
        self.title_entry.focus()
    
    def toggle_complete(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task")
            return
        
        task_id = self.get_selected_task_id()
        if task_id:
            self.controller.toggle_task_completion(task_id)
    
    def delete_task(self):
        selection = self.task_listbox.curselection()
        if not selection:
            messagebox.showwarning("No Selection", "Please select a task")
            return
        
        if messagebox.askyesno("Confirm Delete", "Delete selected task?"):
            task_id = self.get_selected_task_id()
            if task_id:
                self.controller.delete_task(task_id)
    
    def get_selected_task_id(self):
        selection = self.task_listbox.curselection()
        if selection:
            # Extract task ID from listbox text
            item_text = self.task_listbox.get(selection[0])
            # Format: "ID: Title [Priority] (Status)"
            task_id = int(item_text.split(':')[0])
            return task_id
        return None
    
    def show_all_tasks(self):
        self.filter_mode = None
        self.controller.refresh_view()
    
    def show_pending_tasks(self):
        self.filter_mode = False
        self.controller.refresh_view()
    
    def show_completed_tasks(self):
        self.filter_mode = True
        self.controller.refresh_view()
    
    def save_file(self):
        filename = filedialog.asksaveasfilename(
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            if self.controller.save_tasks(filename):
                messagebox.showinfo("Success", "Tasks saved successfully")
            else:
                messagebox.showerror("Error", "Failed to save tasks")
    
    def load_file(self):
        filename = filedialog.askopenfilename(
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        if filename:
            if self.controller.load_tasks(filename):
                messagebox.showinfo("Success", "Tasks loaded successfully")
            else:
                messagebox.showerror("Error", "Failed to load tasks")
    
    def model_changed(self):
        """Called when model data changes"""
        self.update_task_list()
    
    def update_task_list(self):
        self.task_listbox.delete(0, tk.END)
        
        tasks = self.controller.get_tasks(self.filter_mode)
        for task in tasks:
            status = "✓" if task['completed'] else "○"
            item_text = f"{task['id']}: {task['title']} [{task['priority']}] ({status})"
            self.task_listbox.insert(tk.END, item_text)
    
    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.root.destroy()
    
    def run(self):
        self.root.mainloop()


class TaskController:
    """Controller for task management application"""
    
    def __init__(self):
        self.model = TaskModel()
        self.view = TaskView(self)
        self.model.add_observer(self.view)
    
    def add_task(self, title, description="", priority="Medium"):
        return self.model.add_task(title, description, priority)
    
    def delete_task(self, task_id):
        return self.model.delete_task(task_id)
    
    def toggle_task_completion(self, task_id):
        task = self.model.find_task(task_id)
        if task:
            return self.model.update_task(task_id, completed=not task['completed'])
        return False
    
    def get_tasks(self, filter_completed=None):
        return self.model.get_tasks(filter_completed)
    
    def save_tasks(self, filename):
        return self.model.save_to_file(filename)
    
    def load_tasks(self, filename):
        return self.model.load_from_file(filename)
    
    def refresh_view(self):
        self.view.update_task_list()
    
    def run(self):
        self.view.run()


# Usage
if __name__ == "__main__":
    app = TaskController()
    app.run()
```

---

## 9. Best Practices

### GUI Design Principles
1. **Consistency**: Use consistent fonts, colors, and layouts
2. **Clarity**: Make interfaces intuitive and self-explanatory
3. **Feedback**: Provide visual feedback for user actions
4. **Error Prevention**: Validate input and prevent invalid states
5. **Accessibility**: Consider users with different abilities

### Code Organization
```python
# Good structure for GUI applications
class Application:
    def __init__(self):
        self.setup_model()
        self.setup_view()
        self.setup_bindings()
    
    def setup_model(self):
        """Initialize data and business logic"""
        pass
    
    def setup_view(self):
        """Create and arrange widgets"""
        pass
    
    def setup_bindings(self):
        """Connect events to handlers"""
        pass
```

### Error Handling
```python
def safe_file_operation(self, operation, *args, **kwargs):
    """Wrapper for file operations with user-friendly error handling"""
    try:
        return operation(*args, **kwargs)
    except FileNotFoundError:
        messagebox.showerror("File Error", "File not found")
    except PermissionError:
        messagebox.showerror("Permission Error", "Access denied")
    except Exception as e:
        messagebox.showerror("Error", f"Unexpected error: {e}")
    return None
```

---

## 10. Practice Problems

### Problem 1: Calculator GUI
Create a calculator with:
- Number buttons (0-9)
- Operation buttons (+, -, *, /)
- Equals and clear buttons
- Display area showing current calculation

### Problem 2: Text Editor
Implement a basic text editor with:
- File menu (New, Open, Save, Save As)
- Edit menu (Cut, Copy, Paste, Undo)
- Text area with scrollbars
- Status bar showing line/column position

### Problem 3: Contact Manager
Build a contact management system with:
- Add/edit/delete contacts
- Search functionality
- Save/load from file
- Export to CSV

### Problem 4: Drawing Application
Create a simple drawing program with:
- Different drawing tools (pen, line, rectangle, circle)
- Color selection
- Save drawings as images
- Undo/redo functionality

### Problem 5: Database Viewer
Design a GUI for viewing data with:
- Connect to different data sources
- Display data in table format
- Filter and sort capabilities
- Export data functionality

---

## 🎯 Key Takeaways

1. **Event-Driven Programming**: GUI applications respond to user events
2. **Separation of Concerns**: Use MVC pattern to organize code
3. **Error Handling**: Always handle file and user input errors gracefully
4. **User Experience**: Design interfaces that are intuitive and responsive
5. **Code Organization**: Structure GUI code for maintainability and testing

---

## 📚 Additional Resources

- **Python Tkinter Documentation**: Official reference for widgets and methods
- **Real Python GUI Programming**: Comprehensive tutorials and examples
- **Tkinter Tutorials**: Step-by-step guides for common patterns
- **GUI Design Principles**: Resources on user interface design best practices

Remember: Good GUI design combines functional programming with thoughtful user experience design!
