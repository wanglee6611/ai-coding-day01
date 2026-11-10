from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

# 1. 数据库文件名严格设为 device_inventory.db
Base = declarative_base()
engine = create_engine("sqlite:///device_inventory.db", echo=False)
SessionLocal = sessionmaker(bind=engine)


# 2. 定义 devices 表结构及完全一致的打印格式
class Device(Base):
    __tablename__ = "devices"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), index=True, nullable=False)
    type = Column(String(50), nullable=False)
    version = Column(String(50), nullable=False)
    location = Column(String(100), nullable=False)
    create_time = Column(DateTime, default=datetime.now)

    def __repr__(self):
        return (
            f"Device(设备名称: {self.name} | 类型: {self.type} | "
            f"版本: {self.version} | 位置: {self.location} | "
            f"入库时间: {self.create_time})"
        )



# 初始 6 条设备数据
device_list = [
    {'name': 'R1', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Beijing-IDC-A'},
    {'name': 'R2', 'type': 'router', 'version': 'IOS XE 17.14', 'location': 'Shanghai-IDC-B'},
    {'name': 'SW1', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Beijing-IDC-A'},
    {'name': 'SW2', 'type': 'switch', 'version': 'IOS 15.2', 'location': 'Shanghai-IDC-B'},
    {'name': 'FW1', 'type': 'firewall', 'version': 'ASA 9.16', 'location': 'Beijing-IDC-A'},
    {'name': 'FW2', 'type': 'firewall', 'version': 'FTD 7.2', 'location': 'Shenzhen-IDC-C'},
]


def init_db(session):
    """创建表，且仅在空表时插入初始数据（保证重新运行记录不翻倍、入库时间不变）"""
    Base.metadata.create_all(engine)
    if session.query(Device).count() == 0:
        for item in device_list:
            session.add(Device(**item))
        session.commit()


def print_devices(devices):
    if not devices:
        print("未查询到匹配的设备记录。")
        return
    for d in devices:
        print(d)


def main():
    session = SessionLocal()
    init_db(session)

    while True:
        print("\n1. 查询所有设备  2. 按设备名称查询  3. 按设备类型查询  4. 按机房关键词查询  0. 退出")
        choice = input("请选择: ").strip()

        if choice == "0":
            break
        elif choice == "1":
            devices = session.query(Device).all()
            print_devices(devices)
        elif choice == "2":
            name_val = input("请输入设备名称: ").strip()
            devices = session.query(Device).filter_by(name=name_val).all()
            print_devices(devices)
        elif choice == "3":
            type_val = input("请输入设备类型: ").strip()
            devices = session.query(Device).filter_by(type=type_val).all()
            print_devices(devices)
        elif choice == "4":
            keyword = input("请输入机房关键词: ").strip()
            devices = session.query(Device).filter(Device.location.like(f"%{keyword}%")).all()
            print_devices(devices)
        else:
            print("无效选项，请重新输入。")

    session.close()


if __name__ == "__main__":
    main()