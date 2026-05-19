# hardware-test-automation
硬件测试自动化脚本合集 | 适用于IoT/智能硬件/消费电子测试

## 功能清单
| 文件 | 说明 |
|------|----------|
| [`serial_log_capture.py/`](serial_log_capture.py) | 串口日志自动抓取 + 异常关键字告警 |
| [`power_monitor.py`](power_monitor.py) | 程控电源电压/电流自动化采集 |
| [`auto_regeression_test.py`](auto_regeression_test.p) | 硬件功能回归自动化测试 + 报告生成  |

## 依赖安装
```bash
pip install pyserial pyvisa
```

## 适用场景
硬件测试工程师日常自动化、日志排查、数据采集、回归测试
