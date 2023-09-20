import mysql.connector
import os
import csv
from my_logging import logger
from dotenv import load_dotenv

load_dotenv()


def write_to_database(data):
    # 连接到 SQLite 数据库

    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    table_name = os.getenv('TABLE')
    database = os.getenv('DATABASE')
    # 创建一个游标对象
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    print(f"Table '{table_name}' exists and has been deleted.")
    logger.info(f"Table '{table_name}' exists and has been deleted.")
    # 创建数据表（如果不存在）
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        address TEXT,
                        isoCode TEXT,
                        region TEXT,
                        reachability TEXT,
                        rawPower TEXT,
                        verifiedPrice TEXT,
                        minPieceSize TEXT,
                        maxPieceSize TEXT,
                        freeSpace TEXT,
                        averagePrice TEXT,
                        score TEXT,
                        `rank` TEXT 
                    )''')

    # 插入数据
    sql = f'''INSERT INTO {table_name} (address, isoCode, region, reachability, rawPower, verifiedPrice, minPieceSize, maxPieceSize, freeSpace, averagePrice, score, `rank`)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''
    cursor.execute(sql, data)
    logger.info(f" Table '{table_name}' has been writed successful.")

    # 提交事务并关闭连接
    conn.commit()
    conn.close()


def write_to_database_by_csv(csv_file):
    # 连接到 SQLite 数据库
    # jdbc:mysql://124.70.130.44:3306/blockchain?useSSL=false
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    table_name = os.getenv('TABLE')
    database = os.getenv('DATABASE')
    # 创建一个游标对象
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    logger.info(f"Table '{table_name}' exists and has been deleted.")

    # 创建数据表（如果不存在）
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        address TEXT,
                        reachability TEXT,
                        verifiedPrice TEXT,
                        minPieceSize TEXT,
                        maxPieceSize TEXT,
                        rawPower TEXT,
                        isoCode TEXT,
                        region TEXT,
                        score TEXT,
                        freeSpace TEXT,
                        averagePrice TEXT,
                        `rank` TEXT 
                    )''')

    # 插入数据
    sql = f'''INSERT INTO {table_name} (address, reachability, verifiedPrice, minPieceSize,maxPieceSize, rawPower, isoCode, region, score, freeSpace, averagePrice, `rank`)
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

    # 读取 CSV 文件并插入数据
    with open(csv_file, 'r') as file:
        csv_data = csv.reader(file)
        count = 0
        for row in csv_data:
            cursor.execute(sql, row)
            count +=1
        print(count)
    logger.info(f"Table '{table_name}' has been writen successful.")
    # 提交事务并关闭连接
    conn.commit()
    conn.close()


def write_to_database_by_csv_pingminers(csv_file):
    print(csv_file)
    # 连接到 SQLite 数据库
    # jdbc:mysql://124.70.130.44:3306/blockchain?useSSL=false
    conn = mysql.connector.connect(
        host=os.getenv('HOST'),
        port=os.getenv('PORT'),
        user=os.getenv('USER'),
        password=os.getenv('PASSWORD'),
        database=os.getenv('DATABASE')
    )

    table_name = 'pingminers'
    database = os.getenv('DATABASE')
    # 创建一个游标对象
    cursor = conn.cursor()

    cursor.execute(f"DROP TABLE IF EXISTS {table_name}")
    logger.info(f"Table '{table_name}' exists and has been deleted.")

    # 创建数据表（如果不存在）
    cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name} (
                        address TEXT,
                        minPieceSize TEXT,
                        maxPieceSize TEXT,
                        Price TEXT,
                        VerifiedPrice TEXT,
                        Ping TEXT 
                    )''')

    # 插入数据
    sql = f'''INSERT INTO {table_name} (address, minPieceSize, maxPieceSize, Price, VerifiedPrice, Ping)
             VALUES (%s, %s, %s, %s, %s, %s)'''

    # 读取 CSV 文件并插入数据
    with open(csv_file, 'r') as file:
        csv_data = csv.reader(file)
        count = 0
        for row in csv_data:
            row = row[:-1]
            if count == 0:
                row = row[6:]
                row[0] = row[0][9:]
            cursor.execute(sql, row)
            count +=1
        print(count)
    logger.info(f"Table '{table_name}' has been writen successful.")
    # 提交事务并关闭连接
    conn.commit()
    conn.close()