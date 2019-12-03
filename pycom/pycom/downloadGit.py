# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/11/5 16:42


import requests
import zipfile
import configparser


def unzip_single(src_file, dest_dir):
    print("unzip_single start")
    f_str = src_file

    try:
        zf = zipfile.ZipFile(f_str)
        zf.extractall(path=dest_dir)
        zf.close()
    except Exception as e:
        print(f"---***Exception:{e}  ***----")
    finally:
        print("finally do")

    print("unzip_single end")


def download(url, zip_fn):
    r = requests.get(url.strip(), stream=True)
    print(f"status code:{r.status_code}" )

    if r.status_code != 200:
        print(r.headers)
        print("download Erro " + r.status_code)
        return False

    with open(zip_fn, "wb") as zipname:
        data_size = 0
        chunk_size = 16240
        TE = r.headers.get('Transfer-Encoding')
        print(f"Transfer-Encoding:{TE}")
        for chunk in r.iter_content(chunk_size=chunk_size): #边下载边存硬盘
            data_size += 1
            print(f"data_size *{chunk_size}: {data_size}")
            if chunk:
                zipname.write(chunk)

    print("download ok")
    return True


def deal_repository( repository_name):
    config_item ="git_"
    config_item += repository_name
    print(config_item)

    config = configparser.ConfigParser()
    config.read("downloadgit.ini")
    url = config[config_item]["url"]
    print(url)

    zip_filename = config[config_item]["zipfile"]
    uzip_dir = config[config_item]["uzipdir"]

    print(zip_filename + "  "+uzip_dir)

    if download(url, zip_filename):
        unzip_single(zip_filename, uzip_dir)

if __name__ == "__main__":
    deal_repository("mypy")
    #deal_repository("jiudianren")




