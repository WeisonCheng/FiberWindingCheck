class TempDatas(object):
    '''全局变量'''
    def __init__(self):
        #
        self.iStatus = 2 # 炉位状态 0 正常检测 1 断头 2 暂停 
        self.pauseTimes = 0
        self.runflag = False # 是否开始检测
        self.grayFrame          = None
        self.rgbFrame = None
        self.captured        = False
        self.isDead = False
        self.cameraindexpre = 0
        self.cameraindex = 0
        self.condition      = 0
        self.pageCondition  = 0
        self.perviewflag = False
        self.firstFrame = None
        self.secondFrame = None
        self.thirdFrame = None
        #学习和识别
        self.pressTimes = 0
        self.startflag = True
        self.machineStart = False
        self.index = 0
        self.avgValues = [0,0,0,0,0,0]
        self.spiltPerValues = [0,0,0,0,0,0]
        self.condition = 0
        self.normalNum = 0
        #检测数据
        self.detectNum = 0
        self.errorTimes = 0
        self.errortype = 0
        self.loubanfenbu = [0,0,0,0,0,0]
        self.senderrorCount = 0
        self.SendErrorList = []
        self.startShangtou = 0 
        self.endShangtou = 0
        self.timeShangtou = 0
        self.shangtouSucess = 0
        self.ShangtouSucessTime = 0
        self.turnyarntime = 0
        self.turnbrokentime = 0

        #漏板从左到右，六个区域
        self.leftleft = 0
        self.leftright = 0
        self.midleft = 0
        self.midright = 0
        self.rightleft = 0
        self.rightright = 0
        self.interval = 0

        #其他临时变量
        self.OneLevelStr = ""
        self.TwoLevelStr = ""
        self.ThreeLevelStr = ""
        self.TimeFixed = 0
        self.isShowFrame = True