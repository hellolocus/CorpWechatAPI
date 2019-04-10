#!/usr/bin/env python
import logging
import allure
from src.api.contact.department.depmanagment import DeptManagment
class TestCreateDept:
    @allure.story('创建部门')
    def test_create_new_dept(self):
        dept_managment = DeptManagment()
        dept_managment.create_dept()
        result = dept_managment.get_create_dept_response()
        assert "created" == result.get("errmsg")
        logging.info('测试完成')
