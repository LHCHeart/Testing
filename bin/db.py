import cx_Oracle
import configparser
from bin import log


# 读取配置文件
conf = configparser.ConfigParser()
conf.read("./conf/test.conf",encoding='UTF-8')

USERNAME = conf.get("DB", "USERNAME")
PASSWORD = conf.get("DB", "PASSWORD")
IP = conf.get("DB", "IP")
PORT = conf.get("DB", "PORT")
DB_NAME = conf.get("DB", "DB_NAME")

# 连接数据库
db = cx_Oracle.connect(USERNAME + '/' + PASSWORD + '@' + IP + ':' + PORT + '/' + DB_NAME)
# db = cx_Oracle.connect('heart/1@127.0.0.1:1521/ORCL')
# 使用cursor()方法获取操作游标
cursor = db.cursor()


def insert_img(con,imgs_code):
    sql_insert = "insert into image_list (id, images_code, title, issuer, serial_num, image_num, image_size, model_name, issue_data, remarks, comments) \
    values (sys_guid(), '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s',null) " % (imgs_code,con[0], con[1], con[2], con[3], con[4], con[5], con[6], con[7])
    insert(sql_insert)


def select(sql):
    # 使用execute方法执行SQL语句
    cursor.execute(sql)
    all_data = cursor.fetchall()
    log.write_debug(sql)
    log.write_debug("Select successful!")
    return all_data


def insert(sql):
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 提交到数据库执行
        db.commit()
    except Exception as e:
        # 如果发生错误则回滚
        db.rollback()
        log.write_error(sql)
        log.write_error(e)
        log.write_error("Insert failed!")
    else:
        # log.write_debug(sql)
        log.write_debug("Insert successful!")


def close():
    db.close()


def select_name(dirname):
    sql_name = "select case length(t.images_code) \
when 1 then '0000'||t.images_code ||'-'|| t.title \
when 2 then '000'||t.images_code ||'-'|| t.title \
when 3 then '00'||t.images_code ||'-'|| t.title \
when 4 then '0'||t.images_code ||'-'|| t.title \
else t.images_code ||'-'|| t.title end as code \
from image_list t where t.images_code = '%s' " % int(dirname)

    try:
        # 执行sql语句
        cursor.execute(sql_name)
        # 提交到数据库执行
        all_data = cursor.fetchone()
        data_list = list(all_data)
        data = data_list[0]
        return all_data
    except Exception as e:
        # 如果发生错误则回滚
        log.write_error(e)
        log.write_error("Select failed!")
    else:
        # log.write_debug(sql)
        log.write_debug(sql)
        log.write_debug("Select successful!")

