import customtkinter as ctk
from tkinter import messagebox
from ui.dashboard import Dashboard

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

ACCENT = "#a855f7"
BG = "#050507"
CARD = "#0d0d12"
HOVER = "#17171f"

class LoginUI(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("520x320")
        self.resizable(False, False)

        self.title("Login Tool")

        self.configure(
            fg_color="#050507"
        )

        self.build()

    def build(self):

        card = ctk.CTkFrame(
            self,
            width=340,
            height=230,
            fg_color="#0d0d12",
            corner_radius=18,
            border_width=1,
            border_color="#20202a"
        )

        card.place(
            relx=0.5,
            rely=0.5,
            anchor="center"
        )

        title = ctk.CTkLabel(
            card,
            text="ToolSheptie",
            font=("Segoe UI Semibold", 24),
            text_color="white"
        )

        title.pack(
            pady=(28, 4)
        )

        sub = ctk.CTkLabel(
            card,
            text="Private Analysis Framework",
            font=("Segoe UI", 11),
            text_color="#8a8a95"
        )

        sub.pack(
            pady=(0, 20)
        )

        self.pin = ctk.CTkEntry(
            card,
            width=220,
            height=38,
            placeholder_text="Enter PIN",
            show="•",
            fg_color="#09090c",
            border_color="#262633",
            corner_radius=10
        )

        self.pin.pack()

        login_btn = ctk.CTkButton(
            card,
            text="LOGIN",
            width=220,
            height=36,
            fg_color=ACCENT,
            hover_color="#9333ea",
            corner_radius=10,
            font=("Segoe UI Semibold", 12),
            command=self.login
        )

        login_btn.pack(
            pady=20
        )

        footer = ctk.CTkLabel(
            card,
            text="v2 Framework",
            font=("Segoe UI", 10),
            text_color="#666"
        )

        footer.pack()

    def login(self):

        if self.pin.get() == "1313":

            self.destroy()

            app = Dashboard()
            app.mainloop()

        else:

            messagebox.showerror(
                "Access Denied",
                "Invalid PIN."
            )
