

'''
获取异常时的堆栈信息。
'''
def get_tb_info(e:Exception):
    exType, exValue, exTrace = sys.exc_info()
    # msg = msg + f"\nexType {exType}"
    # msg = msg + f"\nexValue {exType}"
    msg="\n"
    trace_msg = "traceback:\n"
    for trace in traceback.extract_tb(exTrace):
        trace_msg = trace_msg + str(trace) + "\n"
    msg = msg + trace_msg
    msg = msg + f"Exception:{e.args}"
    return msg
