import tkinter as tk
from tkinter import messagebox

from AppData import AppData
from ScrollTable import ScrollableTable

class ViewPasswordsApp:
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

        title_label = tk.Label(
            self.root,
            text="PassGo View Passwords",
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

        # If user is not logged in, add a text box
        if self.data.is_user_logged_in():
            table = ScrollableTable(
                action_frame,
                self.data.get_passwords()
            )
            table.pack(fill="both", expand=True)

            copy_note = tk.Label(
                self.root,
                text="Double Click An Item To Copy It",
                font=note_font,
                bg="#e3eaf2"
            )
            copy_note.pack(pady=(10, 15))
        else:
            not_logged_in_label = tk.Label(
                self.root,
                text="You are not logged in:",
                font=title_font,
                bg="#e3eaf2"
            )
            not_logged_in_label.pack(pady=(10, 15))

            load_btn = tk.Button(
                action_frame,
                text="Load You're Passwords",
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
            load_btn.pack(side="right", expand=True, fill="both", padx=(20, 0))


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

    def open_saved_passwords(self):
        """Placeholder for viewing saved passwords."""
        from loadPasswordsScreen import LoadPasswordsApp
        self.root.destroy()
        new_root = tk.Tk()
        LoadPasswordsApp(new_root, self.data)
        new_root.mainloop()


if __name__ == "__main__":
    pass