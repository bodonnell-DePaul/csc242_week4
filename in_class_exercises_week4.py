#!/usr/bin/env python3
"""
Week 4 In-Class Exercises - GUI Programming, Event Handling, and File I/O
CSC 242 - Object-Oriented Programming

These exercises provide hands-on practice with:
1. Creating GUI applications with Tkinter
2. Handling user events (mouse, keyboard, window)
3. File input/output operations
4. Error handling and validation
5. Integrating multiple concepts

Each exercise builds on previous concepts and introduces new challenges.
"""

import tkinter as tk
from tkinter import ttk, messagebox, filedialog, colorchooser
import json
import csv
from pathlib import Path
import random
import time
from datetime import datetime


# ============================================================================
# EXERCISE 1: BASIC GUI CALCULATOR
# ============================================================================

class Calculator:
    """
    Exercise 1: Create a basic calculator GUI
    
    Requirements:
    - Number buttons (0-9)
    - Operation buttons (+, -, *, /)
    - Equals button and clear button
    - Display area showing current calculation
    - Handle basic arithmetic operations
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculator")
        self.root.geometry("300x400")
        
        # TODO: Initialize calculator state variables
        self.current_input = ""
        self.operation = None
        self.previous_value = None
        self.result = 0
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Setup calculator widgets"""
        # TODO: Create display area (Entry widget or Label)
        # Hint: Use a StringVar to track display content
        self.display_var = tk.StringVar(value="0")
        display = tk.Entry(self.root, 
                          textvariable=self.display_var,
                          font=("Arial", 16),
                          justify="right",
                          state="readonly")
        display.pack(fill="x", padx=10, pady=10)
        
        # TODO: Create button frame
        button_frame = tk.Frame(self.root)
        button_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # TODO: Create buttons using grid layout
        # Numbers: 0-9
        # Operations: +, -, *, /
        # Special: =, C (clear)
        
        # Button layout design:
        # Row 0: [C] [ ] [ ] [/]
        # Row 1: [7] [8] [9] [*]
        # Row 2: [4] [5] [6] [-]
        # Row 3: [1] [2] [3] [+]
        # Row 4: [0] [ ] [ ] [=]
        
        # Create buttons (students should implement this)
        buttons = [
            ('C', 0, 0), ('/', 0, 3),
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('*', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('-', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('+', 3, 3),
            ('0', 4, 0), ('=', 4, 3)
        ]
        
        for (text, row, col) in buttons:
            if text == '0':
                # Make 0 button span 3 columns
                btn = tk.Button(button_frame, text=text, 
                               command=lambda t=text: self.button_click(t),
                               font=("Arial", 14))
                btn.grid(row=row, column=col, columnspan=3, sticky="ew", padx=2, pady=2)
            else:
                btn = tk.Button(button_frame, text=text, 
                               command=lambda t=text: self.button_click(t),
                               font=("Arial", 14))
                btn.grid(row=row, column=col, sticky="ew", padx=2, pady=2)
        
        # Configure grid weights
        for i in range(4):
            button_frame.grid_columnconfigure(i, weight=1)
        for i in range(5):
            button_frame.grid_rowconfigure(i, weight=1)
    
    def button_click(self, value):
        """Handle button clicks"""
        # TODO: Implement button click logic
        # Handle numbers, operations, equals, and clear
        pass  # Students implement this
    
    def calculate(self):
        """Perform calculation"""
        # TODO: Implement calculation logic
        pass  # Students implement this
    
    def clear(self):
        """Clear calculator"""
        # TODO: Reset calculator state
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# EXERCISE 2: DRAWING APPLICATION
# ============================================================================

class DrawingApp:
    """
    Exercise 2: Create a simple drawing application
    
    Requirements:
    - Canvas area for drawing
    - Different drawing tools (pen, line, rectangle, circle)
    - Color selection
    - Clear canvas button
    - Mouse event handling for drawing
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Drawing Application")
        self.root.geometry("800x600")
        
        # TODO: Initialize drawing state
        self.current_tool = "pen"
        self.current_color = "black"
        self.drawing = False
        self.last_x = None
        self.last_y = None
        
        self.setup_widgets()
        self.bind_events()
    
    def setup_widgets(self):
        """Setup drawing application widgets"""
        # TODO: Create toolbar with tool buttons and color selection
        toolbar = tk.Frame(self.root, relief="raised", borderwidth=1)
        toolbar.pack(fill="x")
        
        # Tool buttons
        tools = ["pen", "line", "rectangle", "circle"]
        for tool in tools:
            btn = tk.Button(toolbar, text=tool.title(), 
                           command=lambda t=tool: self.set_tool(t))
            btn.pack(side="left", padx=2)
        
        # Color button
        tk.Button(toolbar, text="Color", 
                 command=self.choose_color).pack(side="left", padx=10)
        
        # Clear button
        tk.Button(toolbar, text="Clear", 
                 command=self.clear_canvas).pack(side="right", padx=2)
        
        # TODO: Create canvas for drawing
        self.canvas = tk.Canvas(self.root, bg="white")
        self.canvas.pack(fill="both", expand=True)
    
    def bind_events(self):
        """Bind mouse events for drawing"""
        # TODO: Bind mouse events to canvas
        # Handle mouse press, release, and motion
        pass  # Students implement this
    
    def set_tool(self, tool):
        """Set current drawing tool"""
        # TODO: Update current tool
        pass  # Students implement this
    
    def choose_color(self):
        """Open color chooser dialog"""
        # TODO: Use colorchooser to select color
        pass  # Students implement this
    
    def on_mouse_press(self, event):
        """Handle mouse press events"""
        # TODO: Start drawing based on current tool
        pass  # Students implement this
    
    def on_mouse_drag(self, event):
        """Handle mouse drag events"""
        # TODO: Continue drawing based on current tool
        pass  # Students implement this
    
    def on_mouse_release(self, event):
        """Handle mouse release events"""
        # TODO: Finish drawing based on current tool
        pass  # Students implement this
    
    def clear_canvas(self):
        """Clear the canvas"""
        # TODO: Remove all drawings from canvas
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# EXERCISE 3: TEXT EDITOR WITH FILE OPERATIONS
# ============================================================================

class TextEditor:
    """
    Exercise 3: Create a text editor with file operations
    
    Requirements:
    - Text area for editing
    - File menu (New, Open, Save, Save As, Exit)
    - Edit menu (Cut, Copy, Paste, Undo)
    - Status bar showing file info
    - Handle text changes and prompt for save
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Text Editor")
        self.root.geometry("700x500")
        
        # TODO: Initialize editor state
        self.current_file = None
        self.is_modified = False
        
        self.setup_widgets()
        self.setup_menu()
    
    def setup_widgets(self):
        """Setup text editor widgets"""
        # TODO: Create text area with scrollbars
        self.text_area = tk.Text(self.root, font=("Courier", 11), undo=True)
        
        # Add scrollbars
        v_scrollbar = tk.Scrollbar(self.root, orient="vertical", command=self.text_area.yview)
        h_scrollbar = tk.Scrollbar(self.root, orient="horizontal", command=self.text_area.xview)
        
        self.text_area.config(yscrollcommand=v_scrollbar.set, xscrollcommand=h_scrollbar.set)
        
        # Pack widgets
        self.text_area.pack(side="left", fill="both", expand=True)
        v_scrollbar.pack(side="right", fill="y")
        h_scrollbar.pack(side="bottom", fill="x")
        
        # TODO: Create status bar
        self.status_bar = tk.Label(self.root, text="Ready", relief="sunken", anchor="w")
        self.status_bar.pack(fill="x", side="bottom")
        
        # TODO: Bind text change events
        self.text_area.bind("<KeyPress>", self.on_text_change)
    
    def setup_menu(self):
        """Setup menu bar"""
        # TODO: Create menu bar with File and Edit menus
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        # File menu
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open", command=self.open_file)
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.exit_application)
        
        # Edit menu
        edit_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Cut", command=self.cut_text)
        edit_menu.add_command(label="Copy", command=self.copy_text)
        edit_menu.add_command(label="Paste", command=self.paste_text)
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo", command=self.undo_text)
    
    def new_file(self):
        """Create new file"""
        # TODO: Check for unsaved changes, then clear text area
        pass  # Students implement this
    
    def open_file(self):
        """Open file dialog and load file"""
        # TODO: Use filedialog to select and open file
        pass  # Students implement this
    
    def save_file(self):
        """Save current file"""
        # TODO: Save to current file or prompt for filename
        pass  # Students implement this
    
    def save_as_file(self):
        """Save file with new name"""
        # TODO: Use filedialog to get new filename and save
        pass  # Students implement this
    
    def cut_text(self):
        """Cut selected text"""
        # TODO: Implement cut operation
        pass  # Students implement this
    
    def copy_text(self):
        """Copy selected text"""
        # TODO: Implement copy operation
        pass  # Students implement this
    
    def paste_text(self):
        """Paste text from clipboard"""
        # TODO: Implement paste operation
        pass  # Students implement this
    
    def undo_text(self):
        """Undo last operation"""
        # TODO: Implement undo operation
        pass  # Students implement this
    
    def on_text_change(self, event):
        """Handle text changes"""
        # TODO: Mark file as modified and update title
        pass  # Students implement this
    
    def check_save_changes(self):
        """Check if user wants to save changes"""
        # TODO: Prompt user to save if file is modified
        pass  # Students implement this
    
    def exit_application(self):
        """Exit the application"""
        # TODO: Check for unsaved changes before exiting
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# EXERCISE 4: CONTACT MANAGER
# ============================================================================

class ContactManager:
    """
    Exercise 4: Create a contact management system
    
    Requirements:
    - Add, edit, delete contacts
    - Search functionality
    - Display contacts in a list
    - Save/load contacts from JSON file
    - Form validation
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Contact Manager")
        self.root.geometry("800x600")
        
        # TODO: Initialize contact data
        self.contacts = []
        self.current_contact_index = None
        
        self.setup_widgets()
        self.load_contacts()
    
    def setup_widgets(self):
        """Setup contact manager widgets"""
        # TODO: Create main layout with contact list and form
        
        # Left panel - contact list
        left_panel = tk.Frame(self.root)
        left_panel.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        tk.Label(left_panel, text="Contacts", font=("Arial", 14, "bold")).pack()
        
        # Search frame
        search_frame = tk.Frame(left_panel)
        search_frame.pack(fill="x", pady=5)
        tk.Label(search_frame, text="Search:").pack(side="left")
        self.search_var = tk.StringVar()
        search_entry = tk.Entry(search_frame, textvariable=self.search_var)
        search_entry.pack(side="left", fill="x", expand=True, padx=5)
        search_entry.bind("<KeyRelease>", self.on_search)
        
        # Contact listbox
        self.contact_listbox = tk.Listbox(left_panel)
        self.contact_listbox.pack(fill="both", expand=True, pady=5)
        self.contact_listbox.bind("<<ListboxSelect>>", self.on_contact_select)
        
        # Right panel - contact form
        right_panel = tk.Frame(self.root)
        right_panel.pack(side="right", fill="both", padx=5, pady=5)
        
        tk.Label(right_panel, text="Contact Details", font=("Arial", 14, "bold")).pack()
        
        # Form fields
        form_frame = tk.Frame(right_panel)
        form_frame.pack(fill="x", pady=10)
        
        # TODO: Create form fields (name, email, phone, address)
        fields = ["Name", "Email", "Phone", "Address"]
        self.form_vars = {}
        
        for i, field in enumerate(fields):
            tk.Label(form_frame, text=f"{field}:").grid(row=i, column=0, sticky="e", padx=5, pady=5)
            var = tk.StringVar()
            entry = tk.Entry(form_frame, textvariable=var, width=30)
            entry.grid(row=i, column=1, padx=5, pady=5)
            self.form_vars[field.lower()] = var
        
        # Buttons
        button_frame = tk.Frame(right_panel)
        button_frame.pack(fill="x", pady=10)
        
        tk.Button(button_frame, text="Add", command=self.add_contact).pack(side="left", padx=5)
        tk.Button(button_frame, text="Update", command=self.update_contact).pack(side="left", padx=5)
        tk.Button(button_frame, text="Delete", command=self.delete_contact).pack(side="left", padx=5)
        tk.Button(button_frame, text="Clear", command=self.clear_form).pack(side="left", padx=5)
        
        # File operations
        file_frame = tk.Frame(right_panel)
        file_frame.pack(fill="x", pady=10)
        
        tk.Button(file_frame, text="Load", command=self.load_contacts).pack(side="left", padx=5)
        tk.Button(file_frame, text="Save", command=self.save_contacts).pack(side="left", padx=5)
    
    def add_contact(self):
        """Add new contact"""
        # TODO: Validate form and add contact to list
        pass  # Students implement this
    
    def update_contact(self):
        """Update selected contact"""
        # TODO: Update contact with form data
        pass  # Students implement this
    
    def delete_contact(self):
        """Delete selected contact"""
        # TODO: Delete selected contact from list
        pass  # Students implement this
    
    def clear_form(self):
        """Clear form fields"""
        # TODO: Clear all form fields
        pass  # Students implement this
    
    def on_contact_select(self, event):
        """Handle contact selection"""
        # TODO: Populate form with selected contact data
        pass  # Students implement this
    
    def on_search(self, event):
        """Handle search input"""
        # TODO: Filter contacts based on search term
        pass  # Students implement this
    
    def update_contact_list(self):
        """Update the contact listbox"""
        # TODO: Refresh the contact list display
        pass  # Students implement this
    
    def validate_contact_data(self, data):
        """Validate contact data"""
        # TODO: Validate required fields and email format
        pass  # Students implement this
    
    def load_contacts(self):
        """Load contacts from JSON file"""
        # TODO: Load contacts from file with error handling
        pass  # Students implement this
    
    def save_contacts(self):
        """Save contacts to JSON file"""
        # TODO: Save contacts to file with error handling
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# EXERCISE 5: MEMORY GAME
# ============================================================================

class MemoryGame:
    """
    Exercise 5: Create a memory card matching game
    
    Requirements:
    - Grid of cards (face down)
    - Click to reveal cards
    - Match pairs of cards
    - Track score and time
    - Reset game functionality
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Memory Game")
        self.root.geometry("600x700")
        
        # TODO: Initialize game state
        self.grid_size = 4  # 4x4 grid
        self.cards = []
        self.card_buttons = []
        self.flipped_cards = []
        self.matched_pairs = 0
        self.score = 0
        self.start_time = None
        
        self.setup_widgets()
        self.new_game()
    
    def setup_widgets(self):
        """Setup memory game widgets"""
        # TODO: Create game info display (score, time, etc.)
        info_frame = tk.Frame(self.root)
        info_frame.pack(fill="x", padx=10, pady=5)
        
        self.score_label = tk.Label(info_frame, text="Score: 0", font=("Arial", 12))
        self.score_label.pack(side="left")
        
        self.time_label = tk.Label(info_frame, text="Time: 0:00", font=("Arial", 12))
        self.time_label.pack(side="right")
        
        # TODO: Create game grid
        self.game_frame = tk.Frame(self.root)
        self.game_frame.pack(expand=True, fill="both", padx=10, pady=10)
        
        # TODO: Create control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(fill="x", padx=10, pady=5)
        
        tk.Button(control_frame, text="New Game", command=self.new_game).pack(side="left")
        tk.Button(control_frame, text="Pause", command=self.pause_game).pack(side="left", padx=10)
    
    def create_card_grid(self):
        """Create grid of card buttons"""
        # TODO: Create buttons for card grid
        pass  # Students implement this
    
    def new_game(self):
        """Start a new game"""
        # TODO: Initialize game state and create new card layout
        pass  # Students implement this
    
    def generate_card_values(self):
        """Generate random card values for matching"""
        # TODO: Create pairs of matching values
        pass  # Students implement this
    
    def on_card_click(self, row, col):
        """Handle card click"""
        # TODO: Flip card and check for matches
        pass  # Students implement this
    
    def flip_card(self, row, col):
        """Flip a card face up"""
        # TODO: Show card value
        pass  # Students implement this
    
    def check_for_match(self):
        """Check if flipped cards match"""
        # TODO: Check if two flipped cards match
        pass  # Students implement this
    
    def handle_match(self):
        """Handle successful match"""
        # TODO: Update score and check for game completion
        pass  # Students implement this
    
    def handle_no_match(self):
        """Handle no match - flip cards back"""
        # TODO: Flip cards back after delay
        pass  # Students implement this
    
    def update_timer(self):
        """Update game timer"""
        # TODO: Update elapsed time display
        pass  # Students implement this
    
    def pause_game(self):
        """Pause/unpause the game"""
        # TODO: Implement pause functionality
        pass  # Students implement this
    
    def game_completed(self):
        """Handle game completion"""
        # TODO: Show completion message and final score
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# EXERCISE 6: DATA VISUALIZATION TOOL
# ============================================================================

class DataVisualizationTool:
    """
    Exercise 6: Create a data visualization tool
    
    Requirements:
    - Load data from CSV files
    - Display data in a table
    - Create simple charts (bar chart, pie chart)
    - Export visualizations
    - Data filtering and sorting
    """
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Data Visualization Tool")
        self.root.geometry("900x700")
        
        # TODO: Initialize data state
        self.data = []
        self.headers = []
        self.filtered_data = []
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Setup data visualization widgets"""
        # TODO: Create menu bar
        self.setup_menu()
        
        # TODO: Create main layout with data table and chart area
        # Left side: data table
        # Right side: chart display
        
        # Data panel
        data_frame = tk.LabelFrame(self.root, text="Data")
        data_frame.pack(side="left", fill="both", expand=True, padx=5, pady=5)
        
        # Load data button
        tk.Button(data_frame, text="Load CSV", command=self.load_csv).pack(pady=5)
        
        # Data table (using Treeview)
        self.data_tree = ttk.Treeview(data_frame)
        self.data_tree.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Chart panel
        chart_frame = tk.LabelFrame(self.root, text="Visualization")
        chart_frame.pack(side="right", fill="both", expand=True, padx=5, pady=5)
        
        # Chart controls
        control_frame = tk.Frame(chart_frame)
        control_frame.pack(fill="x", padx=5, pady=5)
        
        tk.Label(control_frame, text="Chart Type:").pack(side="left")
        self.chart_type = tk.StringVar(value="bar")
        chart_combo = ttk.Combobox(control_frame, textvariable=self.chart_type,
                                  values=["bar", "pie", "line"])
        chart_combo.pack(side="left", padx=5)
        
        tk.Button(control_frame, text="Create Chart", 
                 command=self.create_chart).pack(side="left", padx=10)
        
        # Chart display area (Canvas)
        self.chart_canvas = tk.Canvas(chart_frame, bg="white")
        self.chart_canvas.pack(fill="both", expand=True, padx=5, pady=5)
    
    def setup_menu(self):
        """Setup menu bar"""
        # TODO: Create File menu with load/save options
        pass  # Students implement this
    
    def load_csv(self):
        """Load data from CSV file"""
        # TODO: Use filedialog to select and load CSV file
        pass  # Students implement this
    
    def display_data_table(self):
        """Display data in the treeview table"""
        # TODO: Populate treeview with loaded data
        pass  # Students implement this
    
    def create_chart(self):
        """Create chart based on selected data and type"""
        # TODO: Create simple charts using Canvas drawing
        pass  # Students implement this
    
    def draw_bar_chart(self, data, labels):
        """Draw a bar chart"""
        # TODO: Draw bar chart on canvas
        pass  # Students implement this
    
    def draw_pie_chart(self, data, labels):
        """Draw a pie chart"""
        # TODO: Draw pie chart on canvas
        pass  # Students implement this
    
    def draw_line_chart(self, data, labels):
        """Draw a line chart"""
        # TODO: Draw line chart on canvas
        pass  # Students implement this
    
    def export_chart(self):
        """Export chart as image"""
        # TODO: Save canvas as PostScript/image file
        pass  # Students implement this
    
    def run(self):
        self.root.mainloop()


# ============================================================================
# HELPER FUNCTIONS AND TESTING
# ============================================================================

def run_exercise(exercise_number):
    """Run a specific exercise"""
    exercises = {
        1: Calculator,
        2: DrawingApp,
        3: TextEditor,
        4: ContactManager,
        5: MemoryGame,
        6: DataVisualizationTool
    }
    
    if exercise_number in exercises:
        app = exercises[exercise_number]()
        app.run()
    else:
        print(f"Exercise {exercise_number} not found!")


def main():
    """Main function to select and run exercises"""
    print("Week 4 In-Class Exercises")
    print("=========================")
    print("1. Basic GUI Calculator")
    print("2. Drawing Application")
    print("3. Text Editor with File Operations")
    print("4. Contact Manager")
    print("5. Memory Game")
    print("6. Data Visualization Tool")
    print()
    
    try:
        choice = int(input("Enter exercise number (1-6): "))
        run_exercise(choice)
    except ValueError:
        print("Invalid input. Please enter a number between 1 and 6.")
    except KeyboardInterrupt:
        print("\nGoodbye!")


if __name__ == "__main__":
    main()


# ============================================================================
# EXERCISE SOLUTIONS (FOR INSTRUCTOR REFERENCE)
# ============================================================================

"""
SOLUTION HINTS AND IMPLEMENTATION NOTES:

Exercise 1 - Calculator:
- Use StringVar for display
- Track operation state (current number, operation, previous number)
- Handle edge cases (division by zero, multiple operations)

Exercise 2 - Drawing App:
- Bind <Button-1>, <B1-Motion>, <ButtonRelease-1> events
- Track drawing state and tool type
- Use canvas.create_* methods for different shapes

Exercise 3 - Text Editor:
- Use filedialog.askopenfilename() and filedialog.asksaveasfilename()
- Track modification state with boolean flag
- Handle encoding properly when reading/writing files

Exercise 4 - Contact Manager:
- Use list of dictionaries for contact storage
- Implement JSON serialization for persistence
- Add input validation for email format

Exercise 5 - Memory Game:
- Use 2D list for card state
- Implement timer with root.after() method
- Handle card matching logic with state machine

Exercise 6 - Data Visualization:
- Use csv.reader() for file parsing
- Draw charts using canvas coordinates and math
- Implement basic statistical calculations for chart data

Common Patterns:
- Always use try/except for file operations
- Bind events using lambda functions to pass parameters
- Use StringVar/IntVar for data binding
- Implement proper cleanup and state management
"""
