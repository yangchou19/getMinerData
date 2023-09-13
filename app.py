import schedule
import time
from database import *
from extract import *
from dotenv import load_dotenv
from my_logging import logger

load_dotenv()


def get_miner_data(url, miner_json, miner_csv, keep_keys):
    send_request_to_url(url, miner_json)
    extract_json_to_csv(miner_json, miner_csv, keep_keys)
    write_to_database_by_csv(miner_csv)


if __name__ == '__main__':
    url = os.getenv("MINER_URL")
    miner_json = os.getenv("MINER_JSON_FILE")
    miner_csv = os.getenv("MINER_CSV_FILE")
    # 定义需要保留的键名列表
    keep_keys = ["address", "reachability", "verifiedPrice", "minPieceSize", "maxPieceSize", "rawPower", "isoCode",
                 "region", "score", "freeSpace", "averagePrice", "rank"]
    logger.info("start sending request!")

    # get_miner_data(url, miner_json, miner_csv, keep_keys)

    # # 定义每天发送请求的任务
    schedule.every().day.at("19:00").do(get_miner_data)
    # 循环执行任务
    while True:
        logger.info("start sending request!")
        schedule.run_pending()
        time.sleep(1)
        logger.info("finish sending request!")
