import re
from xml.dom.minidom import parse
import xml.dom.minidom
import os

ColumInfo = {};
TabAtri = {};
TabList = [];

TabAtris = ["table-space-id", "record-counts", "expand-record",
            "Is-Zip-Time", "LoadType", "filter-sql", "load-sql", "flush-sql"]

ColumAtris = ["name", "column-pos", "data-type", "data-len", "rep-type",
              "Is-Default", "Default-Value"]

TbName = ""

def Find(str, value):
    if (str.find(value) != -1):
        return True
    else:
        return False
    


def SpliceSql(Sql):
    Sql = Sql +  " "  + ColumInfo["name"] + " " + ColumInfo["data-type"] \
                      + '(' + ColumInfo["data-len"] + ')' + " ";
    if "Y" == ColumInfo["Is-Default"]:
        if ColumInfo["data-type"] == "CHAR":
            Sql = Sql + "default " + '\'' + ColumInfo["Default-Value"] + '\''
    Sql = Sql + '\n';
    return Sql


def transStructXml2(filename):
    Sql = "CREATE TABLE "
    
    DOMTree = xml.dom.minidom.parse(filename)
    collection = DOMTree.documentElement
    TabName = collection.getElementsByTagName("name")
    if(TabName[0].hasAttribute("value")):
        Sql += TabName[0].getAttribute("value")
        Sql = Sql + "\n" + "(" + "\n"
        TbName = TabName[0].getAttribute("value")
    else:
        print("ERROR XML NO Table Name")
        
    Colums = collection.getElementsByTagName("column")
    for colum in Colums:
        for atri in ColumAtris:
            if (colum.hasAttribute(atri)):
                #print (atri, movie.getAttribute(atri))
                ColumInfo[atri] = colum.getAttribute(atri)
        Sql = SpliceSql(Sql)

    TabAtri.clear()
    for atri in TabAtris:
        CAtri = collection.getElementsByTagName(atri)
        for catri in CAtri:
            if (catri.hasAttribute("value")):
                TabAtri[atri] = catri.getAttribute("value")
                print(TabAtri)
    
    Sql = Sql + ')';
    #print(Sql);
    return (Sql, TbName)
    
            
def transPropertyXml2(file):
    
    DOMTree = xml.dom.minidom.parse(file)
    collection = DOMTree.documentElement
    for atri in TabAtris:
        CAtri = collection.getElementsByTagName(atri)
        for catri in CAtri:
            if (catri.hasAttribute("value")):
                TabAtri[atri] = catri.getAttribute("value")
                print(TabAtri)    
        

FileList = [];

def getFiles(path):
    proList = []
    stcList = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if (Find(file, "ProPerty")):
                proList.append(file)
            elif (Find(file, "Struct")):
                stcList.append(file)
    print(proList)
    print(stcList)
    for profl in proList:
        for stcfl in stcList:
            if Find(profl, stcfl[stcfl.find("Struct")+6:]):
                FileList.append((profl, stcfl))
    #print(FileList)
    return FileList

getFiles("./")

def TransXml2Sql(path):
    FileTpList = getFiles(path)
    for fltp in FileList:
        (Sql, tbName) = transStructXml2(fltp[1])
        transPropertyXml2(fltp[0])
        
        strAtri = '';
        for atri in TabAtris:
            if len(TabAtri[atri]) > 0:
                strAtri = strAtri + atri + "=" + "[" +  TabAtri[atri] +"]" + ","
        
        strAtri = strAtri.strip(",")

        while strAtri.find('-') != -1:
            aryStr = list(strAtri)
            aryStr[strAtri.find('-')] = "_"
            strAtri = ''.join(aryStr)
        
        strAtri += ";"

        strAtri.replace('table_space_id', 'table_space'); #not work , why?

        Sql += strAtri
        #print(Sql)
        sqlFlile = tbName + "_SQL";
        #print(sqlFlile)
        fh = open(sqlFlile, 'w')
        fh.write(Sql)
        fh.close

TransXml2Sql("./")


