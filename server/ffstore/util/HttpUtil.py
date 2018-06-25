# -*- coding:utf-8 -*-

import sys
sys.path.append('../')

try:
    from cStringIO import StringIO
except ImportError:
    from StringIO import StringIO
import gzip, json, urllib, urllib2, collections, time, logging
from ErrorInfo import OpenError
from constant import ResponseCode
from LogUtil import LogUtil

def http_get(url, params={}, header={}):
    logging = LogUtil().getLogging()
    httpUrl = url
    # logging.info('-----------------------')
    # logging.info(httpUrl)
    # logging.info('-----------------------')
    if params is not None and len(params) > 0:
        httpUrl = url + "?" + _encode_params(**params)
    httpUrl = httpUrl.replace(': ', ':')
    httpUrl = httpUrl.replace(', ', ',')
    httpUrl = httpUrl.replace("'", '"')
    logging.info('-----> httpUrl: ' + httpUrl)
    # print httpUrl
    req = urllib2.Request(httpUrl, None, headers=header)
    res = urllib2.urlopen(req)
    body = _read_body(res)
    logging.info('-----> body: ' + body)
    # check_status(body)
    return body


def http_post(url, params={}, header={}):
    req = urllib2.Request(url)
    for k, v in header:
        req.add_header(k, v)
    res = urllib2.urlopen(req, data=params, header=header)
    body = _read_body(res)
    check_status(body)
    return body


def check_status(resJson, statusName="status", code="status_code", reason="status_reason"):
    logging = LogUtil().getLogging()
    if (resJson is None):
        logging.info('-------OpenError 1. ---')
        raise OpenError(ResponseCode.sys_error, ResponseCode.sys_error_desc, None)
    res_dic = json.loads(resJson)
    if res_dic.get(statusName) is None:
        logging.info('-------OpenError 2. ---')
        raise OpenError(ResponseCode.sys_error, ResponseCode.sys_error_desc, None)
    status_code = res_dic.get(statusName).get(code)
    status_reason = res_dic.get(statusName).get(reason)
    if 0 != status_code and "0" != status_code:
        logging.info('-------OpenError 3. ---')
        raise OpenError(status_code, status_reason, None)


def _encode_params(**kw):
    params = []
    # kw['lang'] = "python"
    # kw['sdkversion']=TokenConstant.version
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
    using_gzip = res.headers.get('Content-Encoding', '') == 'gzip'
    body = res.read()
    if using_gzip:
        gzipper = gzip.GzipFile(fileobj=StringIO(body))
        body = gzipper.read()
        gzipper.close()
    return body
