"""本封装待调试"""

import pymysql
import pytest


class DBHandler:
    def __init__(self, host, port, user, password,
                 database, charset, **kwargs):
        # 连接数据库服务器
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password,
                                    database=database, cursorclass=pymysql.cursors.DictCursor,
                                    charset=charset, **kwargs)
        # 获取游标
        self.cursor = self.conn.cursor()

    def query(self, sql, args=None, one=True):
        self.cursor.execute(sql, args)
        # 提交事务
        self.conn.commit()
        if one:
            return self.cursor.fetchone()
        else:
            return self.cursor.fetchall()

    def close(self):
        self.cursor.close()
        self.conn.close()
# if __name__ == "__main__":
#     db = DBHandler(host='192.168.3.230', port=3309,
#                    user='sm_user', password='sm_user',
#                    database='测试库', charset='utf8')
#     sql = 'SELECT * FROM test.app_agw LIMIT 10;'
#     data = db.query(sql)
#     print(data)
