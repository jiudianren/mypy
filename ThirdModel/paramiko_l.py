# _*_ coding: utf-8 _*_
# author jiudianren
# time:2020/1/21 11:43


import paramiko



def test():
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(hostname="10.43.83.192",
                   port="22",
                   username="mcs_usr",
                   password="mcs_ver1234")

    stdin,stdout, stderr = client.exec_command("pwd")
    print(dir(stdin))

    print(f"stdin:{stdin}")
    print(f"stdout:{stdout.read()}")
    print(f"stderr:{stderr.read()}")

test()
