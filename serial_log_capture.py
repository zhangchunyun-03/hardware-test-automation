import serial
import time

# ---------------------- 配置区 ----------------------
SERIAL_PORT = "COM3"      # Windows: COMx  Mac:/dev/ttyUSB0
BAUDRATE = 115200
TIMEOUT = 1
KEYWORDS = ["error", "fail", "reset", "crash"]  # 告警关键字
LOG_FILE = "serial_log.txt"
# -----------------------------------------------------

def main():
    try:
        ser = serial.Serial(SERIAL_PORT, BAUDRATE, timeout=TIMEOUT)
        print(f"✅ 串口打开成功：{SERIAL_PORT}")
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            while True:
                data = ser.readline().decode("utf-8", errors="ignore").strip()
                if data:
                    print(data)
                    f.write(f"{time.ctime()} | {data}\n")
                    # 关键字告警
                    for kw in KEYWORDS:
                        if kw in data.lower():
                            print(f"⚠️ 告警：检测到关键字 [{kw}] -> {data}")
    except Exception as e:
        print(f"❌ 串口异常：{e}")

if __name__ == "__main__":
    main()
