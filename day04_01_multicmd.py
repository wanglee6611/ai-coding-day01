import time
import paramiko
from getpass import getpass


def qytang_multicmd(ip, username, password, cmd_list, wait_time=2, verbose=True):
    """在同一个SSH交互终端依次执行cmd_list，返回全部回显文本。"""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(
        ip,
        username=username,
        password=password,
        look_for_keys=False,
        allow_agent=False,
    )

    chan = ssh.invoke_shell()
    time.sleep(1)
    if chan.recv_ready():
        chan.recv(65535)  # 读掉登录欢迎信息

    all_output = ""

    for cmd in cmd_list:
        chan.sendall(cmd.encode("utf-8") + b"\n")
        time.sleep(wait_time)

        cmd_output = ""
        # 循环持续接收，支持长回显
        while chan.recv_ready():
            chunk = chan.recv(65535).decode("utf-8", errors="ignore")
            cmd_output += chunk
            time.sleep(0.2)

        if verbose:
            print(cmd_output, end="")

        all_output += cmd_output

    chan.close()
    ssh.close()
    return all_output


if __name__ == "__main__":
    cmd_list = [
        'terminal length 0',
        'show version | include Software,',
        'show running-config | include hostname',
    ]
    password = getpass('SSH密码: ')
    qytang_multicmd('10.1.1.1', 'admin', password, cmd_list, wait_time=2, verbose=True)