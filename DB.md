##关于智药项目数据库的简要说明
####原有数据库简单说明
***
#####1.alterenvironment
    用于记录用户对培养箱环境修改的的数据
    1. AltEid (修改事件的标识）
    2. Atime (记录修改事件的时间
    3~6 AT~AP(用于记录用户对数据的修改）
    7. APlantStage 意义不明
    8. IncubatorUsing_IUNo (记录进行此次修改的培养箱ID）
#####2. buypost
    此表原先是用于论坛出售药材之用，由于论坛功能暂定删除，此表暂定废弃
#####3.Cart 
#####4.Commentpost
    以上两表猜测原先是为论坛服务，现在暂留，以防万一
#####5.Customenviroment
    意义不明
#####6.Cuseomstatistics
    意义不明
#####7.Incubator
    用于记录培养箱的具体信息
    1.incuNo 用于记录培养箱的ID，培养箱的唯一标识
    2.incuname 用于记录培养箱的名字（计划删除）
    3.purchasetime 用于记录培养箱被购买的日期
    4.User_userid 用于记录培养箱的主人
#####8.Incubatorusing
    用于记录正在工作的培养箱信息
    1.iuno 标识ID
    2.initializatiome 记录开始使用时间
    3. 记录了培养箱的一些数据
    4，和Incubator 连接的ID
    5. 种植的植物名字
    6. 用户ID
#####9.monitorinform
    用于记录对培养箱植物信息的监控
    1. 记录时间
    2. 记录的培养箱的型号
    3. 记录的四个属性
    4. 记录的植物
    5. 实时分数
#####10.order
#####11.orderitem
    用于记录订单信息，暂时弃用
#####12.plant
    记录植物信息，对种植植物的信息统计内容过少，要进行完善
#####13.plantstatistics
    用于记录对植物的数据的统计，计划用于记录对植物适合种植信息的记录
#####14.product
    用于记录产品信息
#####15.productdetail
    产品细节
#####16.repository
    意义不明
#####17.sellpost
    订单信息
#####18.user
    用户信息，过于简陋决定增加内容

***
####结合现在项目的前端页面尽心的数据库修改
#####1.对部分无用数据表暂时弃用
    具体的弃用见代码注视
#####2.结合个人中心，对user表的内容进行增加
    1. 首先是增加了userImg 用于记录用户头像
    2. 加入userSex用于记录用户性别信息
    3. 增加userintroduction 用于记录用户简介
    4. 增加userlastelogintime 用于记录用户上次登录时间
#####3.增加新表usershowlink
    1.此表用于记录用户对自己的展示植物的关系
    2.usLinkID 用于作为主键，标识记录
    3.userID 外键，用户ID
    4.plantshowID 外键，展示ID
#####4.增加Incubatorhardinf
    1.此表用于监控正在运行的培养箱的硬件状态
    2.iuno 外键，用于绑定培养箱
    3.icpu cpu状态
    4.itemp 温度传感器转态
    5.ihum  湿度~
    6.ipress 气压
    7.ilight 光照
    8.data 日期
#####5.增加plantshow
    1.此表用于记录展示药材的信息
    2.spid 展示编号
    3.spname 作物名字
    4.spint 展示的简介
    5.spmark 展示的分实
    6.spplantstime 展示作物种植的开始时间
    7.spplantetime 收获时间
    8.inno种植的培养箱ID
    9.spheat 作物热度
#####6.增加Inplantdetail
    1.此表用于记录培养箱的每日信息
    2.inno 培养箱ID
    3.plantID 种植的药材ID
    4.dayavertemp 日均温度
    5.dayaverhum 日均湿度
    6.dayaverpress 日均气压
    7.dayaverlight 日均关照
    8.data 日期
#####7.增加Incubator内容
    1.usetime 增加使用总时长
    2.managerstage 管理状态
#####8.增加plant内容
    1.改plantID为主键
    2.pplantaverpeople 种植平均人数
    3.pplantsumpeople 种植总人数
    4.pplantavertime 种植平均时间
    5.pplantsumtime 种植总时长
    6.pavermark 植物种植平均评分
#####9.增加selldetail
    1.用于记录具体的销售信息
    2.data 具体年月
    3.mostsellperson 月度销售最多的负责人
    4.mostsellInc ~培养箱
    5.mostsellarea ~地区  
#####10.增加sellmanmger
    1.用于记录各地区销售负责人信息
    2.areaname    地区
    3.managername 负责人
#####11.sellpost用于记录订单信息
#####12.增加fixinfo
    1.此表用于记录上报的维修信息
    2.fixinfoID 维修单号
    3.fixincID 维修机器的ID
    4,fixboxuserID 用户ID
    5.isover 状态
    6.fixmanager 维修负责人
    7.data 维修上报日期
#####13.增加MangerUser
    1.用于记录管理员信息
    2.muserid 管理员ID
    3.musername 管理员姓名
    4.muserphonenum 管理员电话
    5.mpassword 管理员密码
    6.muserimg 管理员头像
   