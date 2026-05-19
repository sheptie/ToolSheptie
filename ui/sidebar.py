import customtkinter as ctk

ctk.set_appearance_mode("dark")


class Sidebar(ctk.CTkFrame):

    def __init__(self, parent, callback):

        super().__init__(
            parent,
            width=210,
            fg_color="#0b0b10",
            corner_radius=0
        )

        self.callback = callback

        self.pack_propagate(False)

        self.build()

    def add_button(self, text, cmd):

        btn = ctk.CTkButton(
            self,
            text=text,
            height=38,
            corner_radius=10,
            fg_color="#111118",
            hover_color="#7d4dff",
            text_color="white",
            font=("Segoe UI Semibold", 12),
            border_width=1,
            border_color="#1f1f2a",
            command=lambda: self.callback(cmd)
        )

        btn.pack(
            fill="x",
            padx=14,
            pady=5
        )

    def build(self):

        logo = ctk.CTkLabel(
            self,
            text="ToolSheptie",
            font=("Segoe UI Semibold", 24),
            text_color="#c084fc"
        )

        logo.pack(
            anchor="w",
            padx=18,
            pady=(18, 0)
        )

        desc = ctk.CTkLabel(
            self,
            text="Advanced Diagnostic Suite",
            font=("Segoe UI", 11),
            text_color="#7c7c8a"
        )

        desc.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )

        section1 = ctk.CTkLabel(
            self,
            text="SCANNERS",
            font=("Segoe UI Semibold", 10),
            text_color="#7d4dff"
        )

        section1.pack(
            anchor="w",
            padx=18,
            pady=(5, 8)
        )

        self.add_button(
            "Prefetch Scanner",
            "prefetch"
        )

        self.add_button(
            "Process Scanner",
            "processes"
        )

        self.add_button(
            "BAM Parser",
            "bam"
        )

        section2 = ctk.CTkLabel(
            self,
            text="TOOLS",
            font=("Segoe UI Semibold", 10),
            text_color="#7d4dff"
        )

        section2.pack(
            anchor="w",
            padx=18,
            pady=(18, 8)
        )

        self.add_button(
            "Everything",
            "everything"
        )

        self.add_button(
            "System Informer",
            "system"
        )

        self.add_button(
            "LastActivityView",
            "lastactivity"
        )

        self.add_button(
            "ExecutedPrograms",
            "executedprograms"
        )

        self.add_button(
            "BrowserHistoryView",
            "browserhistory"
        )

        section3 = ctk.CTkLabel(
            self,
            text="ORBDIFF",
            font=("Segoe UI Semibold", 10),
            text_color="#7d4dff"
        )

        section3.pack(
            anchor="w",
            padx=18,
            pady=(18, 8)
        )

        self.add_button(
            "PrefetchView",
            "orbdiff_prefetch"
        )

        self.add_button(
            "BAMReveal",
            "orbdiff_bam"
        )

        self.add_button(
            "USBDetector",
            "orbdiff_usb"
        )

        self.add_button(
            "UserAssistView",
            "orbdiff_userassist"
        )
