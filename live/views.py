# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect, HttpResponse
# Create your views here.

from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from live.forms import *


@login_required
def home(request):
    return render(request,"Home.html")



def index(request):
    return render(request,"index.html")



def schedule(request):
    import urllib2, urllib, zlib, hmac, hashlib, time, json
    from time import strftime, gmtime
    ROOT_URL = 'http://services.uplynk.com'
    OWNER = '15924b0521f34689810d803be689a3ac' # SE account
    SECRET = 'sw395AXyuIysSgyYNdmd9bzKWQc33+c5Huy2mvCw' # CHANGE THIS TO YOUR SECRET API KEY

    def Call(uri, **msg):
        msg['_owner'] = OWNER
        msg['_timestamp'] = int(time.time())
        msg = json.dumps(msg)
        msg = zlib.compress(msg, 9).encode('base64').strip()
        print "msg",msg
        sig = hmac.new(SECRET.encode('utf-8'), msg.encode('utf-8'), hashlib.sha256).hexdigest()
        print "sig",sig
        body = urllib.urlencode(dict(msg=msg, sig=sig))
        print "body",body
        return json.loads(urllib2.urlopen(ROOT_URL + uri, body).read())


    ts = time.time()
    now = strftime("%Y-%m-%d %H:%M:%S", gmtime(ts))

    # Channel scheduler BETA
    schedule1 = []
    for i in range(1000):
        schedule1.append('aad61071a6fd4556b8e75f093c58db7b') #asset GUID
        break

    # Channel scheduler BETA
    data=Call('/api2/channel/list')
    print(data)
    #print data['channels']
    #print data['channels'][0]['slicer_id']

    channels_name={}
    for i in data['channels']:
        print i['id']
        print i['title']
        channels_name.update({i['title']:i['id']})
    
    print(channels_name)
    if request.method == 'POST':
        channel2=request.POST["channel"]
        video_id=request.POST["Video_GUID"]
        datetime=request.POST["datetime"]
        datetime=datetime.replace('T'," ")
        print("datetime",datetime)
        print "1111111111111111111111",channel2,video_id,channels_name[channel2]
        c_id=channels_name[channel2]

        ts = time.time()
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime(ts))
        print("now",now)
        print(type(now))
        # Channel scheduler BETA
        schedule1 = []
        for i in range(1000):
            schedule1.append(video_id) #asset GUID
            break

        # Channel scheduler BETA
        data2=Call('/api2/channel/schedule/update', id=c_id, schedule=[{"type":"asset", "asset": schedule1, "start": "{}".format(datetime)}])
        print(data2)
        try:
            d=data2['schedule']
        except:
            return render(request,"success.html",{"data5":"true"})
        return render(request,"success.html",{"data1":data2['schedule']})
    return render(request,"schedule.html",{"data1":channels_name})



def multiSchedule(request):
    if request.method == 'POST':
        excel_file = request.FILES["fileToUpload"]
        print("1111111111111111111111",excel_file)
        import urllib2, urllib, zlib, hmac, hashlib, time, json
        from time import strftime, gmtime

        ROOT_URL = 'http://services.uplynk.com'
        OWNER = '15924b0521f34689810d803be689a3ac' # SE account
        SECRET = 'sw395AXyuIysSgyYNdmd9bzKWQc33+c5Huy2mvCw' # CHANGE THIS TO YOUR SECRET API KEY

        def Call(uri, **msg):
            msg['_owner'] = OWNER
            msg['_timestamp'] = int(time.time())
            msg = json.dumps(msg)
            msg = zlib.compress(msg, 9).encode('base64').strip()
            sig = hmac.new(SECRET, msg, hashlib.sha256).hexdigest()
            body = urllib.urlencode(dict(msg=msg, sig=sig))
            return json.loads(urllib2.urlopen(ROOT_URL + uri, body).read())


        ts = time.time()
        now = strftime("%Y-%m-%d %H:%M:%S", gmtime(ts))

        # Channel scheduler BETA
        schedule1 = []
        for i in range(1000):
            schedule1.append('aad61071a6fd4556b8e75f093c58db7b') #asset GUID
            break

        # Channel scheduler BETA
        print(Call('/api2/channel/schedule/update', id='a39650711a294f40a8728c85476b16d9', schedule=[{"type":"asset", "asset": schedule1, "start": "{}".format(now)}]))
    return render(request,"multiSchedule.html")



def signup_page(request):
    if request.method=="POST":
        form=signupform(request.POST)
        if form.is_valid():
            name=request.POST["Name"]
            email=request.POST["Email"]
            password=request.POST["Password"]
            Firstname=request.POST["Firstname"]
            lastname=request.POST["lastname"]
            user = User.objects.create_user(username=name,email=email,password=password,first_name=Firstname,last_name=lastname)
            user.save()
            return redirect('/signin/')
    else:
        form = signupform()
        print("notdshksfdhjsdfhsdfahlsafd")
    return render(request,'signup.html',{"form":form})





def login_user(request):
    if request.user.is_authenticated:
        print("Logged in")
        return redirect("/home/")
    else:
        print("Not logged in")

    if request.method == 'POST':
        form = loginform(request.POST)
        if form.is_valid():
            username = request.POST.get('Username')
            print(username)
            password = request.POST.get('Password')
            print(password)
            user = authenticate(username=username, password=password)
            if user:
                print("yesssssssssssssssss")
                login(request,user)
                return redirect("/home/")

    else:
        form = loginform()
        print("not")
    return render(request, 'signin.html', {"form": form})




@login_required
def user_logout(request):
    logout(request)
    return redirect('/signin/')