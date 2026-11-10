devices = [
    {"name": "CoreSwitch", "ip": "10.1.1.1", "role": "核心交换机"},
    {"name": "Firewall", "ip": "10.1.1.2", "role": "防火墙"},
    {"name": "WLC", "ip": "10.1.1.3", "role": "无线控制器"},
]

# 打印表头和分隔线（中文字符在终端占2个英文字符宽度，4个汉字占8宽，补10个空格刚好对齐18列宽）
print("设备名称          IP地址            角色")
print("-" * 50)

# 用 for 循环逐条读取字典，并按提示的 {:<18}{:<18}{} 格式打印
for device in devices:
    print("{:<18}{:<18}{}".format(device["name"], device["ip"], device["role"]))