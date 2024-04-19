"""bloodbank URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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

from blood import views

urlpatterns = [
    path('', views.login, name="login"),
     path('addblood', views.addblood, name="addblood"),
    path('adminhome', views.adminhome, name="adminhome"),
    path('approvehospitel', views.approvehospitel, name="approvehospitel"),
    path('accepthospital/<int:id>',views.accepthospital,name='accepthospital'),
    path('rejecthospital/<int:id>',views.rejecthospital,name='rejecthospital'),
    path('blockorunblockhospital', views.blockorunblockhospital, name="blockorunblockhospital"),
    path('bloodbank', views.bloodbank, name="bloodbank"),
    path('hospitalhome', views.hospitalhome, name="hospitalhome"),
    path('hospitalregistration', views.hospitalregistration, name="hospitalregistration"),
    path('Managebloodgroup', views.Managebloodgroup, name="Managebloodgroup"),
    path('Reply', views.Reply, name="Reply"),
    path('requstbloodgroupanddonatefromhospital', views.requstbloodgroupanddonatefromhospital, name="requstbloodgroupanddonatefromhospital"),



    path('searchblood', views.searchblood, name="searchblood"),
    path('sendcomplaintandviewreply', views.sendcomplaintandviewreply, name="sendcomplaintandviewreply"),


    path('sendcomplaint', views.sendcomplaint, name="sendcomplaint"),
    path('sendfeedback', views.sendfeedback, name="sendfeedback"),

    path('sendrequstforblood', views.sendrequstforblood, name="sendrequstforblood"),
    path('Updateblood', views.Updateblood, name="Updateblood"),

    path('Userregistration', views.Userregistration, name="Userregistration"),
    path('userhome', views.userhome, name="userhome"),
    path('viewcomplaint', views.viewcomplaint, name="viewcomplaint"),
    path('viewcomplaints', views.viewcomplaints, name="viewcomplaints"),
    path('viewcomplaintssearch', views.viewcomplaintssearch, name="viewcomplaintssearch"),
    path('ViewFeedback', views.ViewFeedback, name="ViewFeedback"),
    path('ViewFeedbacksearch', views.ViewFeedbacksearch, name="ViewFeedbacksearch"),
    path('viewfeedbacks', views.viewfeedbacks, name="viewfeedbacks"),
    path('aviewcomplaints', views.aviewcomplaints, name="aviewcomplaints"),
    path('ViewsearchFeedback', views.ViewsearchFeedback, name="ViewsearchFeedback"),
    path('viewhospitals/<int:id>', views.viewhospitals, name="viewhospitals"),
    path('viewrequestforblood', views.viewrequestforblood, name="viewrequestforblood"),
    path('viewusers', views.viewusers, name="viewusers"),
    path('viewuserssearch', views.viewuserssearch, name="viewuserssearch"),
    path('searchbloodsearch',views.searchbloodsearch,name='searchbloodsearch'),
    path('login1',views.login1,name='login1'),
    path('hospitalregistrationcode',views.hospitalregistrationcode,name='hospitalregistrationcode'),
    path('updatebloodcode',views.updatebloodcode,name='updatebloodcode'),
    path('bloodregistrationcode',views.bloodregistrationcode,name='bloodregistrationcode'),
    path('regbloodbnk',views.regbloodbnk,name='regbloodbnk'),
    path('addbloodcode',views.addbloodcode,name='addbloodcode'),
    path('sendreplycode',views.sendreplycode,name='sendreplycode'),
    path('Reply/<int:id>',views.Reply,name='Reply'),
    path('blockhospital/<int:id>',views.blockhospital,name='blockhospital'),
    path('unblockhospital/<int:id>',views.unblockhospital,name='unblockhospital'),
    path('Updateblood/<int:id>',views.Updateblood,name='Updateblood'),
    path('deleteblood/<int:id>',views.deleteblood,name='deleteblood'),
    path('approvebloodbank',views.approvebloodbank,name='approvebloodbank'),
    path('acceptbloodbank/<int:id>',views.acceptbloodbank,name='acceptbloodbank'),
    path('rejectbloodbank/<int:id>',views.rejectbloodbank,name='rejectbloodbank'),
    path('logout',views.logout,name='logout'),
    path('sendrequest1/<int:id>', views.sendrequest1, name='sendrequest1'),
    path('view_det/<int:id>', views.view_det, name='view_det'),
    path('sentres/<int:id>', views.sentres, name='sentres'),
    path('reject/<int:id>', views.reject, name='reject'),
    path('accept/<int:id>', views.accept, name='accept'),
    path('sendrequest2', views.sendrequest2, name='sendrequest2'),
    path('viewrequestforblood_bb', views.viewrequestforblood_bb, name='viewrequestforblood_bb'),
    path('sendresponsebb', views.sendresponsebb, name='sendresponsebb'),
    path('predict_request', views.predict_request, name='predict_request'),

    path('hs_send_blood_request', views.hs_send_blood_request, name='hs_send_blood_request'),


    path('and_logincode', views.and_logincode, name='and_logincode'),
    path('userreg', views.userreg, name='userreg'),
    path('viewbld', views.viewbld, name='viewbld'),
    path('view_blood', views.view_blood, name='view_blood'),
    path('viewhos', views.viewhos, name='viewhos'),
    path('viewhsp', views.viewhsp, name='viewhsp'),
    path('sendfeed', views.sendfeed, name='sendfeed'),
    path('viewreply', views.viewreply, name='viewreply'),
    path('and_comp', views.and_comp, name='and_comp'),
    path('sendreq', views.sendreq, name='sendreq'),
    path('viewresponse', views.viewresponse, name='viewresponse'),
    path('dltreq', views.dltreq, name='dltreq'),
    path('userrequest', views.userrequest, name='userrequest'),

    path('usersendcomplaint', views.usersendcomplaint, name='usersendcomplaint'),
    path('user_view_complaints', views.user_view_complaints, name='user_view_complaints'),
    path('usersendfeedback', views.usersendfeedback, name='usersendfeedback'),
    path('view_profile', views.view_profile, name='view_profile'),
    path('view_category', views.view_category, name='view_category'),
    path('reg', views.reg, name='reg'),
    path('view_bank', views.view_bank, name='view_bank'),
    path('user_sed_request', views.user_sed_request, name='user_sed_request'),
    path('view_blood_group', views.view_blood_group, name='view_blood_group'),
    path('view_user_blood_request', views.view_user_blood_request, name='view_user_blood_request'),


]


