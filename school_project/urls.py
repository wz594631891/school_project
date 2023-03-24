# from django.views.static import serve #加载本地图片0308

"""school_project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from web import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('student_list/', views.student_list),
	path('index/',views.index),#路径函数对应关系,首页
    path('register/',views.register),#注册页
    path('login/',views.login),#登录页面
    path('google_search_picture/',views.google_search_picture),#谷歌搜图
    path('wait_ship_aliexpress_order/',views.wait_ship_aliexpress_order),#速卖通订单
    path('delete/',views.delete),#删除速卖通订单
    # #加载本地图片X
    # url(r'^book/(?P<path>.*)$', serve, {'document_root':'D:/github_goods'})
]
