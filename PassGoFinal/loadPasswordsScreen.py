import tkinter as tk
from tkinter import messagebox
from FileIO import is_data_file_present

from AppData import AppData
import FileIO

class LoadPasswordsApp:
    def __init__(self, root, data: AppData):
        self.root = root
        # --- Window Configuration ---
        self.root.title("Load Saved Passwords")
        self.root.configure(bg="#e3eaf2")

        self.window_width = 800
        self.window_height = 500

        # App Data
        self.data = data

        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)
        self.center_window(self.window_width, self.window_height)

        # --- Fonts (Matching other screens) ---
        main_font = ("Trebuchet MS", 11)
        title_font = ("Trebuchet MS", 24, "bold")
        note_font = ("Trebuchet MS", 11)
        button_font = ("Trebuchet MS", 14, "bold")
        back_button_font = ("Trebuchet MS", 10, "bold")
        exit_button_font = ("Trebuchet MS", 14, "bold")
        # Font for the link: Underlined
        link_font = ("Trebuchet MS", 11, "underline")

        # --- Header Section ---
        header_frame = tk.Frame(self.root, bg="#e3eaf2")
        header_frame.pack(fill="x", padx=30, pady=(20, 5))

        if FileIO.is_data_file_present():
            title_txt = "Load Passwords"
        else:
            title_txt = "Register User"
        title_label = tk.Label(
            self.root,
            text=f"PassGo {title_txt}",
            font=title_font,
            bg="#e3eaf2"
        )
        title_label.pack(pady=(30, 20))

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

        # --- Main Action Buttons Frame ---
        action_frame = tk.Frame(self.root, bg="#e3eaf2")
        action_frame.pack(fill="x", padx=40, pady=10)

        if FileIO.is_data_file_present():
            btn_txt = "Load Passwords"
        else:
            btn_txt = "Register User"
        
        entry_box = tk.Entry(root, width=40, show="*")
        entry_box.pack(side="top",pady=10)

        # Get user password
        load_button = tk.Button(
            action_frame,
            text=btn_txt,
            command=lambda: self.load_passwords_file(entry_box.get()),
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
        load_button.pack(side="top", expand=False, fill="y", padx=(0, 0))

    def center_window(self, width, height):
        """Calculates and sets the position of the window to the center of the screen."""
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        x_coordinate = int((screen_width / 2) - (width / 2))
        y_coordinate = int((screen_height / 2) - (height / 2))
        self.root.geometry(f'{width}x{height}+{x_coordinate}+{y_coordinate}')

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

    def load_passwords_file(self, mpass: str):      
        self.data.set_master_password(mpass)
        self.data.set_user_logged_in()
        if is_data_file_present():
          self.data.load_passwords()
          messagebox.showinfo("Passwords Loaded", "You're passwords have been loaded!\nReturning you to home screen...")
        else:
            messagebox.showinfo("Passwords File Created", "You are now ready to store passwords!")
          
        if self.data.is_user_logged_in():
              from homeScreen import PassGoHomeApp
              self.root.destroy()
              new_root = tk.Tk()
              PassGoHomeApp(new_root, self.data)
              new_root.mainloop()


if __name__ == "__main__":
    root = tk.Tk()
    app = LoadPasswordsApp(root)
    root.mainloop()