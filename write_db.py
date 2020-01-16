"""
pymysql
"""
# 写
"""
mysql
"""
# 读
import pymysql

# 连接数据库
db = pymysql.connect(host='localhost',
                     port=3306,
                     user='root',
                     password='123456',
                     database='stu',
                     charset='utf8')
# 生成游标对象(操作数据库,执行sql语句,获取结果)
cur = db.cursor()

# 读操作
# af = input('输入学生姓名')
# sql = "select name,age,score from student where name=%s;"
# cur.execute(sql, [af])  # 执行sql语句#通过参数列表给sql语句传入值
# print(cur.fetchall())
# 写操作
try:
    # sql = "insert into student (name,age,score)" \
    #       "values(%s,%s,%s);"
    # cur.execute(sql,['jame',18,96])
    sql="update student set sex='m' where name='jame';"
    cur.execute(sql)
    db.commit()  # 同步到数据库
except Exception:
    db.rollback()  # 数据库回滚

# 关闭游标和数据库连接
cur.close()
db.close()
