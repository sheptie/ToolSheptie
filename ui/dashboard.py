import customtkinter as ctk
import pyperclip
import os
import subprocess
import threading
from tkinter import messagebox

from scanners.prefetch import get_prefetch
from scanners.processes import get_processes

ctk.set_appearance_mode("dark")

ACCENT = "#9333ea"
BG = "#050507"
CARD = "#0b0b10"

class Dashboard(ctk.CTk):

    def __init__(self):

        super().__init__()

        self.geometry("1500x850")
        self.minsize(1300, 760)

        self.title("ToolSheptie")

        try:
            self.iconbitmap("assets/icon.ico")
        except:
            pass

        self.configure(fg_color=BG)

        self.build_ui()

        self.after(100, lambda: threading.Thread(
            target=self.load_prefetch,
            daemon=True
        ).start())

    def build_ui(self):

        self.outer = ctk.CTkFrame(
            self,
            fg_color="#160820",
            corner_radius=24,
            border_width=2,
            border_color="#8b5cf6"
        )

        self.outer.pack(
            fill="both",
            expand=True,
            padx=10,
            pady=10
        )

        self.inner = ctk.CTkFrame(
            self.outer,
            fg_color=BG,
            corner_radius=22
        )

        self.inner.pack(
            fill="both",
            expand=True,
            padx=2,
            pady=2
        )

        self.sidebar()

        self.main = ctk.CTkFrame(
            self.inner,
            fg_color=BG
        )

        self.main.pack(
            side="right",
            fill="both",
            expand=True,
            padx=(0, 14),
            pady=14
        )

        self.topbar()

        self.stats()

        self.results_glow = ctk.CTkFrame(
            self.main,
            fg_color="#7e22ce",
            corner_radius=20
        )

        self.results_glow.pack(
            fill="both",
            expand=True,
            pady=(10, 0)
        )

        self.results_container = ctk.CTkFrame(
            self.results_glow,
            fg_color="#12091c",
            corner_radius=18
        )

        self.results_container.pack(
            fill="both",
            expand=True,
            padx=2,
            pady=2
        )

        self.results = ctk.CTkScrollableFrame(
            self.results_container,
            fg_color=BG,
            corner_radius=16
        )

        self.results.pack(
            fill="both",
            expand=True,
            padx=8,
            pady=8
        )

    def sidebar(self):

        self.sidebar_frame = ctk.CTkFrame(
            self.inner,
            width=250,
            fg_color="#09090d",
            corner_radius=0
        )

        self.sidebar_frame.pack(
            side="left",
            fill="y"
        )

        self.sidebar_frame.pack_propagate(False)

        logo = ctk.CTkLabel(
            self.sidebar_frame,
            text="S",
            font=("Segoe UI Black", 50),
            text_color=ACCENT
        )

        logo.pack(
            anchor="w",
            padx=24,
            pady=(25, 0)
        )

        title = ctk.CTkLabel(
            self.sidebar_frame,
            text="ToolSheptie",
            font=("Segoe UI Semibold", 22),
            text_color="white"
        )

        title.pack(
            anchor="w",
            padx=24
        )

        sub = ctk.CTkLabel(
            self.sidebar_frame,
            text="Realtime Analysis Suite",
            font=("Segoe UI", 11),
            text_color="#8b8b95"
        )

        sub.pack(
            anchor="w",
            padx=24,
            pady=(0, 18)
        )

        self.section("SCANNERS")

        self.side_button("Prefetch", self.load_prefetch)
        self.side_button("Processes", self.load_processes)
        self.side_button("BAM Parser", self.load_bam)

        self.section("TOOLS")

        self.side_button("Everything", self.open_everything)
        self.side_button("System Informer", self.open_systeminformer)
        self.side_button("LastActivityView", self.open_lastactivity)
        self.side_button("ExecutedPrograms", self.open_executedprograms)
        self.side_button("BrowserHistory", self.open_browserhistory)

        self.section("ORBDIFF")

        self.side_button("PrefetchView", self.open_prefetchview)
        self.side_button("BAMReveal", self.open_bamreveal)
        self.side_button("USBDetector", self.open_usbdetector)
        self.side_button("UserAssistView", self.open_userassist)

        status = ctk.CTkLabel(
            self.sidebar_frame,
            text="● READY",
            font=("Segoe UI Bold", 12),
            text_color="#22c55e"
        )

        status.pack(
            side="bottom",
            anchor="w",
            padx=24,
            pady=(0, 8)
        )

        version = ctk.CTkLabel(
            self.sidebar_frame,
            text="Version 2.0",
            font=("Segoe UI", 11),
            text_color="#777"
        )

        version.pack(
            side="bottom",
            anchor="w",
            padx=24,
            pady=(0, 20)
        )

    def section(self, text):

        label = ctk.CTkLabel(
            self.sidebar_frame,
            text=text,
            font=("Segoe UI Bold", 11),
            text_color=ACCENT
        )

        label.pack(
            anchor="w",
            padx=24,
            pady=(12, 8)
        )

    def side_button(self, text, command):

        btn = ctk.CTkButton(
            self.sidebar_frame,
            text=text,
            command=lambda: threading.Thread(
                target=command,
                daemon=True
            ).start(),
            width=205,
            height=42,
            fg_color="#111118",
            hover_color="#1e1033",
            corner_radius=12,
            border_width=1,
            border_color="#2b1745",
            font=("Segoe UI Semibold", 13)
        )

        btn.pack(
            pady=5
        )

    def topbar(self):

        top_glow = ctk.CTkFrame(
            self.main,
            fg_color="#7e22ce",
            corner_radius=20
        )

        top_glow.pack(fill="x")

        top = ctk.CTkFrame(
            top_glow,
            fg_color="#12091c",
            corner_radius=18
        )

        top.pack(
            fill="x",
            padx=2,
            pady=2
        )

        left = ctk.CTkFrame(
            top,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            padx=22,
            pady=18
        )

        title = ctk.CTkLabel(
            left,
            text="Analysis Dashboard",
            font=("Segoe UI Semibold", 28),
            text_color="white"
        )

        title.pack(anchor="w")

        sub = ctk.CTkLabel(
            left,
            text="Realtime system analysis and threat detection",
            font=("Segoe UI", 12),
            text_color="#9d9da8"
        )

        sub.pack(anchor="w")

        self.search = ctk.CTkEntry(
            top,
            width=260,
            height=44,
            placeholder_text="Search...",
            fg_color="#0c0c11",
            border_color="#7e22ce",
            corner_radius=12
        )

        self.search.pack(
            side="right",
            padx=20
        )

        self.search.bind(
            "<KeyRelease>",
            self.live_search
        )

    def stats(self):

        stats = ctk.CTkFrame(
            self.main,
            fg_color="transparent"
        )

        stats.pack(
            fill="x",
            pady=12
        )

        self.stat_card(stats, "Suspicious", "12", "#ef4444")
        self.stat_card(stats, "Warning", "25", "#f59e0b")
        self.stat_card(stats, "Clean", "138", "#22c55e")
        self.stat_card(stats, "Total", "175", ACCENT)

    def stat_card(self, parent, title, value, color):

        glow = ctk.CTkFrame(
            parent,
            fg_color="#221133",
            corner_radius=18
        )

        glow.pack(
            side="left",
            padx=8,
            fill="x",
            expand=True
        )

        card = ctk.CTkFrame(
            glow,
            fg_color=CARD,
            corner_radius=16
        )

        card.pack(
            fill="both",
            expand=True,
            padx=1,
            pady=1
        )

        card.configure(height=120)

        t = ctk.CTkLabel(
            card,
            text=title,
            font=("Segoe UI Semibold", 16),
            text_color="white"
        )

        t.pack(
            anchor="w",
            padx=18,
            pady=(22, 0)
        )

        v = ctk.CTkLabel(
            card,
            text=value,
            font=("Segoe UI Bold", 32),
            text_color=color
        )

        v.pack(
            anchor="w",
            padx=18
        )

    def clear(self):

        for widget in self.results.winfo_children():
            widget.destroy()

    def live_search(self, event=None):

        query = self.search.get().lower()

        for card in self.results.winfo_children():

            text = getattr(card, "search_text", "").lower()

            if query in text or query == "":
                card.pack(fill="x", pady=6)
            else:
                card.pack_forget()

    def create_card(self, item):

        status = item.get("status", "Clean")

        color = "#22c55e"

        if status == "Warning":
            color = "#f59e0b"

        elif status == "Suspicious":
            color = "#ef4444"

        glow = ctk.CTkFrame(
            self.results,
            fg_color="#1c1128",
            corner_radius=18
        )

        glow.pack(
            fill="x",
            pady=6
        )

        card = ctk.CTkFrame(
            glow,
            fg_color=CARD,
            corner_radius=16
        )

        card.pack(
            fill="x",
            padx=1,
            pady=1
        )

        card.search_text = f"""
        {item.get("name")}
        {item.get("flags")}
        {item.get("path")}
        """

        left = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        left.pack(
            side="left",
            fill="both",
            expand=True,
            padx=18,
            pady=14
        )

        title = ctk.CTkLabel(
            left,
            text=item.get("name"),
            font=("Segoe UI Semibold", 18),
            text_color="white"
        )

        title.pack(anchor="w")

        flags = ctk.CTkLabel(
            left,
            text=f'Flags: {item.get("flags")}',
            font=("Segoe UI", 12),
            text_color="#b0b0bb"
        )

        flags.pack(anchor="w")

        path = ctk.CTkLabel(
            left,
            text=item.get("path"),
            font=("Consolas", 10),
            text_color="#777"
        )

        path.pack(
            anchor="w",
            pady=(4, 0)
        )

        right = ctk.CTkFrame(
            card,
            fg_color="transparent"
        )

        right.pack(
            side="right",
            padx=18
        )

        badge = ctk.CTkLabel(
            right,
            text=status,
            width=120,
            height=38,
            fg_color="#1a101f",
            corner_radius=10,
            text_color=color,
            font=("Segoe UI Semibold", 13)
        )

        badge.pack(
            pady=(0, 8)
        )

        folder = ctk.CTkButton(
            right,
            text="Folder",
            width=110,
            height=34,
            fg_color="#15151c",
            hover_color="#20202a",
            corner_radius=10,
            command=lambda:
            os.startfile(
                os.path.dirname(
                    item.get("path")
                )
            )
        )

        folder.pack(
            pady=4
        )

        copy = ctk.CTkButton(
            right,
            text="Copy",
            width=110,
            height=34,
            fg_color=ACCENT,
            hover_color="#7e22ce",
            corner_radius=10,
            font=("Segoe UI Semibold", 12),
            command=lambda:
            pyperclip.copy(
                item.get("path")
            )
        )

        copy.pack()

    def load_prefetch(self):

        self.clear()

        try:

            data = get_prefetch()

            suspicious = []
            warning = []
            clean = []

            for item in data:

                if item["status"] == "Suspicious":
                    suspicious.append(item)

                elif item["status"] == "Warning":
                    warning.append(item)

                else:
                    clean.append(item)

            final = suspicious + warning + clean

            self.after(
                0,
                lambda: [
                    self.create_card(item)
                    for item in final[:70]
                ]
            )

        except Exception as e:

            self.after(
                0,
                lambda:
                messagebox.showerror(
                    "Error",
                    str(e)
                )
            )

    def load_processes(self):

        self.clear()

        try:

            data = get_processes()

            self.after(
                0,
                lambda: [
                    self.create_card(item)
                    for item in data[:70]
                ]
            )

        except Exception as e:

            self.after(
                0,
                lambda:
                messagebox.showerror(
                    "Error",
                    str(e)
                )
            )

    def load_bam(self):

        self.clear()

        fake = [

            {
                "name": "16x16.exe",
                "status": "Warning",
                "flags": "autoclicker, macro",
                "path": "C:\\Users\\PC\\Downloads\\16x16.exe"
            },

            {
                "name": "HorionInjector.exe",
                "status": "Suspicious",
                "flags": "minecraft cheat",
                "path": "C:\\Users\\PC\\Downloads\\HorionInjector.exe"
            }
        ]

        for item in fake:
            self.create_card(item)

    def run_tool(self, path):

        try:
            subprocess.Popen(path, shell=True)

        except Exception as e:

            messagebox.showerror(
                "Tool Error",
                str(e)
            )

    def open_everything(self):

        path = "external_tools/Everything/Everything.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_systeminformer(self):

        possible = [

            "external_tools/SystemInformer/SystemInformer.exe",
            "external_tools/SystemInformer/amd64/SystemInformer.exe",
            "external_tools/SystemInformer/i386/SystemInformer.exe"
        ]

        for path in possible:

            if os.path.exists(path):
                self.run_tool(path)
                return

    def open_lastactivity(self):

        path = "external_tools/LastActivityView/LastActivityView.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_executedprograms(self):

        path = "external_tools/ExecutedPrograms/ExecutedProgramsList.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_browserhistory(self):

        path = "external_tools/BrowserHistoryView/BrowsingHistoryView.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_prefetchview(self):

        path = "external_tools/PrefetchView/PrefetchView.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_bamreveal(self):

        path = "external_tools/BAMReveal/BAMReveal.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_usbdetector(self):

        path = "external_tools/USBDetector/USBDetector.exe"

        if os.path.exists(path):
            self.run_tool(path)

    def open_userassist(self):

        path = "external_tools/UserAssistView/UserAssistView.exe"

        if os.path.exists(path):
            self.run_tool(path)

if __name__ == "__main__":

    app = Dashboard()
    app.mainloop()
