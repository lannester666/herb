"""zhiyao URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from app import views
from django.views.static import serve
from zhiyao.settings import MEDIA_ROOT

urlpatterns = [
    path('admin/', admin.site.urls),
    path('signin/', views.signin),
    path('signup/', views.signup),
    path('login/', views.login, name='login'),
    path('logout/', views.logout),
    path('register/', views.register, name='register'),
    path('incubator/', views.incubator, name='incubator'),
    path('bbs/', views.bbs, name='bbs'),
    path('incubatorDetail/<incubatorno>/', views.incubatorDeatil, name='incubatorDetail'),
    path('alterenviroment/<incubatorno>/', views.alterenviroment, name="alterenviroment"),
    path('bbs/', views.bbs, name="bbs"),
    path("bbs/writePurchase/", views.writePurchase),
    path("bbs/writePurchase/save/<userphone>", views.savePurchase),
    path('bbs/writeSelling/', views.writeSelling),
    path('bbs/writeSelling/save/<userphone>', views.saveSelling),
    path('bbs/writeCommunication/', views.writeCommunication),
    path('bbs/writeCommunication/save/<userphone>', views.saveCommunication),
    path('getbbs/', views.getbbs),
    path('getbbs/purchaseDetail/<id>', views.getPDetail, name='pDetail'),
    path('getbbs/sellingDetail/<id>', views.getSDetail, name='sDetail'),
    path('getbbs/communicationDetail/<id>', views.getCDetail, name='cDetail'),
    path('my/', views.my),
    path('test/', views.test),
    path('backendlogin/', views.backendlogin),
    path('backend/', views.backend, ),
    path('oldplantinfo/', views.plantinf_old),
    path('howtoplant', views.howtoplant),
    path('showplant', views.showplant),
    path('showplant/plantdetail', views.plantdetail),
    #############################路径需要修改
    path('guide', views.guide),
    path('changeEnvironment/<incubatorno>/', views.proIncubator, name="changeEnvironment"),
    path('', views.index),  # 登陆信息
    path('hard', views.proHard),  # 接收本地sock服务器转发的硬件相关数据
    re_path(r'image.*', views.returnImage),  # 由页面自动发起请求，获取箱内图片
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path(r'^media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT})
]
