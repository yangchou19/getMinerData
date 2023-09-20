import schedule
import time
import paramiko
from database import *
from extract import *
from dotenv import load_dotenv
from database import write_to_database_by_csv_pingminers
from my_logging import logger

load_dotenv()

def get_ping_miner_data():
    logger.info("start sending request!")
    # 远程服务器的连接信息
    hostname = '159.138.88.235'
    port = 22  # SSH端口号
    username = 'root'
    password = 'Shunine8'

    # 连接到远程服务器
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    ssh.connect(hostname, port, username, password)

    # 下载文件
    remote_file_path = '/mnt/data/filecoin/miner.csv'
    local_file_path = 'data/pingminers.csv'
    sftp = ssh.open_sftp()
    sftp.get(remote_file_path, local_file_path)
    sftp.close()

    # 关闭SSH连接
    ssh.close()
    write_to_database_by_csv_pingminers(local_file_path)


def get_miner_data(url, miner_json, miner_csv, keep_keys):
    logger.info("start sending request!")
    send_request_to_url(url, miner_json)
    extract_json_to_csv(miner_json, miner_csv, keep_keys)
    get_ping_miner_data()
    write_to_database_by_csv(miner_csv)
    logger.info("finish sending request!")


url = os.getenv("MINER_URL")
miner_json = os.getenv("MINER_JSON_FILE")
miner_csv = os.getenv("MINER_CSV_FILE")

# 定义需要保留的键名列表
keep_keys = ["address", "reachability", "verifiedPrice", "minPieceSize", "maxPieceSize", "rawPower", "isoCode",
             "region", "score", "freeSpace", "averagePrice", "rank"]
logger.info("start sending request!")


get_miner_data(url, miner_json, miner_csv, keep_keys)


# 定义每天发送请求的任务
schedule.every().day.at("19:00").do(get_miner_data, url, miner_json, miner_csv, keep_keys)


# 循环执行任务
while True:
    schedule.run_pending()
    time.sleep(1)
