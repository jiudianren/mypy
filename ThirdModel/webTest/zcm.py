import webbrowser


#webbrowser.open('https://www.baidu.com/')
#webbrowser.open('https://oa.ztesoft.com/index.flex')

def openTask(id):
    url='https://oa.ztesoft.com/queryTransDtl.action?transid='
    url+= id
    url+='&orgState=O&language=zh_CN'
    webbrowser.open(url)
    
print(0%2)

#openTask('1322487')
#openTask('1319895')
#openTask('1322188')
openTask('1296220')
