"""第5天 · 任务2: 采集show run, 计算SHA256, 存库并检测配置变化。"""
# 连接账号和密码直接填写在下面的连接参数中。
import hashlib
import re
import time

from day04_01_multicmd import qytang_multicmd # 复用第四天任务1的函数
from day05_01_router_model import RouterConfig, Session # 复用任务1的表

def get_show_run(host, username, password):
    """获取配置并计算 hash"""
    raw = qytang_multicmd(host, username, password,
                          ['terminal length 0', 'show running-config'],
                          verbose=False)
    match = re.search(r'^(hostname[^\r\n]*\r?\n.*?^end)[ \t]*\r?$', raw,
                      flags=re.MULTILINE | re.DOTALL)
    if match is None:
        raise ValueError('没有收到从hostname到独立end行的完整配置, 停止本次备份')
    
    # 待完成 2: 从match中取出配置文本。
    config = match.group(1)
    
    # 待完成 2: 将配置文本转为字节后计算SHA256。
    config_hash = hashlib.sha256(config.encode('utf-8')).hexdigest()
    
    return config, config_hash

def save_config(host, config, config_hash):
    """写入数据库（使用独立 session，避免事务残留）"""
    with Session() as session:
        # 待完成 3: 填入本次记录
        record = RouterConfig(router_ip=host, router_config=config, config_hash=config_hash)
        session.add(record)
        session.commit()

def get_latest_two_hashes(host):
    """查询最近两条记录"""
    with Session() as session:
        results = (session.query(RouterConfig)
                   .filter(RouterConfig.router_ip == host) # 待完成 4: 只筛选当前设备的记录。
                   .order_by(RouterConfig.id.desc()) # 最新的排第一
                   .limit(2)
                   .all())
        return results

if __name__ == '__main__':
    host     = '10.1.1.1'
    username = 'admin'
    password = 'Cisc0123'

    print(f"[*] 开始监控 {host} 的配置变化，每轮结束后等待 5 秒...\n")
    while True:
        config, config_hash = get_show_run(host, username, password)
        save_config(host, config, config_hash)
        records = get_latest_two_hashes(host)

        if len(records) < 2:
            print(f"本次采集的HASH:{config_hash}")
        elif records[0].config_hash == records[1].config_hash:
            # 待完成 5: 配置无变化，打印本次HASH。
            print(f"配置无变化，本次HASH: {config_hash}")
        else:
            # 待完成 5: 配置有变化，打印告警及前后两次HASH。
            print(f"【告警】配置有变化！")
            print(f"前一次HASH: {records[1].config_hash}")
            print(f"本次HASH: {records[0].config_hash}")
            
        time.sleep(5)