import base64
from datetime import datetime

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponse, JsonResponse
from django.shortcuts import render

# Create your views here.
from blood.models import *
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

def login(request):
    return render(request, "login_index.html")


def logout(request):
    auth.logout(request)
    return render(request, "login_index.html")

def login1(request):
    try:
        Username = request.POST['textfield']
        Password = request.POST['textfield2']
        ob =  login_table.objects.get(username=Username, password=Password)
        if ob.type=="admin":
            # ob1=auth.authenticate(username ='abc',password='admin')
            # if ob1 is not None:
            #     auth.login(request,ob1)
            request.session['lid']=ob.id

            return HttpResponse('''<script>alert("Welcome to Admin Home");window.location='/adminhome#get-started'</script>''')
        elif ob.type=="hospital":
            ob1 = auth.authenticate(username='abc', password='admin')
            # if ob1 is not None:
            #     auth.login(request, ob1)
            request.session['lid'] = ob.id
            return HttpResponse('''<script>alert("Welcome to Hospital Home");window.location='/hospitalhome#get-started'</script>''')
        elif ob.type=="blood bank":
            # ob1 = auth.authenticate(username='abc', password='admin')
            # if ob1 is not None:
            #     auth.login(request, ob1)
            request.session['lid'] = ob.id

            return HttpResponse('''<script>alert("Welcome to blood bank Home");window.location='/bloodbank#get-started'</script>''')
        else:
            return HttpResponse('''<script>alert("Invalid");window.location='/'</script>''')
    except:
        return HttpResponse('''<script>alert("Invalid");window.location='/'</script>''')



def addblood(request):
    return render(request, "addbgrp.html")

def addbloodcode(request):
    b=request.POST['textfield']
    det=request.POST['textfield2']
    ob=blood_table()
    ob.bloodgroup=b
    ob.date=datetime.today()
    ob.details=det
    ob.save()
    return HttpResponse('''<script>alert("added");window.location='/Managebloodgroup#get-started'</script>''')
def sendrequest1(request,id):
    request.session['sr']=id
    return render(request, "ADD_Blood.html")
def sendrequest2(request):
    requests=request.POST['textfield']

    ob=request_table.objects.get(id=request.session['sr'])
    ob.status=requests
    ob.save()
    return HttpResponse('''<script>alert("Request Send");window.location='/sendrequstforblood#get-started'</script>''')



def regbloodbnk(request):
    ob=hospital_table.objects.all()
    return render(request, "bloodbankregindex.html",{"val":ob})

def adminhome(request):
    return render(request, "adminindex.html")

def approvehospitel(request):
    ob=hospital_table.objects.all().order_by('-id')
    return render(request,"approve hospitel.html",{'val':ob})


def accepthospital(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hospital'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location='/approvehospitel#get-started'</script>''')

def rejecthospital(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/approvehospitel#get-started'</script>''')


def approvebloodbank(request):
    ob=blood_bank_table.objects.all().order_by('-id')
    return render(request,"approve bloodbank.html",{'val':ob})


def acceptbloodbank(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='blood bank'
    ob.save()
    return HttpResponse('''<script>alert("accepted");window.location='/approvebloodbank#get-started'</script>''')

def rejectbloodbank(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='reject'
    ob.save()
    return HttpResponse('''<script>alert("rejected");window.location='/approvebloodbank#get-started'</script>''')





def blockhospital(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='block'
    ob.save()
    return HttpResponse('''<script>alert("blocked");window.location='/blockorunblockhospital#get-started'</script>''')

def unblockhospital(request,id):
    ob=login_table.objects.get(id=id)
    ob.type='hospital'
    ob.save()
    return HttpResponse('''<script>alert("unblocked");window.location='/blockorunblockhospital#get-started'</script>''')

def blockorunblockhospital(request):
    ob=hospital_table.objects.filter(Q(LOGIN__type='hospital')|Q(LOGIN__type='block'))
    print(ob)
    return render(request, "block or unblock hospitals.html", {'val2': ob})

def bloodbank(request):
    return render(request,"bloodindex.html")

def hospitalhome (request):
    return render(request, "hospitalindex.html")

def hospitalregistration (request):
    return render(request, "hospitalregindex.html")

def hospitalregistrationcode(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    city = request.POST['city']
    state = request.POST['state']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']
    username = request.POST['textfield9']
    pswd = request.POST['textfield10']
    ob=login_table()
    ob.username=username
    ob.password=pswd
    ob.type='pending'
    ob.save()
    obj=hospital_table()
    obj.LOGIN=ob
    obj.name=name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.city = city
    obj.state = state
    obj.phonno = phone
    obj.email = email
    obj.save()
    return HttpResponse('''<script>alert("success");window.location='/'</script>''')


def bloodregistrationcode(request):
    name=request.POST['textfield']
    place=request.POST['textfield2']
    post=request.POST['textfield3']
    pin=request.POST['textfield4']
    phone = request.POST['textfield7']
    email = request.POST['textfield8']
    username = request.POST['textfield9']
    pswd2 = request.POST['textfield10']
    hos = request.POST['hos']

    ob = login_table()
    ob.username = username
    ob.password = pswd2
    ob.type = 'pending'
    ob.save()

    obj = blood_bank_table()
    obj.LOGIN = ob
    obj.name = name
    obj.place = place
    obj.post = post
    obj.pin = pin
    obj.phonno = phone
    obj.email = email
    obj.HOSPITAL=hospital_table.objects.get(id=hos)
    obj.save()

    a=blood_table.objects.all()
    for i in a:
        blood_id=i.id
        myd=Stock()
        myd.BANK_id=obj.id
        myd.BLOOD_id=blood_id
        myd.stock=0
        myd.save()




    return HttpResponse('''<script>alert("success");window.location='/'</script>''')


def Managebloodgroup(request):
    ob=blood_table.objects.all()
    return render(request, "Manage blood group.html",{'val':ob})


def  requstbloodgroupanddonatefromhospital (request):
    return render(request, "requst blood group and donate from hospital.html")
def searchblood (request):
    ob= blood_table.objects.all()
    return render(request, "search blood.html",{'val':ob})
def searchbloodsearch(request):
    blood=request.POST['b']
    ob = blood_table.objects.all()
    obb=user_table.objects.filter(BLOOD__id=blood)
    return render(request, "search blood.html", {'val': ob,"val1":obb,"b":int(blood)})

def  sendcomplaintandviewreply (request):
    return render(request, "send complaint and view reply.html")
def  sendcomplaint (request):
    return render(request, "send complaint.html")
def  sendfeedback  (request):
    return render(request, "send feedback.html")
def sendrequstforblood(request):
    ob=request_table.objects.all()
    return render(request, "send requst for blood.html",{'val':ob})
def Updateblood(request,id):
    ob=blood_table.objects.get(id=id)
    request.session['bid']=id
    return render(request, "Update blood.html",{'val':ob})
def deleteblood(request,id):
    ob=blood_table.objects.get(id=id)
    ob.delete()
    return HttpResponse('''<script>alert("Deleted");window.location='/Managebloodgroup#get-started'</script>''')


def updatebloodcode(request):
    b=request.POST['textfield']
    det=request.POST['textfield2']
    ob=blood_table.objects.get(id=request.session['bid'])
    ob.bloodgroup=b
    ob.date=datetime.today()
    ob.details=det
    ob.save()
    return HttpResponse('''<script>alert("updated");window.location='/Managebloodgroup#get-started'</script>''')

def  Userregistration(request):
    return render(request, "User registration.html")
def userhome (request):
    return render(request, "user_home.html")
def viewcomplaint(request):
    ob = complaint_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    return render(request, "view complaint.html",{'val':ob})
def viewcomplaints(request):
    ob=complaint_table.objects.all()
    return render(request, "view complaints.html",{'val':ob})

def  aviewcomplaints(request):
    ob=complaint_table.objects.all().order_by('-id')
    return render(request, "adminvcomp.html",{'val':ob})
def viewcomplaintssearch(request):
    date=request.POST['textfield']
    ob=complaint_table.objects.filter(date=date)
    return render(request, "View complaints.html",{'val':ob})
def Reply(request,id):
    request.session['cid']=id
    return render(request, "Reply.html")
def sendreplycode(request):
    reply=request.POST['textarea']
    ob=complaint_table.objects.get(id=request.session['cid'])
    ob.replay=reply
    ob.save()
    return HttpResponse('''<script>alert("Replied");window.location='/viewcomplaint#get-started'</script>''')
def ViewFeedback(request):
    ob=feedback_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'])
    return render(request, "View Feedback.html",{'val3':ob})
def ViewsearchFeedback(request):
    date=request.POST['textfield']
    ob=feedback_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid'],date=date)
    return render(request, "View Feedback.html",{'val3':ob,"dt":str(date)})

def ViewFeedbacksearch(request):
    date=request.POST['textfield']
    ob=feedback_table.objects.filter(date=date)
    return render(request, "View Feedbacks.html",{'val3':ob,'dt':str(date)})


def viewfeedbacks(request):
    ob = feedback_table.objects.all()
    return render(request, "View Feedbacks.html",{'val1':ob})
def viewhospitals(request,id):
    ob=hospital_table.objects.filter(id=id)
    return render(request, "view hospitals.html",{'val':ob})

def  viewrequestforblood(request):
    a=blood_table.objects.all()
    c=Stock.objects.filter(BANK__HOSPITAL__LOGIN_id=request.session['lid'])
    ob=request_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid']).order_by('-id')
    if 'submit' in request.POST:
        search=request.POST['search']
        a=request_table.objects.filter(blood_id=search)
        b=Stock.objects.filter(BLOOD_id=search)
        return render(request, "view request for blood.html", {'val': a,'c':b})

    return render(request, "view request for blood.html",{'val':ob,'data':a,'c':c})











def viewrequestforblood_post(request):
    search = request.POST['search']
    a = request_table.objects.filter(details__icontains='search')
    return render(request, "view request for blood.html", {'val': a})


def  viewrequestforblood_bb(request):
    obh=blood_bank_table.objects.get(LOGIN__id=request.session['lid'])
    ob=request_table.objects.filter(HOSPITAL__id=obh.HOSPITAL.id)
    print(ob,"==============")
    print(ob,"==============")
    return render(request, "view request for blood_bb.html",{'val':ob})

def  view_det(request,id):
    request.session['rid']=id


    ob=response_table.objects.filter(REQUEST__id=id)
    print(ob,"==============")
    print(ob,"==============")

    return render(request, "view request for blood_bb1.html",{'val':ob})
def sentres(request,id):
    request.session['reqid']=id
    oc=response_table.objects.filter(REQUEST__id=id)
    if len(oc)!=0:
        return HttpResponse('''<script>alert('Already Responded');window.location='/viewrequestforblood_bb'</script>''')
    else:
        return render(request, "sentres.html")

def sendresponsebb(request):
    res=request.POST['textarea']
    ob=request_table.objects.get(id=request.session['reqid'])
    oj=response_table()
    oj.REQUEST=request_table.objects.get(id=request.session['reqid'])
    oj.status=res
    oj.date=datetime.today()
    oj.USER=user_table.objects.get(id=ob.USER.id)
    oj.save()
    return HttpResponse('''<script>alert("Responded");window.location='/viewrequestforblood_bb#get-started'</script>''')


def  accept(request,id):
    rid=request.session['rid']


    ob=response_table.objects.get(id=id)
    ob.status="Donated"
    ob.save()
    print(ob,"==============")
    print(ob,"==============")

    return HttpResponse("<script>alert('Accepted');window.location='/view_det/"+str(rid)+"#get-started'</script>")


def  reject(request,id):
    rid=request.session['rid']


    ob=response_table.objects.get(id=id)
    ob.status="Rejected"
    ob.save()
    print(ob,"==============")
    print(ob,"==============")
    ob=request_table.objects.get(id=rid)
    ob.status='pending'
    ob.save()
    return HttpResponse("<script>alert('Accepted');window.location='/view_det/"+str(rid)+"#get-started'</script>")


def predict_request(request):
    ob=blood_bank_table.objects.get(LOGIN__id=request.session['lid'])

    obr=request_table.objects.filter(HOSPITAL__id=ob.HOSPITAL.id).order_by('date')
    d=[]
    for i in obr:
        if str(i.date) not in d:
            d.append(i.date)
    resultlist=[]
    obb=blood_table.objects.all()
    for i in obb:
        r=[i.bloodgroup]
        row=[]
        try:
            for j in d:
                obr = request_table.objects.filter(HOSPITAL__id=ob.HOSPITAL.id,date=j,blood__id=i.id)
                row.append(len(obr))

            x = []
            y = []
            for j in range(len(row)):
                x.append(j + 1)
                y.append(row[j])

            data = {
                'Time': x,  # [1, 2, 3, 4, 5, 6],
                'Value': y  # [10, 12, 14, 16, 18, 20]
            }

            # Create a DataFrame from the data
            df = pd.DataFrame(data)

            # Separate the independent variable (X) and dependent variable (y)
            X = df[['Time']]
            y = df['Value']

            # Create and train the linear regression model
            model = LinearRegression()
            model.fit(X, y)

            # Make predictions for future time points (e.g., forecasting for time = 7)
            future_time = len(X) + 2
            predicted_value = str(model.predict(np.array([[future_time]]))[0]).split('.')[0]
            r.append(predicted_value)
            resultlist.append(r)
        except:
            r.append("NA")
            resultlist.append(r)
    return render(request,"bldpredicty.html",{"val":resultlist})

def send(request):
    ob = request_table.objects.all()
    return render(request, "view request for blood.html", {'val': ob})


def viewusers(request):
    ob=user_table.objects.all()
    return render(request, "view users.html",{'val':ob})
def viewuserssearch(request):
    name= request.POST['textfield']
    ob=user_table.objects.filter(firstname__icontains=name)
    return render(request, "view users.html",{'val':ob})
# @login_required(login_url='/')
# def log(request):
#     uname=request.POST['textfield']
#     pwd=request.POST['textfield2']
#     print(uname)
#     return HttpResponse(uname)




def hs_send_blood_request(request):
    var=blood_table.objects.all()
    a=blood_bank_table.objects.all()
    ob=request_table.objects.filter(HOSPITAL__LOGIN__id=request.session['lid']).order_by('-id')
    return render(request,'hs_send_blood_request.html',{'data':var,'a':a,'ob':ob})

###############################webservice###################


# def and_logincode(request):
#     print(request.POST)
#     Username = request.POST['username']
#     Password = request.POST['password']
#     try:
#         ob = login_table.objects.get(username=Username, password=Password,type="user")
#         if ob is None:
#             data={"task":"invalid"}
#         else:
#             data = {"task": "ok","lid":ob.id}
#         return JsonResponse(data)
#     except:
#
#         data = {"status": "invalid"}
#         return JsonResponse(data)



def and_logincode(request):
    username=request.POST['username']
    password=request.POST['password']

    var=login_table.objects.filter(username=username,password=password)
    if var.exists():
        var2 = login_table.objects.get(username=username, password=password)
        if var2.type=='user':
            return JsonResponse({'status': 'ok', 'lid': str(var2.id), 'type': var2.type})


        else:
            return JsonResponse({'status': 'not ok'})
    else:
        return JsonResponse({'status': 'not ok'})

def viewbld(request):
    ob=blood_table.objects.all()
    list=[]
    for i in ob:
        data={'blood':i.bloodgroup,'id':i.id}
        list.append(data)
    print(list)
    return JsonResponse({"data":list})

def userreg(request):
    fname=request.POST['fname']
    lname=request.POST['lname']
    age=request.POST['age']
    gender = request.POST['gender']
    place = request.POST['place']
    post = request.POST['post']
    pin = request.POST['pin']
    phoneno = request.POST['phone']
    email = request.POST['email']
    username = request.POST['uname']
    password = request.POST['pswd']
    bld = request.POST['blood']

    ob=login_table()
    ob.username=username
    ob.password=password
    ob.type="user"
    ob.save()
    obu=user_table()
    obu.firstname = fname
    obu.lastname = lname
    obu.age = age
    obu.gender = gender
    obu.place = place
    obu.post = post
    obu.pin = pin
    obu.phonno =phoneno
    obu.email =email
    obu.LOGIN=ob
    obu.BLOOD=blood_table.objects.get(id=bld)
    obu.save()
    return JsonResponse({"task":"ok"})


#
# def viewhos(request):
#     list=[]
#     ob=hospital_table.objects.all()
#     for i in ob:
#         data = {
#             'name': i.name,
#             'address': i.place,
#             'phone': i.phonno,
#             'loc': str(i.latitude)+","+str(i.longitude),
#             'id': i.id
#         }
#         list.append(data)
#     return JsonResponse({"data":list})





def viewhos(request):
    var=hospital_table.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'name':i.name,'place':i.place,'post':i.post,'pin':str(i.pin),'city':i.city,'phonno':str(i.phonno)})
    return JsonResponse({'status':'ok','data':l})



def sendresponse(request):
    REQUEST_id=request.POST['rqst']
    USER_id=request.POST['usr']
    date = request.POST['dte']
    ob=response_table()
    ob.REQUEST=response_table.objects.get(id=REQUEST_id)
    ob.date=date
    ob.status='Donated'
    ob.USER=user_table.objects.get(LOGIN__id=USER_id)
    ob.save()
    return JsonResponse({"task":"ok"})

def and_comp(request):
    complaint = request.POST['complaint']
    HOSPITAL_id = request.POST['logid']
    lid = request.POST['lid']
    ob = complaint_table()
    ob.complaint = complaint
    ob.replay = "pending"
    ob.date = datetime.today()
    ob.HOSPITAL=hospital_table.objects.get(id=HOSPITAL_id)
    ob.USER=user_table.objects.get(LOGIN__id=lid)
    ob.save()
    return JsonResponse({"task":"ok"})

def sendfeed(request):
    feedback = request.POST['review']
    HOSPITAL_id = request.POST['logid']
    lid = request.POST['lid']
    ob = feedback_table()
    ob.feedback = feedback
    ob.date = datetime.today()
    ob.HOSPITAL = hospital_table.objects.get(id=HOSPITAL_id)
    ob.USER = user_table.objects.get(LOGIN__id=lid)
    ob.save()
    return JsonResponse({"task": "ok"})


def viewhsp(request):
    ob=hospital_table.objects.all()
    list=[]
    for i in ob:
        data={'name':i.name,'id':i.id}
        list.append(data)
    print(list)
    return JsonResponse({"data":list})



def viewreply(request):
    lid=request.POST['lid']
    list=[]
    ob=complaint_table.objects.filter(USER__LOGIN__id=lid).order_by('-id')
    for i in ob:
        row={'complaint':i.complaint,'reply':i.replay,'hos':i.HOSPITAL.name,'date':str(i.date)}
        list.append(row)
        print(list)
    return JsonResponse({'data':list})

#
def view_blood(request):
    # id=request.POST['bid']
    var=blood_table.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'bloodgroup':i.bloodgroup,'date':str(i.date),'details':i.details})
        print(l)
    return JsonResponse({'status':'ok','data':l})

def usersendcomplaint(request):
    lid=request.POST['lid']
    hid=request.POST['hid']
    comp=request.POST['comp']

    var=complaint_table()
    var.USER=user_table.objects.get(LOGIN_id=lid)
    var.HOSPITAL=hospital_table.objects.get(id=hid)
    var.complaint=comp
    var.replay='pending'
    var.date=datetime.now().today().date()
    var.save()
    return JsonResponse({'status':'ok'})

def usersendfeedback(request):
    lid=request.POST['lid']
    hid=request.POST['hid']
    comp=request.POST['comp']

    var=feedback_table()
    var.USER=user_table.objects.get(LOGIN_id=lid)
    var.HOSPITAL=hospital_table.objects.get(id=hid)
    var.feedback=comp
    var.date=datetime.now().today().date()
    var.save()
    return JsonResponse({'status':'ok'})

def user_view_complaints(request):
    lid=request.POST['lid']
    var=complaint_table.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'complaint':i.complaint,'replay':i.replay,'date':i.date,'HOSPITAL':i.HOSPITAL.name})
        print(l)
    return JsonResponse({'status':'ok','data':l})




def view_category(request):
    var=blood_table.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'bloodgroup':i.bloodgroup})

    return JsonResponse({'status': 'ok' ,'data':l})










def reg(request):
    firstname=request.POST['firstname']
    lastname=request.POST['lastname']
    contact=request.POST['contact']
    email=request.POST['email']
    age=request.POST['age']
    gender=request.POST['gender']
    place=request.POST['place']
    post=request.POST['post']
    pin=request.POST['pin']
    BLOOD=request.POST['BLOOD']
    password=request.POST['password']
    confirm=request.POST['confirm']
    # status='Pending'

    # image = request.POST['image']
    # fs1 = base64.b64decode(image)
    # date1 = datetime.now().strftime("%Y%m%d-%H%M%S") + ".jpg"
    #
    # # open(r'C:\Users\GAYATHRI\PycharmProjects\seatAllocation\media\user\\' + date1, 'wb').write(fs1)
    # open(r'C:\Users\GAYATHRI\Pictures\blood donation erattupetta\web 22-3-24\bloodbank\media\\' + date1, 'wb').write(fs1)
    #
    # path1 = "/media/" + date1

    v=login_table.objects.filter(username=email)
    if v.exists():
        return JsonResponse({'status':'not ok'})



    if password==confirm:
        l = login_table()
        l.username = email
        l.password = confirm
        l.type = 'user'
        l.save()

        u=user_table()
        u.LOGIN=l
        u.firstname = firstname
        u.lastname = lastname
        u.phonno = contact
        u.email = email
        u.age = age
        u.gender = gender
        u.place = place
        u.post = post
        u.pin = pin
        u.BLOOD = blood_table.objects.get(id=BLOOD)
        u.status = 'user'
        u.save()
        return JsonResponse({'status':'ok'})




def view_bank(request):
    id=request.POST['bid']

    var=blood_bank_table.objects.filter(HOSPITAL_id=id)
    l=[]
    for i in var:
        l.append({'id':i.id,'name':i.name,'place':i.place,'post':i.post,'pin':i.pin,'phonno':i.phonno,'email':i.email})

    return JsonResponse({'status':'ok','data':l})

def view_profile(request):
    lid=request.POST['lid']
    i=user_table.objects.get(LOGIN_id=lid)
    return JsonResponse({'status':'ok','firstname':i.firstname,'lastname':i.lastname,
                         'age':i.age,'gender':i.gender,'place':i.place,'post':i.post,'pin':i.pin,
                         'phonno':i.phonno,'email':i.email,'BLOOD':i.BLOOD.bloodgroup})

def sendreq(request):
    bloodid=request.POST['bid']
    count=request.POST['count']
    details=request.POST['details']
    HOSPITAL_id=request.POST['hid']
    lid=request.POST['lid']
    ob=request_table()
    ob.blood=blood_table.objects.get(id=bloodid)
    ob.details=details
    ob.date=datetime.today()
    ob.count=count
    ob.status='pending'
    ob.HOSPITAL=hospital_table.objects.get(id=HOSPITAL_id)
    ob.USER=user_table.objects.get(LOGIN__id=lid)
    ob.save()
    return JsonResponse({"task":"ok"})


def view_blood_group(request):
    var=blood_table.objects.all()
    l=[]
    for i in var:
        l.append({'id':i.id,'bloodgroup':i.bloodgroup})
    return JsonResponse({"status":"ok",'data':l})



def user_sed_request(request):
    bloodid = request.POST['bid']
    count = request.POST['count']
    details = request.POST['details']
    HOSPITAL_id = request.POST['hid']
    lid = request.POST['lid']

    ob = request_table()
    ob.blood = blood_table.objects.get(id=bloodid)
    ob.details = details
    ob.date = datetime.today()
    ob.count = count
    ob.status = 'pending'
    ob.HOSPITAL = hospital_table.objects.get(id=HOSPITAL_id)
    ob.USER = user_table.objects.get(LOGIN__id=lid)
    ob.save()
    return JsonResponse({"status":"ok"})




def view_user_blood_request(request):
    lid=request.POST['lid']
    var=request_table.objects.filter(USER__LOGIN_id=lid)
    l=[]
    for i in var:
        l.append({'id':i.id,'blood':i.blood.bloodgroup,'details':i.details,'date':i.date,'count':i.count,'status':i.status,
                  'HOSPITAL':i.HOSPITAL.name})
        print(l)
    return JsonResponse({"status":"ok",'data':l})


def viewresponse(request):
    lid=request.POST['lid']
    print(lid)
    list=[]
    ob=response_table.objects.filter(REQUEST__USER__LOGIN__id=lid)
    for i in ob:
        row={'blood':i.REQUEST.blood.bloodgroup,'hospital':i.REQUEST.HOSPITAL.name,'reqdate':str(i.REQUEST.date),'resdate':str(i.date),'response':i.status,'count':i.REQUEST.count,'id':i.REQUEST.id}
        list.append(row)
    print(list)
    return JsonResponse({'data':list})

def dltreq(request):
    rid=request.POST['rid']
    ob=request_table.objects.get(id=rid)
    ob.delete()
    return JsonResponse({'task':"ok"})

def userrequest(request):
    lid=request.POST['lid']
    ob=request_table.objects.filter(status="pending").exclude(USER__LOGIN__id=lid).order_by('-id')
    list = []
    for i in ob:
        row={'blood':i.blood.bloodgroup,'reqdate':str(i.date),'count':i.count,'id':i.id,'name':i.USER.firstname+" "+i.USER.lastname,'phn':i.USER.phonno,'plc':i.USER.place,'id':i.id}
        list.append(row)
    print(list)
    return JsonResponse({'data':list})