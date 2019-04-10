#!/usr/bin/env python
import logging
from src.initialization.sysconfig import sys_cfg
from src.api.baseapi import BaseAPI
class DeptManagment(BaseAPI):
    def __init__(self):
        BaseAPI.__init__(self)
        self.create_dept_url = sys_cfg.get('contact_para','create_dept_url')
        self.delete_dept_url = sys_cfg.get('contact_para','delete_dept_url')
        logging.info("Init department managment api")
    def create_dept(self):
        new_dept = {
            "name": "河北研发中心",
            "parentid": 3,
            "order": 1
            }
        logging.info(self.get_token())
        params = {'access_token':self.get_token()}
        self.extend_post_json(url=self.create_dept_url,json_obj=new_dept,params=params)

    def get_create_dept_response(self):
        return self.get_response()

    def delete_dept(self):
        params = {'access_token':self.get_token(),'id':7 }
        self.extend_get(self.delete_dept_url,params)

    def get_delete_response(self):
        return self.get_response()

