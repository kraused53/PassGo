# By Andrew Hamade
import tkinter as tk
from tkinter import messagebox
import os
import csv

class SaveAndEditScreen:
    def __init__(self, root):
        self.root = root
        # Window Title
        self.root.title("Saved Passwords - PassGo")
        
        # --- Set Background Color ---
        self.root.configure(bg="#e3eaf2")
        
        # --- Window Dimensions ---
        self.window_width = 1000
        self.window_height = 620 
        
        self.root.geometry(f"{self.window_width}x{self.window_height}")
        self.root.resizable(False, False)

        # Create UI elements and Populate Passwords
        self.create_widgets()

        # Auto-Center Logic
        self.center_window(self.window_width, self.window_height)

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
        bold_title_font = ("Trebuchet MS", 12, "bold")
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
            text="Saved Passwords", 
            font=display_font, 
            bg="#e3eaf2"
        )
        title_label.pack(pady=(10, 15))

        # --- Platform Box ---
        platform_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        platform_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=20, padx=(20, 2.5), ipady=20, ipadx=20)

        platform_text_frame = tk.Frame(platform_frame, bg="white", bd=1, relief="solid")
        platform_text_frame.pack(fill=tk.X)

        platform_text_label = tk.Label(platform_text_frame, text="Platform", font=bold_title_font, bg="white", justify="center")
        platform_text_label.pack()

        # --- Password Box ---
        password_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        password_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=20, padx=(2.5), ipady=20, ipadx=20)

        password_text_frame = tk.Frame(password_frame, bg="white", bd=1, relief="solid")
        password_text_frame.pack(fill=tk.X)

        password_text_label = tk.Label(password_text_frame, text="Password", font=bold_title_font, bg="white", justify="center")
        password_text_label.pack()

        # --- Date Created Box ---
        date_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        date_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=20, padx=(2.5), ipady=20, ipadx=20)

        date_text_frame = tk.Frame(date_frame, bg="white", bd=1, relief="solid")
        date_text_frame.pack(fill=tk.X)

        date_text_label = tk.Label(date_text_frame, text="Date", font=bold_title_font, bg="white", justify="center")
        date_text_label.pack()

        # --- Options Box ---
        options_frame = tk.Frame(self.root, bg="white", bd=1, relief="solid")
        options_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, pady=20, padx=(2.5, 20), ipady=20, ipadx=20)

        options_text_frame = tk.Frame(options_frame, bg="white", bd=1, relief="solid")
        options_text_frame.pack(fill=tk.X)

        options_text_label = tk.Label(options_text_frame, text="Options", font=bold_title_font, bg="white", justify="center")
        options_text_label.pack()
        
        # --- Populating Passwords ---
        file = "passSave.csv"

        if os.path.exists(file):
            with open(file, "r") as fileR:
                csv_reader = csv.reader(fileR)
                for i in csv_reader:
                    platform = i[0]
                    password = i[1]
                    date = i[2]

                    # Platform Value
                    platform_text_frame = tk.Frame(platform_frame, bg="white", bd=1, relief="solid")
                    platform_text_frame.pack(fill=tk.X)

                    platform_text_label = tk.Label(platform_text_frame, text=platform, font=title_font, bg="white", justify="center")
                    platform_text_label.pack(ipady=5)

                    #Password Value
                    password_text_frame = tk.Frame(password_frame, bg="white", bd=1, relief="solid")
                    password_text_frame.pack(fill=tk.X)

                    password_text_label = tk.Label(password_text_frame, text=password, font=title_font, bg="white", justify="center")
                    password_text_label.pack(ipady=5)

                    #Date Value
                    date_text_frame = tk.Frame(date_frame, bg="white", bd=1, relief="solid")
                    date_text_frame.pack(fill=tk.X)

                    date_text_label = tk.Label(date_text_frame, text=date, font=title_font, bg="white", justify="center")
                    date_text_label.pack(ipady=5)

                    #Options
                    options_button_frame = tk.Frame(options_frame, bg="white", bd=1, relief="solid")
                    options_button_frame.pack(fill=tk.X)

                    options_button_center_frame = tk.Frame(options_button_frame, bg="white")
                    options_button_center_frame.pack()

                    edit_button = tk.Button(
                        options_button_center_frame, text="Edit", command=lambda plat=platform, pw=password: self.edit_password(plat, pw),
                        bg="#f7ad1b", activebackground="#fac255", borderwidth=0, font=back_button_font, width = 7
                    ).pack(side=tk.LEFT, padx=(0,10), pady=5)

                    copy_button = tk.Button(
                        options_button_center_frame, text="Copy", command=lambda pw=password: self.copy_password(pw),
                        bg="#ffd91c", activebackground="#ffe047", borderwidth=0, font=back_button_font, width = 7
                    ).pack(side=tk.LEFT, padx=10, pady=5)

                    delete_button = tk.Button(
                        options_button_center_frame, text="Delete", command=lambda plat=platform, pw=password, dt=date: self.delete_password(plat, pw, dt),
                        bg="#cc0000", activebackground="#db3535", borderwidth=0, font=back_button_font, width = 7
                    ).pack(side=tk.LEFT, padx=(10,0), pady=5)

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
            PassGoHomeApp(new_root)
            new_root.mainloop()

    def edit_password(self, platform, password):
        """Navigates to a password generation screen to edit an old password."""
        from editGenerationScreen import EditGeneratorApp
        self.root.destroy()
        new_root = tk.Tk()
        EditGeneratorApp(new_root, platform, password)
        new_root.mainloop()


    def copy_password(self, password):
        """Copies selected password to clipboard."""
        self.root.clipboard_clear()
        self.root.clipboard_append(password)
        self.root.update() 
        messagebox.showinfo("Success", "Password copied to clipboard!")

    def delete_password(self, platform, password, date):
        """Deletes passwords in passSave.csv"""
        file = "passSave.csv"
        newPasswordList = []

        if os.path.exists(file):
            with open(file, "r", newline='') as fileR:
                csv_reader = csv.reader(fileR)
                for i in csv_reader:
                    if (i != [platform, password, date]):
                        newPasswordList.append(i)

            with open(file, "w", newline='') as fileW:
                writer = csv.writer(fileW)
                writer.writerows(newPasswordList)


def main():
    root = tk.Tk()
    app = SaveAndEditScreen(root)
    root.mainloop()

if __name__ == "__main__":
    main()