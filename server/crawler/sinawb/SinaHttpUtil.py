# -*- coding:utf-8 -*-
"""
Author: AsherYang
Email : ouyangfan1991@gmail.com
Date  : 2017/11/22
Desc  : Sina Http Util 参考 Shserver 微店 OpenRequest.py
"""

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import gzip, json,  urllib, urllib2, collections,time,logging

def http_get(url,params={},header={}):
    httpUrl=url
    if params is not None and len(params)>0:
        httpUrl=url+"?"+_encode_params(**params)
    httpUrl=httpUrl.replace(': ',':')
    httpUrl=httpUrl.replace(', ',',')
    httpUrl=httpUrl.replace("'",'"')
    print httpUrl
    req=urllib2.Request(httpUrl,None,headers=header)
    res=urllib2.urlopen(req)
    body=_read_body(res)
    # check_status(body)
    return body

def http_post(url,params={},header={}):
    req=urllib2.Request(url)
    for k,v in header:
        req.add_header(k,v)
    res=urllib2.urlopen(req,data=params,header=header)
    body=_read_body(res)
    # check_status(body)
    return body

# def check_status(resJson,statusName="status",code="status_code",reason="status_reason"):
#     if(resJson is None ):
#         raise OpenError("10001","系统错误,返回的结果为空",None)
#     res_dic=json.loads(resJson)
#     if(res_dic.get(statusName) is None):
#         raise OpenError("10001","系统错误,状态码为空",None)
#     status_code=res_dic.get(statusName).get(code)
#     status_reason=res_dic.get(statusName).get(reason)
#     if(0!=status_code and "0"!=status_code):
#         raise OpenError(status_code,status_reason,None)


def _encode_params(**kw):
    params = []
    for k, v in kw.iteritems():
        if isinstance(v, basestring):
            qv = v.encode('utf-8') if isinstance(v, unicode) else v
            params.append('%s=%s' % (k, urllib.quote(qv)))
        elif isinstance(v, collections.Iterable):
            for i in v:
                qv = i.encode('utf-8') if isinstance(i, unicode) else str(i)
                params.append('%s=%s' % (k, urllib.quote(qv)))
        else:
            qv = str(v)
            params.append('%s=%s' % (k, urllib.quote(qv)))
    return '&'.join(params)


def _read_body(res):
    using_gzip = res.headers.get('Content-Encoding', '')=='gzip'
    body = res.read()
    if using_gzip:
        gzipper = gzip.GzipFile(fileobj=StringIO(body))
        body = gzipper.read()
        gzipper.close()
    return body
