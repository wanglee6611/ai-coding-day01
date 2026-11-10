from pythonping import ping


def ping_check(host, count=1, timeout=2):
    """ping通返回(True, 平均延迟毫秒)，不通返回(False, None)。"""
    result = ping(host, count=count, timeout=timeout, verbose=False)
    if result.success():
        return (True, result.rtt_avg_ms)
    else:
        return (False, None)


if __name__ == "__main__":
    hosts = ['10.1.1.1', '10.1.1.2', '10.1.1.3']
    for h in hosts:
        ok, rtt = ping_check(h)
        if ok:
            print(f"{h}: 可达, 延迟={rtt}ms")
        else:
            print(f"{h}: 不可达")