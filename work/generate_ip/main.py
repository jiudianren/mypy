# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/12/10 9:22


# perform-config epdg-address 1.1.1.1 vrf Gn desc epdg_1

def gen_ip(size=1024):
    cnt = 0
    no_str_list =[]
    for i in range(1, 255):
        for j in range(1, 255):
            for k in range(1, 255):
                for m in range(1, 255):
                    strs = "perform-config epdg-address "
                    cnt = cnt + 1
                    strs += f"{i}.{j}.{k}.{m}"
                    strs += " vrf Gn desc "
                    strs += "epdg_"
                    strs += str(cnt)
                    print(strs)

                    #no perform-config epdg-address 1.1.1.1 vrf Gn
                    no_str = "no perform-config epdg-address "
                    no_str += f"{i}.{j}.{k}.{m}"
                    no_str += " vrf Gn"
                    no_str_list.append(no_str)
                    if cnt == size:
                        for it in no_str_list:
                            print(it)
                        return


if __name__ == "__main__":
    str(1000)
    gen_ip()
