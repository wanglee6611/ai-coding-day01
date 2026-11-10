import random

# 随机生成 4 个 0-255 之间的整数，并用 str() 转为字符串
sec1 = str(random.randint(0, 255))
sec2 = str(random.randint(0, 255))
sec3 = str(random.randint(0, 255))
sec4 = str(random.randint(0, 255))

# 使用 + 号和点号拼接成 IPv4 地址
random_ip = sec1 + "." + sec2 + "." + sec3 + "." + sec4

print(random_ip)
