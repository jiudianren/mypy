# coding=gbk
import os
import sys
import time
import pdb
import logging

logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

'''
准备：
1、 设置  $PCRF_HOME 环境变量
2、 设置$IMPSYSDIR 环境变量
3、 目录结构要求：
   %PCRF_HOME----
                |
                |
                ---PCRFSERVER---
                                |
                                |
                                |
                                ---HUB
                                |
                                |
                                ---techlib
                                |
                                .......
                                
                                
4 请设置  make -j 中使用的核心数  "GMakejcout= xx" （将 xx 改为 需要使用的核心数 默认为 4）                    


使用:
python cmpscript.py xx1 xx2 xx3 xx4 ....

1 如需 执行perl， 需要加入 pe(perl) 选项
2 如果需要Release 模式，则需要加入r (Release) 选项
3 hub部分默认编译方式 DB + QMDB [default]  如果需要采用QMDB模式（qmdb only） ，需要  加入  q(qmdb)选项
4 如果 （techlib或者servicelib） 和 其他模块 同时需要编译，则先编译（techlib或者servicelib） ,后编译 其他模块
5 如果pcrf和 unintest同时需要编译，则先编译pcrf ,后编译 unittest
6 参数输入： 
    techlib        需要至少一个字符 : t te techlib
    hub            需要至少一个字符 : h
    unittest        需要至少一个字符 : u
    release        需要至少一个字符 ：r
    qmdb          需要至少一个字符 ：q （for hub qmdb only 模式）
    
    pcrf            需要 至少两个 : pc
    perl          需要至少两个字符 ：pe
    servicelib    需要至少两个字符 ：se
    spr            需要至少两个字符 ：sp

示例   
1 编译 techlib 内容
python cmpscript.py t 
或者
python cmpscript.py  techlib
python cmpscript.py  techli
python cmpscript.py  techl
python cmpscript.py  tech
python cmpscript.py  tec
python cmpscript.py  te

2 同时编译多个模块 
python cmpscript.py te se pc (同时编译 te se pc 等 模块)
3 需要执行perl 后 编译 pcrf 和 unittest
python cmpscript.py pe pc un
4  hub部分，需要以 qmdbonly方式编译，并且需要同时编译pcrf模块
python cmpscript.py qmdb h pc
'''


logging.warn("**********" )
# 更改如下配置为自己的配置
logging.warn("Confirm change these args" )
GMakejcout= 4
logging.warn("make -j ?? j=%d" % GMakejcout )

# 执行make install时候，回显到屏幕的内容  同时输出到文件 名称
GMakeInstallResultFile="MIRSFILE"

#只观察脚本执行的编译顺序，不执行 cmake make等命令 默认false
ObserveCompileOrder = False
logging.warn(" just obser the compile order flag :%s" % ObserveCompileOrder )
logging.warn("**********" )


#全局变量
#默认debug 模式
GDebugModle=True
#默认hub编译时候 采用 DB+QMDB模式
HubQmdbOnlyFlag=False



## PCRFServer 检查PCRFServer是否存在
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
    CompileDir={'techlib': 1,'servicelib':2,'hub':3 ,'pcrf':4,'spr':5 ,'unittest':6, "perl":7, "release":8,"qmdb":9}
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
#     pdb.set_trace()
    compile=""
    for k in CompileDir :
        if (k.find( arg)  == 0 ) and ( arg[0] =='t' or arg[0] =='h'  or arg[0] =='u' or arg[0]=='r' or arg[0]=='q'  ) :
            compile = k
            logging.info("get your input :%s--> %s" % (arg ,compile))
            return  compile
        elif ( k.find( arg)  == 0 ) and ( arg[0:2]=="pc" or arg[0:2] =="pe" or arg[0:2] =="sp" or arg[0:2] =="se" ) :        
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
    
    if (key == "unittest"):
        key+="/src/"
        logging.info("unittest key is: %s" % key)
    
    keyDir=os.path.join(PServerHome,key)
    logging.debug("keyDir is %s" % keyDir)
    buildKeyWord="build"
    buildPath=os.path.join(keyDir,buildKeyWord)
    logging.info(" buildPath is %s" % buildPath)
    subKeyDir= [x for x in os.listdir(keyDir) if os.path.isdir(x)]
    
    for key in subKeyDir:
        logging.debug(" key is %s" % key)
    
    # 是否存在build路径，如果不存在 则尝试创建一次，如果创建失败 ，则退出脚本
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


def RmMakeInstallRecordFile():
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

def GetCmakeCmd( curPath ):
    logging.debug(" curPath %s" % curPath)
    cmakeCmd="cmake "
    
    if (curPath.find("hub") >= 0) and ( HubQmdbOnlyFlag == True ):
        logging.debug(" hub  %s" % curPath)
        cmakeCmd += " -DCMAKE_INSTALL_PREFIX=${IMPSYSDIR} "
        cmakeCmd += " -DQMDB=QuickMDB "
    else:
        cmakeCmd += " -DCMAKE_INSTALL_PREFIX=$HOME " 
        
    if GDebugModle:
        cmakeCmd+="-DCMAKE_BUILD_TYPE=Debug "
    
    cmakeCmd+="-DCMAKE_C_COMPILER=`which gcc` -DCMAKE_CXX_COMPILER=`which c++` .."
    logging.debug("cmake cmd :%s" ,cmakeCmd)
    return cmakeCmd

def CompileBuildPath(buildPath) :
    oldPath=os.path.abspath('.')
    logging.info("current path is: %s" % oldPath)
    os.chdir(buildPath)
    curPath=os.path.abspath('.')
    logging.info("current path is: %s" % curPath)
    
    RmMakeInstallRecordFile()
    
    if ObserveCompileOrder == False:
        cmakeCmd=GetCmakeCmd( curPath )
        DoCmd(cmakeCmd)
        
        makeclean="make clean"
        DoCmd(makeclean)
        
        makeinstall = GetMakeInstallCmd()
        DoCmd(makeinstall)

    os.chdir(oldPath)
    logging.info("current path is: %s" % oldPath)
        
            
def CompileSubDir(needCompSubDir):
    #'techlib', '.git', 'servicelib', 'unittest', '.settings', 'spr', 'document', 'pcrf', 'hub'
    compileSubDir=['techlib', 'servicelib', 'unittest', 'spr', 'pcrf', 'hub']
    if  "perl" in needCompSubDir:
        DoPerlCmd()
        
    if "release"  in needCompSubDir:
        #release模式
        logging.warn("Release Modem")
        GDebugModle = False

    if "qmdb" in needCompSubDir:
        HubQmdbOnlyFlag = True
        logging.warn(" QMDB Only model for hub")
    
    if   ("techlib" in needCompSubDir) :
            buildPath = GetBuildPath("techlib")
            CompileBuildPath(buildPath)
            needCompSubDir.remove("techlib")
            
    if  ("servicelib" in needCompSubDir) :
            buildPath = GetBuildPath("servicelib")
            CompileBuildPath(buildPath)
            needCompSubDir.remove("servicelib")
            
    #如果pcrf和unintest同时需要编译，则先编译pcrf 后编译 unittest
    if  ("pcrf" in needCompSubDir) and ("unittest" in needCompSubDir):
            buildPath = GetBuildPath("pcrf")
            CompileBuildPath(buildPath)
            
            buildPath = GetBuildPath("unittest")
            CompileBuildPath(buildPath)
            
            needCompSubDir.remove("pcrf")
            needCompSubDir.remove("unittest")
            
    for key in needCompSubDir:
        if key in compileSubDir:
            logging.debug("Key:[%s] is a subdir" % key)
            buildPath = GetBuildPath(key)
            CompileBuildPath(buildPath)
        elif (key == "perl" ) or (key == "release" ) or (key == "qmdb" ):
            logging.info("Key:[%s] is a Flag Key Word" % key)
        else:
            logging.warn("Cann't find key : %s" % key)
            pass
        
    
def CompileAll():
    CompileDir = GetPCRFServerSubdir();
    needCompSubDir = GetParma(CompileDir)
    CompileSubDir( needCompSubDir);



if __name__=='__main__':
    CompileAll()





