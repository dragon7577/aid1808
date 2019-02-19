项目流程
了解项目
了解项目流程
了解项目功能
判断可行性
通过UI设计图分析功能
确定大体实现方案
设计表


二手车交易系统
项目简介
进入21世纪以来，随着国家经济的飞速发展，国民生活水平的不断提高，人们对于生活质量有了更高的需求，汽车对于一个家庭来说可以提供更多的生活上的便利，提高生活水平，满足日常家庭出行需求，公司办公需要等，所以中国汽车保有量逐年呈增长趋势，销量有大幅增长。随着汽车数量的不断增长，随之而来的是汽车相关产业井喷式的发展，汽车配件、维修、二手车交易等相关产业觉醒，带来了庞大的需求团体，基于此庞大的需求市场，本系统将依托于互联网技术搭建一个O2O（online to offline）模式的二手车交易平台系统，替代原有传统的二手车交易市场。将原有纯线下交易过程革新为线上线下相结合，以满足二手车进行线上公开透明交易，线下进行实体车交易，使得二手车交易变得更加快捷、方便、安全、公正。

项目流程
用户可进行线上对代卖二手车进行浏览(页面展示)，查看代卖二手车详情(详情页展示)，包括汽车相关信息(汽车图片,描述)等。卖车用户可进行在线注册个人信息(卖家角色,提交表单)以及填写所卖车辆信息(车辆信息.上传汽车图片)，申请卖车用户需等待平台进行信息审核(平台用户)，待审核验证成功(状态)，发布卖车信息。对于有购买意向的买家(买家用户)，买家用户可在平台看到相关卖车信息(查看信息)，如需购买(购买功能),可进行在线注册(提交表单),登记相关个人信息(提交表单),绑定银行卡(银行卡),并进行认证.可以对有意向的汽车进行出价(出价模块),双方达成买卖协议(PDF,打印),线下交付(订单状态).

分析可能出现功能点
首页展示(汽车表)
列表页展示(汽车表)
详情页展示(汽车表)
买家卖家角色区分?(用户表)
卖家注册(用户表)
验证码X
邮箱验证,手机号验证X
完善汽车信息(汽车表)
上传图片*(汽车表)
更改汽车审核状态(汽车表)
买家注册(用户表)
购买出价功能?(出价表)
银行卡绑定X(银行卡表)
撮合功能X
订单功能(订单表)
登录(用户表)
生成PDFX
打印X
消息功能?(消息表)
卖车列表(汽车表)
个人信息展示(用户表)
个人信息修改(用户表)
服务保障
在线咨询X
轮播图(轮播图表)
汽车分类(汽车分类表)
最近浏览?(最近浏览表)


新车价格数据来源(爬虫)

卖家流程
用户注册 >> 登录 >> 完善个人信息 >> 完善卖车信息 >> 等待审核 >> 发布卖车信息 >> 确认买家 >> 生成订单

买家流程
用户注册 >> 登录 >> 完善个人信息 >> 浏览首页 >> 浏览列表页 >> 浏览详情页 >> 出价 >> 等待撮合 >> 生成订单

平台
审核发布信息, 审核订单

设计表
用户表 Userinfo
    用户名 username (C)
    密码 password (C)
    真实姓名 realname (C)
    身份证号 identity (C)
    住址 ads (T)
    手机号 uphone (C)
    性别 sex (Ic)
    角色 : 卖家/买家 role (Ic)
    激活状态 : 是否激活 isActive (B)
    是否禁用 : isBan (B)

品牌表 Brandinfo
    名称 title(C)
    logo logo(IM)
    新车价格 newprice(DE)
    是否删除 isdelete(B)
    

汽车表 Carinfo
    品牌 brand (F)
    上牌日期 regist_data(DATA)
    发动机号码 engineNo(C)
    公里数 mileage(I)
    维护记录 record(C)
    期望成功价格 price(D)
    图片 picture(IM)
    手续是否齐全 formalities(B)
    是否有债务 debt(B)
    卖家承诺 promise(TEXT)
    审核状态 status(B)
    用户user(F)
    是否删除isDelete

出价表 Cartinfo
    价格 price(D)
    买家 buser()
    汽车 car()    

银行卡表 Bankinfo
    卡号cardNo(C)
    用户user(F)
    交易密码cpwd(C)
    开户银行bank(Ic)
    是否删除isDelete(B)

订单表 Orderinfo
    用户买家buser(F userinfo)
    用户卖家suser(F userinfo)
    汽车car(TEXT)
    价格price(D)
    订单号orderNo(C)
    订单状态status(Ic)
    时间datetime(DT)
    是否删除isDelete(B)
*************************************
json:[{'name','wangwc','age',37},
            {'name','wangsouzhang','age',26}]
*************************************
    1. 保存json格式 或 : 创建一张附属表,记录商品,购买一件就记一个记录,字段和汽车表一样,永远不删除
**************************************
消息表 Message
    消息message(c)
    用户user(F)
    时间datetime(DT)
    是否阅读isRead(B) 
轮播图表 banners
    title(C)
    picture(IM)
    url(URL)
    isDelete(B)
******************************
表 或 cookie 或 session
密码 : cookie和session都不存,但浏览器记住密码的时候,会存储在浏览器的cookie中,不是访问URL的cookie上
cookie : 存储在浏览器,存储的对于你来说都是不重要的东西
session : 存储在服务器上的东西
    如果用户没有登录的情况下,添加的商品是存储在什么地方的?
    存储在cookie上
******************************

开发
新建文件夹

新建django项目
django-admin startproject xxxx

新建app
python3 manage.py startapp xxxx
***********************************
为了管理项目,合作性开发,创建多个app
1. 按照功能流程分类app
比如购物项目: 用户模块,购物车模块,订单模块,支付模块,前台显示模块
2. 按照角色流程分类app
比如二手车: 买模块,卖模块,用户模块,前台显示模块,
***********************************
sudo /etc/init.d/mysql start 启动mysql服务
写django项目的流程
    1. html,为了让html显示出来
    2. views,定义views方法,逻辑处理完整
    3. urls,指向views中的方法
    4. 处理好最后的html
    5. 点击完成


***********************************
基于django自带user表扩展
引用
from django.contrib,auth.models import AbstractUser

继承表
class UserInfo(AbstractUser):

添加指定表settings.py
AUTH_USER_MODLE = 'userinfo.UserInfo'

注册表 admin.py
from .models import *
admin.site.register(UserInfo)
admin.site.register(Bank)
***********************************

创建超级用户
python3 manage.py createsuperuser

执行创建表
python3 manage.py makemigrations
python3 manage.py migrate

**************************************
1. '\ex7'错误: 编码格式,出现中文
# -*- coding: UTF-8 -*-
**************************************


购物车,如果是未注册,添加物品则放入cookie中
购物车,如果是注册,添加物品到数据库中

**************************************
1. display:block/none/inline...
    display有32中用法
**************************************


***************************************
filter查询不需要添加try保护,查不到返回空
Carinfo.objects.get(id=car_id)需要添加try保护
因为一旦查不到,则会报错
***************************************

