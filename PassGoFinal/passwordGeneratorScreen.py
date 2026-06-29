# By Neil Patil
import tkinter as tk
from tkinter import messagebox
# Import the algorithm function from the separate file
from passwordGenerationAlgo import generate_password

from AppData import AppData

class PasswordGeneratorApp:
    def __init__(self, root, data: AppData):
        self.root = root
        # Window Title
        self.root.title("Password Generator - PassGo")
        
        # --- Set Background Color ---
        self.root.configure(bg="#e3eaf2")
        
        self.data = data

        # --- Window Dimensions ---
        self.window_width = 700
        self.window_height = 620 
        
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)

        # Initialize variables for character types
        self.include_lowercase = tk.BooleanVar(value=True) 
        self.include_uppercase = tk.BooleanVar(value=True)
        self.include_numbers = tk.BooleanVar(value=True)
        self.include_special = tk.BooleanVar(value=True)

        # Create UI elements
        self.create_widgets()
      
        # Auto-Center Logic
        self.center_window(self.window_width, self.window_height)

        # --- Exit Logic ---
        root.protocol("WM_DELETE_WINDOW", self.exit_app)

    def center_window(self, width, height):
        """Calculates and sets the position of the window to the center of the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))

        self.root.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

    def create_widgets(self):
        # Define fonts using Trebuchet MS
        main_font = ("Trebuchet MS", 11)
        title_font = ("Trebuchet MS", 12)
        note_font = ("Trebuchet MS", 9, "italic")
        button_font = ("Trebuchet MS", 11, "bold")
        display_font = ("Trebuchet MS", 16)
        back_button_font = ("Trebuchet MS", 10, "bold")

        # --- Header Section ---
        header_frame = tk.Frame(self.root, bg="#e3eaf2")
        header_frame.pack(fill="x", padx=30, pady=(20, 5))

        back_button = tk.Button(
            header_frame, 
            text="← Back to Home", 
            command=self.back_to_home, 
            bg="#e6f2ff", 
            activebackground="#cce5ff", 
            borderwidth=0, 
            font=back_button_font
        )
        back_button.pack(side="left")

        title_label = tk.Label(
            self.root, 
            text="Please fill in the following details about your password contents:", 
            font=title_font, 
            bg="#e3eaf2"
        )
        title_label.pack(pady=(10, 15))

        note_label = tk.Label(
            self.root, 
            text="Note: A password may be generated already with default settings. \n Passwords must be between 6 and 64 characters long. At least one character type must be selected.", 
            fg="gray", 
            font=note_font, 
            bg="#e3eaf2"
        )
        note_label.pack(anchor="w", padx=30, pady=(0, 20))

        # --- Input Options Frame ---
        options_frame = tk.Frame(self.root, bg="#e3eaf2")
        options_frame.pack(fill="x", padx=30, pady=5)

        # Minimum Length
        tk.Label(options_frame, text="Minimum Password Length:", font=main_font, bg="#e3eaf2").grid(row=0, column=0, sticky="w", pady=8)
        min_len_entry = tk.Entry(options_frame, width=8, justify="center", font=main_font)
        min_len_entry.insert(0, "6")
        min_len_entry.grid(row=0, column=1, sticky="w", padx=(15, 0), pady=8)
        self.min_len_var = min_len_entry 

        # Maximum Length
        tk.Label(options_frame, text="Maximum Password Length:", font=main_font, bg="#e3eaf2").grid(row=1, column=0, sticky="w", pady=8)
        max_len_entry = tk.Entry(options_frame, width=8, justify="center", font=main_font)
        max_len_entry.insert(0, "10")
        max_len_entry.grid(row=1, column=1, sticky="w", padx=(15, 0), pady=8)
        self.max_len_var = max_len_entry 

        # Uppercase Letters
        tk.Label(options_frame, text="Want Uppercase Letters?", font=main_font, bg="#e3eaf2").grid(row=2, column=0, sticky="w", pady=8)
        tk.Radiobutton(options_frame, text="Yes", variable=self.include_uppercase, value=True, font=main_font, bg="#e3eaf2").grid(row=2, column=1, sticky="w", padx=(15, 0), pady=8)
        tk.Radiobutton(options_frame, text="No", variable=self.include_uppercase, value=False, font=main_font, bg="#e3eaf2").grid(row=2, column=2, sticky="w", padx=(5, 0), pady=8)

        # Lowercase Letters
        tk.Label(options_frame, text="Want Lowercase Letters?", font=main_font, bg="#e3eaf2").grid(row=3, column=0, sticky="w", pady=8)
        tk.Radiobutton(options_frame, text="Yes", variable=self.include_lowercase, value=True, font=main_font, bg="#e3eaf2").grid(row=3, column=1, sticky="w", padx=(15, 0), pady=8)
        tk.Radiobutton(options_frame, text="No", variable=self.include_lowercase, value=False, font=main_font, bg="#e3eaf2").grid(row=3, column=2, sticky="w", padx=(5, 0), pady=8)

        # Numbers
        tk.Label(options_frame, text="Want Numbers?", font=main_font, bg="#e3eaf2").grid(row=4, column=0, sticky="w", pady=8)
        tk.Radiobutton(options_frame, text="Yes", variable=self.include_numbers, value=True, font=main_font, bg="#e3eaf2").grid(row=4, column=1, sticky="w", padx=(15, 0), pady=8)
        tk.Radiobutton(options_frame, text="No", variable=self.include_numbers, value=False, font=main_font, bg="#e3eaf2").grid(row=4, column=2, sticky="w", padx=(5, 0), pady=8)

        # Special Characters
        tk.Label(options_frame, text="Want Special Characters?", font=main_font, bg="#e3eaf2").grid(row=5, column=0, sticky="w", pady=8)
        tk.Radiobutton(options_frame, text="Yes", variable=self.include_special, value=True, font=main_font, bg="#e3eaf2").grid(row=5, column=1, sticky="w", padx=(15, 0), pady=8)
        tk.Radiobutton(options_frame, text="No", variable=self.include_special, value=False, font=main_font, bg="#e3eaf2").grid(row=5, column=2, sticky="w", padx=(5, 0), pady=8)

        # --- Action Buttons and Display Frame ---
        action_frame = tk.Frame(self.root, bg="#e3eaf2")
        action_frame.pack(fill="x", padx=30, pady=(30, 60))

        generate_button = tk.Button(
            action_frame, 
            text="Generate/Regenerate", 
            command=self.generate_password, 
            bg="#FFD700", 
            activebackground="#FFC107", 
            font=button_font, 
            width=18
        )
        generate_button.grid(row=0, column=0, padx=(0, 15), pady=5)

        # Password Display Field
        self.password_display = tk.Entry(
            action_frame, 
            state="readonly", 
            font=display_font, 
            width=18, 
            justify="center", 
            bg="white"
        )
        self.password_display.grid(row=0, column=1, padx=10, pady=5)

        # Copy Password Button
        copy_button = tk.Button(
            action_frame, 
            text="Copy Password", 
            command=self.copy_password, 
            bg="#FFA500", 
            activebackground="#FF8C00", 
            font=button_font, 
            width=14
        )
        copy_button.grid(row=0, column=2, padx=(15, 0), pady=5)

        # Save Password Button
        save_button = tk.Button(
            action_frame, 
            text="Save Password", 
            command=self.save_password, 
            bg="#FFA500", 
            activebackground="#FF8C00", 
            font=button_font, 
            width=14
        )
        save_button.grid(row=1, column=2, padx=(15, 0), pady=(0, 5))

        # Generate initial password on startup
        self.generate_password()

    def generate_password(self):
        """
        Retrieves input from GUI and calls the external algorithm.
        Handles errors returned by the algorithm.
        """
        try:
            # Get values from GUI
            min_len = self.min_len_var.get()
            max_len = self.max_len_var.get()
            
            # Call the external algorithm
            generated_password = generate_password(
                min_len=min_len,
                max_len=max_len,
                include_lower=self.include_lowercase.get(),
                include_upper=self.include_uppercase.get(),
                include_numbers=self.include_numbers.get(),
                include_special=self.include_special.get()
            )

            # Handle empty password case (if no boxes checked)
            if not generated_password:
                self.password_display.config(state="normal")
                self.password_display.delete(0, tk.END)
                self.password_display.config(state="readonly")
                return

            # Update Display
            self.password_display.config(state="normal")
            self.password_display.delete(0, tk.END)
            self.password_display.insert(0, generated_password)
            self.password_display.config(state="readonly")

        except ValueError as e:
            messagebox.showerror("Input Error", str(e))

    def copy_password(self):
        """Copies the displayed password to the clipboard and shows confirmation."""
        password = self.password_display.get()
        if password:
            self.root.clipboard_clear()
            self.root.clipboard_append(password)
            self.root.update() 
            messagebox.showinfo("Success", "Password copied to clipboard!")
        else:   
            messagebox.showwarning("Warning", "No password to copy. Please generate one first.")

    def save_password(self):
        """Opens the Save Password screen and passes the current password."""
        current_password = self.password_display.get()
        
        if not current_password:
            messagebox.showwarning("Warning", "No password to save. Please generate one first.")
            return

        # LAZY IMPORT: Moved inside function to prevent circular dependency
        from savePasswordScreen import SavePasswordApp

        # Close the current generator window
        self.root.destroy()
        
        # Create a new root window for the save screen
        new_root = tk.Tk()
        SavePasswordApp(new_root, generated_password=current_password, data = self.data)
        new_root.mainloop()

    def back_to_home(self):
        """Navigates back to home screen with confirmation."""
        confirm = messagebox.askyesno(
            "Confirm Exit", 
            "Are you sure you want to cancel the operation and go back to Home?"
        )
        if confirm:
            from homeScreen import PassGoHomeApp
            self.root.destroy()
            new_root = tk.Tk()
            PassGoHomeApp(new_root, self.data)
            new_root.mainloop()

    def exit_app(self):
        """Exits the application."""
        self.data.save_passwords()
        self.root.destroy()

def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()