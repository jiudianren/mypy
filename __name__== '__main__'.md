

# 如何理解

https://blog.konghy.cn/2017/04/24/python-entry-program/

#  1

    const.py
    PI = 3.14

    def main():
        print "PI:", PI

    main()
    
    
    
    cal.py
    from const import PI

    def calc_round_area(radius):
        return PI * (radius ** 2)

    def main():
        print "round area: ", calc_round_area(2)

    main()
    
    ----print PI
    ----print round area
    

#  2

    const.py
    PI = 3.14

    def main():
        print "PI:", PI
  
    if __name__ == "__main__":
      main()
    
   
    
    cal.py
    from const import PI

    def calc_round_area(radius):
        return PI * (radius ** 2)

    def main():
        print "round area: ", calc_round_area(2)

    main()
   
    ----print round area
    
    
    
