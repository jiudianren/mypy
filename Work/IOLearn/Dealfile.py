# coding=gbk

import os





def findstr(str, sstr,estr):
    start=str.find(sstr)
    if start >0 :
        start=start+len(sstr)
        end=str.find(estr,start)
        if end >0:
            return str[(start) :end]
    


teststring="Sp|2018-06-28 13:51:36|Session=c11-10-13-11-50-epgrab1.gprs.meditelecom.com;1529205715;51570570|SubsData=212621062013|Begin=20180628104134|Update=20180628093553"
print(findstr(teststring,"SubsData=","|"))
testfile="C:\\Users\\Administrator\\Desktop\\s2\\aa.txt"
fl=open(testfile,'r')
print(fl.readline())


path="C:\\Users\\Administrator\\Desktop\\s2\\"
file1="pcrf\\SessionInfo_11678_20180628052002_0_Abn"
file2="pcrf\\SessionInfo_16345_20180628052002_0_Abn"

file3="phub\\GxSubsSession_20180628042859_0"
file4="phub\\GxSubsSession_20180628043120_0"
startstr1="SubsData="
startstr2="SubData="

endstr="|"

offile=path+"aa1.txt"
if os.path.exists( offile ):
    os.remove(offile)


def dealfile(ifname, ofname ,sstart):
    ff1=open( ifname,'r')
    off1=open( ofname,'a')
    sline=ff1.readline()
    while sline:
        off1.write( findstr( sline, sstart , endstr)  +",\n" )
        sline=ff1.readline()
    ff1.close()
    off1.close()
    
    
    
    
dealfile( path+file1,offile, startstr1 )
dealfile( path+file2,offile, startstr1 )
dealfile( path+file3,offile, startstr2 )
dealfile( path+file4,offile, startstr2)





