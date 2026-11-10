
import datetime

from sqlalchemy import create_engine, inspect, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker

engine = create_engine('sqlite:///router_config.db',
                       connect_args={'check_same_thread': False})
Base = declarative_base()
Session = sessionmaker(bind=engine)

class RouterConfig(Base):
    """路由器配置备份模型：每采集一次新增一行。"""
    __tablename__ = 'router_config'
    
    # 待完成 1: 按表结构定义五个字段及其约束。
    id = Column(Integer, primary_key=True, autoincrement=True)
    router_ip = Column(String(64), nullable=False, index=True)
    router_config = Column(String(99999), nullable=False)
    config_hash = Column(String(500), nullable=False)
    record_time = Column(DateTime, default=datetime.datetime.now)

    def __repr__(self):
        return (f"{self.__class__.__name__}("
                f"路由器IP地址: {self.router_ip} | "
                f"配置Hash: {self.config_hash} | "
                f"记录时间: {self.record_time})")

Base.metadata.create_all(engine, checkfirst=True)

if __name__ == '__main__':
    inspector = inspect(engine)
    print('router_config 表结构：')
    for column in inspector.get_columns('router_config'):
        print(f"  {column['name']:<14}{str(column['type']):<16}nullable={column['nullable']}")
    for index in inspector.get_indexes('router_config'):
        print(f"  索引 {index['name']} -> {index['column_names']}")
        
    print('  主键 ->', inspector.get_pk_constraint('router_config')['constrained_columns'])
    
    # 测试自动生成的值，不把测试记录留在正式备份表里。
    with Session() as session:
        started = datetime.datetime.now()
        record = RouterConfig(router_ip='test', router_config='test', config_hash='test')
        session.add(record)
        session.flush()
        
        if not isinstance(record.id, int) or record.record_time is None or record.record_time < started:
            raise ValueError('检查自动ID与record_time的default设置')
        print(f'自动生成：id={record.id}, record_time={record.record_time}')
        print('自动ID和写入时间：通过')
        session.rollback()  # 测试结束撤销这一行。