import json
import urllib3
import uuid
import hmac
import hashlib


endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
partnerCode = "MOMOBDAF20201207"
accessKey = "ccldtqqNipAr0PdL"
serectkey = "6VzFAPfP9eGsw47dEPx6FiYqGWete93n"
orderInfo = "pay with MoMo"
returnUrl = "https://momo.vn/return"
notifyurl = "localhost:5000/status_payment"
amount = "50000"
orderId = str(uuid.uuid4())
requestId = str(uuid.uuid4())
requestType = "captureMoMoWallet"
extraData = "name=a;age=12"
signature = ''


rawSignature = "partnerCode="+partnerCode+"&accessKey="+accessKey+"&requestId="+requestId+"&amount="+amount+"&orderId="+orderId+"&orderInfo="+orderInfo+"&returnUrl="+returnUrl+"&notifyUrl="+notifyurl+"&extraData="+extraData


#puts raw signature
print ("--------------------RAW SIGNATURE----------------")
print (rawSignature)
#signature
h = hmac.new( bytes(serectkey, 'utf-8'), rawSignature.encode('utf-8'), hashlib.sha256 )
signature = h.hexdigest()
print ("--------------------SIGNATURE----------------")
print (signature)

#json object send to MoMo endpoint

data = {
        'partnerCode' : partnerCode,
      	'accessKey' : accessKey,
      	'requestId' : requestId,
      	'amount' : amount,
      	'orderId' : orderId,
      	'orderInfo' : orderInfo,
      	'returnUrl' : returnUrl,
      	'notifyUrl' : notifyurl,
      	'extraData' : extraData,
      	'requestType' : requestType,
      	'signature' : signature
}
print ("--------------------JSON REQUEST----------------\n")
data = json.dumps(data)
print (data)


http = urllib3.PoolManager()

clen = len(data)
req = http.request(method='POST',url=endpoint, body=data, headers = {'Content-Type': 'application/json; charset=UTF-8', 'Content-Length': clen})
# f = urllib3.urlopen(req)
#
# response = f.read()
# f.close()
# print ("--------------------JSON response----------------\n")
# print (response+"\n")
#
# print ("payUrl\n")
# print (json.loads(response)['payUrl']+"\n")

print( json.loads(req.data.decode('utf-8')) )




