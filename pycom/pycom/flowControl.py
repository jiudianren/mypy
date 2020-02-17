import  time
import  random
TIME_UNIT = 10
CNT_UNIT  = 100

total_cnt = 0;
last_time = 0;
cur_time  = 0;


def flowContral( cnt):
    global  last_time
    global  cur_time
    global  total_cnt

    if last_time == 0 :
        last_time = time.time()
    cur_time = time.time()

    total_cnt +=  cnt
    if   total_cnt >  CNT_UNIT:
        if cur_time -last_time > TIME_UNIT:
            total_cnt = 0
            last_time = time.time()
        else:
            print(f"last :{last_time} cur:{cur_time}--{last_time - cur_time} total:{total_cnt} discard :{cnt}")
    else:
        print(f"last :{last_time} cur:{cur_time}--{last_time - cur_time} total:{total_cnt} pass :{cnt}")


if  __name__ == "__main__" :

    times = 100

    while times > 0:
        one_time = random.randrange(0, 20)
        cnt = random.randrange(0, 200)
        time.sleep( one_time )
        print(f" sleep {one_time} add cnt {cnt} ")
        flowContral( cnt)
        times = times -1