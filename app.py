from flask import Flask, request, render_template, jsonify
from datetime import datetime
import requests
import os

app = Flask(__name__)

LOG_FILE = 'access_logs.txt'

def get_client_ip():
    ip = request.headers.get('CF-Connecting-IP') or \
         request.headers.get('X-Forwarded-For') or \
         request.remote_addr
    return ip

def get_geolocation(ip_address):
    if ip_address.startswith('127.') or ip_address == '::1':
        return "Localhost Access"
    try:
        response = requests.get(f'https://ipapi.co/{ip_address}/json/', timeout=5)
        if response.ok:
            data = response.json()
            if not data.get('error'):
                country = data.get('country_name', 'Unknown')
                city = data.get('city', 'Unknown')
                region = data.get('region', 'Unknown')
                org = data.get('org', 'Unknown')
                return f"{city}, {region}, {country} | ISP: {org}"

        response = requests.get(f'https://ipinfo.io/{ip_address}/json', timeout=5)
        if response.ok:
            data = response.json()
            loc = data.get('loc', 'Unknown')
            country = data.get('country', 'Unknown')
            city = data.get('city', 'Unknown')
            region = data.get('region', 'Unknown')
            org = data.get('org', 'Unknown')
            return f"{city}, {region}, {country} | ISP: {org} | Coords: {loc}"

        return "Location Unknown"
    except Exception:
        return "Location Error"

@app.route('/')
def confirm():
    ip_address = get_client_ip()
    user_agent = request.headers.get('User-Agent', 'Unknown')
    referrer_header = request.headers.get('Referer', 'No Referrer Header')
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    location = get_geolocation(ip_address)

    log_entry = (f"[{timestamp}] IP: {ip_address} | Location: {location} | "
                 f"User-Agent: {user_agent} | Referrer Header: {referrer_header}\n")
    print(log_entry.strip())

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    return render_template('confirm.html')

@app.route('/log_client_info', methods=['POST'])
def log_client_info():
    ip_address = get_client_ip()
    data = request.get_json() or {}
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    log_entry = (f"[{timestamp}] IP: {ip_address} | "
                 f"Screen Resolution: {data.get('resolution', 'Unknown')} | "
                 f"Language: {data.get('language', 'Unknown')} | "
                 f"Time Zone: {data.get('timezone', 'Unknown')} | "
                 f"Network Type: {data.get('network_type', 'Unknown')} | "
                 f"Battery Level: {data.get('battery_level', 'Unknown')} | "
                 f"Charging: {data.get('charging', 'Unknown')} | "
                 f"Device Memory: {data.get('device_memory', 'Unknown')} | "
                 f"Touch Support: {data.get('touch_support', 'Unknown')} | "
                 f"Device Type: {data.get('device_type', 'Unknown')} | "
                 f"Cookies: {data.get('cookies', 'Unknown')} | "
                 f"Referrer (JS): {data.get('referrer', 'Unknown')}\n")

    print(log_entry.strip())

    with open(LOG_FILE, 'a') as f:
        f.write(log_entry)

    return jsonify({'status': 'logged'})

if __name__ == '__main__':
    os.makedirs('templates', exist_ok=True)
    app.run(host='0.0.0.0', port=80)
