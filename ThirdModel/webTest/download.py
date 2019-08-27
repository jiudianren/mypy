import requests,bs4

#pip install requests

res =requests.get("https://oa.ztesoft.com/index.flex")
if res.status_code == requests.codes.ok :
    print("ok")

htmlfile=open("baidu.html", 'wb')
for chunk in res.iter_content(100000):
    htmlfile.write(chunk)
    
    
    
mybsss = bs4.BeautifulSoup(res.text)


print("ok")
htmlfile.close()