import json
import urllib3
import uuid
import hmac
import hashlib

class MoMo():
    endpoint = "https://test-payment.momo.vn/gw_payment/transactionProcessor"
    partnerCode = "MOMOBDAF20201207"
    accessKey = "ccldtqqNipAr0PdL"
    serectkey = "6VzFAPfP9eGsw47dEPx6FiYqGWete93n"

    orderInfo = "Pay for flight with MoMo"
    returnUrl = "http://0.0.0.0:5000/status_payment"
    notifyUrl = "http://0.0.0.0:5000/notifyUrl-momo"
    amount = "50000" 
    orderId = str(uuid.uuid4())
    requestId = str(uuid.uuid4())
    requestType = "captureMoMoWallet"
    extraData = "name=a;age=12"


    def __init__(self, amount):
        self.amount = amount

    def set_orderId(self, id):
        self.orderId = id

    def set_extraData(self, *args):
        if len(args) > 0:
            extraData=''
            for i in args: 
                extraData += i+'='+i+';'
            self.extraData=extraData[:-1]

    
    def make_signature(self):
        rawSignature = "partnerCode=" + self.partnerCode + "&accessKey=" + self.accessKey + "&requestId=" + self.requestId + "&amount=" + self.amount + "&orderId=" + self.orderId + "&orderInfo=" + self.orderInfo + "&returnUrl=" + self.returnUrl + "&notifyUrl=" + self.notifyUrl + "&extraData=" + self.extraData
        h = hmac.new(bytes(self.serectkey, 'utf-8'), rawSignature.encode('utf-8'), hashlib.sha256)
        return h.hexdigest()


    def body_config(self):
        return {
            "accessKey": self.accessKey,
            "partnerCode": self.partnerCode,
            "requestType": self.requestType,
            "notifyUrl": self.notifyUrl,
            "returnUrl": self.returnUrl,
            "orderId": self.orderId,
            "amount": self.amount,
            "orderInfo": self.orderInfo,
            "requestId": self.requestId,
            "extraData": self.extraData,
            "signature": self.make_signature()
        }

    def send_momo(self):
        body = json.dumps(self.body_config())
        http = urllib3.PoolManager()

        clen = len(body)
        req = http.request(method='POST', url=self.endpoint, body=body,
                           headers={'Content-Type': 'application/json; charset=UTF-8', 'Content-Length': clen})
        if req.status ==200:
            res = json.loads(req.data.decode('utf-8'))
            return res['payUrl']
        else:
            return ""