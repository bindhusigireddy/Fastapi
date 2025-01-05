from mysql.connector import connect

class DatabaseManager:


    _connection_pool = None
    _cursor = None

    @classmethod
    def initialize_connection(cls, config):
        host = config['mysql']['host']
        port = config['mysql']['port']
        user = config['mysql']['user']
        password = config['mysql']['password']
        cls._connection_pool = connect(host=host, port=port, user=user, password=password)
        cls._cursor = cls._connection_pool.cursor()

    @classmethod
    def execute_sql(cls, sql_string):
        cls._cursor.execute(sql_string)
        rows = cls._cursor.fetchall()
        return rows



