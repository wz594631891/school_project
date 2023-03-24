from django.db import models
#速卖通待发货
class Wait_ship_aliexpress_order(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    oid = models.TextField(verbose_name="单号")
    status = models.TextField(verbose_name="订单状态")
    buyer = models.TextField(verbose_name="买家名称")
    pay_time = models.DateTimeField(default='2023-01-01 00:00:00',verbose_name="付款时间")
    product_amount = models.TextField(verbose_name="产品总金额")
    shipping_fee = models.TextField(verbose_name="快递费")
    order_amount = models.TextField(verbose_name="订单金额")
    goods_title = models.TextField(verbose_name="商品信息")
    model = models.TextField(verbose_name="商品编码")
    tips = models.TextField(verbose_name="订单备注")
    address = models.TextField(verbose_name="收货地址")
    receiver = models.TextField(verbose_name="收件人名称")
    country = models.TextField(verbose_name="国家")
    express = models.TextField(verbose_name="物流")
    ship_limit = models.DateTimeField(verbose_name="发货期限")
    ship_time = models.DateTimeField(verbose_name="发货时间")
    time=models.DateTimeField(auto_now=True)#更新时间
    #区号 电话
    area_code = models.TextField(verbose_name="区号")
    tel = models.TextField(verbose_name="电话")
    #邮编
    zip_code =models.TextField(verbose_name="邮编")
    my_tip = models.TextField(verbose_name="内部备注")
    #创建时间(只在记录创建时变动,然后不可修改)
    create_time=models.DateTimeField(auto_now_add=True)
class Student(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    name = models.CharField(max_length=32,verbose_name="名字")
    # age int;
    age = models.IntegerField(verbose_name="年龄")
    # pwd int;
    pwd = models.IntegerField("密码",null=True)
	#性别
    gender=models.CharField(max_length=10,verbose_name="性别")
	#年级
    grade = models.IntegerField(default=0)
	#
    is_delete = models.IntegerField(default=0)

class Username(models.Model):
	"""website项目	用户表"""
	#建立字段
	username=models.CharField(verbose_name='用户名' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	password=models.CharField(verbose_name='密码' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	tel=models.CharField(verbose_name='电话' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	address=models.CharField(verbose_name='地址' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	company=models.CharField(verbose_name='公司' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	mail=models.CharField(verbose_name='邮箱' ,max_length=100) #charfield char类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	# age=models.IntegerField(verbose_name='用户表密码' ) #charfield 整数类型 100长度 ;verbose:注解 title为字段(id不用谢默认生成主键和自增)
	# account=models.DecimalField(verbose_name='用户表密码' ,max_digits=10,decimal_places=2) #精准数据类型 最大数位 精确到2位

	time=models.DateTimeField(verbose_name='时间',auto_now_add=True)#时间戳
class Google_search_picture(models.Model):
    """
    CharField 类型必须设置 max_length 参数
    verbose_name 是对字段的解释,每个字段都有,且是第一个默认形参,所以可以直接在第一个位置实参处写值不需要写verbose_name=
    null=True 允许字段为空
    default=0 设置默认值
    """
    # id int primary key auto_increment;(sql语句效果与下面orm语句相同)
    id = models.AutoField(primary_key=True,verbose_name="主键ID")
    # name varchar(32);
    title = models.TextField(verbose_name="标题")
    #图片url
    pic1_url = models.TextField(verbose_name="图片url")
    pic1_loc_img = models.TextField(verbose_name="标签图片url")
    pic2_url = models.TextField(verbose_name="图片url")
    pic3_url = models.TextField(verbose_name="图片url")
    pic4_url = models.TextField(verbose_name="图片url")
    pic5_url = models.TextField(verbose_name="图片url")
    pic6_url = models.TextField(verbose_name="图片url")
    #图片位置
    pic1_loc = models.TextField(verbose_name="图片位置")
    pic2_loc = models.TextField(verbose_name="图片位置")
    pic3_loc = models.TextField(verbose_name="图片位置")
    pic4_loc = models.TextField(verbose_name="图片位置")
    pic5_loc = models.TextField(verbose_name="图片位置")
    pic6_loc = models.TextField(verbose_name="图片位置")
    #搜图查到的图url
    goods1_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods2_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods3_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods4_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods5_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods6_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods7_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods8_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods9_pic_url = models.TextField(verbose_name="搜图查到的图url")
    goods10_pic_url = models.TextField(verbose_name="搜图查到的图url")
    #找到的10个产品url
    goods1_url = models.TextField(verbose_name="找到的10个产品url")
    goods2_url = models.TextField(verbose_name="找到的10个产品url")
    goods3_url = models.TextField(verbose_name="找到的10个产品url")
    goods4_url = models.TextField(verbose_name="找到的10个产品url")
    goods5_url = models.TextField(verbose_name="找到的10个产品url")
    goods6_url = models.TextField(verbose_name="找到的10个产品url")
    goods7_url = models.TextField(verbose_name="找到的10个产品url")
    goods8_url = models.TextField(verbose_name="找到的10个产品url")
    goods9_url = models.TextField(verbose_name="找到的10个产品url")
    goods10_url = models.TextField(verbose_name="找到的10个产品url")
    #查到的标题
    goods1_title = models.TextField(verbose_name="查到的标题")
    goods2_title = models.TextField(verbose_name="查到的标题")
    goods3_title = models.TextField(verbose_name="查到的标题")
    goods4_title = models.TextField(verbose_name="查到的标题")
    goods5_title = models.TextField(verbose_name="查到的标题")
    goods6_title = models.TextField(verbose_name="查到的标题")
    goods7_title = models.TextField(verbose_name="查到的标题")
    goods8_title = models.TextField(verbose_name="查到的标题")
    goods9_title = models.TextField(verbose_name="查到的标题")
    goods10_title = models.TextField(verbose_name="查到的标题")
    #已经搜图
    search_picture = models.TextField(verbose_name="已经搜图")
    #更新时间
    time=models.DateTimeField(auto_now=True)
    #创建时间(只在记录创建时变动,然后不可修改)
    create_time=models.DateTimeField(auto_now_add=True)
    # # age int;
    # age = models.IntegerField(verbose_name="年龄")
    # # pwd int;
    # pwd = models.IntegerField("密码",null=True)
    # #性别
    # gender=models.CharField(max_length=10,verbose_name="性别")
    # #年级
    # grade = models.IntegerField(default=0)
    # #
    # is_delete = models.IntegerField(default=0)
