
def set_mysql_config(env):
    if env == "dev":
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': '123456',
            'db': 'test',
            'port': 3306,
            'charset': 'utf8'
        }
    if env == "pro":
        db_config = {
            'host': 'localhost',
            'user': 'root',
            'passwd': '123456',
            'db': 'sys',
            'port': 3306,
            'charset': 'utf8'
        }
    return db_config
