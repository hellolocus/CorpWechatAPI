import logging
import pytest
if __name__ == '__main__':
    pytest.main(['-sq','--alluredir','../report','testcases\contact\department\test_create_dept.py'])
    logging.basicConfig()