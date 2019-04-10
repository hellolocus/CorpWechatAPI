#!/usr/bin/env python
import logging
import allure
from src.api.contact.department.depmanagment import DeptManagment
class TestDeleteDept:
    @allure.story('删除部门')
    def test_delete_dept(self):
        dept_managment = DeptManagment()
        dept_managment.delete_dept()
        result = dept_managment.get_delete_response()
        assert "deleted" == result.get("errmsg")
        logging.info('测试完成')
