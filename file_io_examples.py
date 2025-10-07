#!/usr/bin/env python3
"""
Week 4 File I/O Examples - Comprehensive File Operations
CSC 242 - Object-Oriented Programming

This file demonstrates various file input/output operations and techniques:
1. Basic file reading and writing
2. Different file formats (text, CSV, JSON)
3. Error handling and exception management
4. File system operations
5. Integration with GUI applications
"""

import os
import json
import csv
import pickle
import shutil
import tempfile
from pathlib import Path
from datetime import datetime
import tkinter as tk
from tkinter import filedialog, messagebox, scrolledtext


class BasicFileOperations:
    """Demonstrates fundamental file I/O operations"""
    
    def __init__(self):
        self.demo_directory = Path("file_demo")
        self.setup_demo_environment()
    
    def setup_demo_environment(self):
        """Create demo directory and sample files"""
        self.demo_directory.mkdir(exist_ok=True)
        
        # Create sample text file
        sample_text = """This is a sample text file.
It contains multiple lines of text.
Each line demonstrates different content.

Line 5: Numbers 12345
Line 6: Special characters !@#$%^&*()
Line 7: Unicode characters: é, ñ, 中文
Line 8: Empty line follows:

Line 10: Final line of sample text."""
        
        with open(self.demo_directory / "sample.txt", "w", encoding="utf-8") as f:
            f.write(sample_text)
        
        print(f"Demo environment created in: {self.demo_directory.absolute()}")
    
    def demonstrate_basic_reading(self):
        """Demonstrate basic file reading techniques"""
        print("\n=== Basic File Reading ===")
        
        file_path = self.demo_directory / "sample.txt"
        
        # Method 1: Read entire file
        print("1. Reading entire file:")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                content = file.read()
                print(f"File content ({len(content)} characters):")
                print(content[:100] + "..." if len(content) > 100 else content)
        except FileNotFoundError:
            print(f"File not found: {file_path}")
        except Exception as e:
            print(f"Error reading file: {e}")
        
        # Method 2: Read line by line
        print("\n2. Reading line by line:")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                line_number = 1
                for line in file:
                    print(f"Line {line_number}: {line.rstrip()}")
                    line_number += 1
                    if line_number > 5:  # Limit output
                        print("... (truncated)")
                        break
        except Exception as e:
            print(f"Error reading file: {e}")
        
        # Method 3: Read all lines into list
        print("\n3. Reading all lines into list:")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                lines = file.readlines()
                print(f"Total lines: {len(lines)}")
                print(f"First line: {lines[0].rstrip()}")
                print(f"Last line: {lines[-1].rstrip()}")
        except Exception as e:
            print(f"Error reading file: {e}")
        
        # Method 4: Read specific number of characters
        print("\n4. Reading specific number of characters:")
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                chunk = file.read(50)
                print(f"First 50 characters: '{chunk}'")
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def demonstrate_basic_writing(self):
        """Demonstrate basic file writing techniques"""
        print("\n=== Basic File Writing ===")
        
        # Method 1: Write text to file (overwrite)
        print("1. Writing text to file (overwrite mode):")
        try:
            output_file = self.demo_directory / "output1.txt"
            with open(output_file, "w", encoding="utf-8") as file:
                file.write("This is line 1\n")
                file.write("This is line 2\n")
                file.write("This is line 3\n")
            print(f"Successfully wrote to: {output_file}")
            
            # Verify content
            with open(output_file, "r", encoding="utf-8") as file:
                content = file.read()
                print(f"File content:\n{content}")
        except Exception as e:
            print(f"Error writing file: {e}")
        
        # Method 2: Append to file
        print("\n2. Appending to file:")
        try:
            output_file = self.demo_directory / "output1.txt"
            with open(output_file, "a", encoding="utf-8") as file:
                file.write("This is appended line 4\n")
                file.write("This is appended line 5\n")
            print(f"Successfully appended to: {output_file}")
            
            # Show updated content
            with open(output_file, "r", encoding="utf-8") as file:
                lines = file.readlines()
                print(f"Updated file has {len(lines)} lines")
                print(f"Last line: {lines[-1].rstrip()}")
        except Exception as e:
            print(f"Error appending to file: {e}")
        
        # Method 3: Write list of lines
        print("\n3. Writing list of lines:")
        try:
            output_file = self.demo_directory / "output2.txt"
            lines = [
                "Line 1: Introduction\n",
                "Line 2: Main content\n",
                "Line 3: Conclusion\n",
                "Line 4: End of file\n"
            ]
            
            with open(output_file, "w", encoding="utf-8") as file:
                file.writelines(lines)
            print(f"Successfully wrote lines to: {output_file}")
        except Exception as e:
            print(f"Error writing lines: {e}")
    
    def demonstrate_error_handling(self):
        """Demonstrate comprehensive error handling"""
        print("\n=== File Error Handling ===")
        
        # Test 1: File not found
        print("1. Testing FileNotFoundError:")
        try:
            with open("nonexistent_file.txt", "r") as file:
                content = file.read()
        except FileNotFoundError as e:
            print(f"Caught FileNotFoundError: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
        
        # Test 2: Permission error (try to write to protected directory)
        print("\n2. Testing PermissionError:")
        try:
            # Try to write to root directory (usually protected)
            protected_file = "/root/test_file.txt" if os.name == "posix" else "C:\\Windows\\test_file.txt"
            with open(protected_file, "w") as file:
                file.write("This should fail")
        except PermissionError as e:
            print(f"Caught PermissionError: {e}")
        except FileNotFoundError as e:
            print(f"Directory doesn't exist: {e}")
        except Exception as e:
            print(f"Other error: {e}")
        
        # Test 3: Encoding error
        print("\n3. Testing UnicodeDecodeError:")
        try:
            # Create a file with binary data
            binary_file = self.demo_directory / "binary_test.dat"
            with open(binary_file, "wb") as file:
                file.write(b'\xff\xfe\x00\x01\x02\x03')
            
            # Try to read as text
            with open(binary_file, "r", encoding="utf-8") as file:
                content = file.read()
        except UnicodeDecodeError as e:
            print(f"Caught UnicodeDecodeError: {e}")
        except Exception as e:
            print(f"Other error: {e}")
        
        # Test 4: Robust file operation with multiple exception handling
        print("\n4. Robust file operation:")
        self.robust_file_operation("test_robust.txt", "This is robust content")
    
    def robust_file_operation(self, filename, content):
        """Demonstrate robust file operation with comprehensive error handling"""
        file_path = self.demo_directory / filename
        
        try:
            # Ensure directory exists
            file_path.parent.mkdir(parents=True, exist_ok=True)
            
            # Write file with backup
            backup_path = file_path.with_suffix(file_path.suffix + ".backup")
            
            # If file exists, create backup
            if file_path.exists():
                shutil.copy2(file_path, backup_path)
                print(f"Created backup: {backup_path}")
            
            # Write new content
            with open(file_path, "w", encoding="utf-8") as file:
                file.write(content)
            
            print(f"Successfully wrote to: {file_path}")
            
            # Verify write was successful
            with open(file_path, "r", encoding="utf-8") as file:
                written_content = file.read()
                if written_content == content:
                    print("Write verification successful")
                else:
                    print("Write verification failed!")
        
        except PermissionError:
            print(f"Permission denied: Cannot write to {file_path}")
        except OSError as e:
            print(f"OS error occurred: {e}")
        except Exception as e:
            print(f"Unexpected error: {e}")
            # Restore from backup if it exists
            if backup_path.exists():
                try:
                    shutil.copy2(backup_path, file_path)
                    print("Restored from backup")
                except Exception as restore_error:
                    print(f"Failed to restore from backup: {restore_error}")


class CSVFileOperations:
    """Demonstrates CSV file operations"""
    
    def __init__(self):
        self.demo_directory = Path("file_demo")
        self.demo_directory.mkdir(exist_ok=True)
    
    def demonstrate_csv_operations(self):
        """Demonstrate CSV reading and writing"""
        print("\n=== CSV File Operations ===")
        
        # Sample data
        sample_data = [
            ["Name", "Age", "City", "Email"],
            ["Alice Johnson", "28", "New York", "alice@email.com"],
            ["Bob Smith", "34", "Los Angeles", "bob@email.com"],
            ["Carol Davis", "22", "Chicago", "carol@email.com"],
            ["David Wilson", "45", "Houston", "david@email.com"],
            ["Eve Brown", "31", "Phoenix", "eve@email.com"]
        ]
        
        # Write CSV file
        csv_file = self.demo_directory / "people.csv"
        self.write_csv_file(csv_file, sample_data)
        
        # Read CSV file
        self.read_csv_file(csv_file)
        
        # Demonstrate CSV with different delimiters
        self.demonstrate_custom_csv()
        
        # Demonstrate DictReader/DictWriter
        self.demonstrate_dict_csv()
    
    def write_csv_file(self, file_path, data):
        """Write data to CSV file"""
        print(f"\n1. Writing CSV file: {file_path}")
        
        try:
            with open(file_path, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file)
                writer.writerows(data)
            
            print(f"Successfully wrote {len(data)} rows to CSV")
        except Exception as e:
            print(f"Error writing CSV: {e}")
    
    def read_csv_file(self, file_path):
        """Read and display CSV file"""
        print(f"\n2. Reading CSV file: {file_path}")
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                reader = csv.reader(file)
                
                for row_num, row in enumerate(reader, 1):
                    print(f"Row {row_num}: {row}")
                    if row_num > 5:  # Limit output
                        break
        except Exception as e:
            print(f"Error reading CSV: {e}")
    
    def demonstrate_custom_csv(self):
        """Demonstrate CSV with custom delimiter and quoting"""
        print("\n3. Custom CSV format (tab-delimited):")
        
        data = [
            ["Product", "Price", "Description"],
            ["Widget A", "19.99", "A useful widget"],
            ["Gadget B", "29.99", "An amazing gadget"],
            ["Tool C", "39.99", "A powerful tool"]
        ]
        
        tab_csv_file = self.demo_directory / "products.tsv"
        
        try:
            # Write with tab delimiter
            with open(tab_csv_file, "w", newline="", encoding="utf-8") as file:
                writer = csv.writer(file, delimiter="\t", quoting=csv.QUOTE_MINIMAL)
                writer.writerows(data)
            
            print(f"Wrote tab-delimited file: {tab_csv_file}")
            
            # Read back
            with open(tab_csv_file, "r", encoding="utf-8") as file:
                reader = csv.reader(file, delimiter="\t")
                for row in reader:
                    print(f"  {row}")
        except Exception as e:
            print(f"Error with custom CSV: {e}")
    
    def demonstrate_dict_csv(self):
        """Demonstrate CSV operations using DictReader/DictWriter"""
        print("\n4. CSV operations with dictionaries:")
        
        # Sample data as list of dictionaries
        people_data = [
            {"name": "Frank Miller", "age": 35, "city": "Seattle", "email": "frank@email.com"},
            {"name": "Grace Lee", "age": 27, "city": "Portland", "email": "grace@email.com"},
            {"name": "Henry Kim", "age": 42, "city": "Denver", "email": "henry@email.com"}
        ]
        
        dict_csv_file = self.demo_directory / "people_dict.csv"
        
        try:
            # Write using DictWriter
            with open(dict_csv_file, "w", newline="", encoding="utf-8") as file:
                fieldnames = ["name", "age", "city", "email"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                
                writer.writeheader()  # Write column headers
                writer.writerows(people_data)
            
            print(f"Wrote dictionary CSV: {dict_csv_file}")
            
            # Read using DictReader
            with open(dict_csv_file, "r", encoding="utf-8") as file:
                reader = csv.DictReader(file)
                
                print("Reading as dictionaries:")
                for row in reader:
                    print(f"  {row['name']}: {row['age']} years old, lives in {row['city']}")
        except Exception as e:
            print(f"Error with dictionary CSV: {e}")


class JSONFileOperations:
    """Demonstrates JSON file operations"""
    
    def __init__(self):
        self.demo_directory = Path("file_demo")
        self.demo_directory.mkdir(exist_ok=True)
    
    def demonstrate_json_operations(self):
        """Demonstrate JSON reading and writing"""
        print("\n=== JSON File Operations ===")
        
        # Sample complex data structure
        sample_data = {
            "application": {
                "name": "File Demo App",
                "version": "1.0.0",
                "author": "CSC 242 Student"
            },
            "users": [
                {
                    "id": 1,
                    "username": "alice123",
                    "profile": {
                        "first_name": "Alice",
                        "last_name": "Johnson",
                        "age": 28,
                        "email": "alice@email.com",
                        "preferences": {
                            "theme": "dark",
                            "notifications": True,
                            "language": "en"
                        }
                    },
                    "last_login": "2024-01-15T10:30:00Z"
                },
                {
                    "id": 2,
                    "username": "bob456",
                    "profile": {
                        "first_name": "Bob",
                        "last_name": "Smith",
                        "age": 34,
                        "email": "bob@email.com",
                        "preferences": {
                            "theme": "light",
                            "notifications": False,
                            "language": "en"
                        }
                    },
                    "last_login": "2024-01-14T15:45:00Z"
                }
            ],
            "settings": {
                "max_users": 1000,
                "debug_mode": False,
                "allowed_domains": ["email.com", "company.com"],
                "rate_limits": {
                    "requests_per_minute": 60,
                    "requests_per_hour": 1000
                }
            },
            "metadata": {
                "created": "2024-01-01T00:00:00Z",
                "last_modified": "2024-01-15T12:00:00Z"
            }
        }
        
        # Write JSON file
        json_file = self.demo_directory / "app_data.json"
        self.write_json_file(json_file, sample_data)
        
        # Read JSON file
        self.read_json_file(json_file)
        
        # Demonstrate JSON manipulation
        self.demonstrate_json_manipulation(json_file)
        
        # Demonstrate error handling
        self.demonstrate_json_errors()
    
    def write_json_file(self, file_path, data):
        """Write data to JSON file"""
        print(f"\n1. Writing JSON file: {file_path}")
        
        try:
            with open(file_path, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            print("Successfully wrote JSON data")
            
            # Show file size
            file_size = file_path.stat().st_size
            print(f"File size: {file_size} bytes")
        except Exception as e:
            print(f"Error writing JSON: {e}")
    
    def read_json_file(self, file_path):
        """Read and display JSON file"""
        print(f"\n2. Reading JSON file: {file_path}")
        
        try:
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            print("Successfully loaded JSON data")
            print(f"Application: {data['application']['name']} v{data['application']['version']}")
            print(f"Number of users: {len(data['users'])}")
            
            # Display first user
            if data['users']:
                user = data['users'][0]
                print(f"First user: {user['profile']['first_name']} {user['profile']['last_name']}")
                print(f"  Email: {user['profile']['email']}")
                print(f"  Preferences: {user['profile']['preferences']}")
        except Exception as e:
            print(f"Error reading JSON: {e}")
    
    def demonstrate_json_manipulation(self, file_path):
        """Demonstrate JSON data manipulation"""
        print("\n3. JSON data manipulation:")
        
        try:
            # Load data
            with open(file_path, "r", encoding="utf-8") as file:
                data = json.load(file)
            
            # Add a new user
            new_user = {
                "id": 3,
                "username": "carol789",
                "profile": {
                    "first_name": "Carol",
                    "last_name": "Davis",
                    "age": 22,
                    "email": "carol@email.com",
                    "preferences": {
                        "theme": "auto",
                        "notifications": True,
                        "language": "es"
                    }
                },
                "last_login": "2024-01-16T08:15:00Z"
            }
            
            data['users'].append(new_user)
            
            # Update metadata
            data['metadata']['last_modified'] = datetime.now().isoformat() + "Z"
            
            # Save modified data
            modified_file = self.demo_directory / "app_data_modified.json"
            with open(modified_file, "w", encoding="utf-8") as file:
                json.dump(data, file, indent=2, ensure_ascii=False)
            
            print(f"Added new user and saved to: {modified_file}")
            print(f"Total users now: {len(data['users'])}")
        except Exception as e:
            print(f"Error manipulating JSON: {e}")
    
    def demonstrate_json_errors(self):
        """Demonstrate JSON error handling"""
        print("\n4. JSON error handling:")
        
        # Create invalid JSON file
        invalid_json_file = self.demo_directory / "invalid.json"
        
        try:
            with open(invalid_json_file, "w") as file:
                file.write('{"name": "test", "age": 25, "invalid": }')  # Missing value
            
            # Try to read invalid JSON
            with open(invalid_json_file, "r") as file:
                data = json.load(file)
        except json.JSONDecodeError as e:
            print(f"Caught JSONDecodeError: {e}")
            print(f"Error at line {e.lineno}, column {e.colno}")
        except Exception as e:
            print(f"Other error: {e}")
        
        # Demonstrate handling non-serializable objects
        try:
            class CustomObject:
                def __init__(self, name):
                    self.name = name
            
            non_serializable_data = {
                "object": CustomObject("test"),
                "function": lambda x: x + 1
            }
            
            json.dumps(non_serializable_data)
        except TypeError as e:
            print(f"Caught TypeError (non-serializable): {e}")


class BinaryFileOperations:
    """Demonstrates binary file operations"""
    
    def __init__(self):
        self.demo_directory = Path("file_demo")
        self.demo_directory.mkdir(exist_ok=True)
    
    def demonstrate_binary_operations(self):
        """Demonstrate binary file operations"""
        print("\n=== Binary File Operations ===")
        
        # Demonstrate pickle operations
        self.demonstrate_pickle()
        
        # Demonstrate raw binary operations
        self.demonstrate_raw_binary()
        
        # Demonstrate file copying
        self.demonstrate_file_copying()
    
    def demonstrate_pickle(self):
        """Demonstrate Python object serialization with pickle"""
        print("\n1. Pickle operations (Python object serialization):")
        
        # Create complex Python objects
        data = {
            "numbers": [1, 2, 3, 4, 5],
            "text": "Hello, pickle!",
            "nested": {
                "list": ["a", "b", "c"],
                "tuple": (1, 2, 3),
                "set": {10, 20, 30}
            },
            "datetime": datetime.now()
        }
        
        pickle_file = self.demo_directory / "data.pickle"
        
        try:
            # Write (serialize) objects
            with open(pickle_file, "wb") as file:
                pickle.dump(data, file)
            
            print(f"Pickled data to: {pickle_file}")
            
            # Read (deserialize) objects
            with open(pickle_file, "rb") as file:
                loaded_data = pickle.load(file)
            
            print("Successfully unpickled data:")
            print(f"  Numbers: {loaded_data['numbers']}")
            print(f"  Text: {loaded_data['text']}")
            print(f"  Nested list: {loaded_data['nested']['list']}")
            print(f"  Datetime: {loaded_data['datetime']}")
        except Exception as e:
            print(f"Error with pickle operations: {e}")
    
    def demonstrate_raw_binary(self):
        """Demonstrate raw binary file operations"""
        print("\n2. Raw binary operations:")
        
        binary_file = self.demo_directory / "binary_data.bin"
        
        try:
            # Write binary data
            binary_data = bytes([0, 1, 2, 3, 255, 254, 253, 252])
            text_bytes = "Hello, binary world! 🌍".encode("utf-8")
            
            with open(binary_file, "wb") as file:
                file.write(binary_data)
                file.write(text_bytes)
            
            print(f"Wrote binary data to: {binary_file}")
            
            # Read binary data
            with open(binary_file, "rb") as file:
                # Read first 8 bytes
                first_chunk = file.read(8)
                print(f"First 8 bytes: {list(first_chunk)}")
                
                # Read remaining bytes and decode as text
                remaining_bytes = file.read()
                text = remaining_bytes.decode("utf-8")
                print(f"Text portion: {text}")
        except Exception as e:
            print(f"Error with binary operations: {e}")
    
    def demonstrate_file_copying(self):
        """Demonstrate file copying operations"""
        print("\n3. File copying operations:")
        
        source_file = self.demo_directory / "sample.txt"
        
        if source_file.exists():
            try:
                # Method 1: Using shutil.copy2 (preserves metadata)
                copy1 = self.demo_directory / "sample_copy1.txt"
                shutil.copy2(source_file, copy1)
                print(f"Copied with metadata: {copy1}")
                
                # Method 2: Manual binary copy
                copy2 = self.demo_directory / "sample_copy2.txt"
                with open(source_file, "rb") as src, open(copy2, "wb") as dst:
                    chunk_size = 4096
                    while True:
                        chunk = src.read(chunk_size)
                        if not chunk:
                            break
                        dst.write(chunk)
                
                print(f"Manual binary copy: {copy2}")
                
                # Verify copies are identical
                with open(source_file, "rb") as f1, \
                     open(copy1, "rb") as f2, \
                     open(copy2, "rb") as f3:
                    
                    data1 = f1.read()
                    data2 = f2.read()
                    data3 = f3.read()
                    
                    if data1 == data2 == data3:
                        print("All copies are identical ✓")
                    else:
                        print("Copies differ ✗")
            except Exception as e:
                print(f"Error copying files: {e}")
        else:
            print(f"Source file not found: {source_file}")


class FileSystemOperations:
    """Demonstrates file system operations"""
    
    def __init__(self):
        self.demo_directory = Path("file_demo")
        self.demo_directory.mkdir(exist_ok=True)
    
    def demonstrate_filesystem_operations(self):
        """Demonstrate various file system operations"""
        print("\n=== File System Operations ===")
        
        self.demonstrate_path_operations()
        self.demonstrate_directory_operations()
        self.demonstrate_file_metadata()
        self.demonstrate_temp_files()
    
    def demonstrate_path_operations(self):
        """Demonstrate path manipulation"""
        print("\n1. Path operations:")
        
        # Path construction and manipulation
        file_path = Path("documents") / "projects" / "myfile.txt"
        print(f"Constructed path: {file_path}")
        print(f"Parent directory: {file_path.parent}")
        print(f"Filename: {file_path.name}")
        print(f"Stem (without extension): {file_path.stem}")
        print(f"Suffix (extension): {file_path.suffix}")
        
        # Absolute path
        abs_path = file_path.resolve()
        print(f"Absolute path: {abs_path}")
        
        # Path parts
        print(f"Path parts: {file_path.parts}")
        
        # Check path properties
        current_file = Path(__file__)
        print(f"\nCurrent script: {current_file}")
        print(f"Is file: {current_file.is_file()}")
        print(f"Is directory: {current_file.is_dir()}")
        print(f"Exists: {current_file.exists()}")
    
    def demonstrate_directory_operations(self):
        """Demonstrate directory operations"""
        print("\n2. Directory operations:")
        
        # Create nested directories
        nested_dir = self.demo_directory / "level1" / "level2" / "level3"
        nested_dir.mkdir(parents=True, exist_ok=True)
        print(f"Created nested directory: {nested_dir}")
        
        # List directory contents
        print(f"\nContents of {self.demo_directory}:")
        try:
            for item in self.demo_directory.iterdir():
                item_type = "DIR" if item.is_dir() else "FILE"
                size = item.stat().st_size if item.is_file() else "-"
                print(f"  {item_type:4} {size:>8} {item.name}")
        except Exception as e:
            print(f"Error listing directory: {e}")
        
        # Find files with glob patterns
        print(f"\nText files in {self.demo_directory}:")
        for txt_file in self.demo_directory.glob("*.txt"):
            print(f"  {txt_file.name}")
        
        print(f"\nAll files recursively:")
        for file_path in self.demo_directory.rglob("*"):
            if file_path.is_file():
                relative_path = file_path.relative_to(self.demo_directory)
                print(f"  {relative_path}")
    
    def demonstrate_file_metadata(self):
        """Demonstrate file metadata operations"""
        print("\n3. File metadata:")
        
        sample_file = self.demo_directory / "sample.txt"
        if sample_file.exists():
            try:
                stat = sample_file.stat()
                
                print(f"File: {sample_file}")
                print(f"Size: {stat.st_size} bytes")
                print(f"Created: {datetime.fromtimestamp(stat.st_ctime)}")
                print(f"Modified: {datetime.fromtimestamp(stat.st_mtime)}")
                print(f"Accessed: {datetime.fromtimestamp(stat.st_atime)}")
                
                # File permissions (Unix-like systems)
                if hasattr(stat, 'st_mode'):
                    import stat as stat_module
                    mode = stat.st_mode
                    print(f"Permissions: {stat_module.filemode(mode)}")
                
                # Check if file is readable/writable
                print(f"Readable: {os.access(sample_file, os.R_OK)}")
                print(f"Writable: {os.access(sample_file, os.W_OK)}")
                print(f"Executable: {os.access(sample_file, os.X_OK)}")
            except Exception as e:
                print(f"Error getting file metadata: {e}")
        else:
            print(f"Sample file not found: {sample_file}")
    
    def demonstrate_temp_files(self):
        """Demonstrate temporary file operations"""
        print("\n4. Temporary file operations:")
        
        # Create temporary file
        try:
            with tempfile.NamedTemporaryFile(mode='w+', suffix='.txt', delete=False) as temp_file:
                temp_file.write("This is temporary content\n")
                temp_file.write("It will be deleted after demonstration\n")
                temp_path = temp_file.name
            
            print(f"Created temporary file: {temp_path}")
            
            # Read from temporary file
            with open(temp_path, 'r') as temp_file:
                content = temp_file.read()
                print(f"Temporary file content:\n{content}")
            
            # Clean up
            os.unlink(temp_path)
            print("Temporary file deleted")
        except Exception as e:
            print(f"Error with temporary file: {e}")
        
        # Create temporary directory
        try:
            with tempfile.TemporaryDirectory() as temp_dir:
                temp_dir_path = Path(temp_dir)
                print(f"Created temporary directory: {temp_dir_path}")
                
                # Create files in temporary directory
                (temp_dir_path / "temp1.txt").write_text("Temporary file 1")
                (temp_dir_path / "temp2.txt").write_text("Temporary file 2")
                
                print("Files in temporary directory:")
                for file_path in temp_dir_path.iterdir():
                    print(f"  {file_path.name}")
            
            print("Temporary directory automatically deleted")
        except Exception as e:
            print(f"Error with temporary directory: {e}")


class FileGUIIntegration:
    """Demonstrates file operations integrated with GUI"""
    
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("File Operations GUI Demo")
        self.root.geometry("700x600")
        
        self.current_file = None
        self.file_content = ""
        
        self.setup_widgets()
    
    def setup_widgets(self):
        """Setup GUI widgets"""
        # Menu bar
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        
        file_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", command=self.new_file)
        file_menu.add_command(label="Open Text File", command=self.open_text_file)
        file_menu.add_command(label="Open CSV File", command=self.open_csv_file)
        file_menu.add_command(label="Open JSON File", command=self.open_json_file)
        file_menu.add_separator()
        file_menu.add_command(label="Save", command=self.save_file)
        file_menu.add_command(label="Save As", command=self.save_as_file)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", command=self.root.quit)
        
        # Toolbar
        toolbar = tk.Frame(self.root, relief="raised", borderwidth=1)
        toolbar.pack(fill="x")
        
        tk.Button(toolbar, text="New", command=self.new_file).pack(side="left", padx=2)
        tk.Button(toolbar, text="Open", command=self.open_text_file).pack(side="left", padx=2)
        tk.Button(toolbar, text="Save", command=self.save_file).pack(side="left", padx=2)
        
        # Main content area
        content_frame = tk.Frame(self.root)
        content_frame.pack(fill="both", expand=True, padx=5, pady=5)
        
        # File info display
        info_frame = tk.LabelFrame(content_frame, text="File Information")
        info_frame.pack(fill="x", pady=(0, 5))
        
        self.file_info_label = tk.Label(info_frame, text="No file loaded", anchor="w")
        self.file_info_label.pack(fill="x", padx=5, pady=5)
        
        # Text editor
        editor_frame = tk.LabelFrame(content_frame, text="Content Editor")
        editor_frame.pack(fill="both", expand=True)
        
        self.text_editor = scrolledtext.ScrolledText(editor_frame, 
                                                    wrap=tk.WORD,
                                                    font=("Courier", 11))
        self.text_editor.pack(fill="both", expand=True, padx=5, pady=5)
        
        # Bind text change events
        self.text_editor.bind("<KeyPress>", self.on_text_change)
        
        # Status bar
        self.status_bar = tk.Label(self.root, text="Ready", relief="sunken", anchor="w")
        self.status_bar.pack(fill="x", side="bottom")
        
        # Track if file has been modified
        self.is_modified = False
    
    def new_file(self):
        """Create a new file"""
        if self.check_save_changes():
            self.text_editor.delete("1.0", tk.END)
            self.current_file = None
            self.is_modified = False
            self.update_file_info()
            self.status_bar.config(text="New file created")
    
    def open_text_file(self):
        """Open a text file"""
        if not self.check_save_changes():
            return
        
        file_path = filedialog.askopenfilename(
            title="Open Text File",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    content = file.read()
                
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", content)
                
                self.current_file = file_path
                self.is_modified = False
                self.update_file_info()
                self.status_bar.config(text=f"Opened: {Path(file_path).name}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open file:\n{e}")
    
    def open_csv_file(self):
        """Open and display CSV file"""
        file_path = filedialog.askopenfilename(
            title="Open CSV File",
            filetypes=[("CSV files", "*.csv"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                content = []
                with open(file_path, 'r', encoding='utf-8') as file:
                    reader = csv.reader(file)
                    for row_num, row in enumerate(reader, 1):
                        content.append(f"Row {row_num}: {', '.join(row)}")
                
                display_content = "\n".join(content)
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", f"CSV File: {Path(file_path).name}\n")
                self.text_editor.insert(tk.END, "=" * 50 + "\n")
                self.text_editor.insert(tk.END, display_content)
                
                self.status_bar.config(text=f"Displayed CSV: {Path(file_path).name}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open CSV file:\n{e}")
    
    def open_json_file(self):
        """Open and display JSON file"""
        file_path = filedialog.askopenfilename(
            title="Open JSON File",
            filetypes=[("JSON files", "*.json"), ("All files", "*.*")]
        )
        
        if file_path:
            try:
                with open(file_path, 'r', encoding='utf-8') as file:
                    data = json.load(file)
                
                # Pretty print JSON
                formatted_json = json.dumps(data, indent=2, ensure_ascii=False)
                
                self.text_editor.delete("1.0", tk.END)
                self.text_editor.insert("1.0", f"JSON File: {Path(file_path).name}\n")
                self.text_editor.insert(tk.END, "=" * 50 + "\n")
                self.text_editor.insert(tk.END, formatted_json)
                
                self.status_bar.config(text=f"Displayed JSON: {Path(file_path).name}")
            except json.JSONDecodeError as e:
                messagebox.showerror("JSON Error", f"Invalid JSON file:\n{e}")
            except Exception as e:
                messagebox.showerror("Error", f"Could not open JSON file:\n{e}")
    
    def save_file(self):
        """Save the current file"""
        if self.current_file:
            self.save_to_file(self.current_file)
        else:
            self.save_as_file()
    
    def save_as_file(self):
        """Save file with a new name"""
        file_path = filedialog.asksaveasfilename(
            title="Save File As",
            defaultextension=".txt",
            filetypes=[
                ("Text files", "*.txt"),
                ("Python files", "*.py"),
                ("All files", "*.*")
            ]
        )
        
        if file_path:
            self.save_to_file(file_path)
            self.current_file = file_path
            self.update_file_info()
    
    def save_to_file(self, file_path):
        """Save content to specified file"""
        try:
            content = self.text_editor.get("1.0", tk.END)
            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(content)
            
            self.is_modified = False
            self.status_bar.config(text=f"Saved: {Path(file_path).name}")
        except Exception as e:
            messagebox.showerror("Error", f"Could not save file:\n{e}")
    
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
        self.update_file_info()
    
    def update_file_info(self):
        """Update file information display"""
        if self.current_file:
            file_path = Path(self.current_file)
            info = f"File: {file_path.name}"
            
            if file_path.exists():
                stat = file_path.stat()
                size = stat.st_size
                modified = datetime.fromtimestamp(stat.st_mtime)
                info += f" | Size: {size} bytes | Modified: {modified.strftime('%Y-%m-%d %H:%M:%S')}"
            
            if self.is_modified:
                info += " | Modified*"
        else:
            info = "New file"
            if self.is_modified:
                info += " | Modified*"
        
        self.file_info_label.config(text=info)
    
    def run(self):
        """Run the GUI application"""
        self.root.mainloop()


def main():
    """Main function to demonstrate file I/O operations"""
    print("File I/O Operations Demonstration")
    print("=================================")
    print("1. Basic File Operations")
    print("2. CSV File Operations")
    print("3. JSON File Operations")
    print("4. Binary File Operations")
    print("5. File System Operations")
    print("6. GUI File Integration")
    print("7. Run All Demos")
    
    choice = input("\nEnter your choice (1-7): ").strip()
    
    if choice == "1":
        demo = BasicFileOperations()
        demo.demonstrate_basic_reading()
        demo.demonstrate_basic_writing()
        demo.demonstrate_error_handling()
    
    elif choice == "2":
        demo = CSVFileOperations()
        demo.demonstrate_csv_operations()
    
    elif choice == "3":
        demo = JSONFileOperations()
        demo.demonstrate_json_operations()
    
    elif choice == "4":
        demo = BinaryFileOperations()
        demo.demonstrate_binary_operations()
    
    elif choice == "5":
        demo = FileSystemOperations()
        demo.demonstrate_filesystem_operations()
    
    elif choice == "6":
        app = FileGUIIntegration()
        app.run()
    
    elif choice == "7":
        # Run all non-GUI demos
        demos = [
            ("Basic File Operations", BasicFileOperations),
            ("CSV File Operations", CSVFileOperations),
            ("JSON File Operations", JSONFileOperations),
            ("Binary File Operations", BinaryFileOperations),
            ("File System Operations", FileSystemOperations)
        ]
        
        for name, demo_class in demos:
            print(f"\n{'='*50}")
            print(f"Running {name}...")
            print('='*50)
            
            demo = demo_class()
            if hasattr(demo, 'demonstrate_basic_reading'):
                demo.demonstrate_basic_reading()
                demo.demonstrate_basic_writing()
                demo.demonstrate_error_handling()
            elif hasattr(demo, 'demonstrate_csv_operations'):
                demo.demonstrate_csv_operations()
            elif hasattr(demo, 'demonstrate_json_operations'):
                demo.demonstrate_json_operations()
            elif hasattr(demo, 'demonstrate_binary_operations'):
                demo.demonstrate_binary_operations()
            elif hasattr(demo, 'demonstrate_filesystem_operations'):
                demo.demonstrate_filesystem_operations()
        
        print(f"\n{'='*50}")
        print("All demos completed!")
        print("To run the GUI demo, choose option 6")
    
    else:
        print("Invalid choice. Please run the script again.")


if __name__ == "__main__":
    main()
