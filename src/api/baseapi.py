from src.initialization.sysconfig import sys_cfg
import  logging
import requests
class BaseAPI:
    def __init__(self):
        logging.info("init base api interface")
        self.copid = sys_cfg.get('corp_para','corp_id')
        self.url = sys_cfg.get('corp_para','token_url')
        self.secret = sys_cfg.get('contact_para','secret')
        self.res = ''
    def get_token(self):
        params = {'corpid':self.copid,'corpsecret':self.secret}
        res = requests.get(self.url,params=params)
        return res.json().get('access_token')
    def extend_post_json(self,url,json_obj,params=None):

        headers = {
            'Content-Type': 'application/json; charset=UTF-8'
          }
        if params:
            self.res = requests.post(url,json=json_obj,params=params,headers=headers,verify=False)
        else:
            self.res = requests.post(url,json=json_obj,headers=headers,verify=False)

    def get_response(self):
        return self.res.json()

    def extend_get(self,url,params=None):
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8'
          }
        self.res = requests.get(url=url,params=params,headers=headers)

