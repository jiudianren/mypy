import requests
import json


MyHttpheadStr ='http://'
IP='172.18.188.134'
Port=':2017'

TracelogDir='/pcrf/tracelog'
Number='15077889999'
NumberStr='/' +Number 


def DealGet():
    GetTracelogURL= MyHttpheadStr + IP + Port +TracelogDir
    print(GetTracelogURL)
    RS=requests.get(GetTracelogURL)  
    if RS.status_code == requests.codes.ok :
        print("GET OK!!",RS.text )
        
        getRes = json.loads(RS.text)
        if(getRes.get('tracelog') =='OFF'):
            print("tracelog off,and you can set track number now.")
            return True;
        else:
            if(getRes.get('accnbr') != Number):
                print("Get accr is ",getRes.get('accnbr'),' your accr is' ,Number)
                return True;
            else:
                print("you have already set the accr:", getRes.get('accnbr'))
                return False;
    else:
        print("Get Erro, pleast check!")
        exit(0)

def DealPost():
    PostTraceNumberURL= MyHttpheadStr + IP + Port +TracelogDir +NumberStr
    print(PostTraceNumberURL)
    
    RS=requests.post(PostTraceNumberURL)
    print( RS.status_code.__str__() )  
    if RS.status_code == requests.codes.ok :
        print("POST OK!!",RS.text )
    else:
        print("POST Erro, pleast check!")
        exit(0)
        
        

#curl -w'\n' -v -X DELETE 'http://10.45.80.189:2027/pcrf/tracelog/{08613382019887}'        
def DealDelete():
    DeleteTraceNumberURL=MyHttpheadStr + IP + Port +TracelogDir +NumberStr
    print(DeleteTraceNumberURL)
    RS=requests.delete(DeleteTraceNumberURL)  
    if RS.status_code == requests.codes.ok :
        print("Delete OK!!",RS.text )
    else:
        print("Delete Erro, pleast check!")
        exit(0)  
        


def POST():
    GetNoNumber= DealGet()
    if(GetNoNumber):
        print("going to deal post")
        DealPost()
    

def Delete():
    DealDelete()


while(1):
    
    opreat=int ( input("1:get 2,delete ,3 post,4 ,exit"))
    if  opreat == 1 :
        DealGet()
    elif opreat == 2 :
        DealDelete()
    elif  opreat == 3:
        DealPost()
    else:
        exit(0)


