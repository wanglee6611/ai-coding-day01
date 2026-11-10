import re

# 给定输入
conn = 'TCP server 172.16.1.101:443 localserver 172.16.66.1:53710, idle 0:01:09, bytes 27575949, flags UIO'

# 1. 定义正则表达式（严格提取5个捕获组）
# ([A-Z]+) 匹配协议类型，如 TCP
# \s+server\s+ 匹配固定的 " server " 文本
# ([\d\.]+) 匹配目标IP地址
# : 匹配IP和端口之间的分隔符
# (\d+) 匹配目标端口
# \s+localserver\s+ 匹配固定的 " localserver " 文本
# ([\d\.]+) 匹配源IP地址
# : 匹配IP和端口之间的分隔符
# (\d+) 匹配源端口
pattern = r"([A-Z]+)\s+server\s+([\d\.]+):(\d+)\s+localserver\s+([\d\.]+):(\d+)"

# 2. 使用 re.match() 进行匹配
match = re.match(pattern, conn)

# 3. 提取捕获组并按要求格式化打印
if match:
    # 指定技术要求：标签左对齐占12个字符，再打印冒号和值[cite: 7]
    print("{:<12}: {}".format("Protocol", match.group(1)))
    print("{:<12}: {}".format("Server IP", match.group(2)))
    print("{:<12}: {}".format("Server Port", match.group(3)))
    print("{:<12}: {}".format("Local IP", match.group(4)))
    print("{:<12}: {}".format("Local Port", match.group(5)))