# -*- coding: utf-8 -*-
from ftplib import FTP
import time,tarfile,os
from mylogger import logger


#连接ftp
def ftpconnect(host,port, username, password):
    ftp = FTP()
    # 打开调试级别2，显示详细信息
    # ftp.set_debuglevel(2)
    ftp.connect(host, port)
    ftp.login(username, password)
    return ftp

#从ftp下载文件
def downloadfile(ftp, remotepath, localpath):
    # 设置的缓冲区大小
    bufsize = 1024
    fp = open(localpath, 'wb')
    ftp.retrbinary('RETR ' + remotepath, fp.write, bufsize)
    ftp.set_debuglevel(0) # 参数为0，关闭调试模式
    fp.close()

#从本地上传文件到ftp
def uploadfile(ftp, remotepath, localpath):
    bufsize = 1024
    fp = open(localpath, 'rb')
    ftp.storbinary('STOR ' + remotepath, fp, bufsize)
    ftp.set_debuglevel(0)
    fp.close()

def download_dir(ftp, remotedir, localdir):
    logger.debug( ftp.nlst(remotedir))
    if not os.path.exists(localdir):
        os.mkdir(localdir)
    files = ftp.nlst(remotedir)
    for  it in files:
        remotfile = os.path.join(remotedir, it)
        localfile = os.path.join(localdir, it)
        downloadfile(ftp,remotfile,localfile )


def upload_dir(ftp, remotedir, localdir):
    if not os.path.exists(localdir):
        logger.erro("erro")
        return
    files = os.listdir(localdir)
    logger.debug(files)
    for it in files:
        remotfile = os.path.join(remotedir, it)
        localfile = os.path.join(localdir, it)
        uploadfile(ftp, remotfile,localfile )

if __name__ == "__main__":
    #host,port, username, password 10.43.22.160:2121
    ftp = ftpconnect("10.43.22.160", 2121,"iop", "iop_123")
    #download_dir(ftp,"/lpf_test","D:\jiudianren\Temp")
    upload_dir(ftp, "/lpf_test", "D:\jiudianren\Temp")
    if 0:
        #下载文件，第一个是ftp服务器路径下的文件，第二个是要下载到本地的路径文件
        downloadfile(ftp, "/12.mp3", r"C:\Users\Administrator\Desktop\ftp\download\test.mp3")
        # 上传文件，第一个是要上传到ftp服务器路径下的文件，第二个是本地要上传的的路径文件
        #uploadfile(ftp, '/upload/1.txt', "C:/Users/Administrator/Desktop/1.txt")
    ftp.close() #关闭ftp