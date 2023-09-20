# import paramiko
from database import write_to_database_by_csv_pingminers
# 远程服务器的连接信息
# hostname = '159.138.88.235'
# port = 22  # SSH端口号
# username = 'root'
# password = 'Shunine8'
#
# # 连接到远程服务器
# ssh = paramiko.SSHClient()
# ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
# ssh.connect(hostname, port, username, password)
#
# # 下载文件
# remote_file_path = '/mnt/data/filecoin/miner.csv'
local_file_path = 'data/pingminers.csv'
# sftp = ssh.open_sftp()
# sftp.get(remote_file_path, local_file_path)
# sftp.close()
#
# # 关闭SSH连接
# ssh.close()
write_to_database_by_csv_pingminers(local_file_path)