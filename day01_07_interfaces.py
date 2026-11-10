interfaces = [
    {"name": "Gi0/0", "status": "up", "speed": "1G"},
    {"name": "Gi0/1", "status": "down", "speed": "1G"},
    {"name": "Gi0/2", "status": "up", "speed": "10G"},
]

# 打印表头和分隔线（如网页下方“预期输出”无表头或表头文字不同，可按预期输出微调）
print("接口      状态    速率")
print("-" * 26)

# 用 for 遍历 interfaces，按提示设置 {:<10}{:<8}{} 列宽对齐输出
for intf in interfaces:
    print("{:<10}{:<8}{}".format(intf["name"], intf["status"], intf["speed"]))