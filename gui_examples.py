#!/usr/bin/env python3
"""
Week 4 GUI Examples - Comprehensive Tkinter Demonstrations
CSC 242 - Object-Oriented Programming

This file contains progressive examples of GUI programming concepts:
1. Basic window and widgets
2. Layout management examples
3. Event handling demonstrations
4. File dialog integration
5. Complex application examples
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import json
import os


class BasicWidgetDemo:
    """Demonstrates basic Tkinter widgets"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Basic Widget Demo")
        self.root.geometry("400x500")
        
        self.setup_widgets()
    
    def setup_widgets(self):
        # Label widget
        title_label = tk.Label(self.root, 
                              text="Tkinter Widget Demonstration",
                              font=("Arial", 16, "bold"),
                              fg="blue")
        title_label.pack(pady=10)
        
        # Entry widget with label
        tk.Label(self.root, text="Enter your name:").pack()
        self.name_entry = tk.Entry(self.root, width=30, font=("Arial", 12))
        self.name_entry.pack(pady=5)
        self.name_entry.bind("<Return>", self.on_name_entered)
        
        # Button
        greet_button = tk.Button(self.root,
                                text="Greet Me!",
                                command=self.greet_user,
                                bg="lightgreen",
                                font=("Arial", 12))
        greet_button.pack(pady=10)
        
        # Text widget with scrollbar
        text_frame = tk.Frame(self.root)
        text_frame.pack(pady=10, padx=20, fill="both", expand=True)
        
        tk.Label(text_frame, text="Multi-line text area:").pack(anchor="w")
        
        # Text widget with scrollbar
        text_container = tk.Frame(text_frame)
        text_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(text_container)
        scrollbar.pack(side="right", fill="y")
        
        self.text_area = tk.Text(text_container, 
                                height=8, 
                                wrap="word",
                                yscrollcommand=scrollbar.set,
                                font=("Courier", 10))
        self.text_area.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.text_area.yview)
        
        # Insert initial text
        self.text_area.insert("1.0", "This is a multi-line text widget.\n")
        self.text_area.insert(tk.END, "You can type here and scroll if needed.\n")
        self.text_area.insert(tk.END, "Try the other widgets above!")
        
        # Checkbutton
        self.check_var = tk.BooleanVar()
        check_button = tk.Checkbutton(self.root,
                                     text="Enable advanced features",
                                     variable=self.check_var,
                                     command=self.on_check_changed)
        check_button.pack(pady=5)
        
        # Radio buttons
        self.radio_var = tk.StringVar(value="option1")
        radio_frame = tk.Frame(self.root)
        radio_frame.pack(pady=5)
        
        tk.Label(radio_frame, text="Choose an option:").pack()
        for i, option in enumerate(["Option 1", "Option 2", "Option 3"], 1):
            radio = tk.Radiobutton(radio_frame,
                                  text=option,
                                  variable=self.radio_var,
                                  value=f"option{i}",
                                  command=self.on_radio_changed)
            radio.pack(anchor="w")
        
        # Scale widget
        tk.Label(self.root, text="Select a value:").pack()
        self.scale = tk.Scale(self.root,
                             from_=0,
                             to=100,
                             orient="horizontal",
                             command=self.on_scale_changed)
        self.scale.set(50)
        self.scale.pack(pady=5)
        
        # Status label
        self.status_label = tk.Label(self.root,
                                    text="Ready",
                                    relief="sunken",
                                    anchor="w")
        self.status_label.pack(fill="x", side="bottom")
    
    def on_name_entered(self, event):
        """Handle Enter key in name entry"""
        self.greet_user()
    
    def greet_user(self):
        """Greet the user with their entered name"""
        name = self.name_entry.get().strip()
        if name:
            greeting = f"Hello, {name}! Welcome to Tkinter!"
            self.text_area.insert(tk.END, f"\n{greeting}")
            self.text_area.see(tk.END)  # Scroll to bottom
            self.status_label.config(text=f"Greeted {name}")
        else:
            messagebox.showwarning("Warning", "Please enter your name first!")
    
    def on_check_changed(self):
        """Handle checkbox state change"""
        state = "enabled" if self.check_var.get() else "disabled"
        self.status_label.config(text=f"Advanced features {state}")
    
    def on_radio_changed(self):
        """Handle radio button selection"""
        selection = self.radio_var.get()
        self.status_label.config(text=f"Selected {selection}")
    
    def on_scale_changed(self, value):
        """Handle scale value change"""
        self.status_label.config(text=f"Scale value: {value}")
    
    def run(self):
        self.root.mainloop()


class LayoutManagerDemo:
    """Demonstrates different layout managers"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Layout Manager Demo")
        self.root.geometry("600x400")
        
        self.create_notebook()
    
    def create_notebook(self):
        """Create tabbed interface for different layout examples"""
        notebook = ttk.Notebook(self.root)
        notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Pack demo
        pack_frame = ttk.Frame(notebook)
        notebook.add(pack_frame, text="Pack Manager")
        self.setup_pack_demo(pack_frame)
        
        # Grid demo
        grid_frame = ttk.Frame(notebook)
        notebook.add(grid_frame, text="Grid Manager")
        self.setup_grid_demo(grid_frame)
        
        # Place demo
        place_frame = ttk.Frame(notebook)
        notebook.add(place_frame, text="Place Manager")
        self.setup_place_demo(place_frame)
    
    def setup_pack_demo(self, parent):
        """Demonstrate pack geometry manager"""
        tk.Label(parent, text="Pack Manager Examples", 
                font=("Arial", 14, "bold")).pack(pady=10)
        
        # Top section
        top_frame = tk.Frame(parent, bg="lightblue", height=50)
        top_frame.pack(side="top", fill="x", padx=5, pady=2)
        tk.Label(top_frame, text="Top (fill=x)", bg="lightblue").pack()
        
        # Bottom section
        bottom_frame = tk.Frame(parent, bg="lightgreen", height=50)
        bottom_frame.pack(side="bottom", fill="x", padx=5, pady=2)
        tk.Label(bottom_frame, text="Bottom (fill=x)", bg="lightgreen").pack()
        
        # Left section
        left_frame = tk.Frame(parent, bg="lightyellow", width=100)
        left_frame.pack(side="left", fill="y", padx=2, pady=5)
        tk.Label(left_frame, text="Left\n(fill=y)", bg="lightyellow").pack()
        
        # Right section
        right_frame = tk.Frame(parent, bg="lightcoral", width=100)
        right_frame.pack(side="right", fill="y", padx=2, pady=5)
        tk.Label(right_frame, text="Right\n(fill=y)", bg="lightcoral").pack()
        
        # Center section
        center_frame = tk.Frame(parent, bg="lightgray")
        center_frame.pack(fill="both", expand=True, padx=5, pady=5)
        tk.Label(center_frame, text="Center (fill=both, expand=True)", 
                bg="lightgray").pack(expand=True)
    
    def setup_grid_demo(self, parent):
        """Demonstrate grid geometry manager"""
        tk.Label(parent, text="Grid Manager Examples", 
                font=("Arial", 14, "bold")).grid(row=0, column=0, columnspan=3, pady=10)
        
        # Create form-like layout
        tk.Label(parent, text="Name:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        name_entry = tk.Entry(parent, width=20)
        name_entry.grid(row=1, column=1, sticky="ew", padx=5, pady=5)
        
        tk.Label(parent, text="Email:").grid(row=2, column=0, sticky="e", padx=5, pady=5)
        email_entry = tk.Entry(parent, width=20)
        email_entry.grid(row=2, column=1, sticky="ew", padx=5, pady=5)
        
        tk.Label(parent, text="Phone:").grid(row=3, column=0, sticky="e", padx=5, pady=5)
        phone_entry = tk.Entry(parent, width=20)
        phone_entry.grid(row=3, column=1, sticky="ew", padx=5, pady=5)
        
        # Buttons spanning multiple columns
        button_frame = tk.Frame(parent)
        button_frame.grid(row=4, column=0, columnspan=3, pady=20)
        
        tk.Button(button_frame, text="Submit").pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear").pack(side="left", padx=5)
        tk.Button(button_frame, text="Cancel").pack(side="left", padx=5)
        
        # Text area spanning multiple rows
        tk.Label(parent, text="Comments:").grid(row=5, column=0, sticky="ne", padx=5, pady=5)
        text_widget = tk.Text(parent, width=30, height=8)
        text_widget.grid(row=5, column=1, columnspan=2, sticky="nsew", padx=5, pady=5)
        
        # Configure grid weights for resizing
        parent.grid_columnconfigure(1, weight=1)
        parent.grid_rowconfigure(5, weight=1)
    
    def setup_place_demo(self, parent):
        """Demonstrate place geometry manager"""
        tk.Label(parent, text="Place Manager Examples", 
                font=("Arial", 14, "bold")).place(x=10, y=10)
        
        # Absolute positioning
        tk.Label(parent, text="Absolute position (x=50, y=50)", 
                bg="yellow").place(x=50, y=50)
        
        # Relative positioning
        tk.Label(parent, text="Center (relx=0.5, rely=0.5)", 
                bg="lightblue").place(relx=0.5, rely=0.5, anchor="center")
        
        # Relative sizing
        tk.Label(parent, text="80% width (relwidth=0.8)", 
                bg="lightgreen").place(relx=0.1, rely=0.7, relwidth=0.8)
        
        # Corner positions
        tk.Label(parent, text="Top-right", bg="pink").place(relx=1.0, y=10, anchor="ne")
        tk.Label(parent, text="Bottom-left", bg="orange").place(x=10, rely=1.0, anchor="sw")
        tk.Label(parent, text="Bottom-right", bg="lightcoral").place(relx=1.0, rely=1.0, anchor="se")
    
    def run(self):
        self.root.mainloop()


class EventHandlingDemo:
    """Demonstrates various event handling techniques"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Event Handling Demo")
        self.root.geometry("500x400")
        
        self.setup_widgets()
        self.bind_events()
    
    def setup_widgets(self):
        # Instructions
        instructions = tk.Label(self.root,
                               text="Event Handling Demonstration\n" +
                                    "Try clicking, typing, and moving the mouse",
                               font=("Arial", 12),
                               justify="center")
        instructions.pack(pady=10)
        
        # Canvas for drawing
        self.canvas = tk.Canvas(self.root, width=400, height=250, bg="white")
        self.canvas.pack(pady=10)
        
        # Event log
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="Event Log:").pack(anchor="w")
        
        # Log text area with scrollbar
        log_container = tk.Frame(log_frame)
        log_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side="right", fill="y")
        
        self.log_text = tk.Text(log_container,
                               height=6,
                               yscrollcommand=scrollbar.set,
                               font=("Courier", 9))
        self.log_text.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.log_text.yview)
        
        # Control buttons
        button_frame = tk.Frame(self.root)
        button_frame.pack(pady=5)
        
        tk.Button(button_frame, text="Clear Canvas", 
                 command=self.clear_canvas).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear Log", 
                 command=self.clear_log).pack(side="left", padx=5)
    
    def bind_events(self):
        """Bind various events to handlers"""
        # Mouse events on canvas
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        self.canvas.bind("<Double-Button-1>", self.on_double_click)
        self.canvas.bind("<B1-Motion>", self.on_drag)
        self.canvas.bind("<Motion>", self.on_mouse_move)
        self.canvas.bind("<Enter>", self.on_mouse_enter)
        self.canvas.bind("<Leave>", self.on_mouse_leave)
        
        # Keyboard events
        self.canvas.bind("<KeyPress>", self.on_key_press)
        self.canvas.bind("<Key-Escape>", self.on_escape_key)
        
        # Make canvas focusable for keyboard events
        self.canvas.focus_set()
        
        # Window events
        self.root.bind("<Configure>", self.on_window_resize)
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)
        
        # Track variables for drawing
        self.last_x = None
        self.last_y = None
        self.drawing = False
    
    def log_event(self, message):
        """Add event to log"""
        self.log_text.insert(tk.END, f"{message}\n")
        self.log_text.see(tk.END)
    
    def on_left_click(self, event):
        """Handle left mouse click"""
        self.log_event(f"Left click at ({event.x}, {event.y})")
        self.canvas.create_oval(event.x-3, event.y-3, event.x+3, event.y+3, 
                               fill="red", outline="darkred")
        self.last_x, self.last_y = event.x, event.y
        self.drawing = True
    
    def on_right_click(self, event):
        """Handle right mouse click"""
        self.log_event(f"Right click at ({event.x}, {event.y})")
        self.canvas.create_rectangle(event.x-10, event.y-10, event.x+10, event.y+10,
                                   fill="blue", outline="darkblue")
    
    def on_double_click(self, event):
        """Handle double click"""
        self.log_event(f"Double click at ({event.x}, {event.y})")
        self.canvas.create_text(event.x, event.y, text="Double!", 
                               fill="green", font=("Arial", 12, "bold"))
    
    def on_drag(self, event):
        """Handle mouse drag (drawing)"""
        if self.drawing and self.last_x and self.last_y:
            self.canvas.create_line(self.last_x, self.last_y, event.x, event.y,
                                   fill="black", width=2)
            self.last_x, self.last_y = event.x, event.y
    
    def on_mouse_move(self, event):
        """Handle mouse movement (update coordinates)"""
        # Only log occasionally to avoid spam
        pass
    
    def on_mouse_enter(self, event):
        """Handle mouse entering canvas"""
        self.log_event("Mouse entered canvas")
        self.canvas.config(cursor="crosshair")
    
    def on_mouse_leave(self, event):
        """Handle mouse leaving canvas"""
        self.log_event("Mouse left canvas")
        self.canvas.config(cursor="")
        self.drawing = False
    
    def on_key_press(self, event):
        """Handle key press"""
        self.log_event(f"Key pressed: {event.keysym} ('{event.char}')")
        
        # Special key handling
        if event.keysym == "space":
            self.clear_canvas()
        elif event.keysym == "c":
            self.canvas.config(bg="lightcyan")
        elif event.keysym == "w":
            self.canvas.config(bg="white")
    
    def on_escape_key(self, event):
        """Handle Escape key"""
        self.log_event("Escape key pressed - clearing selection")
        self.drawing = False
    
    def on_window_resize(self, event):
        """Handle window resize"""
        if event.widget == self.root:  # Only log main window resize
            self.log_event(f"Window resized to {event.width}x{event.height}")
    
    def on_window_close(self):
        """Handle window close"""
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.log_event("Application closing...")
            self.root.destroy()
    
    def clear_canvas(self):
        """Clear the canvas"""
        self.canvas.delete("all")
        self.log_event("Canvas cleared")
    
    def clear_log(self):
        """Clear the event log"""
        self.log_text.delete("1.0", tk.END)
    
    def run(self):
        self.root.mainloop()


class FileDialogDemo:
    """Demonstrates file dialogs and file operations"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Dialog Demo")
        self.root.geometry("600x500")
        
        self.current_filename = None
        self.setup_widgets()
    
    def setup_widgets(self):
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file, accelerator="Ctrl+N")
        file_menu.add_command(label="Open", command=self.open_file, accelerator="Ctrl+O")
        file_menu.add_command(label="Save", command=self.save_file, accelerator="Ctrl+S")
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Keyboard shortcuts
        self.root.bind("<Control-n>", lambda e: self.new_file())
        self.root.bind("<Control-o>", lambda e: self.open_file())
        self.root.bind("<Control-s>", lambda e: self.save_file())
        
        # Toolbar
        toolbar = tk.Frame(self.root, relief="raised", borderwidth=1)
        toolbar.pack(fill="x")
        
        tk.Button(toolbar, text="New", command=self.new_file).pack(side="left", padx=2)
        tk.Button(toolbar, text="Open", command=self.open_file).pack(side="left", padx=2)
        tk.Button(toolbar, text="Save", command=self.save_file).pack(side="left", padx=2)
        tk.Button(toolbar, text="Save As", command=self.save_as_file).pack(side="left", padx=2)
        
        # Separator
        separator = tk.Frame(toolbar, width=2, bg="gray")
        separator.pack(side="left", fill="y", padx=5)
        
        tk.Button(toolbar, text="Open Image", command=self.open_image).pack(side="left", padx=2)
        tk.Button(toolbar, text="Choose Color", command=self.choose_color).pack(side="left", padx=2)
        
        # Main text area
        text_frame = tk.Frame(self.root)
        text_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Text widget with scrollbars
        text_scroll_frame = tk.Frame(text_frame)
        text_scroll_frame.pack(fill="both", expand=True)
        
        # Vertical scrollbar
        v_scrollbar = tk.Scrollbar(text_scroll_frame)
        v_scrollbar.pack(side="right", fill="y")
        
        # Horizontal scrollbar
        h_scrollbar = tk.Scrollbar(text_scroll_frame, orient="horizontal")
        h_scrollbar.pack(side="bottom", fill="x")
        
        # Text widget
        self.text_area = tk.Text(text_scroll_frame,
                                wrap="none",
                                yscrollcommand=v_scrollbar.set,
                                xscrollcommand=h_scrollbar.set,
                                font=("Courier", 11),
                                undo=True)
        self.text_area.pack(fill="both", expand=True)
        
        v_scrollbar.config(command=self.text_area.yview)
        h_scrollbar.config(command=self.text_area.xview)
        
        # Status bar
        self.status_bar = tk.Label(self.root,
                                  text="Ready",
                                  relief="sunken",
                                  anchor="w")
        self.status_bar.pack(fill="x", side="bottom")
        
        # Track changes
        self.text_area.bind("<KeyPress>", self.on_text_change)
        self.text_area.bind("<Button-1>", self.update_cursor_position)
        self.text_area.bind("<KeyRelease>", self.update_cursor_position)
        
        self.is_modified = False
        self.update_title()
    
    def new_file(self):
        """Create a new file"""
        if self.check_save_changes():
            self.text_area.delete("1.0", tk.END)
            self.current_filename = None
            self.is_modified = False
            self.update_title()
            self.status_bar.config(text="New file created")
    
    def open_file(self):
        """Open an existing file"""
        if not self.check_save_changes():
            return
        
        filename = filedialog.askopenfilename(
            title="Open File",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                with open(filename, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.text_area.delete("1.0", tk.END)
                self.text_area.insert("1.0", content)
                
                self.current_filename = filename
                self.is_modified = False
                self.update_title()
                self.status_bar.config(text=f"Opened: {os.path.basename(filename)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")
    
    def save_file(self):
        """Save the current file"""
        if self.current_filename:
            self.save_to_file(self.current_filename)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save file with a new name"""
        filename = filedialog.asksaveasfilename(
            title="Save File As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            self.save_to_file(filename)
            self.current_filename = filename
            self.update_title()
    
    def save_to_file(self, filename):
        """Save content to specified file"""
        try:
            content = self.text_area.get("1.0", tk.END)
            with open(filename, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.is_modified = False
            self.update_title()
            self.status_bar.config(text=f"Saved: {os.path.basename(filename)}")
            
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
    
    def open_image(self):
        """Open and display image information"""
        filename = filedialog.askopenfilename(
            title="Open Image",
            filetypes=[
                ("Image files", "*.png *.jpg *.jpeg *.gif *.bmp"),
                ("PNG files", "*.png"),
                ("JPEG files", "*.jpg *.jpeg"),
                ("All files", "*.*")
            ]
        )
        
        if filename:
            try:
                file_size = os.path.getsize(filename)
                info = f"Selected image: {os.path.basename(filename)}\n"
                info += f"Full path: {filename}\n"
                info += f"File size: {file_size:,} bytes\n"
                
                self.text_area.insert(tk.END, f"\n{info}\n")
                self.status_bar.config(text=f"Image info added: {os.path.basename(filename)}")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not process image:\n{e}")
    
    def choose_color(self):
        """Choose a color and insert color information"""
        color = colorchooser.askcolor(title="Choose a color")
        
        if color[1]:  # color[1] is the hex value
            rgb = color[0]  # RGB tuple
            hex_color = color[1]  # Hex string
            
            color_info = f"\nSelected color:\n"
            color_info += f"RGB: ({int(rgb[0])}, {int(rgb[1])}, {int(rgb[2])})\n"
            color_info += f"Hex: {hex_color}\n"
            
            self.text_area.insert(tk.END, color_info)
            self.status_bar.config(text=f"Color added: {hex_color}")
    
    def check_save_changes(self):
        """Check if user wants to save changes before continuing"""
        if self.is_modified:
            result = messagebox.askyesnocancel(
                "Save Changes",
                "Do you want to save changes to the current document?"
            )
            
            if result is True:  # Yes
                self.save_file()
                return True
            elif result is False:  # No
                return True
            else:  # Cancel
                return False
        
        return True
    
    def on_text_change(self, event):
        """Handle text changes"""
        self.is_modified = True
        self.update_title()
    
    def update_cursor_position(self, event=None):
        """Update cursor position in status bar"""
        self.root.after_idle(self._update_cursor_position)
    
    def _update_cursor_position(self):
        """Internal method to update cursor position"""
        cursor_pos = self.text_area.index(tk.INSERT)
        line, col = cursor_pos.split('.')
        self.status_bar.config(text=f"Line: {line}, Column: {int(col)+1}")
    
    def update_title(self):
        """Update window title"""
        title = "File Dialog Demo"
        
        if self.current_filename:
            title += f" - {os.path.basename(self.current_filename)}"
        else:
            title += " - Untitled"
        
        if self.is_modified:
            title += " *"
        
        self.root.title(title)
    
    def run(self):
        self.root.mainloop()


class AdvancedGUIDemo:
    """Demonstrates advanced GUI patterns and techniques"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Advanced GUI Demo")
        self.root.geometry("700x600")
        
        self.data = []
        self.setup_widgets()
        self.load_sample_data()
    
    def setup_widgets(self):
        # Create notebook for tabs
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(fill="both", expand=True, padx=10, pady=10)
        
        # Data management tab
        self.setup_data_tab()
        
        # Settings tab
        self.setup_settings_tab()
        
        # About tab
        self.setup_about_tab()
    
    def setup_data_tab(self):
        """Setup data management tab"""
        data_frame = ttk.Frame(self.notebook)
        self.notebook.add(data_frame, text="Data Management")
        
        # Input section
        input_frame = tk.LabelFrame(data_frame, text="Add New Entry", padx=10, pady=10)
        input_frame.pack(fill="x", padx=10, pady=5)
        
        # Form fields
        tk.Label(input_frame, text="Name:").grid(row=0, column=0, sticky="e", padx=5, pady=5)
        self.name_entry = tk.Entry(input_frame, width=20)
        self.name_entry.grid(row=0, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Age:").grid(row=0, column=2, sticky="e", padx=5, pady=5)
        self.age_entry = tk.Entry(input_frame, width=10)
        self.age_entry.grid(row=0, column=3, padx=5, pady=5)
        
        tk.Label(input_frame, text="City:").grid(row=1, column=0, sticky="e", padx=5, pady=5)
        self.city_entry = tk.Entry(input_frame, width=20)
        self.city_entry.grid(row=1, column=1, padx=5, pady=5)
        
        tk.Label(input_frame, text="Email:").grid(row=1, column=2, sticky="e", padx=5, pady=5)
        self.email_entry = tk.Entry(input_frame, width=25)
        self.email_entry.grid(row=1, column=3, padx=5, pady=5)
        
        # Buttons
        button_frame = tk.Frame(input_frame)
        button_frame.grid(row=2, column=0, columnspan=4, pady=10)
        
        tk.Button(button_frame, text="Add Entry", command=self.add_entry).pack(side="left", padx=5)
        tk.Button(button_frame, text="Update Selected", command=self.update_entry).pack(side="left", padx=5)
        tk.Button(button_frame, text="Delete Selected", command=self.delete_entry).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear Form", command=self.clear_form).pack(side="left", padx=5)
        
        # Data display section
        display_frame = tk.LabelFrame(data_frame, text="Data Entries", padx=10, pady=10)
        display_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        # Treeview for data display
        columns = ("Name", "Age", "City", "Email")
        self.tree = ttk.Treeview(display_frame, columns=columns, show="headings", height=15)
        
        # Define column headings and widths
        self.tree.heading("Name", text="Name")
        self.tree.heading("Age", text="Age")
        self.tree.heading("City", text="City")
        self.tree.heading("Email", text="Email")
        
        self.tree.column("Name", width=120)
        self.tree.column("Age", width=60)
        self.tree.column("City", width=120)
        self.tree.column("Email", width=200)
        
        # Scrollbars for treeview
        tree_scroll_y = ttk.Scrollbar(display_frame, orient="vertical", command=self.tree.yview)
        tree_scroll_x = ttk.Scrollbar(display_frame, orient="horizontal", command=self.tree.xview)
        self.tree.configure(yscrollcommand=tree_scroll_y.set, xscrollcommand=tree_scroll_x.set)
        
        # Pack treeview and scrollbars
        self.tree.grid(row=0, column=0, sticky="nsew")
        tree_scroll_y.grid(row=0, column=1, sticky="ns")
        tree_scroll_x.grid(row=1, column=0, sticky="ew")
        
        display_frame.grid_rowconfigure(0, weight=1)
        display_frame.grid_columnconfigure(0, weight=1)
        
        # Bind treeview selection
        self.tree.bind("<<TreeviewSelect>>", self.on_tree_select)
        
        # Control buttons
        control_frame = tk.Frame(data_frame)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(control_frame, text="Load from JSON", command=self.load_from_json).pack(side="left", padx=5)
        tk.Button(control_frame, text="Save to JSON", command=self.save_to_json).pack(side="left", padx=5)
        tk.Button(control_frame, text="Export to CSV", command=self.export_to_csv).pack(side="left", padx=5)
        tk.Button(control_frame, text="Clear All Data", command=self.clear_all_data).pack(side="right", padx=5)
    
    def setup_settings_tab(self):
        """Setup settings/preferences tab"""
        settings_frame = ttk.Frame(self.notebook)
        self.notebook.add(settings_frame, text="Settings")
        
        # Theme selection
        theme_frame = tk.LabelFrame(settings_frame, text="Appearance", padx=10, pady=10)
        theme_frame.pack(fill="x", padx=10, pady=10)
        
        self.theme_var = tk.StringVar(value="Default")
        themes = ["Default", "Dark", "Light", "Blue"]
        
        tk.Label(theme_frame, text="Theme:").pack(anchor="w")
        for theme in themes:
            tk.Radiobutton(theme_frame, text=theme, variable=self.theme_var, 
                          value=theme, command=self.change_theme).pack(anchor="w")
        
        # Font settings
        font_frame = tk.LabelFrame(settings_frame, text="Font Settings", padx=10, pady=10)
        font_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(font_frame, text="Font Size:").pack(anchor="w")
        self.font_size = tk.IntVar(value=10)
        font_scale = tk.Scale(font_frame, from_=8, to=16, orient="horizontal", 
                             variable=self.font_size, command=self.change_font_size)
        font_scale.pack(fill="x")
        
        # Application settings
        app_frame = tk.LabelFrame(settings_frame, text="Application Settings", padx=10, pady=10)
        app_frame.pack(fill="x", padx=10, pady=10)
        
        self.auto_save_var = tk.BooleanVar(value=True)
        tk.Checkbutton(app_frame, text="Auto-save data", 
                      variable=self.auto_save_var).pack(anchor="w")
        
        self.confirm_delete_var = tk.BooleanVar(value=True)
        tk.Checkbutton(app_frame, text="Confirm before deleting", 
                      variable=self.confirm_delete_var).pack(anchor="w")
        
        self.show_tooltips_var = tk.BooleanVar(value=True)
        tk.Checkbutton(app_frame, text="Show tooltips", 
                      variable=self.show_tooltips_var).pack(anchor="w")
    
    def setup_about_tab(self):
        """Setup about/info tab"""
        about_frame = ttk.Frame(self.notebook)
        self.notebook.add(about_frame, text="About")
        
        # Application info
        info_text = """
Advanced GUI Demo Application
Version 1.0

This application demonstrates various advanced GUI programming concepts including:

• Tabbed interfaces using ttk.Notebook
• Treeview widgets for data display
• File dialogs for import/export
• Settings and preferences management
• Dynamic theme changing
• Data validation and error handling
• Model-View separation

Built with Python and Tkinter

Features:
- Add, edit, and delete data entries
- Import/export data in JSON and CSV formats
- Customizable appearance and settings
- Comprehensive error handling
- User-friendly interface design

© 2024 CSC 242 - Object-Oriented Programming
        """
        
        text_widget = tk.Text(about_frame, wrap="word", font=("Arial", 11))
        text_widget.pack(fill="both", expand=True, padx=20, pady=20)
        text_widget.insert("1.0", info_text)
        text_widget.config(state="disabled")  # Make read-only
    
    def load_sample_data(self):
        """Load some sample data"""
        sample_data = [
            {"name": "Alice Johnson", "age": 28, "city": "New York", "email": "alice@email.com"},
            {"name": "Bob Smith", "age": 34, "city": "Los Angeles", "email": "bob@email.com"},
            {"name": "Carol Davis", "age": 22, "city": "Chicago", "email": "carol@email.com"},
            {"name": "David Wilson", "age": 45, "city": "Houston", "email": "david@email.com"},
        ]
        
        for entry in sample_data:
            self.data.append(entry)
        
        self.refresh_tree()
    
    def add_entry(self):
        """Add a new data entry"""
        # Get form data
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        city = self.city_entry.get().strip()
        email = self.email_entry.get().strip()
        
        # Validate input
        if not name:
            messagebox.showerror("Error", "Name is required")
            return
        
        try:
            age = int(age_str) if age_str else 0
            if age < 0 or age > 150:
                raise ValueError("Age must be between 0 and 150")
        except ValueError as e:
            messagebox.showerror("Error", f"Invalid age: {e}")
            return
        
        if not city:
            messagebox.showerror("Error", "City is required")
            return
        
        if email and "@" not in email:
            messagebox.showerror("Error", "Invalid email format")
            return
        
        # Add to data
        entry = {
            "name": name,
            "age": age,
            "city": city,
            "email": email
        }
        
        self.data.append(entry)
        self.refresh_tree()
        self.clear_form()
        
        messagebox.showinfo("Success", "Entry added successfully")
    
    def update_entry(self):
        """Update selected entry"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an entry to update")
            return
        
        # Get selected index
        item = selection[0]
        index = self.tree.index(item)
        
        # Get form data and validate (same as add_entry)
        name = self.name_entry.get().strip()
        age_str = self.age_entry.get().strip()
        city = self.city_entry.get().strip()
        email = self.email_entry.get().strip()
        
        if not name or not city:
            messagebox.showerror("Error", "Name and city are required")
            return
        
        try:
            age = int(age_str) if age_str else 0
        except ValueError:
            messagebox.showerror("Error", "Invalid age")
            return
        
        # Update data
        self.data[index] = {
            "name": name,
            "age": age,
            "city": city,
            "email": email
        }
        
        self.refresh_tree()
        self.clear_form()
        messagebox.showinfo("Success", "Entry updated successfully")
    
    def delete_entry(self):
        """Delete selected entry"""
        selection = self.tree.selection()
        if not selection:
            messagebox.showwarning("Warning", "Please select an entry to delete")
            return
        
        if self.confirm_delete_var.get():
            if not messagebox.askyesno("Confirm Delete", "Delete selected entry?"):
                return
        
        # Get selected index and delete
        item = selection[0]
        index = self.tree.index(item)
        del self.data[index]
        
        self.refresh_tree()
        self.clear_form()
        messagebox.showinfo("Success", "Entry deleted successfully")
    
    def clear_form(self):
        """Clear all form fields"""
        self.name_entry.delete(0, tk.END)
        self.age_entry.delete(0, tk.END)
        self.city_entry.delete(0, tk.END)
        self.email_entry.delete(0, tk.END)
    
    def clear_all_data(self):
        """Clear all data entries"""
        if messagebox.askyesno("Confirm Clear", "Delete all data entries?"):
            self.data.clear()
            self.refresh_tree()
            messagebox.showinfo("Success", "All data cleared")
    
    def on_tree_select(self, event):
        """Handle tree selection - populate form"""
        selection = self.tree.selection()
        if selection:
            item = selection[0]
            index = self.tree.index(item)
            entry = self.data[index]
            
            # Populate form
            self.clear_form()
            self.name_entry.insert(0, entry["name"])
            self.age_entry.insert(0, str(entry["age"]))
            self.city_entry.insert(0, entry["city"])
            self.email_entry.insert(0, entry["email"])
    
    def refresh_tree(self):
        """Refresh the treeview with current data"""
        # Clear existing items
        for item in self.tree.get_children():
            self.tree.delete(item)
        
        # Add current data
        for entry in self.data:
            self.tree.insert("", "end", values=(
                entry["name"],
                entry["age"],
                entry["city"],
                entry["email"]
            ))
    
    def load_from_json(self):
        """Load data from JSON file"""
        filename = filedialog.askopenfilename(
            title="Load Data",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'r') as file:
                    loaded_data = json.load(file)
                
                if isinstance(loaded_data, list):
                    self.data = loaded_data
                    self.refresh_tree()
                    messagebox.showinfo("Success", f"Loaded {len(self.data)} entries")
                else:
                    messagebox.showerror("Error", "Invalid JSON format")
                    
            except Exception as e:
                messagebox.showerror("Error", f"Could not load file:\n{e}")
    
    def save_to_json(self):
        """Save data to JSON file"""
        filename = filedialog.asksaveasfilename(
            title="Save Data",
            defaultextension=".json",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                with open(filename, 'w') as file:
                    json.dump(self.data, file, indent=2)
                
                messagebox.showinfo("Success", f"Saved {len(self.data)} entries")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not save file:\n{e}")
    
    def export_to_csv(self):
        """Export data to CSV file"""
        filename = filedialog.asksaveasfilename(
            title="Export to CSV",
            defaultextension=".csv",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if filename:
            try:
                import csv
                with open(filename, 'w', newline='') as file:
                    if self.data:
                        fieldnames = self.data[0].keys()
                        writer = csv.DictWriter(file, fieldnames=fieldnames)
                        writer.writeheader()
                        writer.writerows(self.data)
                
                messagebox.showinfo("Success", f"Exported {len(self.data)} entries to CSV")
                
            except Exception as e:
                messagebox.showerror("Error", f"Could not export file:\n{e}")
    
    def change_theme(self):
        """Change application theme"""
        theme = self.theme_var.get()
        
        # This is a simplified theme system
        if theme == "Dark":
            bg_color = "#2b2b2b"
            fg_color = "white"
        elif theme == "Light":
            bg_color = "white"
            fg_color = "black"
        elif theme == "Blue":
            bg_color = "#e6f3ff"
            fg_color = "navy"
        else:  # Default
            bg_color = None
            fg_color = None
        
        # Apply theme (simplified - in real app, would be more comprehensive)
        if bg_color:
            self.root.config(bg=bg_color)
        
        messagebox.showinfo("Theme", f"Theme changed to {theme}")
    
    def change_font_size(self, value):
        """Change application font size"""
        # In a real application, this would update all fonts
        messagebox.showinfo("Font", f"Font size changed to {value}")
    
    def run(self):
        self.root.mainloop()


def main():
    """Main function to demonstrate all GUI examples"""
    print("GUI Programming Examples")
    print("========================")
    print("1. Basic Widget Demo")
    print("2. Layout Manager Demo")
    print("3. Event Handling Demo")
    print("4. File Dialog Demo")
    print("5. Advanced GUI Demo")
    print("6. Run All Demos")
    
    choice = input("\nEnter your choice (1-6): ").strip()
    
    if choice == "1":
        app = BasicWidgetDemo()
        app.run()
    elif choice == "2":
        app = LayoutManagerDemo()
        app.run()
    elif choice == "3":
        app = EventHandlingDemo()
        app.run()
    elif choice == "4":
        app = FileDialogDemo()
        app.run()
    elif choice == "5":
        app = AdvancedGUIDemo()
        app.run()
    elif choice == "6":
        # Run demos sequentially
        demos = [
            ("Basic Widgets", BasicWidgetDemo),
            ("Layout Managers", LayoutManagerDemo),
            ("Event Handling", EventHandlingDemo),
            ("File Dialogs", FileDialogDemo),
            ("Advanced GUI", AdvancedGUIDemo)
        ]
        
        for name, demo_class in demos:
            print(f"\nRunning {name} demo...")
            app = demo_class()
            app.run()
    else:
        print("Invalid choice. Please run the script again.")


if __name__ == "__main__":
    main()
