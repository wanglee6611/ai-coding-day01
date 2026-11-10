from getpass import getpass
from day04_01_multicmd import qytang_multicmd
from day04_02_ping_check import ping_check

hosts = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
RIP_COMMANDS = [
    'configure terminal',
    'router rip',
    'version 2',
    'network 172.16.0.0',
    'end',
]

if __name__ == "__main__":
    password = getpass('SSH密码: ')

    for host in hosts:
        ok, rtt = ping_check(host)
        if not ok:
            print(f"\n=== {host} ping不通，跳过SSH配置 ===")
            continue

        print(f"\n=== {host} ping通 ({rtt} ms)，开始配置RIP ===")
        qytang_multicmd(host, 'admin', password, RIP_COMMANDS, wait_time=2, verbose=True)



        