# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/5 16:42


import requests
import zipfile
import configparser


def unzip_single(src_file, dest_dir):
    print("unzip_single start")
    f_str = src_file
    zf = zipfile.ZipFile(f_str)
    try:
        zf.extractall(path=dest_dir)
    except RuntimeError as e:
        print(e)
    zf.close()
    print("unzip_single end")


def download(url, zip_fn):
    r = requests.get(url.strip(), stream=True)
    print(r.status_code)
    if r.status_code != 200:
        print(r.headers)
        print("download Erro " + r.status_code)
        return False

    with open(zip_fn, "wb") as zipname:
        for chunk in r.iter_content(chunk_size=1024): #边下载边存硬盘
            if chunk:
                zipname.write(chunk)

    print("download ok")
    return True


if __name__ == "__main__":
    config = configparser.ConfigParser()
    config.read("downloadgit.ini")
    url = config["git"]["url"]
    print(url)
    print(type(url))
    zip_fn = config["dir"]["zipfile"]
    uzip_dir = config["dir"]["uzipdir"]
    print(zip_fn + uzip_dir)

    if download(url, zip_fn):
        unzip_single(zip_fn, uzip_dir)







