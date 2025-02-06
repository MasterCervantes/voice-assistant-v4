import tkinter as tk
from tkinter import ttk
import json
import os
from XTTSClient import XTTSClient
from OllamaChecker import OllamaChecker

class ChatApplication:
    def __init__(self, root):
        self.root = root
        self.root.title("XTTS Chat")
        self.root.geometry("800x600")
        self.setup_ui()
        self.xtts_client = XTTSClient("http://localhost:8020")
        
    def setup_ui(self):
        # Chat display
        self.chat_display = tk.Text(self.root, wrap=tk.WORD, state='disabled')
        self.chat_display.pack(expand=True, fill='both', padx=5, pady=5)
        
        # Input area
        self.input_frame = ttk.Frame(self.root)
        self.input_frame.pack(fill=tk.X, padx=5, pady=5)
        
        self.input_field = ttk.Entry(self.input_frame)
        self.input_field.pack(side=tk.LEFT, expand=True, fill=tk.X)
        
        self.send_btn = ttk.Button(self.input_frame, text="Send", command=self.send_message)
        self.send_btn.pack(side=tk.LEFT, padx=5)
        
    def send_message(self):
        message = self.input_field.get().strip()
        if message:
            self.input_field.delete(0, tk.END)
            self.add_message("You", message)
            # This would trigger the AI response and XTTS
            self.xtts_client.synthesize(message)
            
    def add_message(self, sender, message):
        self.chat_display.configure(state='normal')
        self.chat_display.insert(tk.END, f"{sender}: {message}\n\n")
        self.chat_display.configure(state='disabled')
        self.chat_display.see(tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = ChatApplication(root)
    root.mainloop()