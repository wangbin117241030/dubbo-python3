# -*- coding: utf-8 -*-
"""
https://github.com/wangbin117241030/dubbo-python3-jsonrpc
"""

import time

from dubbo_client import ApplicationConfig
from dubbo_client import DubboClient, DubboClientError
from dubbo_client import ZookeeperRegistry
import pandas as pd

def test_config_init():

    config = ApplicationConfig('test_rpclib') 
    service_interface = 'com.gjzq.gdsy.api.ysp.DeptConfigDictService' 
    #Contains a connection to zookeeper, which needs caching. 
    registry = ZookeeperRegistry('127.0.0.1:2181', config) 
    user_provider = DubboClient(service_interface, registry, version='1.0.0') 
    for i in range(1000): 
        try: 
            result = user_provider.queryPage({u'age': 18, u'time': 1428463514153, u'sex': u'MAN', u'id': u'A003', u'name': u'zhangsan'})
            print(type(result))
            print(result['list'])
            print(type(result['list']))
            new = pd.DataFrame(result['list'])
            print(new)

        except DubboClientError as client_error: 
            print(client_error) 

        time.sleep(5)


if __name__ == '__main__':
    test_config_init()