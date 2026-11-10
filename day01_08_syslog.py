import re

date = "2026-03-03"
hostname = "SW-Core-01"
level = "CRITICAL"
message = "%LINK-3-UPDOWN: Interface GigabitEthernet0/1, changed state to down"

# 使用正则表达式匹配：第一个括号捕获 Interface 和逗号之间的接口名，第二个括号捕获 changed state to 后的状态
match = re.search(r"Interface (\S+), changed state to (\S+)", message)

interface = match.group(1)
status = match.group(2)

# 使用 f-string 按“标签 : 值”格式输出告警卡片
print(f"日期 : {date}")
print(f"设备 : {hostname}")
print(f"等级 : {level}")
print(f"接口 : {interface}")
print(f"状态 : {status}")