import re

# 给定输入：包含多行记录的字符串
asa_conn = """TCP Student 192.168.189.167:32806 Teacher 137.78.5.128:65247, idle 0:00:00, bytes 74, flags UIO
TCP Student 192.168.189.167:80 Teacher 137.78.5.128:65233, idle 0:00:03, bytes 334516, flags UIO"""

# 1. 定义正则表达式捕获6个核心字段
# ([\d\.]+) 匹配IP地址
# (\d+) 匹配端口号和bytes数字
# ([A-Z]+) 匹配大写字母组成的flags
pattern = r"TCP\s+[a-zA-Z]+\s+([\d\.]+):(\d+)\s+[a-zA-Z]+\s+([\d\.]+):(\d+).*?bytes\s+(\d+),\s+flags\s+([A-Z]+)"

# 初始化空字典
conn_dict = {}

# 2. 用 split("\n") 将字符串按行拆分，并逐行处理
for line in asa_conn.split("\n"):
    match = re.match(pattern, line)
    if match:
        # 3. 使用元组 (源IP, 源端口, 目的IP, 目的端口) 作为字典的键[cite: 9]
        dict_key = (match.group(1), match.group(2), match.group(3), match.group(4))
        
        # 使用元组 (bytes, flags) 作为字典的值[cite: 9]
        # 提示：提取出的端口和 bytes 保持为字符串，无需转换数据类型[cite: 9]
        dict_value = (match.group(5), match.group(6))
        
        # 将键值对存入字典
        conn_dict[dict_key] = dict_value

# 4. 使用 items() 和 format() 遍历字典并打印格式化报告[cite: 9]
print("=" * 70)
for k, v in conn_dict.items():
    print("Source: {:<15} Port: {:<6} -> Dest: {:<15} Port: {:<6}".format(k[0], k[1], k[2], k[3]))
    print("Bytes : {:<15} Flags: {}".format(v[0], v[1]))
    print("-" * 70)