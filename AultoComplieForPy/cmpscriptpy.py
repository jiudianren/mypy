# coding=gbk
import os
import sys
import time
import pdb

import logging
from FunctionLearning.DecoratorTest import log
logging.basicConfig(level=logging.DEBUG)


'''
python cmpscriptpy.py t
0 请设置  make -j 中使用的核心数
1 如需 执行perl， 需要加入 pe(perl) 选项
2 如果需要release 模式，则需要加入r (debug) 选项
3 
    techlib        需要至少一个字符 : t te techlib
    hub            需要至少一个字符 : h
    unittest        需要至少一个字符 : u
    pcrf            需要 至少两个 : pc
    perl          需要至少两个字符 ：pe
    servicelib    需要至少两个字符 ：se
    spr            需要至少两个字符 ：sp

#待加入
hub部分编译特殊，需要增加特殊处理

'''


logging.warn("**********" )
# 更改如下配置为自己的配置
logging.warn("Confirm changt thest args" )
GMakejcout= 4
logging.warn("make -j ?? j=%d" % GMakejcout )
# 执行make install时候，回显到屏幕的内容 
GMakeInstallResultFile="MIRSFILE"
#默认debug 模式
GDebugModle=True
#当前编译是否包含hub模块
GContainHub=False

logging.warn("**********" )

##
def GetPcrfServerPath():
    PCRF_HOME=os.popen("echo $PCRF_HOME").read().strip('\n')
    logging.debug(PCRF_HOME) 
    PCRFServer="PCRFServer"
    PCRFServer_HOME = os.path.join(PCRF_HOME,PCRFServer)
    print("PCRFServer_HOME is %s" % PCRFServer_HOME)
    #检查是否存在
    if not os.path.exists(PCRFServer_HOME):
        logging.warn("%s not exist， Faild" % PCRFServer_HOME)
        os._exit()
    logging.info("PCRFServer_HOME is %s" % PCRFServer_HOME)
    return  PCRFServer_HOME



def GetPCRFServerSubdir():
    GetPcrfServerPath()
    '''
    subDir= [x for x in os.listdir(PCRFServer_HOME) if os.path.isdir(x)]
    for key in subDir:
        print(key)
    '''
    #编译子目录有顺序的 perl 是一个标志
    CompileDir=   {'techlib': 1,'servicelib':2,'hub':3 ,'pcrf':4,'spr':5 ,'unittest':6, "perl":7, "release":8}
    for k, v in CompileDir.items():
        logging.debug("dir: %s, index :%d" %(k,v))
    return   CompileDir 
        

    
def GetParma( CompileDir ):
    args = sys.argv
    argslen =len(args)
    needCmpSubDir=[]
    logging.info("You input (%d) models" % (argslen -1) )
    if len(args)==1:
        logging.warn('Please Input the compile model ! Failed')
        os._exit()
    else:
        AnalyParma=args[1:argslen]
        for arg in AnalyParma :
            #参数全部转化为小写
            arg=arg.lower()
            logging.info("arg : %s " % arg  )
#             pdb.set_trace()
            rs = GetSubDir(arg, CompileDir);
            if  rs != "" :
                needCmpSubDir.append(rs)
            else:
                logging.warn("please check the parm :%s" % arg) 
        
        logging.info("**************")
        for key in    needCmpSubDir:
            logging.info("going to compile : %s" % key)
        logging.info("**************")
    return needCmpSubDir


def GetSubDir(arg , CompileDir):
    compile=""
    for k in CompileDir :
        if (k.find( arg)  == 0 ) and ( arg[0] =='t' or arg[0] =='h'  or arg[0] =='u' or arg[0]=='r' ) :
            compile = k
            logging.info("get your input :%s--> %s" % (arg ,compile))
            return  compile
        elif (k.find( arg)  == 0 ) and ( arg[0:2]=="pc" or arg[0:2] =="pe" or arg[0:2] =="sp" or arg[0:2] =="se" ) :        
            compile = k
            logging.info("get your input :%s--> %s" % (arg ,compile))
            return  compile 
        else :
            continue
    return compile

#perl 执行结束，需要一个end  todo
def  DoPerlCmd():
    PServerHome = GetPcrfServerPath()
    unitTestKeyWord="unittest"
    unitTestDir=os.path.join(PServerHome,unitTestKeyWord)
    
    if not os.path.exists(unitTestDir):
        logging.warn("%s not exist， Faild" % unitTestDir)
        os._exit()
    #需要查看下文件是否存在 todo
    
    perlscritp="/home/phub/n81/PCRFServer/unittest/make_mocker_actions.pl"
    cmd="perl "
    cmd+=perlscritp
    logging.info("perl cmd is %s " % cmd)
    os.system(cmd)
    
  


def GetBuildPath(key) :
    PServerHome = GetPcrfServerPath()
  
    keyDir=os.path.join(PServerHome,key)
    logging.debug("keyDir is %s" % keyDir)
    buildKeyWord="build"
    buildPath=os.path.join(keyDir,buildKeyWord)
    logging.info(" buildPath is %s" % buildPath)
    subKeyDir= [x for x in os.listdir(keyDir) if os.path.isdir(x)]
    
    for key  in subKeyDir:
        logging.debug(" key is %s" % key)
    
    
    if not os.path.exists(buildPath):
        logging.info("%s not exist." % buildPath)
        os.mkdir(buildPath)
        if not os.path.exists(buildPath):
            logging.warn("make dir : %s faild and exit" % buildPath)
            os._exit()
        else : 
            return buildPath
    else:
        return buildPath


def RmMakeInstallFile():
    rmFileCmd ="rm "
    rmFileCmd += GMakeInstallResultFile
    rmFileCmd +="*"
    logging.debug("rm file cmd is %s" % rmFileCmd )
    os.system(rmFileCmd)


def DoCmd(cmdStr):
    print("cmd is %s" % cmdStr)
    cmdRS=os.system(cmdStr)
    if  cmdRS != 0 :
        logging.warn("cmd faild，and result code:%d " % (cmdRS) )
        os._exit()
    
def GetMakeInstallCmd():
    strTime = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) 
    strTime=strTime.replace(" ","").replace(":","").replace("-","")
    logging.debug(strTime)
    
    makeinstall="make -j "
    makeinstall += str( GMakejcout )
    makeinstall +=" install | tee -a MIRSFILE"
    makeinstall += strTime
    logging.debug(" cmd makeinstall is %s" ,makeinstall)
    return makeinstall

def GetCmakeCmd():
    cmakeCmd="cmake -DCMAKE_INSTALL_PREFIX=$HOME "
    if GDebugModle:
        cmakeCmd+="-DCMAKE_BUILD_TYPE=Debug "
    #todo
    if GContainHub:
        logging.warn("going todo option for hub to add")
    
    cmakeCmd+="-DCMAKE_C_COMPILER=`which gcc` -DCMAKE_CXX_COMPILER=`which c++` .."
    logging.debug("cmake cmd :%s" ,cmakeCmd)
    return cmakeCmd

def CompileBuildPath(buildPath) :
    oldPath=os.path.abspath('.')
    logging.info("current path is: %s" % oldPath)
    os.chdir(buildPath)
    curPath=os.path.abspath('.')
    logging.info("current path is: %s" % curPath)
    
    RmMakeInstallFile()
    
    cmakeCmd=GetCmakeCmd()
    DoCmd(cmakeCmd)
    
    makeclean="make clean"
    DoCmd(makeclean)
    
    makeinstall = GetMakeInstallCmd()
    DoCmd(makeinstall)

    os.chdir(oldPath)
    logging.info("current path is: %s" % oldPath)
        
            
def CompileSubDir(needCompSubDir , CompileDir):
    if  "perl" in needCompSubDir:
        DoPerlCmd()
    if "release"  in needCompSubDir:
        #release模式
        logging.warn("Release Modem")
        GDebugModle = False
    if "hub" in needCompSubDir:
        GContainHub=True
        logging.warn("Contain  Hub model")
    for key    in  needCompSubDir:
        #先编译 techlib service 如果存在的话
        #CompileDir=   {'techlib': 1,'servicelib':2,'hub':3 ,'pcrf':4,'spr':5 ,'unittest':6, "perl":7}
        if (key == "techlib") or  ( key != "servicelib") :
            buildPath = GetBuildPath(key)
            CompileBuildPath(buildPath)
        elif (key == "hub" ) or (key == "pcrf" ) or (key == "spr" ) :
            buildPath = GetBuildPath(key)
            CompileBuildPath(buildPath)
        elif key =='unittest':
            key+="/src/"
            logging.info("unittest key is: %s" % key)
            buildPath=  GetBuildPath(key)
            CompileBuildPath(buildPath)
        else:
            logging.warn("Cann: %s" % key)
            pass
        
        
    
def CompileAll():
    CompileDir = GetPCRFServerSubdir();
    needCompSubDir = GetParma(CompileDir)
    CompileSubDir( needCompSubDir, CompileDir);



if __name__=='__main__':
    CompileAll()





