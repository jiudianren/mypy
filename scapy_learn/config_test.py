# _*_ coding: utf-8 _*_
# author jiudianren
# time:2019/8/8 19:43

class MyConfClass(object):
    def configure(self, cnf):
        self.__dict__ = cnf.__dict__.copy()

    def __repr__(self):
        return str(self)

    def __str__(self):
        s = ""
        keys = self.__class__.__dict__.copy()
        keys.update(self.__dict__)
        keys = sorted(keys)
        for i in keys:
            if i[0] != "_":
                r = repr(getattr(self, i))
                r = " ".join(r.split())
                wlen = 76 - max(len(i), 10)
                if len(r) > wlen:
                    r = r[:wlen - 3] + "..."
                s += "%-10s = %s\n" % (i, r)
        return s[:-1]

class MyCommandsList(list):
    def __repr__(self):
        s = []
        for l in sorted(self, key=lambda x: x.__name__):
            doc = l.__doc__.split("\n")[0] if l.__doc__ else "--"
            s.append("%-20s: %s" % (l.__name__, doc))
        return "\n".join(s)

    def register(self, cmd):
        self.append(cmd)
        return cmd  # return cmd so that method can be used as a decorator


class MyConf(MyConfClass):
    commands = MyCommandsList()

myconf = MyConf()

@myconf.commands.register
def func1(filename ):
    """Read a pcap or pcapng file and return a packet list

count: read only <count> packets

    """
    print(filename)



if __name__ == "__main__":
    print(myconf.commands)
    print("Bye Bye")
