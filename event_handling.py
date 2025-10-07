#!/usr/bin/env python3
"""
Week 4 Event Handling Examples - Event-Driven Programming Patterns
CSC 242 - Object-Oriented Programming

This file demonstrates comprehensive event handling techniques in GUI applications:
1. Mouse and keyboard event handling
2. Window and widget events
3. Custom event creation and handling
4. Event binding patterns
5. Advanced event propagation
"""

import tkinter as tk
from tkinter import messagebox, Canvas
import time
import threading


class MouseEventDemo:
    """Comprehensive demonstration of mouse event handling"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Mouse Event Handling Demo")
        self.root.geometry("600x500")
        
        self.setup_widgets()
        self.bind_mouse_events()
        
        # Track mouse state
        self.mouse_pressed = False
        self.drag_start = None
        self.current_shape = None
    
    def setup_widgets(self):
        # Instructions
        instructions = tk.Label(self.root,
                               text="Mouse Event Demonstrations\n" +
                                    "Left click: Draw circles\n" +
                                    "Right click: Draw rectangles\n" +
                                    "Middle click: Clear canvas\n" +
                                    "Drag: Draw lines\n" +
                                    "Double-click: Add text",
                               font=("Arial", 10),
                               justify="left",
                               bg="lightyellow")
        instructions.pack(fill="x", padx=5, pady=5)
        
        # Drawing canvas
        self.canvas = Canvas(self.root, bg="white", width=580, height=350)
        self.canvas.pack(padx=10, pady=10)
        
        # Mouse position display
        self.position_label = tk.Label(self.root, text="Mouse position: (0, 0)")
        self.position_label.pack()
        
        # Event log
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="Event Log:").pack(anchor="w")
        
        # Scrollable text area for events
        log_container = tk.Frame(log_frame)
        log_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side="right", fill="y")
        
        self.event_log = tk.Text(log_container,
                                height=6,
                                yscrollcommand=scrollbar.set,
                                font=("Courier", 9))
        self.event_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.event_log.yview)
        
        # Control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)
        
        tk.Button(control_frame, text="Clear Canvas", 
                 command=self.clear_canvas).pack(side="left", padx=5)
        tk.Button(control_frame, text="Clear Log", 
                 command=self.clear_log).pack(side="left", padx=5)
    
    def bind_mouse_events(self):
        """Bind all mouse events to the canvas"""
        # Basic mouse button events
        self.canvas.bind("<Button-1>", self.on_left_click)
        self.canvas.bind("<Button-2>", self.on_middle_click)
        self.canvas.bind("<Button-3>", self.on_right_click)
        
        # Double and triple clicks
        self.canvas.bind("<Double-Button-1>", self.on_double_click)
        self.canvas.bind("<Triple-Button-1>", self.on_triple_click)
        
        # Mouse button press and release
        self.canvas.bind("<ButtonPress-1>", self.on_button_press)
        self.canvas.bind("<ButtonRelease-1>", self.on_button_release)
        
        # Mouse motion events
        self.canvas.bind("<Motion>", self.on_mouse_motion)
        self.canvas.bind("<B1-Motion>", self.on_drag_motion)
        
        # Mouse enter and leave
        self.canvas.bind("<Enter>", self.on_mouse_enter)
        self.canvas.bind("<Leave>", self.on_mouse_leave)
        
        # Mouse wheel events
        self.canvas.bind("<MouseWheel>", self.on_mouse_wheel)
        self.canvas.bind("<Button-4>", self.on_mouse_wheel_up)    # Linux
        self.canvas.bind("<Button-5>", self.on_mouse_wheel_down)  # Linux
    
    def log_event(self, event_type, details=""):
        """Log event to the text area"""
        timestamp = time.strftime("%H:%M:%S")
        message = f"[{timestamp}] {event_type}"
        if details:
            message += f": {details}"
        
        self.event_log.insert(tk.END, f"{message}\n")
        self.event_log.see(tk.END)
    
    def on_left_click(self, event):
        """Handle left mouse button click"""
        self.log_event("Left Click", f"({event.x}, {event.y})")
        
        # Draw a circle at click position
        radius = 10
        self.canvas.create_oval(event.x - radius, event.y - radius,
                               event.x + radius, event.y + radius,
                               fill="red", outline="darkred", width=2)
    
    def on_middle_click(self, event):
        """Handle middle mouse button click"""
        self.log_event("Middle Click", f"({event.x}, {event.y}) - Clearing canvas")
        self.clear_canvas()
    
    def on_right_click(self, event):
        """Handle right mouse button click"""
        self.log_event("Right Click", f"({event.x}, {event.y})")
        
        # Draw a rectangle at click position
        size = 20
        self.canvas.create_rectangle(event.x - size//2, event.y - size//2,
                                   event.x + size//2, event.y + size//2,
                                   fill="blue", outline="darkblue", width=2)
    
    def on_double_click(self, event):
        """Handle double click"""
        self.log_event("Double Click", f"({event.x}, {event.y})")
        
        # Add text at double-click position
        self.canvas.create_text(event.x, event.y,
                               text="Double!",
                               fill="green",
                               font=("Arial", 12, "bold"))
    
    def on_triple_click(self, event):
        """Handle triple click"""
        self.log_event("Triple Click", f"({event.x}, {event.y})")
        
        # Add special text for triple click
        self.canvas.create_text(event.x, event.y,
                               text="TRIPLE!",
                               fill="purple",
                               font=("Arial", 16, "bold"))
    
    def on_button_press(self, event):
        """Handle mouse button press"""
        self.mouse_pressed = True
        self.drag_start = (event.x, event.y)
        self.log_event("Button Press", f"({event.x}, {event.y})")
    
    def on_button_release(self, event):
        """Handle mouse button release"""
        self.mouse_pressed = False
        self.log_event("Button Release", f"({event.x}, {event.y})")
        
        if self.drag_start:
            start_x, start_y = self.drag_start
            distance = ((event.x - start_x)**2 + (event.y - start_y)**2)**0.5
            if distance > 5:  # Only log significant drags
                self.log_event("Drag Complete", 
                              f"From ({start_x}, {start_y}) to ({event.x}, {event.y}), distance: {distance:.1f}")
    
    def on_mouse_motion(self, event):
        """Handle mouse movement"""
        # Update position display (don't log every movement to avoid spam)
        self.position_label.config(text=f"Mouse position: ({event.x}, {event.y})")
    
    def on_drag_motion(self, event):
        """Handle mouse drag (button held down while moving)"""
        if self.drag_start:
            # Draw line from drag start to current position
            start_x, start_y = self.drag_start
            
            # Remove previous drag line if it exists
            if self.current_shape:
                self.canvas.delete(self.current_shape)
            
            # Draw new line
            self.current_shape = self.canvas.create_line(start_x, start_y, event.x, event.y,
                                                        fill="orange", width=3)
    
    def on_mouse_enter(self, event):
        """Handle mouse entering canvas"""
        self.log_event("Mouse Enter", "Canvas area")
        self.canvas.config(cursor="crosshair")
    
    def on_mouse_leave(self, event):
        """Handle mouse leaving canvas"""
        self.log_event("Mouse Leave", "Canvas area")
        self.canvas.config(cursor="")
        self.mouse_pressed = False
    
    def on_mouse_wheel(self, event):
        """Handle mouse wheel scrolling (Windows/Mac)"""
        direction = "up" if event.delta > 0 else "down"
        self.log_event("Mouse Wheel", f"{direction} (delta: {event.delta})")
        
        # Change canvas background color based on scroll
        if event.delta > 0:
            self.canvas.config(bg="#f0f0f0")
        else:
            self.canvas.config(bg="white")
    
    def on_mouse_wheel_up(self, event):
        """Handle mouse wheel up (Linux)"""
        self.log_event("Mouse Wheel", "up")
        self.canvas.config(bg="#f0f0f0")
    
    def on_mouse_wheel_down(self, event):
        """Handle mouse wheel down (Linux)"""
        self.log_event("Mouse Wheel", "down")
        self.canvas.config(bg="white")
    
    def clear_canvas(self):
        """Clear the canvas"""
        self.canvas.delete("all")
        self.current_shape = None
    
    def clear_log(self):
        """Clear the event log"""
        self.event_log.delete("1.0", tk.END)
    
    def run(self):
        self.root.mainloop()


class KeyboardEventDemo:
    """Demonstration of keyboard event handling"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Keyboard Event Handling Demo")
        self.root.geometry("600x500")
        
        self.setup_widgets()
        self.bind_keyboard_events()
        
        # Track keyboard state
        self.keys_pressed = set()
        self.caps_lock = False
        self.num_lock = False
    
    def setup_widgets(self):
        # Instructions
        instructions = tk.Label(self.root,
                               text="Keyboard Event Demonstrations\n" +
                                    "Type text in the entry field\n" +
                                    "Press various keys to see events\n" +
                                    "Try modifier keys (Ctrl, Alt, Shift)\n" +
                                    "Use arrow keys, function keys, etc.",
                               font=("Arial", 10),
                               justify="left",
                               bg="lightcyan")
        instructions.pack(fill="x", padx=5, pady=5)
        
        # Text input area
        input_frame = tk.Frame(self.root)
        input_frame.pack(fill="x", padx=10, pady=10)
        
        tk.Label(input_frame, text="Type here:").pack(anchor="w")
        self.text_entry = tk.Entry(input_frame, font=("Arial", 14))
        self.text_entry.pack(fill="x", pady=5)
        
        # Multi-line text area
        tk.Label(input_frame, text="Multi-line text area:").pack(anchor="w")
        self.text_area = tk.Text(input_frame, height=6, font=("Courier", 10))
        self.text_area.pack(fill="x", pady=5)
        
        # Key state display
        state_frame = tk.Frame(self.root)
        state_frame.pack(fill="x", padx=10, pady=5)
        
        self.key_state_label = tk.Label(state_frame, text="Keys pressed: None", 
                                       font=("Courier", 10), bg="lightyellow")
        self.key_state_label.pack(fill="x")
        
        self.modifier_state_label = tk.Label(state_frame, text="Modifiers: None", 
                                           font=("Courier", 10), bg="lightgreen")
        self.modifier_state_label.pack(fill="x")
        
        # Event log
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="Keyboard Event Log:").pack(anchor="w")
        
        log_container = tk.Frame(log_frame)
        log_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side="right", fill="y")
        
        self.event_log = tk.Text(log_container,
                                height=8,
                                yscrollcommand=scrollbar.set,
                                font=("Courier", 9))
        self.event_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.event_log.yview)
        
        # Control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=5)
        
        tk.Button(control_frame, text="Clear Entry", 
                 command=self.clear_entry).pack(side="left", padx=5)
        tk.Button(control_frame, text="Clear Text Area", 
                 command=self.clear_text_area).pack(side="left", padx=5)
        tk.Button(control_frame, text="Clear Log", 
                 command=self.clear_log).pack(side="left", padx=5)
    
    def bind_keyboard_events(self):
        """Bind keyboard events to widgets"""
        # Global key events (bind to root window)
        self.root.bind("<KeyPress>", self.on_key_press)
        self.root.bind("<KeyRelease>", self.on_key_release)
        
        # Specific key events
        self.root.bind("<Return>", self.on_enter_key)
        self.root.bind("<Escape>", self.on_escape_key)
        self.root.bind("<Tab>", self.on_tab_key)
        self.root.bind("<BackSpace>", self.on_backspace_key)
        self.root.bind("<Delete>", self.on_delete_key)
        
        # Arrow keys
        self.root.bind("<Up>", self.on_arrow_key)
        self.root.bind("<Down>", self.on_arrow_key)
        self.root.bind("<Left>", self.on_arrow_key)
        self.root.bind("<Right>", self.on_arrow_key)
        
        # Function keys
        for i in range(1, 13):
            self.root.bind(f"<F{i}>", self.on_function_key)
        
        # Modifier combinations
        self.root.bind("<Control-c>", self.on_ctrl_c)
        self.root.bind("<Control-v>", self.on_ctrl_v)
        self.root.bind("<Control-x>", self.on_ctrl_x)
        self.root.bind("<Control-z>", self.on_ctrl_z)
        self.root.bind("<Control-a>", self.on_ctrl_a)
        self.root.bind("<Control-s>", self.on_ctrl_s)
        
        self.root.bind("<Alt-F4>", self.on_alt_f4)
        
        # Text widget specific events
        self.text_entry.bind("<KeyPress>", self.on_entry_key_press)
        self.text_area.bind("<KeyPress>", self.on_text_area_key_press)
        
        # Focus events
        self.text_entry.bind("<FocusIn>", self.on_focus_in)
        self.text_entry.bind("<FocusOut>", self.on_focus_out)
        self.text_area.bind("<FocusIn>", self.on_focus_in)
        self.text_area.bind("<FocusOut>", self.on_focus_out)
        
        # Make root focusable for global key events
        self.root.focus_set()
    
    def log_event(self, event_type, details=""):
        """Log keyboard event"""
        timestamp = time.strftime("%H:%M:%S")
        message = f"[{timestamp}] {event_type}"
        if details:
            message += f": {details}"
        
        self.event_log.insert(tk.END, f"{message}\n")
        self.event_log.see(tk.END)
    
    def update_key_state_display(self):
        """Update the key state display"""
        if self.keys_pressed:
            keys_text = f"Keys pressed: {', '.join(sorted(self.keys_pressed))}"
        else:
            keys_text = "Keys pressed: None"
        self.key_state_label.config(text=keys_text)
    
    def update_modifier_display(self, event):
        """Update modifier key display"""
        modifiers = []
        if event.state & 0x1:    # Shift
            modifiers.append("Shift")
        if event.state & 0x4:    # Control
            modifiers.append("Ctrl")
        if event.state & 0x8:    # Alt
            modifiers.append("Alt")
        if event.state & 0x2:    # Caps Lock
            modifiers.append("CapsLock")
        if event.state & 0x10:   # Num Lock
            modifiers.append("NumLock")
        
        if modifiers:
            modifier_text = f"Modifiers: {', '.join(modifiers)}"
        else:
            modifier_text = "Modifiers: None"
        self.modifier_state_label.config(text=modifier_text)
    
    def on_key_press(self, event):
        """Handle general key press"""
        self.keys_pressed.add(event.keysym)
        self.update_key_state_display()
        self.update_modifier_display(event)
        
        # Log detailed key information
        details = f"keysym='{event.keysym}', keycode={event.keycode}"
        if event.char and event.char.isprintable():
            details += f", char='{event.char}'"
        
        self.log_event("Key Press", details)
    
    def on_key_release(self, event):
        """Handle key release"""
        self.keys_pressed.discard(event.keysym)
        self.update_key_state_display()
        self.update_modifier_display(event)
        
        self.log_event("Key Release", f"keysym='{event.keysym}'")
    
    def on_enter_key(self, event):
        """Handle Enter key"""
        self.log_event("Enter Key", "Return/Enter pressed")
    
    def on_escape_key(self, event):
        """Handle Escape key"""
        self.log_event("Escape Key", "Escape pressed - clearing focus")
        self.root.focus_set()
    
    def on_tab_key(self, event):
        """Handle Tab key"""
        self.log_event("Tab Key", "Tab pressed")
    
    def on_backspace_key(self, event):
        """Handle Backspace key"""
        self.log_event("Backspace Key", "Backspace pressed")
    
    def on_delete_key(self, event):
        """Handle Delete key"""
        self.log_event("Delete Key", "Delete pressed")
    
    def on_arrow_key(self, event):
        """Handle arrow keys"""
        self.log_event("Arrow Key", f"{event.keysym} arrow pressed")
    
    def on_function_key(self, event):
        """Handle function keys"""
        self.log_event("Function Key", f"{event.keysym} pressed")
    
    def on_ctrl_c(self, event):
        """Handle Ctrl+C"""
        self.log_event("Ctrl+C", "Copy command")
    
    def on_ctrl_v(self, event):
        """Handle Ctrl+V"""
        self.log_event("Ctrl+V", "Paste command")
    
    def on_ctrl_x(self, event):
        """Handle Ctrl+X"""
        self.log_event("Ctrl+X", "Cut command")
    
    def on_ctrl_z(self, event):
        """Handle Ctrl+Z"""
        self.log_event("Ctrl+Z", "Undo command")
    
    def on_ctrl_a(self, event):
        """Handle Ctrl+A"""
        self.log_event("Ctrl+A", "Select All command")
    
    def on_ctrl_s(self, event):
        """Handle Ctrl+S"""
        self.log_event("Ctrl+S", "Save command")
        messagebox.showinfo("Save", "Save functionality would be implemented here")
    
    def on_alt_f4(self, event):
        """Handle Alt+F4"""
        self.log_event("Alt+F4", "Close window command")
        if messagebox.askokcancel("Quit", "Close the application?"):
            self.root.quit()
    
    def on_entry_key_press(self, event):
        """Handle key press in entry widget"""
        widget_name = "Entry"
        self.log_event(f"{widget_name} Key", f"'{event.keysym}' in entry field")
    
    def on_text_area_key_press(self, event):
        """Handle key press in text area"""
        widget_name = "Text Area"
        self.log_event(f"{widget_name} Key", f"'{event.keysym}' in text area")
    
    def on_focus_in(self, event):
        """Handle widget gaining focus"""
        widget_name = event.widget.__class__.__name__
        self.log_event("Focus In", f"{widget_name} gained focus")
    
    def on_focus_out(self, event):
        """Handle widget losing focus"""
        widget_name = event.widget.__class__.__name__
        self.log_event("Focus Out", f"{widget_name} lost focus")
    
    def clear_entry(self):
        """Clear the entry field"""
        self.text_entry.delete(0, tk.END)
        self.log_event("Action", "Entry field cleared")
    
    def clear_text_area(self):
        """Clear the text area"""
        self.text_area.delete("1.0", tk.END)
        self.log_event("Action", "Text area cleared")
    
    def clear_log(self):
        """Clear the event log"""
        self.event_log.delete("1.0", tk.END)
    
    def run(self):
        self.root.mainloop()


class WindowEventDemo:
    """Demonstration of window and application events"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Window Event Handling Demo")
        self.root.geometry("500x400")
        
        self.setup_widgets()
        self.bind_window_events()
        
        # Track window state
        self.window_state = "normal"
        self.last_size = (500, 400)
    
    def setup_widgets(self):
        # Instructions
        instructions = tk.Label(self.root,
                               text="Window Event Demonstrations\n" +
                                    "Resize the window, minimize/maximize it\n" +
                                    "Move the window around\n" +
                                    "Try to close the window\n" +
                                    "Switch focus to other applications",
                               font=("Arial", 10),
                               justify="left",
                               bg="lightcyan")
        instructions.pack(fill="x", padx=5, pady=5)
        
        # Window info display
        info_frame = tk.LabelFrame(self.root, text="Window Information", padx=10, pady=10)
        info_frame.pack(fill="x", padx=10, pady=10)
        
        self.size_label = tk.Label(info_frame, text="Size: 500x400")
        self.size_label.pack(anchor="w")
        
        self.position_label = tk.Label(info_frame, text="Position: (0, 0)")
        self.position_label.pack(anchor="w")
        
        self.state_label = tk.Label(info_frame, text="State: normal")
        self.state_label.pack(anchor="w")
        
        self.focus_label = tk.Label(info_frame, text="Focus: Yes")
        self.focus_label.pack(anchor="w")
        
        # Control buttons
        control_frame = tk.Frame(self.root)
        control_frame.pack(pady=10)
        
        tk.Button(control_frame, text="Minimize", 
                 command=self.minimize_window).pack(side="left", padx=5)
        tk.Button(control_frame, text="Maximize", 
                 command=self.maximize_window).pack(side="left", padx=5)
        tk.Button(control_frame, text="Restore", 
                 command=self.restore_window).pack(side="left", padx=5)
        tk.Button(control_frame, text="Center Window", 
                 command=self.center_window).pack(side="left", padx=5)
        
        # Event log
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="Window Event Log:").pack(anchor="w")
        
        log_container = tk.Frame(log_frame)
        log_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side="right", fill="y")
        
        self.event_log = tk.Text(log_container,
                                yscrollcommand=scrollbar.set,
                                font=("Courier", 9))
        self.event_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.event_log.yview)
        
        tk.Button(self.root, text="Clear Log", 
                 command=self.clear_log).pack(pady=5)
    
    def bind_window_events(self):
        """Bind window-related events"""
        # Window configuration changes (resize, move)
        self.root.bind("<Configure>", self.on_window_configure)
        
        # Window state changes
        self.root.bind("<Map>", self.on_window_map)
        self.root.bind("<Unmap>", self.on_window_unmap)
        
        # Focus events
        self.root.bind("<FocusIn>", self.on_window_focus_in)
        self.root.bind("<FocusOut>", self.on_window_focus_out)
        
        # Window manager events
        self.root.protocol("WM_DELETE_WINDOW", self.on_window_close)
        self.root.protocol("WM_TAKE_FOCUS", self.on_window_take_focus)
        
        # Visibility events
        self.root.bind("<Visibility>", self.on_visibility_change)
        
        # Iconify/deiconify events
        self.root.bind("<Map>", self.on_map_event)
        self.root.bind("<Unmap>", self.on_unmap_event)
        
        # Update display periodically
        self.update_window_info()
    
    def log_event(self, event_type, details=""):
        """Log window event"""
        timestamp = time.strftime("%H:%M:%S")
        message = f"[{timestamp}] {event_type}"
        if details:
            message += f": {details}"
        
        self.event_log.insert(tk.END, f"{message}\n")
        self.event_log.see(tk.END)
    
    def update_window_info(self):
        """Update window information display"""
        try:
            # Get window geometry
            geometry = self.root.geometry()
            width, height, x, y = map(int, geometry.split('+')[0].split('x') + geometry.split('+')[1:])
            
            self.size_label.config(text=f"Size: {width}x{height}")
            self.position_label.config(text=f"Position: ({x}, {y})")
            
            # Get window state
            state = self.root.state()
            self.state_label.config(text=f"State: {state}")
            
            # Check focus
            focus_widget = self.root.focus_get()
            has_focus = focus_widget is not None
            self.focus_label.config(text=f"Focus: {'Yes' if has_focus else 'No'}")
            
        except Exception as e:
            pass  # Ignore errors during updates
        
        # Schedule next update
        self.root.after(1000, self.update_window_info)
    
    def on_window_configure(self, event):
        """Handle window configuration changes"""
        if event.widget == self.root:  # Only handle root window events
            width = event.width
            height = event.height
            
            # Check if this is a resize event
            if (width, height) != self.last_size:
                self.log_event("Window Resize", f"New size: {width}x{height}")
                self.last_size = (width, height)
            
            # Log other configuration details
            details = f"width={width}, height={height}, x={event.x}, y={event.y}"
            self.log_event("Window Configure", details)
    
    def on_window_map(self, event):
        """Handle window mapping (becoming visible)"""
        if event.widget == self.root:
            self.log_event("Window Map", "Window became visible")
    
    def on_window_unmap(self, event):
        """Handle window unmapping (becoming invisible)"""
        if event.widget == self.root:
            self.log_event("Window Unmap", "Window became invisible")
    
    def on_window_focus_in(self, event):
        """Handle window gaining focus"""
        if event.widget == self.root:
            self.log_event("Window Focus In", "Window gained focus")
    
    def on_window_focus_out(self, event):
        """Handle window losing focus"""
        if event.widget == self.root:
            self.log_event("Window Focus Out", "Window lost focus")
    
    def on_window_close(self):
        """Handle window close request"""
        self.log_event("Window Close Request", "User requested to close window")
        
        result = messagebox.askyesnocancel("Close Window",
                                          "Do you want to save before closing?")
        
        if result is True:  # Yes - save and close
            self.log_event("Window Close", "Saving and closing")
            messagebox.showinfo("Save", "Data would be saved here")
            self.root.destroy()
        elif result is False:  # No - close without saving
            self.log_event("Window Close", "Closing without saving")
            self.root.destroy()
        else:  # Cancel - don't close
            self.log_event("Window Close", "Close cancelled by user")
    
    def on_window_take_focus(self):
        """Handle window manager focus request"""
        self.log_event("Window Take Focus", "Window manager requested focus")
    
    def on_visibility_change(self, event):
        """Handle visibility change events"""
        visibility_states = {
            "VisibilityUnobscured": "fully visible",
            "VisibilityPartiallyObscured": "partially visible", 
            "VisibilityFullyObscured": "fully obscured"
        }
        
        state = visibility_states.get(str(event.state), str(event.state))
        self.log_event("Visibility Change", f"Window is {state}")
    
    def on_map_event(self, event):
        """Handle map events (window shown)"""
        if event.widget == self.root:
            self.log_event("Map Event", "Window mapped/shown")
    
    def on_unmap_event(self, event):
        """Handle unmap events (window hidden)"""
        if event.widget == self.root:
            self.log_event("Unmap Event", "Window unmapped/hidden")
    
    def minimize_window(self):
        """Minimize the window"""
        self.root.iconify()
        self.log_event("Action", "Window minimized programmatically")
    
    def maximize_window(self):
        """Maximize the window"""
        self.root.state('zoomed')  # Windows/Linux
        self.log_event("Action", "Window maximized programmatically")
    
    def restore_window(self):
        """Restore the window to normal state"""
        self.root.state('normal')
        self.log_event("Action", "Window restored to normal state")
    
    def center_window(self):
        """Center the window on screen"""
        self.root.update_idletasks()
        
        # Get window size
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        
        # Get screen size
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        # Calculate center position
        x = (screen_width - width) // 2
        y = (screen_height - height) // 2
        
        # Set window position
        self.root.geometry(f"{width}x{height}+{x}+{y}")
        self.log_event("Action", f"Window centered at ({x}, {y})")
    
    def clear_log(self):
        """Clear the event log"""
        self.event_log.delete("1.0", tk.END)
    
    def run(self):
        self.root.mainloop()


class CustomEventDemo:
    """Demonstration of custom event creation and handling"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Custom Event Handling Demo")
        self.root.geometry("600x500")
        
        self.setup_widgets()
        self.setup_custom_events()
        
        # Custom event data
        self.custom_event_counter = 0
        self.timer_active = False
    
    def setup_widgets(self):
        # Instructions
        instructions = tk.Label(self.root,
                               text="Custom Event Demonstrations\n" +
                                    "This demo shows how to create and handle custom events\n" +
                                    "Click buttons to trigger custom events",
                               font=("Arial", 10),
                               justify="center",
                               bg="lightgreen")
        instructions.pack(fill="x", padx=5, pady=5)
        
        # Event trigger buttons
        trigger_frame = tk.LabelFrame(self.root, text="Custom Event Triggers", padx=10, pady=10)
        trigger_frame.pack(fill="x", padx=10, pady=10)
        
        button_frame1 = tk.Frame(trigger_frame)
        button_frame1.pack(fill="x", pady=5)
        
        tk.Button(button_frame1, text="Trigger Custom Event 1", 
                 command=self.trigger_custom_event_1).pack(side="left", padx=5)
        tk.Button(button_frame1, text="Trigger Custom Event 2", 
                 command=self.trigger_custom_event_2).pack(side="left", padx=5)
        tk.Button(button_frame1, text="Trigger Data Event", 
                 command=self.trigger_data_event).pack(side="left", padx=5)
        
        button_frame2 = tk.Frame(trigger_frame)
        button_frame2.pack(fill="x", pady=5)
        
        tk.Button(button_frame2, text="Start Timer Events", 
                 command=self.start_timer_events).pack(side="left", padx=5)
        tk.Button(button_frame2, text="Stop Timer Events", 
                 command=self.stop_timer_events).pack(side="left", padx=5)
        tk.Button(button_frame2, text="Trigger Chain Event", 
                 command=self.trigger_chain_event).pack(side="left", padx=5)
        
        # Event status display
        status_frame = tk.LabelFrame(self.root, text="Event Status", padx=10, pady=10)
        status_frame.pack(fill="x", padx=10, pady=10)
        
        self.event_counter_label = tk.Label(status_frame, text="Custom events triggered: 0")
        self.event_counter_label.pack(anchor="w")
        
        self.timer_status_label = tk.Label(status_frame, text="Timer events: Stopped")
        self.timer_status_label.pack(anchor="w")
        
        self.last_event_label = tk.Label(status_frame, text="Last event: None")
        self.last_event_label.pack(anchor="w")
        
        # Canvas for visual event feedback
        self.canvas = tk.Canvas(self.root, height=150, bg="white")
        self.canvas.pack(fill="x", padx=10, pady=10)
        
        # Event log
        log_frame = tk.Frame(self.root)
        log_frame.pack(fill="both", expand=True, padx=10, pady=5)
        
        tk.Label(log_frame, text="Custom Event Log:").pack(anchor="w")
        
        log_container = tk.Frame(log_frame)
        log_container.pack(fill="both", expand=True)
        
        scrollbar = tk.Scrollbar(log_container)
        scrollbar.pack(side="right", fill="y")
        
        self.event_log = tk.Text(log_container,
                                yscrollcommand=scrollbar.set,
                                font=("Courier", 9))
        self.event_log.pack(side="left", fill="both", expand=True)
        scrollbar.config(command=self.event_log.yview)
        
        tk.Button(self.root, text="Clear Log", 
                 command=self.clear_log).pack(pady=5)
    
    def setup_custom_events(self):
        """Setup custom event handling"""
        # Bind custom virtual events
        self.root.bind("<<CustomEvent1>>", self.on_custom_event_1)
        self.root.bind("<<CustomEvent2>>", self.on_custom_event_2)
        self.root.bind("<<DataEvent>>", self.on_data_event)
        self.root.bind("<<TimerEvent>>", self.on_timer_event)
        self.root.bind("<<ChainEvent>>", self.on_chain_event)
        self.root.bind("<<ChainEvent2>>", self.on_chain_event_2)
        self.root.bind("<<ChainEvent3>>", self.on_chain_event_3)
    
    def log_event(self, event_type, details=""):
        """Log custom event"""
        timestamp = time.strftime("%H:%M:%S")
        message = f"[{timestamp}] {event_type}"
        if details:
            message += f": {details}"
        
        self.event_log.insert(tk.END, f"{message}\n")
        self.event_log.see(tk.END)
        
        # Update status
        self.last_event_label.config(text=f"Last event: {event_type}")
    
    def trigger_custom_event_1(self):
        """Trigger first custom event"""
        self.root.event_generate("<<CustomEvent1>>")
        self.log_event("Custom Event 1 Triggered", "Generated by button click")
    
    def trigger_custom_event_2(self):
        """Trigger second custom event"""
        self.root.event_generate("<<CustomEvent2>>")
        self.log_event("Custom Event 2 Triggered", "Generated by button click")
    
    def trigger_data_event(self):
        """Trigger event with data"""
        import random
        data = {
            "value": random.randint(1, 100),
            "timestamp": time.time(),
            "source": "manual_trigger"
        }
        
        # Store data for event handler to access
        self.root.custom_event_data = data
        self.root.event_generate("<<DataEvent>>")
        self.log_event("Data Event Triggered", f"With data: {data}")
    
    def start_timer_events(self):
        """Start generating timer events"""
        if not self.timer_active:
            self.timer_active = True
            self.timer_status_label.config(text="Timer events: Running")
            self.schedule_timer_event()
            self.log_event("Timer Events Started", "Will fire every 2 seconds")
    
    def stop_timer_events(self):
        """Stop generating timer events"""
        self.timer_active = False
        self.timer_status_label.config(text="Timer events: Stopped")
        self.log_event("Timer Events Stopped", "No more timer events")
    
    def schedule_timer_event(self):
        """Schedule the next timer event"""
        if self.timer_active:
            self.root.after(2000, self.generate_timer_event)
    
    def generate_timer_event(self):
        """Generate a timer event"""
        if self.timer_active:
            self.root.event_generate("<<TimerEvent>>")
            self.schedule_timer_event()
    
    def trigger_chain_event(self):
        """Trigger a chain of events"""
        self.root.event_generate("<<ChainEvent>>")
        self.log_event("Chain Event Started", "Will trigger sequence of events")
    
    def on_custom_event_1(self, event):
        """Handle first custom event"""
        self.custom_event_counter += 1
        self.event_counter_label.config(text=f"Custom events triggered: {self.custom_event_counter}")
        
        # Visual feedback on canvas
        import random
        x = random.randint(50, 550)
        y = random.randint(20, 130)
        self.canvas.create_oval(x-10, y-10, x+10, y+10, 
                               fill="red", outline="darkred")
        
        self.log_event("Custom Event 1 Handled", f"Drew red circle at ({x}, {y})")
    
    def on_custom_event_2(self, event):
        """Handle second custom event"""
        self.custom_event_counter += 1
        self.event_counter_label.config(text=f"Custom events triggered: {self.custom_event_counter}")
        
        # Visual feedback on canvas
        import random
        x = random.randint(50, 550)
        y = random.randint(20, 130)
        self.canvas.create_rectangle(x-15, y-10, x+15, y+10, 
                                   fill="blue", outline="darkblue")
        
        self.log_event("Custom Event 2 Handled", f"Drew blue rectangle at ({x}, {y})")
    
    def on_data_event(self, event):
        """Handle event with associated data"""
        self.custom_event_counter += 1
        self.event_counter_label.config(text=f"Custom events triggered: {self.custom_event_counter}")
        
        # Access custom data
        data = getattr(self.root, 'custom_event_data', {})
        value = data.get('value', 0)
        source = data.get('source', 'unknown')
        
        # Visual feedback based on data
        x = (value / 100) * 500 + 50  # Scale value to canvas width
        y = 75
        color = "green" if value > 50 else "orange"
        
        self.canvas.create_text(x, y, text=str(value), 
                               fill=color, font=("Arial", 14, "bold"))
        
        self.log_event("Data Event Handled", f"Value: {value}, Source: {source}, Position: ({x:.0f}, {y})")
    
    def on_timer_event(self, event):
        """Handle timer event"""
        self.custom_event_counter += 1
        self.event_counter_label.config(text=f"Custom events triggered: {self.custom_event_counter}")
        
        # Visual feedback - moving dot
        import random
        x = random.randint(50, 550)
        y = random.randint(20, 130)
        
        # Create a temporary dot that fades
        dot = self.canvas.create_oval(x-5, y-5, x+5, y+5, 
                                     fill="purple", outline="darkviolet")
        
        # Remove dot after 1 second
        self.root.after(1000, lambda: self.canvas.delete(dot))
        
        self.log_event("Timer Event Handled", f"Temporary purple dot at ({x}, {y})")
    
    def on_chain_event(self, event):
        """Handle first event in chain"""
        self.log_event("Chain Event 1 Handled", "Triggering next event in chain")
        
        # Trigger next event in chain after delay
        self.root.after(500, lambda: self.root.event_generate("<<ChainEvent2>>"))
    
    def on_chain_event_2(self, event):
        """Handle second event in chain"""
        self.log_event("Chain Event 2 Handled", "Triggering final event in chain")
        
        # Trigger final event in chain
        self.root.after(500, lambda: self.root.event_generate("<<ChainEvent3>>"))
    
    def on_chain_event_3(self, event):
        """Handle final event in chain"""
        self.log_event("Chain Event 3 Handled", "Chain complete!")
        
        # Visual indication of chain completion
        self.canvas.create_text(300, 75, text="CHAIN COMPLETE!", 
                               fill="red", font=("Arial", 16, "bold"))
        
        # Clear text after 2 seconds
        self.root.after(2000, lambda: self.canvas.delete("all"))
    
    def clear_log(self):
        """Clear the event log"""
        self.event_log.delete("1.0", tk.END)
        self.canvas.delete("all")
    
    def run(self):
        self.root.mainloop()


def main():
    """Main function to run event handling demonstrations"""
    print("Event Handling Demonstrations")
    print("=============================")
    print("1. Mouse Event Demo")
    print("2. Keyboard Event Demo")
    print("3. Window Event Demo")
    print("4. Custom Event Demo")
    print("5. Run All Demos")
    
    choice = input("\nEnter your choice (1-5): ").strip()
    
    if choice == "1":
        app = MouseEventDemo()
        app.run()
    elif choice == "2":
        app = KeyboardEventDemo()
        app.run()
    elif choice == "3":
        app = WindowEventDemo()
        app.run()
    elif choice == "4":
        app = CustomEventDemo()
        app.run()
    elif choice == "5":
        # Run demos sequentially
        demos = [
            ("Mouse Events", MouseEventDemo),
            ("Keyboard Events", KeyboardEventDemo),
            ("Window Events", WindowEventDemo),
            ("Custom Events", CustomEventDemo)
        ]
        
        for name, demo_class in demos:
            print(f"\nRunning {name} demo...")
            app = demo_class()
            app.run()
    else:
        print("Invalid choice. Please run the script again.")


if __name__ == "__main__":
    main()
