## 📋 Flask Visitor Logger App
This is a Flask-based web application that logs basic visitor information such as IP address, user agent, screen resolution, device memory, and geolocation (via public APIs). It is designed for educational purposes, like learning about request metadata, geolocation APIs, and client-side data collection.

## ⚙️ Features
Logs IP address, browser user agent, referrer header

Attempts geolocation using ipapi.co and ipinfo.io

Logs extra client-side info via JavaScript (screen resolution, battery, language, etc.)

Saves all logs in access_logs.txt

Uses a confirm.html template to display the landing page

## 🧑‍💻 Use Case (Ethical)
This project is suitable for:

Educational environments (cybersecurity training, self-learning)

Local network tests

Ethical hacking labs (e.g., with permission in CTFs)

### 🚀 How to Run
## 1. Clone the repository
```bash
git clone https://github.com/ItsDarker/Visitor-Logger-App
cd Visitor-Logger-App
```
## 2. Install dependencies
Make sure you have Python 3 and pip installed.

```bash
pip install flask requests
```
## 3. Add an HTML template
Create a templates/confirm.html file in your project folder.

Example:
```bash
<!DOCTYPE html>
<html>
<head>
  <title>Visitor Info Logged</title>
</head>
<body>
  <h1>Thank you for visiting</h1>
  <script>
    // Example JS to send client info
    fetch('/log_client_info', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        resolution: screen.width + "x" + screen.height,
        language: navigator.language,
        timezone: Intl.DateTimeFormat().resolvedOptions().timeZone,
        network_type: navigator.connection?.effectiveType || "unknown",
        battery_level: (await navigator.getBattery())?.level * 100 || "unknown",
        charging: (await navigator.getBattery())?.charging || "unknown",
        device_memory: navigator.deviceMemory || "unknown",
        touch_support: navigator.maxTouchPoints > 0,
        device_type: /Mobi|Android/i.test(navigator.userAgent) ? "Mobile" : "Desktop",
        cookies: navigator.cookieEnabled,
        referrer: document.referrer
      })
    });
  </script>
</body>
</html>
```

## 4. Start the server
```bash
python app.py
```
## 5. Access the app
Visit:

```bash
http://localhost:80
```
### ❗Important Notes
- Do NOT use this project to deceive or collect data from people without their knowledge and consent.

- This is for local testing, consented experiments, or lab environments only.

- Never deploy to the public internet without proper legal and ethical considerations.

### 📂 Log File
All log entries are saved to:

```bash
access_logs.txt
```
### ✅ Legal & Ethical Alternatives for Learning
- For ethical cybersecurity practice, try:

- OWASP Juice Shop

- TryHackMe

- Hack The Box

- GoPhish

