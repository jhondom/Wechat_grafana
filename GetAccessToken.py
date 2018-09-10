
#coding=utf-8
import urllib2
import json
import ConfigParser
import WriteFile

#class getAccessTokenFromWechat():
def GetAccessTokenFromWechat():
    CorpID="ww02946fb9034b5649"
    CorpSecret="X56RLPUFZYyoaEBCNaZecSkWN-s3_ZRdKMYlK2KJuCA"
    AgentId=1000003
    conn = urllib2.urlopen("https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=" + CorpID + "&corpsecret=" + CorpSecret )
    getToken = conn.read()
    print getToken
    conn.close()
    result = json.loads(getToken)
    try:
        Accesstoken = result['access_token']
        message = '[token]\nAccessToken=' + Accesstoken + '\n'
        WriteFile.WriteFile('AccessToken.ini', message, 'w')
            
    except:
        Accesstoken = False
        message = 'getAccessTokenFromWechat Error'
        WriteFile.WriteLog('WeChatServer','Error',message,'w')


def GetAccessTokenFromLocal():
    cf = ConfigParser.ConfigParser()
    cf.read('./AccessToken.ini')
    LocalAccessToken = cf.get("token", "AccessToken")
    #cf.close
    return LocalAccessToken

GetAccessTokenFromWechat() #如果发现返回code：301002，40014 等token过期问题，取消该行注释，执行python GetAccessToken.py重新获取token
#print GetAccessTokenFromLocal()   
