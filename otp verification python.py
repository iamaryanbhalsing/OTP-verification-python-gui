import tkinter as tk
from tkinter import messagebox
import random
import time
import threading

class OTPVerificationApp:
    def __init__(self, root):
        self.root = root
        self.root.title("OTP Verification GUI")
        self.root.geometry("400x320")
        self.root.resizable(False, False)
        
        self.otp = None
        self.otp_expiry = None
        self.timer_running = False
        
        self.create_widgets()
    
    def create_widgets(self):
        # Title
        title_label = tk.Label(self.root, text="OTP Verification", font=("Helvetica", 16, "bold"))
        title_label.pack(pady=20)
        
        # Contact input
        self.phone_label = tk.Label(self.root, text="Enter your phone or email:")
        self.phone_label.pack(pady=5)
        self.phone_entry = tk.Entry(self.root, width=35, justify='center')
        self.phone_entry.pack(pady=5)
        self.phone_entry.insert(0, "user@example.com")
        
        # Send OTP Button
        self.send_button = tk.Button(self.root, text="Send OTP", command=self.send_otp, 
                                    bg="#4CAF50", fg="white", font=("Helvetica", 11, "bold"), width=15)
        self.send_button.pack(pady=15)
        
        # OTP Input
        self.otp_label = tk.Label(self.root, text="Enter 6-digit OTP:", font=("Helvetica", 10))
        self.otp_label.pack(pady=5)
        self.otp_entry = tk.Entry(self.root, width=20, font=("Helvetica", 14), justify='center')
        self.otp_entry.pack(pady=5)
        
        # Verify Button
        self.verify_button = tk.Button(self.root, text="Verify OTP", command=self.verify_otp, 
                                      bg="#2196F3", fg="white", font=("Helvetica", 11, "bold"), width=15)
        self.verify_button.pack(pady=10)
        
        # Timer
        self.timer_label = tk.Label(self.root, text="", fg="red", font=("Helvetica", 10))
        self.timer_label.pack(pady=5)
        
        # Status
        self.status_label = tk.Label(self.root, text="", fg="blue", wraplength=350)
        self.status_label.pack(pady=10)
    
    def generate_otp(self):
        return ''.join([str(random.randint(0, 9)) for _ in range(6)])
    
    def send_otp(self):
        contact = self.phone_entry.get().strip()
        if not contact:
            messagebox.showerror("Error", "Please enter your phone or email")
            return
        
        self.otp = self.generate_otp()
        self.otp_expiry = time.time() + 60  # 60 seconds
        self.status_label.config(text=f"✅ OTP sent to {contact}\n(Demo OTP: {self.otp})", fg="green")
        
        self.otp_entry.delete(0, tk.END)
        
        if not self.timer_running:
            self.timer_running = True
            threading.Thread(target=self.update_timer, daemon=True).start()
    
    def update_timer(self):
        while self.timer_running and time.time() < self.otp_expiry:
            remaining = int(self.otp_expiry - time.time())
            self.timer_label.config(text=f"⏳ OTP expires in {remaining} seconds")
            time.sleep(1)
        
        if time.time() >= self.otp_expiry and self.otp:
            self.timer_label.config(text="❌ OTP Expired!")
            self.otp = None
            self.timer_running = False
    
    def verify_otp(self):
        if not self.otp:
            messagebox.showwarning("Warning", "Please send OTP first")
            return
        
        if time.time() > self.otp_expiry:
            messagebox.showerror("Expired", "OTP has expired. Request a new one.")
            return
        
        user_input = self.otp_entry.get().strip()
        
        if user_input == self.otp:
            messagebox.showinfo("Success", "✅ OTP Verified Successfully!")
            self.status_label.config(text="Verification Successful 🎉", fg="green")
            self.reset_app()
        else:
            messagebox.showerror("Failed", "❌ Invalid OTP. Try again.")
    
    def reset_app(self):
        self.otp = None
        self.timer_running = False
        self.timer_label.config(text="")
        self.otp_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = OTPVerificationApp(root)
    root.mainloop()