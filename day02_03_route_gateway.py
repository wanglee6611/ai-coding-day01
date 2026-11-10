import re

# 给定输入
route_n_result = """Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         192.168.214.2   0.0.0.0         UG    100    0        0 eno16777984
192.168.122.0   0.0.0.0         255.255.255.0   U     0      0        0 virbr0
192.168.214.0   0.0.0.0         255.255.255.0   U     100    0        0 eno16777984
202.100.1.0     0.0.0.0         255.255.255.0   U     100    0        0 eno33554944"""

# 1. 定义正则表达式
# 0\.0\.0\.0 匹配目标地址 Destination 为默认路由
# \s+ 匹配多个空格
# ([\d\.]+) 捕获网关 Gateway（由数字和点组成）
# \s+0\.0\.0\.0\s+UG 确保后面紧跟的掩码是 0.0.0.0 且 Flags 包含 UG（Up & Gateway）
pattern = r"0\.0\.0\.0\s+([\d\.]+)\s+0\.0\.0\.0\s+UG"

# 2. 使用 re.search() 在整段文本中搜索匹配项
match = re.search(pattern, route_n_result)

# 3. 提取并打印捕获组中的网关IP
if match:
    print("Default Gateway:", match.group(1))