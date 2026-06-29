# OTP Verification GUI with Python

A modern, secure OTP (One-Time Password) verification desktop application built with **CustomTkinter**.

---

## ✨ Features

- **Modern Dark UI** using CustomTkinter
- **Real Email OTP Delivery** via Gmail (`smtplib`)
- **60-second OTP expiry** with live countdown
- **Resend OTP** functionality
- **Detailed Logging** of all verification attempts
- **Input validation** and user-friendly error messages
- **Cross-platform** (Windows, macOS, Linux)

---

## Configure Gmail (for real email sending)

Enable 2-Step Verification on your Google Account
Generate an App Password:
Go to Google Account Settings → Security → App passwords
Select "Mail" → Generate

Copy the 16-character app password
---

```## 📋 Project Structure
otp-verification-gui/
├── otp_verification_gui.py     # Main application
├── otp_logs.txt                # Auto-generated log file
└── README.md
```
---

## 🔄 Workflow
User Flow:

Enter Email → Click Send OTP
System generates 6-digit OTP
OTP is sent via real email (or shown in UI if email fails)
60-second timer starts
User enters OTP → Click Verify OTP
System validates:
Success → Green success message
Fail/Expired → Appropriate error

All actions are logged with timestamps

Technical Flow:

OTP generated using random
Email sent using smtplib + Gmail SMTP
Timer runs in background thread
All attempts logged to otp_logs.txt

---

⚙️ Configuration
Update these variables in :
```
Pythonsender_email = "your.email@gmail.com"
app_password = "your-16-character-app-password"
```

---
## 🔮 Future Enhancements

Twilio SMS integration
Rate limiting (max attempts)
Config file for email settings
Light/Dark mode toggle
Database support (SQLite)
Expiry notification sound
---

## 🛠️ Installation

### 1. Clone or Download the Project

### 2. Install Dependencies
bash
```
pip install customtkinter

```
---

### 📫 Contact & Socials

<p align="center">
  <a href="mailto:aryanbhalsing7090@gmail.com">
    <img src="https://img.shields.io/badge/Email-aryanbhalsing7090%40gmail.com-red?style=for-the-badge&logo=gmail" />
  </a>
  <a href="https://www.linkedin.com/in/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LinkedIn-iamaryanbhalsing-blue?style=for-the-badge&logo=linkedin" />
  </a>
  <a href="https://github.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/GitHub-iamaryanbhalsing-black?style=for-the-badge&logo=github" />
  </a>
  <a href="https://leetcode.com/iamaryanbhalsing">
    <img src="https://img.shields.io/badge/LeetCode-Profile-orange?style=for-the-badge&logo=leetcode" />
  </a>
</p>

---

<p align="center">
  <img src="https://komarev.com/ghpvc/?username=iamaryanbhalsing&label=Profile%20views&color=0e75b6&style=flat" alt="Profile views" />
</p>
