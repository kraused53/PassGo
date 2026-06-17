# By Neil Patil
import tkinter as tk
from tkinter import messagebox
import webbrowser

class PassGoHomeApp:
    def __init__(self, root):
        self.root = root
        # --- Window Configuration ---
        self.root.title("PassGo Home")
        self.root.configure(bg="#e3eaf2")
        
        self.window_width = 800
        self.window_height = 500 
        
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)
        self.center_window(self.window_width, self.window_height)

        # --- Fonts (Matching other screens) ---
        main_font = ("Trebuchet MS", 11)
        title_font = ("Trebuchet MS", 24, "bold")  
        note_font = ("Trebuchet MS", 11)            
        button_font = ("Trebuchet MS", 14, "bold")  
        exit_button_font = ("Trebuchet MS", 14, "bold")
        # Font for the link: Underlined
        link_font = ("Trebuchet MS", 11, "underline")

        # --- Header Section ---
        title_label = tk.Label(
            self.root, 
            text="PassGo Home", 
            font=title_font, 
            bg="#e3eaf2"
        )
        title_label.pack(pady=(30, 20))

        # --- Main Action Buttons Frame ---
        action_frame = tk.Frame(self.root, bg="#e3eaf2")
        action_frame.pack(fill="x", padx=40, pady=10)

        # Generate New Password Button
        gen_btn = tk.Button(
            action_frame, 
            text="Generate New Password", 
            command=self.open_generator,
            bg="#FFA500",              
            activebackground="#FF8C00", 
            fg="black",                
            font=button_font, 
            width=20,                  
            height=3,                  
            bd=0,                      
            relief="flat",
            cursor="hand2"
        )
        gen_btn.pack(side="left", expand=True, fill="both", padx=(0, 20))

        # View and Edit Saved Passwords Button
        view_btn = tk.Button(
            action_frame, 
            text="View and Edit\nSaved Passwords", 
            command=self.open_saved_passwords,
            bg="#FFA500", 
            activebackground="#FF8C00", 
            fg="black", 
            font=button_font, 
            width=20, 
            height=3, 
            bd=0, 
            relief="flat",
            cursor="hand2"
        )
        view_btn.pack(side="right", expand=True, fill="both", padx=(20, 0))

        # --- Info / Breach Check Box ---
        info_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        info_frame.pack(pady=20, padx=60, ipady=15, ipadx=10)

        link_text = "https://haveibeenpwned.com/"
        
        # Static text label
        info_label_text = tk.Label(
            info_frame, 
            text="Concerned about data breaches? Check if your email has been compromised:", 
            font=note_font, 
            bg="white", 
            justify="center"
        )
        info_label_text.pack()

        # Clickable link label with Aqua color and Underline
        info_label_link = tk.Label(
            info_frame, 
            text=link_text, 
            font=link_font, 
            bg="white", 
            fg="#00FFFF",  # Aqua color
            cursor="hand2"
        )
        info_label_link.pack()
        
        # Bind click event to the link label
        info_label_link.bind("<Button-1>", lambda e: webbrowser.open_new(link_text))

        # --- Exit Button  ---
        exit_btn = tk.Button(
            self.root, 
            text="Exit", 
            command=self.exit_app,
            bg="#990000",            
            activebackground="#7a0000", 
            fg="white",                
            font=exit_button_font, 
            width=15,                  
            height=2,                  
            bd=0, 
            relief="flat",
            cursor="hand2"
        )
        exit_btn.pack(pady=(10, 30))

    def center_window(self, width, height):
        """Calculates and sets the position of the window to the center of the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

    def open_generator(self):
        """Navigates to the Password Generator Screen."""
        from passwordGeneratorScreen import PasswordGeneratorApp
        self.root.destroy()
        new_root = tk.Tk()
        PasswordGeneratorApp(new_root)
        new_root.mainloop()

    def open_saved_passwords(self):
        """Placeholder for viewing saved passwords."""
        messagebox.showinfo("Coming Soon", "The 'View and Edit Saved Passwords' feature is under development.")

    def exit_app(self):
        """Exits the application."""
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    app = PassGoHomeApp(root)
    root.mainloop()