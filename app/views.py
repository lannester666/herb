from django.shortcuts import render
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from django.http import HttpResponse
from app import models
from app.models import Incubatorusing
from app.models import Monitorinform
from app.models import Incubator
# 作图
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator
import time
import json
# Create your views here.

from . import predict




# 注释掉的内容为解决错误的另一种方法
# from keras.models import load_model
# import os
# import numpy as np
# from keras.preprocessing import image
# from keras.applications.imagenet_utils import preprocess_input
# import keras
#
# model=None
#
# def read_image(img_name):
#     print('imagename:'+img_name)
#     img = image.load_img(img_name, target_size=(224, 224))
#     x = image.img_to_array(img)
#     x = np.expand_dims(x, axis=0)
#     x = preprocess_input(x)
#     return x
#
#
#
# def predict(imagepath):
#     categories=['bad','good','green','normal','red']
#     model=None
#     if os.path.exists('app//inception_1.h5'):
#         print('predict if')
#         keras.backend.clear_session()
#         model = load_model('app//inception_1.h5')
#         print('load successful')
#
#
#     if model != None:
#         img=read_image(imagepath)
#         print('readimage successful')
#         prediction=model.predict(img)
#         result=categories[int(prediction[0][0])]
#         print(result)
#         return result
#     else:
#         print('predict else')
#         return "error"

def index(request):
    """
    实现首页面功能
    :param request:
    :return:
    """
    return render(request, 'index1.html')


# #实现用户登陆功能
def login(request):
    if request.method == 'POST':
        userphone = request.POST.get('username')
        password = request.POST.get('password')
        if userphone and password:
            userphone = userphone.strip()
            try:
                user = models.User.objects.get(userphonenum=userphone)
                if user.password == password:
                    request.session['is_login'] = True
                    request.session['userphone'] = user.userphonenum
                    request.session['username'] = user.username
                    request.session['userimg'] = user.userimg

                    # get是获取单个对象，filte是设置筛选条件
                    incubators = models.Incubator.objects.filter(user_userid=userphone)
                    incuName = []
                    incuID = []
                    incu = []
                    for item in incubators:
                        incuName.append(item.incuname)
                        incuID.append(item.incuno)
                        incu = zip(incuName, incuID)
                    print('login success')
                    return render(request, 'index1.html', {"incu": incu})
                else:
                    message = '密码错误'
                    return render(request, 'index1.html', {'message': message})
            except:
                message = '用户不存在'
                return render(request, 'index1.html', {'message': message})
    return render(request, 'index1.html')


# 用户注册
def register(request):
    if request.method == 'POST':
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        usermail = request.POST.get('usermail')
        username = request.POST.get("username")
        try:
            user = models.User.objects.get(userphonenum=userphone)
            message = '此用户已存在'
            return render(request, '../temp/register.html', {'message': message})
        except:
            try:
                user = models.User.objects.get(usermail=usermail)
                message = '此邮箱已被注册'
                return render(request, '../temp/register.html', {'message': message})
            except:
                try:
                    user = models.User.objects.get(username=username)
                    message = '此用户名已被注册'
                    return render(request, '../temp/register.html', {'message': message})
                except:
                    # userid和userphone是一样的
                    newUser = models.User()
                    newUser.userid = userphone
                    newUser.userphonenum = userphone
                    newUser.username = username
                    newUser.usermail = usermail
                    newUser.password = password
                    newUser.save()
                    return redirect('/login/')
    return render(request, '../temp/register.html')


# 用户登录
def signin(request):
    return render(request, 'signin.html')


# 用户注册
def signup(request):
    if request.method == 'POST':
        userphone = request.POST.get('userphone')
        password = request.POST.get('password')
        usermail = request.POST.get('usermail')
        username = request.POST.get("username")
        try:
            user = models.User.objects.get(userphonenum=userphone)
            message = '此用户已存在'
            return render(request, 'signup.html', {'message': message})
        except:
            try:
                user = models.User.objects.get(usermail=usermail)
                message = '此邮箱已被注册'
                return render(request, 'signup.html', {'message': message})
            except:
                try:
                    user = models.User.objects.get(username=username)
                    message = '此用户名已被注册'
                    return render(request, 'signup.html', {'message': message})
                except:
                    # userid和userphone是一样的
                    newUser = models.User()
                    newUser.userid = userphone
                    newUser.userphonenum = userphone
                    newUser.username = username
                    newUser.usermail = usermail
                    newUser.password = password
                    newUser.save()
                    return redirect('/signin')
    return render(request, 'signup.html')


def logout(request):
    request.session.clear();
    return redirect('/')


# 通过用户id也就是手机号获取用户所有正在使用的培养箱
def getIncubator(userid):
    incubators = models.Incubator.objects.get(user_userid=userid)
    return incubators
    # 获取用户所有正在使用的培养箱


def getIncubator_(request):
    incubator1 = models.Incubator.objects.all()
    for inc in incubator1:
        print(inc)
    context = {
        'incubator1': incubator1,
    }
    return render(request, 'Backend.html', context)


def incubator(request):
   # userphone = request.session['userphone']
    # get是获取单个对象，filte是设置筛选条件
    # incubators = models.Incubator.objects.filter(user_userid=userphone)


    incubators = models.Incubator.objects.all()
    incuName = []
    incuID = []
    incu = []
    for item in incubators:
        incuName.append(item.incuname)
        incuID.append(item.incuno)
        incu = zip(incuName, incuID)
    print('jump to incubator success')
    return render(request, 'incubator.html', {"incu": incu})


def getAdvice(category):
    # categories=['bad','good','green','normal','red']
    humidity = {'bad': 46.42, 'good': 46.42, 'green': 46.42, 'normal': 46.42, 'red': 46.42}
    temperature = {'bad': 25.46, 'good': 25.46, 'green': 25.46, 'normal': 25.46, 'red': 25.46}
    pressure = {'bad': 104375, 'good': 104375, 'green': 104375, 'normal': 104375, 'red': 104375}
    light = {'bad': 55231, 'good': 55231, 'green': 55231, 'normal': 55231, 'red': 55231}
    state = {'bad': '糟糕', 'good': '很好', 'green': '幼苗', 'normal': '正常状态', 'red': '营养过剩'}
    if category == 'error':
        print('读取图片存在错误，无法判断类别')
        return {"state": '暂无建议', "adviceHumidity": '暂无建议', "adviceTemperature": '暂无建议',
                "advicepressure": '暂无建议', "adviceLight": '暂无建议'}
    else:
        return {"state": state[category], "adviceHumidity": humidity[category],
                "adviceTemperature": temperature[category], "advicepressure": pressure[category],
                "adviceLight": light[category]}


# 查看培养箱的详细信息
def incubatorDeatil(request, incubatorno):
    # 这个incubatorno传递进来的是培养箱的编号
    # 需要再调用方法找到现在正在使用的培养箱的编号
    # 此处需要从培养箱的首页传递要查看培养箱的id
    # 此处假设获得，使用数据库中的 incubatorusing的id为i0101
    # iuno='i0101'

    print("pie" + incubatorno)
    ino = incubatorno
    # ino = Incubatorusing.objects.filter(incubator_incuno=incubatorno)
    initalInfo = getInital(ino)
    monitorInfo = getCurrent(ino)
    iuno = getIncubatorusingID(ino)

    # 将当前用户访问的培养箱的信息存放再session中
    request.session['incubatorid'] = iuno
    # session中的inid用于之后的页面重定向
    request.session['inid'] = ino
    request.session['true'] = True
    # 将包含初始信息和当前监控信息的两个字典合并起来
    info = {}
    info.update(initalInfo)
    info.update(monitorInfo)
    # info=combineDict(initalInfo,monitorInfo)
    print(info)

    # 处理监控信息
    incubatorsUsing = models.Incubatorusing.objects.filter(incubator_incuno=incubatorno).order_by('initializetime')
    iuno = incubatorsUsing[len(incubatorsUsing) - 1].iuno  # 获取这个培养箱的使用编号的最新的那个编号
    print(iuno)
    # monitorDatas = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno).order_by('mtime')
    monitorDatas = models.Monitorinform.objects.all().order_by('-mtime')
    # print(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    # print(monitorDatas)
    time = []
    temperature = []
    humidity = []
    pressure = []
    lightIntensity = []
    for data in monitorDatas:
        time.append(str(data.mtime)[:16])
        temperature.append(data.mtemperature)
        humidity.append(data.mhumidity)
        pressure.append(data.mpressure)
        lightIntensity.append(data.mlightlntensity)
    monitorDatas2 = {"Mtimes": json.dumps(time[:10]), "Mtemperatures": temperature[:10], "Mhumiditys": humidity[:10],
                     "Mpressures": pressure[:10], "MlightIntensitys": lightIntensity[:10]}
    print(time)
    info.update(monitorDatas2)

    dir = 'realtime_images'
    lists = os.listdir(dir)  # 列出目录的下所有文件和文件夹保存到lists
    print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(dir + "/" + fn), reverse=True)  # 按时间排序
    file_new = os.path.join(dir, lists[-1])  # 获取最新的文件保存到file_new
    print(file_new)

    category = predict(file_new)
    adviceData = getAdvice(category)
    # adviceData的内容为：{"state":state,"adviceHumidity":humidity[category],"adviceTemperature":temperature[category],"advicepressure":pressure[category],"adviceLight":light[category]}
    info.update(adviceData)
    return render(request, "incubator_details.html", info)


# 获取监控信息返回给调用函数
def getMointorData(incubatorno):
    incubatorsUsing = models.Incubatorusing.objects.filter(incubator_incuno=incubatorno).order_by('initializetime')
    iuno = incubatorsUsing[len(incubatorsUsing) - 1].iuno  # 获取这个培养箱的使用编号的最新的那个编号
    print(iuno)
    monitorDatas = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno)


# 辅助的功能函数 将两个字典合并
def combineDict(dic1, dic2):
    info = {}
    return combineDict(dic1, dic2)


# 通过培养箱的id获得当前正在使用的这个incubatorusing的id
def getIncubatorusingID(iuno):
    inusing = models.Incubatorusing.objects.filter(incubator_incuno=iuno).last()
    # 这里需要注意的是，django里的外键是对象，不只是id
    return inusing.iuno


# 获取培养箱的初始信息，并在页面种显示出来
def getInital(ino):
    iuno = getIncubatorusingID(ino)
    # 传入的是培养箱的id
    # 这里需要使用的是incubatorusing的id
    try:
        # 获取培养箱的初始信息
        incubatorUsing = models.Incubatorusing.objects.get(iuno=iuno)
        # print(incubatorUsing.itemperature)
        # 很气人啊，在model里面，所有的id都会变成小写
        item = incubatorUsing.itemperature
        ihum = incubatorUsing.ihumidity
        ipre = incubatorUsing.ipressure
        ilig = incubatorUsing.ilightlntensity
        info = {"Itemperature": item, "Ihumidity": ihum, "Ipressure": ipre, "IlightIntensity": ilig, "IisSucceed": True}
        return info
    except:
        info = {"IisSucceed": True}
        return info


# 获得培养箱内的最新监控信息
def getCurrent(ino):
    iuno = getIncubatorusingID(ino)
    try:
        monitorInfo = models.Monitorinform.objects.filter(incubatorusing_iuno=iuno).order_by("mtime").last()
        mtem = monitorInfo.mtemperature
        mhum = monitorInfo.mhumidity
        mpre = monitorInfo.mpressure
        mlig = monitorInfo.mlightlntensity
        info = {"Mtemperature": mtem, "Mhumidity": mhum, "Mpressure": mpre, "MlightIntensity": mlig, "MisSucceed": True}
        return info
    except:
        info = {"MisSucceed": True}
        return info


# 由正在使用的培养箱的id获得培养箱本身的id
def getIncubatorID(iuno):
    try:
        Incubatorusing = models.Incubatorusing.objects.get(iuno=iuno)
        inno = Incubatorusing.incubator_incuno
        return inno
    except:
        print("寻找培养箱时发生错误")
    return 0


# 修改培养箱的环境信息
def alterenviroment(request, incubatorno):
    print("jingruhanshu")
    if request.method == "POST":
        AlightIntensity = request.POST.get('AlightIntensity')
        Atemperature = request.POST.get("Atemperature")
        Ahumidity = request.POST.get("Ahumidity")
        Apressure = request.POST.get("Apressure")
        incubatorusing_iuno = incubatorno
        # 修改信息的id使用正在使用的培养箱的编号加上提交修改的时间戳
        alteid = incubatorusing_iuno + str(time.time())
        print("xiugaile" + alteid)

        newAlter = models.Alterenvironment()
        newAlter.alteid = alteid
        newAlter.alightlntensity = AlightIntensity
        newAlter.atemperature = Atemperature
        newAlter.ahumidity = Ahumidity
        newAlter.apressure = Apressure
        # 将植物所处的阶段默认设置为0
        newAlter.aplantstage = '0'
        newAlter.save()
        inno = str(getIncubatorID(incubatorno).incuno)
        print(inno)
        urlr = "/incubatorDetail/" + inno + "/"
    return redirect(urlr)


def backendlogin(request):
    return render(request, 'backendlogin.html')


def backend(request):
    incubator1 = models.Incubator.objects.all()
    context = {
        'incubator1': incubator1,
    }
    return render(request, 'Backend.html', context)


def plantinf_old(request):
    return render(request, 'old_plant_info.html')


def howtoplant(request):
    return render(request, 'how_to_plant.html')


def showplant(request):
    return render(request, 'show_plant.html')


def plantdetail(request):
    return render(request, 'plant_detail.html')


def bbs(request):
    return render(request, 'bbs.html')


def my(request):
    userphone = request.session['userphone']
    # get是获取单个对象，filte是设置筛选条件
    incubators = models.Incubator.objects.filter(user_userid=userphone)
    incuName = []
    incuID = []
    incu = []
    for item in incubators:
        incuName.append(item.incuname)
        incuID.append(item.incuno)
        incu = zip(incuName, incuID)
    print('jump to incubator success')
    return render(request, 'my.html', {"incu": incu})
    # return render(request,'my.html')


def writePurchase(request):
    return render(request, 'writePurchase.html')


def writeSelling(request):
    return render(request, "write_selling.html")


def writeCommunication(request):
    return render(request, "writeCommunication.html")


def savePurchase(request, userphone):
    if request.method == 'POST':
        pid = str(userphone) + str(time.time())
        pMedicine = request.POST.get('pMedicine')
        pPrice = request.POST.get("pPrice")
        pDescribe = request.POST.get("pDescribe")
        pPhone = request.POST.get("pPhone")

        newBuy = models.Buypost()
        newBuy.bid = pid
        newBuy.bplant = pMedicine
        newBuy.bprice = pPrice
        newBuy.bdescription = pDescribe
        newBuy.bphonenum = pPhone
        usr = models.User.objects.get(userid=userphone)
        newBuy.user_userid = usr
        newBuy.save()
    return redirect("/bbs/")


def saveSelling(request, userphone):
    return redirect('/bbs/')


def saveCommunication(request, userphone):
    return redirect('/bbs/')


def getPurchase(request):
    print("尝试成功")
    # return HttpResponse('执行成功')
    return render(request, '../temp2/../temp/bbs.html')


def getSelling(request):
    return HttpResponse("selling")


def getAll(request):
    return HttpResponse('all')


def getMy():
    pass


def getbbs(request):
    # 把所有的信息都展示出来
    clist = models.Commentpost.objects.all().order_by('-releasectime')
    slist = models.Sellpost.objects.all().order_by('-releasestime')
    plist = models.Buypost.objects.all().order_by('-releasebtime')
    return render(request, '../temp2/../temp/bbs.html', {'clist': clist, 'slist': slist, 'plist': plist})


# 购买
def getPDetail(request, id):
    try:
        purchase = models.Buypost.objects.get(bid=id)
        return render(request, 'purchaseDetail.html', {"pDetail": purchase, 'success': True})
    except:
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


def getSDetail(request, id):
    try:
        selling = models.Sellpost.objects.get(sid=id)
        return render(request, 'sellingDetail.html', {'sDetail': selling, 'success': True})
    except:
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


def getCDetail(request, id):
    try:
        communication = models.Commentpost.objects.get(cid=id)
        return render(request, 'communicationDetail.html', {'cDetail': communication, 'success': True})
    except:
        print('meizhaodao')
        return render(request, '../temp2/../temp/bbs.html', {'success': False})


#########################################################################################################
# 以下是有关硬件的请求处理代码
#########################################################################################################
from django.shortcuts import render
from app.models import ChangeLog
from app.models import ViewParam
from django.http import HttpResponse
import os
# 1.处理来自 硬件的请求
# 在ViewLog中添加一条环境参数，查看并返回最新的一条ChangeLog表的记录
# 2.返回一张最新的监控图片
# 3.网页上来自用户的修改记录被存库，并返回箱子的实时数据

# 1.
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def proHard(request):
    request.encode = "utf-8"
    response = ''
    clg = ChangeLog.objects.all().order_by("-addtime")
    clg = clg[0]
    tem_ctl = clg.tem
    hum_ctl = clg.hum
    pre_ctl = clg.pre
    led_ctl = clg.led
    tem_ctl_need = 5 - len(tem_ctl)
    hum_ctl_need = 5 - len(hum_ctl)
    led_ctl_need = 5 - len(led_ctl)
    pre_ctl_need = 6 - len(pre_ctl)
    a = "0"
    for i in range(tem_ctl_need):
        tem_ctl = a + tem_ctl
    for i in range(led_ctl_need):
        led_ctl = a + led_ctl
    for i in range(pre_ctl_need):
        pre_ctl = a + pre_ctl
    for i in range(hum_ctl_need):
        hum_ctl = a + hum_ctl
    response += 't=' + tem_ctl + '&' + 'l=' + led_ctl + '&p=' + pre_ctl + '&h=' + hum_ctl
    # response+='_*_'+'t='+tem_ctl+'&'+'l='+led_ctl+'&p='+pre_ctl+'&h='+hum_ctl
    print(request)
    if request.method == 'POST':
        txt = request.POST['text']
        print("get text:", txt)
        # 处理文本数据并存库
        param_split = txt.split('&')
        param_t = param_split[0].split('=')[1]
        param_l = param_split[1].split('=')[1]
        param_p = param_split[2].split('=')[1]
        param_h = param_split[3].split('=')[1]

        mif = Monitorinform()
        mif.mpressure = param_p
        mif.mtemperature = param_t
        mif.mlightlntensity = param_l
        mif.mhumidity = param_h
        mif.mplantstage = 1
        mif.save()

        vpm = ViewParam()
        vpm.tem = param_t
        vpm.led = param_l
        vpm.pre = param_p
        vpm.hum = param_h
        vpm.save()

    return HttpResponse(response)


# 2.
def returnImage(request):
    dir = 'realtime_images'
    lists = os.listdir(dir)  # 列出目录的下所有文件和文件夹保存到lists
    # print(lists)
    lists.sort(key=lambda fn: os.path.getmtime(dir + "/" + fn))  # 按时间排序
    file_new = os.path.join(dir, lists[-1])  # 获取最新的文件保存到file_new
    # print(file_new)
    f = open(file_new, 'rb')
    data = f.read()
    f.close()
    return HttpResponse(data, content_type="image/jpeg")


# 3.
def proIncubator2(request):
    res = {}  # 存储箱子的相关信息
    # 取出最早的一条数据
    Obj = ViewParam.objects.all().order_by('-addtime')
    if Obj:
        Obj = Obj[0]
        res['pressure'] = Obj.pre
        res['light'] = Obj.led
    else:
        pass
    # 事实上这些生成图像的代码应该放到处理硬件的视图中
    vplist = ViewParam.objects.all()
    timelist = []
    temperaturelist = []
    humiditylist = []
    pressurelist = []
    lightlist = []
    for vp in vplist:
        timelist.append(vp.addtime)
        temperaturelist.append(vp.tem)
        humiditylist.append(vp.hum)
        pressurelist.append(vp.pre)
        lightlist.append(vp.led)
    dir = 'media'
    file = os.path.join(dir, "humidityChart.jpg")  # 图片要保存到的位置
    graph(timelist, humiditylist, file)
    file = os.path.join(dir, "temperatureChart.jpg")  # 图片要保存到的位置
    graph(timelist, temperaturelist, file)
    file = os.path.join(dir, "pressureChart.jpg")  # 图片要保存到的位置
    graph(timelist, pressurelist, file)
    file = os.path.join(dir, "lightChart.jpg")  # 图片要保存到的位置
    graph(timelist, lightlist, file)

    if request.POST:
        clg = ChangeLog()
        clg.tem = request.POST['tem_ctl']
        clg.hum = request.POST['hum_ctl']
        clg.led = request.POST['led_ctl']
        clg.pre = request.POST['pre_ctl']
        clg.save()
        res['response'] = "修改已经收到：" + clg.tem
    return render(request, 'incubatorDetail2.html', res)


# 4.
def proIncubator(request, incubatorno):
    if request.POST:
        print("开始处理++++++++++++++++++++++++++++++++++++++++++")
        clg = ChangeLog()
        clg.tem = request.POST['tem_ctl']
        clg.hum = request.POST['hum_ctl']
        clg.led = request.POST['led_ctl']
        clg.pre = request.POST['pre_ctl']

        clg.save()

        incubator = Incubatorusing.objects.get(iuno=incubatorno)

        ino1 = incubator.incubator_incuno.incuno
        ino = (ino1,)
    return HttpResponseRedirect(reverse('incubatorDetail', args=ino))


# 用户初次使用系统流程
def guide(request):
    return render(request, 'connectingGuide.html')


# 作图：

def graph(x, y, file):
    # y = [0.236, 0.256, 0.288, 0.483, 0.621, 0.737, 0.796, 0.845, 0.833, 0.802]
    # x = [20, 30, 40, 80, 150, 250, 350, 400, 450, 500]
    fig = plt.figure()
    ax1 = fig.add_subplot(1, 1, 1, facecolor='white')
    ax1.set_xlabel('时间')  # 设置x轴名称
    ax1.set_ylabel('值')  # 设置y轴名称
    # 设置y轴坐标范围
    plt.title("Figure1_GrayLevel&F1core")

    ax1.yaxis.grid(True, which='minor')
    ax1.plot(x, y, marker='v', color='k', label='fun1', linestyle='dashed')
    plt.savefig(file)


# 用作测试
def test(request):
    return render(request, 'test.html')
