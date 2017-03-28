# 三行情书

## 总体概况

1. 创建时间：2017年3月18日
2. 项目结构：mvp + dagger2 + rxJava + realm
3. 1句话就可以插入数据, 数据库操作从未如此简单
```
ThreeLine
    -- app
        --src
            --net
            --db
                --bean
            --serve
            --ui
                --main
                --login
            --util
            
说明: 
a. net 包下放置api
b. db 包下放置数据库初始化、以及数据库实体bean
c. serve包下放置数据库操作以及网络操作
d. ui 包下放置界面相关类，以module模块名划分，包含presenter|view 层
e. util 包下放置工具类相关
```