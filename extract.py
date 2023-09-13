import json
import csv
import os
import urllib.request
from dotenv import load_dotenv
from my_logging import logger

load_dotenv()
'{"pagination":{"total":6176,"limit":10},"miners":[{"id":0,"address":"f01393827","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"500000000","verifiedPrice":"50000000","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"1100989096525824","qualityAdjPower":"1101022310957056","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"846658313125888","storageDeals":{"total":7,"noPenalties":7,"successRate":"1.00000000000000000000","averagePrice":"42871093","dataStored":"4297719808","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":5},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"1","regionRank":"1"},{"id":1,"address":"f01690643","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"0","verifiedPrice":"0","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"384794709983232","qualityAdjPower":"1138343935672320","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"53498112638976","storageDeals":{"total":675,"noPenalties":675,"successRate":"1.00000000000000000000","averagePrice":"29629","dataStored":"23158463791104","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":544},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":true,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"2","regionRank":"2"},{"id":2,"address":"f01694564","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"0","verifiedPrice":"0","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"343425584988160","qualityAdjPower":"1272068995055616","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"71330816851968","storageDeals":{"total":212,"noPenalties":212,"successRate":"1.00000000000000000000","averagePrice":"94339","dataStored":"7249904926720","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":208},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":true,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"3","regionRank":"3"},{"id":3,"address":"f01690774","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"0","verifiedPrice":"0","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"308619170021376","qualityAdjPower":"1101670667223040","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"50474455662592","storageDeals":{"total":706,"noPenalties":706,"successRate":"1.00000000000000000000","averagePrice":"28328","dataStored":"24223615680512","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":439},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":true,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"4","regionRank":"4"},{"id":4,"address":"f01652952","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"0","verifiedPrice":"0","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"262336602439680","qualityAdjPower":"1109892119461888","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"54219667144704","storageDeals":{"total":757,"noPenalties":757,"successRate":"1.00000000000000000000","averagePrice":"26420","dataStored":"25975962337280","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":498},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":true,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"5","regionRank":"5"},{"id":5,"address":"f01690781","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"0","verifiedPrice":"0","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"259897061015552","qualityAdjPower":"1101403320975360","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"53360673685504","storageDeals":{"total":953,"noPenalties":953,"successRate":"1.00000000000000000000","averagePrice":"20986","dataStored":"26086646491648","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":606},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":true,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"6","regionRank":"6"},{"id":6,"address":"f01448847","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"500000000","verifiedPrice":"50000000","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"137885630070784","qualityAdjPower":"137885630070784","isoCode":"CN","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"92736933855232","storageDeals":{"total":5,"noPenalties":5,"successRate":"1.00000000000000000000","averagePrice":"112000000","dataStored":"1074135040","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":1},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"7","regionRank":"7"},{"id":7,"address":"f0117439","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"1000000000000000000","verifiedPrice":null,"minPieceSize":null,"maxPieceSize":null,"rawPower":"39685497815040","qualityAdjPower":"39685497815040","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"48206712930304","storageDeals":{"total":7,"noPenalties":7,"successRate":"1.00000000000000000000","averagePrice":"100000000","dataStored":"2575302656","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":null},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"8","regionRank":"8"},{"id":8,"address":"f07819","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"10000000000","verifiedPrice":null,"minPieceSize":null,"maxPieceSize":null,"rawPower":"31851477467136","qualityAdjPower":"31851477467136","isoCode":"CN","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"17076789968896","storageDeals":{"total":78,"noPenalties":78,"successRate":"1.00000000000000000000","averagePrice":"25518131702","dataStored":"170465837056","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":null},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"9","regionRank":"9"},{"id":9,"address":"f01399784","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"500000000","verifiedPrice":"50000000","minPieceSize":"256","maxPieceSize":"68719476736","rawPower":"11957188952064","qualityAdjPower":"11957188952064","isoCode":"TW","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"2680059592704","storageDeals":{"total":1,"noPenalties":1,"successRate":"1.00000000000000000000","averagePrice":"20000000","dataStored":"131072","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":1},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"10","regionRank":"10"}]}'

def send_request_to_url(url: str, file_dir):
    url_number =  url + "?limit=1"
    response_number = urllib.request.urlopen(url_number)
    response_number = response_number.read()
    json_data = json.loads(response_number)
    total = json_data['pagination']['total']
    url_total = url + "?limit=" + str(total)
    print(url_total)
    response = urllib.request.urlopen(url_total)
    response = response.read()
    json_data = json.loads(response)
    miners = json_data['miners']
    # 将 JSON 对象写入文件
    with open(file_dir, 'w') as file:
        json.dump(miners, file)
    logger.info(f"The miner json read from {url_total} successfully!")



# 提取需要保留的键值对
def extract_data(json_obj, keys):
    extracted_data = {}
    for key, value in json_obj.items():
        if key in keys:
            extracted_data[key] = value
        elif isinstance(value, dict):
            nested_data = extract_data(value, keys)
            extracted_data.update(nested_data)
    return extracted_data


def extract_json_to_csv(input_name, output_name, keep_keys):

    # 加载 JSON 文件
    with open(input_name, encoding='utf') as json_file:
        json_list = json.load(json_file)

    # 检查文件是否存在
    if os.path.isfile(output_name):
        # 删除文件
        os.remove(output_name)
        logger.info(f"csv file has been successfully deleted!")
    else:
        logger.info(f"csv file does not exist.")
    # 写入 CSV 文件
    for json_obj in json_list:
        filtered_data = extract_data(json_obj, keep_keys)
        # 提取键名作为表头
        headers = filtered_data.keys()
        with open(output_name, 'a', newline='') as csv_file:
            writer = csv.writer(csv_file)

            # # 写入表头（只在第一个 JSON 对象写入）
            # if json_obj == json_list[0]:
            #     writer.writerow(headers)

            # 写入数据行
            writer.writerow(filtered_data.values())
    logger.info(f"csv file has been successfully writen to {output_name}!")

if __name__ == '__main__':
    url = os.getenv("MINER_URL")
    miner_json = os.getenv("MINER_JSON_FILE")
    miner_csv = os.getenv("MINER_CSV_FILE")

    # 定义需要保留的键名列表
    keep_keys = ["address","isoCode","region","reachability","rawPower","verifiedPrice","minPieceSize","maxPieceSize","freeSpace","averagePrice","score","rank"]
    # result = send_request_to_url(url, fir_dir)

    # result = '{"pagination":{"total":1,"offset":0,"limit":10},"miners":[{"id":0,"address":"f01393827","status":true,"reachability":"reachable","tag":{"name":null,"verified":null},"uptimeAverage":1,"price":"500000000","verifiedPrice":"50000000","minPieceSize":"256","maxPieceSize":"34359738368","rawPower":"1100989096525824","qualityAdjPower":"1101022310957056","isoCode":"KR","region":"Asia","creditScore":null,"score":"100","scores":{"total":"100","uptime":"30","storageDeals":"40","committedSectorsProofs":"30"},"freeSpace":"846658313125888","storageDeals":{"total":7,"noPenalties":7,"successRate":"1.00000000000000000000","averagePrice":"42871093","dataStored":"4297719808","slashed":0,"terminated":0,"faultTerminated":0,"recent30days":5},"goldenPath":{"storageDealSuccessRate":true,"retrievalDealSuccessRate":false,"fastRetrieval":null,"verifiedDealNoPrice":false,"faultsBelowThreshold":true},"energy":{"recs":null,"pageUrl":null},"rank":"1","regionRank":"1"}]}'
    # extract_data(result, keep_keys)
    extract_json_to_csv(miner_json, miner_csv, keep_keys)
