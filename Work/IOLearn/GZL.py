# coding=gbk
import os


 

path="E:\\myPy\\IOLearn\\"
ifile="ss1.csv"
#ifile="aa.csv"
ofile="sheet1new.csv"

offile=path+ofile
if os.path.exists( offile ):
    os.remove(offile)

def dealfile(ifname, ofname):
    ff1=open( ifname,'r')
    sD={}
    sT={}
    sDirt= {"DATE":sD,"TIME":sT}
    sline=ff1.readline()
    while sline:
        srst = sline.split(",")
        if srst[0] =="部门":
            sline=ff1.readline()  
            continue
        else:
            skey=(srst[0]+","+srst[1])
            if  srst[3] == '\n':
                srst[3] =" "
            else:
                srst[3]=srst[3].strip('\n')
                
            print(srst[3])  
            print(srst)  
            sDate=srst[2]
            sTime=srst[3]
                
            if  skey in sD :
                stemp = sD[skey] 
                stemp += ","
                stemp += sDate
                sD[skey]= stemp
                #print( sDirt[skey] )
            else:
                sD[skey] =sDate
                
            if  skey in sT :
                stemp = sT[skey] 
                stemp += ","
                stemp += sTime
                sT[skey]= stemp
                #print( sDirt[skey] )
            else:
                sT[skey] =sTime
                
        sline=ff1.readline()  
             
    ff1.close()
                
    ff2=open( ofname,'a')
    
    for k in sD.keys():
        ff2.write( "," +","+sD[k] +"\n" )
        ff2.write(k +","+sT[k] +"\n" )
        
    ff2.close()
    
dealfile( path+ifile,  path+ofile)

