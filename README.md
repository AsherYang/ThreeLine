# 三行情书

## 总体概况

1. 创建时间：2017年3月18日
2. 项目结构：mvp + dagger2 + rxJava + realm
3. 一句话就可以插入数据, 数据库操作从未如此简单
4. 运行程序需要注意先要在gradle task中选择uploadArchives进行上传插件库文件，然后再sync build
才可运行，因为使用了自定义gradle插件
5. 项目结构说明：
```
ThreeLine
    --app
        --src
            --aop
            --api
            --db
                --bean
            --serve
                --data
                    --music
                    --article
                --net
                    --base
                    --bean
            --ui
                --main
                --login
            --util
    --server
        --tornado
        --crawler
        --im
    --wx
        --client
            
说明:
a. aop 包下放置切面编程相关处理
b. api 包下放置与服务器定义api,以及一些网络相关常量
c. db 包下放置数据库初始化,以及数据库实体bean，数据常量
d. serve 包下放置各个模块数据库操作以及网络操作，基础网络封装
e. ui 包下放置界面相关类，以module模块名划分，包含presenter|view 层
f. util 包下放置工具类相关
g. server 包下放置服务器端程序，使用Python编写
h. wx 包下放置微信小程序端程序
```

## TODO
- [x] 换肤 --- 20170430 Finished
- [x] 推送 --- 20170504 Finished
- [ ] 服务器数据库
- [ ] 数据爬虫
- [ ] 小程序端

## 交流
目前项目正在紧急开发中,高速发展。

欢迎交流意见。

QQ 群 ThreeLine <a target="_blank" href="//shang.qq.com/wpa/qunwpa?idkey=6c6e583b86c4b57c2e36c8a93366a4e38ab974f912a8ad1c1e154b205ea8d5f0"><img border="0" src="https://camo.githubusercontent.com/615c9901677f501582b6057efc9396b3ed27dc29/687474703a2f2f7075622e69647171696d672e636f6d2f7770612f696d616765732f67726f75702e706e67" alt="ThreeLine" title="ThreeLine"></a>

