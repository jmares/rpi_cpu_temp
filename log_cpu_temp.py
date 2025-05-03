import os
import sqlite3
from datetime import datetime

# Path to the temperature file
TEMP_FILE = "/sys/class/thermal/thermal_zone0/temp"
# Database file
DB_FILE = "/home/birder/python/rpi_cpu_temp/db/cpu_temp_log.db"

# Read temperature from file
def read_temperature():
    try:
        with open(TEMP_FILE, "r") as f:
            temp_str = f.read().strip()
            temp_c = int(temp_str) / 1000.0
            return round(temp_c, 1)
    except Exception as e:
        print(f"Error reading temperature: {e}")
        return None

# Initialize the database
def init_db():
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS temperature_log (
            timestamp TEXT NOT NULL,
            temperature REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()

# Insert a temperature reading
def log_temperature(temp):
    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()
    timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cursor.execute('''
        INSERT INTO temperature_log (timestamp, temperature)
        VALUES (?, ?)
    ''', (timestamp, temp))
    conn.commit()
    conn.close()

# Main function
def main():
    init_db()
    temp = read_temperature()
    if temp is not None:
        log_temperature(temp)

if __name__ == "__main__":
    main()
