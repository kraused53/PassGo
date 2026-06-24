import tkinter as tk
from tkinter import ttk


class ScrollableTable(tk.Frame):
    """
    A scrollable two-column (Key | Value) table widget.

    Usage:
        table = ScrollableTable(parent, data=my_dict)
        table.pack(fill="both", expand=True)

    You can also update the data after creation:
        table.load(new_dict)
    """

    def __init__(self, parent, data: dict = None, **kwargs):
        super().__init__(parent, **kwargs)

        # --- Treeview + Scrollbar ---
        self._tree = ttk.Treeview(
            self,
            columns=("key", "value"),
            show="headings",          # hides the phantom first column
            selectmode="browse",
        )

        self._tree.heading("key",   text="Key")
        self._tree.heading("value", text="Value")

        self._tree.column("key",   anchor="w", width=180, minwidth=80)
        self._tree.column("value", anchor="w", width=260, minwidth=80)

        scrollbar = ttk.Scrollbar(self, orient="vertical", command=self._tree.yview)
        self._tree.configure(yscrollcommand=scrollbar.set)

        self._tree.grid(row=0, column=0, sticky="nsew")
        scrollbar.grid(row=0, column=1, sticky="ns")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(0, weight=1)

        # Alternating row colours
        self._tree.tag_configure("odd",  background="#f5f5f5")
        self._tree.tag_configure("even", background="#ffffff")
        self._tree.tag_configure("flash", background="#cce8ff")  # copy feedback

        # Double-click to copy the cell that was clicked
        self._tree.bind("<Double-1>", self._on_double_click)

        # Tooltip label (hidden until needed)
        self._tooltip = tk.Label(
            self, text="Copied!",
            background="#333333", foreground="#ffffff",
            relief="flat", padx=4, pady=2, font=("Segoe UI", 8),
        )

        if data:
            self.load(data)

    # ------------------------------------------------------------------
    # Copy helpers
    # ------------------------------------------------------------------

    def _on_double_click(self, event: tk.Event):
        """Identify which column was double-clicked and copy that cell's text."""
        row_id = self._tree.identify_row(event.y)
        col_id = self._tree.identify_column(event.x)   # returns '#1', '#2', …
        if not row_id or not col_id:
            return

        col_index = int(col_id.lstrip("#")) - 1        # 0 = key, 1 = value
        values = self._tree.item(row_id, "values")
        if col_index >= len(values):
            return

        text = values[col_index]
        self.clipboard_clear()
        self.clipboard_append(text)

        self._flash_row(row_id)
        self._show_tooltip(event.x_root, event.y_root, f'Copied: "{text}"')

    def _flash_row(self, row_id: str):
        """Briefly highlight the row, then restore its original tag."""
        original_tags = self._tree.item(row_id, "tags")
        self._tree.item(row_id, tags=("flash",))
        self.after(400, lambda: self._tree.item(row_id, tags=original_tags))

    def _show_tooltip(self, x: int, y: int, message: str):
        """Show a small 'Copied!' tooltip near the cursor, then fade it."""
        self._tooltip.config(text=message)
        self._tooltip.place(x=x - self.winfo_rootx() + 10,
                            y=y - self.winfo_rooty() - 24)
        self._tooltip.lift()
        self.after(1200, self._tooltip.place_forget)

    def load(self, data: dict):
        """Clear the table and populate it with a new dictionary."""
        self._tree.delete(*self._tree.get_children())
        for i, (k, v) in enumerate(data.items()):
            tag = "even" if i % 2 == 0 else "odd"
            self._tree.insert("", "end", values=(k, v), tags=(tag,))

    def update_entry(self, key, value):
        """Update the value for an existing key (linear scan)."""
        for item in self._tree.get_children():
            if self._tree.item(item, "values")[0] == str(key):
                self._tree.item(item, values=(key, value))
                return
        # Key not found — append it
        n = len(self._tree.get_children())
        tag = "even" if n % 2 == 0 else "odd"
        self._tree.insert("", "end", values=(key, value), tags=(tag,))


# ---------------------------------------------------------------------------
# Demo — run this file directly to see it in action
# ---------------------------------------------------------------------------
if __name__ == "__main__":
    sample_data = {
        "Name":        "Dan",
        "Language":    "Python",
        "Framework":   "Tkinter",
        "Version":     "3.12",
        "Platform":    "Windows",
        "Project":     "Book Repository",
        "Database":    "MySQL",
        "API":         "Open Library",
        "Theme":       "Dark",
        "Status":      "In Progress",
        "License":     "MIT",
        "Author":      "kraused53",
    }

    root = tk.Tk()
    root.title("Scrollable Key/Value Table")
    root.geometry("500x280")
    root.resizable(True, True)

    table = ScrollableTable(root, data=sample_data, padx=8, pady=8)
    table.pack(fill="both", expand=True)

    root.mainloop()