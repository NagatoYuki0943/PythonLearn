import hashlib
import json
import random
import time
import requests


class SmsSendAPIDemo(object):
    """
    易盾短信发送接口示例代码
    https://support.dun.163.com/documents/2018101001?docId=436710603760996352
    """

    API_URL = "https://sms.dun.163.com/v2/sendsms"
    VERSION = "v2"

    def __init__(self, secret_id, secret_key, business_id):
        """
        Args:
            secret_id (str) 产品密钥ID，产品标识
            secret_key (str) 产品私有密钥，服务端生成签名信息使用
            business_id (str) 业务ID，易盾根据产品业务特点分配
        """
        self.secret_id = secret_id
        self.secret_key = secret_key
        self.business_id = business_id

    def gen_signature(self, params=None):
        """生成签名信息
        Args:
            params (object) 请求参数
        Returns:
            参数签名md5值
        """
        buff = ""
        for k in sorted(params.keys()):
            buff += str(k) + str(params[k])
        buff += self.secret_key
        return hashlib.md5(buff.encode("utf-8")).hexdigest()

    def send(self, params):
        """请求易盾接口
        Args:
            params (object) 请求参数
        Returns:
            请求结果，json格式
        """
        params["secretId"] = self.secret_id
        params["businessId"] = self.business_id
        params["version"] = self.VERSION
        params["timestamp"] = int(time.time() * 1000)  # 时间戳
        params["nonce"] = int(random.random() * 100000000)
        params["signature"] = self.gen_signature(params)  # 签名

        try:
            # 参数: url data
            response = requests.post(self.API_URL, data=params)
            return response.json()
        except Exception as ex:
            print("调用API接口失败:", str(ex))


if __name__ == "__main__":
    """示例代码入口"""
    SECRET_ID = "ef8a1e23fc76790c80c97bf6134a75a2"  # 产品密钥ID，产品标识
    SECRET_KEY = "f951ca65d2437d4432a8e0a4c9183e91"  # 产品私有密钥，服务端生成签名信息使用，请严格保管，避免泄露
    BUSINESS_ID = "98d06d9b06ba49d68f38cbb5c453299f"  # 业务ID，易盾根据产品业务特点分配
    api = SmsSendAPIDemo(SECRET_ID, SECRET_KEY, BUSINESS_ID)

    params = {
        "mobile": "1881111960",
        "templateId": "10084",
        "paramType": "json",
        "params": "json格式字符串.要自己替换掉 ",
        # 国际短信对应的国际编码(非国际短信接入请注释掉该行代码)
        # "internationalCode": "对应的国家编码"
    }
    res = api.send(params)
    print(res)
    print("*" * 50)
    if res is not None:
        if res["code"] == 200:
            taskId = res["result"]["taskId"]
            print("taskId = %s" % taskId)
        else:
            print("ERROR: ret.code=%s,msg=%s" % (res["code"], res["msg"]))
