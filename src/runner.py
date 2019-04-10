import logging
import pytest
if __name__ == '__main__':
    pytest.main(['-sq','--alluredir','../report',''])
    logging.basicConfig()