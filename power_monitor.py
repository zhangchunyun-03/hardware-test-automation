import pyvisa
import time

# ---------------------- 配置区 ----------------------
INSTR_ADDRESS = "ASRL3::INSTR"  # 或 GPIB/USB
VOLTAGE = 5.0
DURATION = 30  # 采集时长（秒’）
# -----------------------------------------------------

def main():
    rm = pyvisa.ResourceManager()
    try:
        inst = rm.open_resource(INSTR_ADDRESS)
        print("✅ 程控电源连接成功")

        # 设定电压、输出开启
        inst.write(f"VOLT {VOLTAGE}")
        inst.write("OUTP ON")

        start = time.time()
        with open("power_data.csv", "w") as f:
            f.write("timestamp,voltage(V),current(A)\n")
            while time.time() - start < DURATION:
                v = float(inst.query("MEAS:VOLT?"))
                i = float(inst.query("MEAS:CURR?"))
                t = time.ctime()
                print(f"{t} | V={v:.2f}V  I={i:.3f}A")
                f.write(f"{t},{v:.2f},{i:.3f}\n")
                time.sleep(1)

        inst.write("OUTP OFF")
        print("✅ 数据采集完成，已保存到 power_data.csv")
    except Exception as e:
        print(f"❌ 设备异常：{e}")

if __name__ == "__main__":
    main()
