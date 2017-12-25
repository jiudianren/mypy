# coding=gbk
import os
import sys
import time
import pdb
import logging

logging.basicConfig(level=logging.INFO)
#logging.basicConfig(level=logging.DEBUG)

'''
׼����
1�� ����  $PCRF_HOME ��������
2�� ����$IMPSYSDIR ��������
3�� Ŀ¼�ṹҪ��
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
                                
                                
4 ������  make -j ��ʹ�õĺ�����  "GMakejcout= xx" ���� xx ��Ϊ ��Ҫʹ�õĺ����� Ĭ��Ϊ 4��                    


ʹ��:
python cmpscript.py xx1 xx2 xx3 xx4 ....

1 ���� ִ��perl�� ��Ҫ���� pe(perl) ѡ��
2 �����ҪRelease ģʽ������Ҫ����r (Release) ѡ��
3 hub����Ĭ�ϱ��뷽ʽ DB + QMDB [default]  �����Ҫ����QMDBģʽ��qmdb only�� ����Ҫ  ����  q(qmdb)ѡ��
4 ��� ��techlib����servicelib�� �� ����ģ�� ͬʱ��Ҫ���룬���ȱ��루techlib����servicelib�� ,����� ����ģ��
5 ���pcrf�� unintestͬʱ��Ҫ���룬���ȱ���pcrf ,����� unittest
6 �������룺 
    techlib        ��Ҫ����һ���ַ� : t te techlib
    hub            ��Ҫ����һ���ַ� : h
    unittest        ��Ҫ����һ���ַ� : u
    release        ��Ҫ����һ���ַ� ��r
    qmdb          ��Ҫ����һ���ַ� ��q ��for hub qmdb only ģʽ��
    
    pcrf            ��Ҫ �������� : pc
    perl          ��Ҫ���������ַ� ��pe
    servicelib    ��Ҫ���������ַ� ��se
    spr            ��Ҫ���������ַ� ��sp

ʾ��   
1 ���� techlib ����
python cmpscript.py t 
����
python cmpscript.py  techlib
python cmpscript.py  techli
python cmpscript.py  techl
python cmpscript.py  tech
python cmpscript.py  tec
python cmpscript.py  te

2 ͬʱ������ģ�� 
python cmpscript.py te se pc (ͬʱ���� te se pc �� ģ��)
3 ��Ҫִ��perl �� ���� pcrf �� unittest
python cmpscript.py pe pc un
4  hub���֣���Ҫ�� qmdbonly��ʽ���룬������Ҫͬʱ����pcrfģ��
python cmpscript.py qmdb h pc
'''


logging.warn("**********" )
# ������������Ϊ�Լ�������
logging.warn("Confirm change these args" )
GMakejcout= 4
logging.warn("make -j ?? j=%d" % GMakejcout )

# ִ��make installʱ�򣬻��Ե���Ļ������  ͬʱ������ļ� ����
GMakeInstallResultFile="MIRSFILE"

#ֻ�۲�ű�ִ�еı���˳�򣬲�ִ�� cmake make������ Ĭ��false
ObserveCompileOrder = False
logging.warn(" just obser the compile order flag :%s" % ObserveCompileOrder )
logging.warn("**********" )


#ȫ�ֱ���
#Ĭ��debug ģʽ
GDebugModle=True
#Ĭ��hub����ʱ�� ���� DB+QMDBģʽ
HubQmdbOnlyFlag=False



## PCRFServer ���PCRFServer�Ƿ����
def GetPcrfServerPath():
    PCRF_HOME=os.popen("echo $PCRF_HOME").read().strip('\n')
    logging.debug(PCRF_HOME)
     
    PCRFServer="PCRFServer"
    PCRFServer_HOME = os.path.join(PCRF_HOME,PCRFServer)
    print("PCRFServer_HOME is %s" % PCRFServer_HOME)
    #����Ƿ����
    if not os.path.exists(PCRFServer_HOME):
        logging.warn("%s not exist�� Faild" % PCRFServer_HOME)
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
    #������Ŀ¼��˳��� perl ��һ����־ 
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
            #����ȫ��ת��ΪСд
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

#perl ִ�н�������Ҫһ��end  todo
def  DoPerlCmd():
    PServerHome = GetPcrfServerPath()
    unitTestKeyWord="unittest"
    unitTestDir=os.path.join(PServerHome,unitTestKeyWord)
    
    if not os.path.exists(unitTestDir):
        logging.warn("%s not exist�� Faild" % unitTestDir)
        os._exit()
    #��Ҫ�鿴���ļ��Ƿ���� todo
    
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
    
    # �Ƿ����build·������������� ���Դ���һ�Σ��������ʧ�� �����˳��ű�
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
        logging.warn("cmd faild��and result code:%d " % (cmdRS) )
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
        #releaseģʽ
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
            
    #���pcrf��unintestͬʱ��Ҫ���룬���ȱ���pcrf ����� unittest
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





