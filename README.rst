Python Client For Apache Dubbo
------------------------------
Python Dubbo Client
=====================================  
实现客户端的负载均衡、配合Zookeeper自动发现服务功能
-------------------------------------

Achieve load balancing on the client side、auto discovery service function with Zookeeper
-----------------------------------------------------------------------------------------

Python calls the Dubbo interface's jsonrpc protocol

### Python调用Dubbo接口的jsonrpc协议  
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Please use dubbo-rpc-jsonrpc and configure protocol in Dubbo for jsonrpc protocol
| *Reference* https://github.com/apache/incubator-dubbo-rpc-jsonrpc

请使用dubbo-rpc-jsonrpc 并在dubbo中配置protocol为jsonrpc协议
参考 https://github.com/apache/incubator-dubbo-rpc-jsonrpc

Installation
~~~~~~~~~~~~

https://github.com/nickfan/dubbo-python3

pip install dubbo-python3
or

pip install git+https://github.com/nickfan/dubbo-python3.git@1.0.1

| Download code
| python setup.py install
| pip install
| pip install dubbo-python3>=1.0.3 Git install
| pip install git+https://github.com/nickfan/dubbo-python3.git@1.0.3

### 安装
下载代码   
python setup.py install  
pip安装  
pip install dubbo-client==1.0.0b5  
Git安装   
pip install git+http://git.dev.qianmi.com/tda/dubbo-client-py.git@1.0.0b5   
或者   
pip install git+https://github.com/qianmiopen/dubbo-client-py.git@1.0.0b5

Load balancing on the client side, service discovery
### 在客户端实现负载均衡，服务发现 
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

| Get the registration information of the service through the zookeeper of the registry.
| Dubbo-client-py supports configuring multiple zookeeper service addresses.
| "host":"192.168.1.183:2181,192.168.1.184:2181,192.168.1.185:2181"
| Then the load balancing algorithm is implemented by proxy, and the
| server is called.
| Support Version and Group settings.

### 在客户端实现负载均衡，服务发现  
通过注册中心的zookeeper，获取服务的注册信息   
dubbo-client-py支持配置多个zookeeper服务地址   
"host": "192.168.1.183:2181,192.168.1.184:2181,192.168.1.185:2181"   
然后通过代理实现负载均衡算法，调用服务端  
支持Version、Group设置  

### Example
```python 
    config = ApplicationConfig('test_rpclib')
    service_interface = 'com.ofpay.demo.api.UserProvider'
    #Contains a connection to zookeeper, which needs caching.
    registry = ZookeeperRegistry('192.168.59.103:2181', config)
    user_provider = DubboClient(service_interface, registry, version='1.0')
    for i in range(1000):
    try:
        print( user_provider.getUser('A003'))
        print( user_provider.queryUser(
            {u'age': 18, u'time': 1428463514153, u'sex': u'MAN', u'id': u'A003', u'name': u'zhangsan'}))
        print( user_provider.queryAll())
        print( user_provider.isLimit('MAN', 'Joe'))
        print( user_provider('getUser', 'A005'))

    except DubboClientError as client_error:
        print (client_error)
    time.sleep(5)
```
TODO


| Optimize performance, minimize the impact of service upper and lower lines.
| Support Retry parameters
| Support weight call
| Unit test coverage
优化性能，将服务上下线的影响降到最小  
支持Retry参数    
支持权重调用    
单元测试覆盖率

### Licenses Apache License ### Thanks Thank @jingpeicomp for being a
Guinea pig. It has been running normally for several months in the
production environment. Thank you!
