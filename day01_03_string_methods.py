version_raw = "  Cisco IOS XE Software, Version 17.03.04  "

# 1. 去掉首尾空格 (strip)
version_clean = version_raw.strip()
print("去掉空格:" + version_clean)

# 2. 把字符串转成全大写 (upper)
print("转成全大写:" + version_clean.upper())

# 3. 把 "17.03.04" 替换成 "17.06.01" (replace)
print("替换版本号:" + version_clean.replace("17.03.04", "17.06.01"))