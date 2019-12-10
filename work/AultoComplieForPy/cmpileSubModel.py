# coding=gbk
import os

GoOnFlag=True

curPath=os.path.abspath('.')
print("current path is: %s" % curPath )

splitresut=os.path.split(curPath)
print("Path info is %s--%s" % (splitresut[0],splitresut[1]))


parentPath=splitresut[0]
if os.path.split(parentPath)[1]!="PCRFServer" :
    print("exit")
    os._exit()

subDir= [x for x in os.listdir('.') if os.path.isdir(x)]

buildPathName="build"
buildPath = os.path.join(curPath,buildPathName)
print("build path is  %s" % buildPath)
    
#build 目录不存在，则创建
if buildPathName  not in subDir :
    os.mkdir(buildPath)

os.chdir(buildPath)
curPath=os.path.abspath('.')
print("current path is: %s" % curPath)

curCmd=""
cmakeCmd="cmake -DCMAKE_INSTALL_PREFIX=$HOME -DCMAKE_BUILD_TYPE=Debug -DCMAKE_C_COMPILER=`which gcc` -DCMAKE_CXX_COMPILER=`which c++` .."
print("cmake cmd is %s " % cmakeCmd)

curCmd=cmakeCmd
cmdRS=os.system(curCmd)
if  cmdRS != 0 :
    print("cmd :%s faild，and result code:%d " % (curCmd, cmdRS) )
    os._exit()

    
makecleanCmd="make clean"    
curCmd=makecleanCmd
cmdRS=os.system(curCmd)
if  cmdRS != 0 :
    print("cmd :%s faild，and result code:%d " % (curCmd, cmdRS) )
    os._exit()
#清除 编译生成的文件
    
makeinstallCmd="make -j 4 install "   


curCmd=makeinstallCmd
cmdRS=os.system(curCmd)
if  cmdRS != 0 :
    print("cmd :%s faild，and result code:%d " % (curCmd, cmdRS) )
    os._exit()    
else:
    print("cmd :%s ok " % curCmd )
    print("Congratulation !!"  )
