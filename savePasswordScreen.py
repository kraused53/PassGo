# By Neil Patil
import tkinter as tk
from tkinter import messagebox
# Import the save logic from your friend's file
from savePassword import save_password

class SavePasswordApp:
    def __init__(self, root, generated_password=""):
        self.root = root
        self.generated_password = generated_password
        
        # --- Window Configuration ---
        self.root.title("Save Password - PassGo")
        self.root.configure(bg="#e3eaf2")
        
        self.window_width = 700
        self.window_height = 370 
        
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)
        self.center_window(self.window_width, self.window_height)

        # --- Fonts ---
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
            command=self.navigate_back, 
            bg="#e6f2ff", 
            activebackground="#cce5ff", 
            borderwidth=0, 
            font=back_button_font
        )
        back_button.pack(side="left")

        title_label = tk.Label(
            self.root, 
            text="Please fill in the following details about your generated password:", 
            font=title_font, 
            bg="#e3eaf2"
        )
        title_label.pack(pady=(10, 15))

        # --- Input Options Frame (Centered) ---
        options_frame = tk.Frame(self.root, bg="#e3eaf2")
        options_frame.pack(anchor="center", pady=5)

        # Platform/Service Entry
        tk.Label(options_frame, text="Platform/Service:", font=main_font, bg="#e3eaf2").grid(row=0, column=0, sticky="w", pady=8)
        self.platform_entry = tk.Entry(
            options_frame, 
            width=20, 
            justify="center", 
            font=display_font  # Matched font size to password display for equal width
        )
        self.platform_entry.grid(row=0, column=1, sticky="w", padx=(15, 0), pady=8)

        # Password Created Display (Read-only)
        tk.Label(options_frame, text="Password Created:", font=main_font, bg="#e3eaf2").grid(row=1, column=0, sticky="w", pady=8)
        self.password_display = tk.Entry(
            options_frame, 
            state="readonly", 
            font=display_font, 
            width=20, 
            justify="center", 
            bg="white"
        )
        self.password_display.grid(row=1, column=1, sticky="w", padx=(15, 0), pady=8)
        
        # Populate the password field if passed from previous screen
        if self.generated_password:
            self.password_display.config(state="normal")
            self.password_display.insert(0, self.generated_password)
            self.password_display.config(state="readonly")

        # --- Action Buttons Frame (Centered Button) ---
        action_frame = tk.Frame(self.root, bg="#e3eaf2")
        action_frame.pack(anchor="center", pady=(20, 0))

        save_button = tk.Button(
            action_frame, 
            text="Save Password", 
            command=self.handle_save_password,  # Updated to call the handler
            bg="#FFA500", 
            activebackground="#FF8C00", 
            font=button_font, 
            width=18
        )
        # Centered using columnspan=2 to span across label and input columns
        save_button.grid(row=0, column=0, columnspan=2, pady=5) 

        # Bottom note with consolidated text
        bottom_note = tk.Label(
            self.root, 
            text='Note: To cancel, click "Back to Home" on the top left.\nOnly one password per platform/service is allowed.', 
            fg="gray", 
            font=note_font, 
            bg="#e3eaf2"
        )
        bottom_note.pack(pady=(5, 0))

    def center_window(self, width, height):
        """Calculates and sets the position of the window to the center of the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

    def handle_save_password(self):
        """Retrieves data from GUI and calls the external save function."""
        platform = self.platform_entry.get().strip()
        password = self.password_display.get()
        
        if not platform:
            messagebox.showwarning("Input Missing", "Please enter a Platform/Service name.")
            return
            
        # Call the external save function and handle success or failure
        try:
            save_password(platform, password)
            # Password Storage Team: Uncomment this once savePassword.py is updated
            # messagebox.showinfo("Success", f"Password for '{platform}' saved successfully!")
            # this is placeholder for us
            messagebox.showinfo("This feature is currently under development.")
        except Exception as e:
            messagebox.showerror("Save Error", f"Failed to save password: {str(e)}")

    def navigate_back(self):
        """Closes save screen and re-opens the home screen with confirmation."""
        confirm = messagebox.askyesno(
            "Confirm Exit", 
            "Are you sure you want to cancel the operation and go back to Home?"
        )
        if confirm:
            # LAZY IMPORT: Moved inside function to prevent circular dependency
            from homeScreen import PassGoHomeApp
            
            self.root.destroy()
            new_root = tk.Tk()
            PassGoHomeApp(new_root)
            new_root.mainloop()

# Example usage to test this file independently
if __name__ == "__main__":
    root = tk.Tk()
    app = SavePasswordApp(root, generated_password="qTs_iJ1G")
    root.mainloop()