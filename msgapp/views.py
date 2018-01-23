from django.shortcuts import render
from datetime import datetime
from msgapp.models import MsgData
# Create your views here.

def msgproc(request):
    # 这是老师给出的实例
    datalist = []

    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}\n".format(userB, userA, msg, time))

    if request.method =="GET":
        userC = request.GET.get("userC", None)
        if userC != None:
            with open("msgdata.txt", "r") as f:
                cnt =0
                for line in f:
                    linedata = line.split("--")
                    if linedata[0] == userC:
                        cnt = cnt +1
                        d = {
                            "userA": linedata[1],
                            "msg":linedata[2],
                            "time":linedata[3]
                        }
                        datalist.append(d)
                    if cnt >=10:
                        break

    return render(request, "msgweb.html", {"data":datalist})

def msgproc2(request):
    # 将数据存储修改为sqlite,有空继续，先放着，暂时不会
    datalist = []

    if request.method == "POST":
        userA = request.POST.get("userA", None)
        userB = request.POST.get("userB", None)
        msg = request.POST.get("msg", None)
        time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open("msgdata.txt", "a+") as f:
            f.write("{}--{}--{}--{}\n".format(userB, userA, msg, time))

    if request.method =="GET":
        userC = request.GET.get("userC", None)

        if userC != None:
            datas = MsgData.objects.filter(send_name=userC)
                
            d = {
                "userA": linedata[1],
                "msg":linedata[2],
                "time":linedata[3]
            }
            datalist.append(d)
                    
    return render(request, "msgweb.html", {"data":datalist})