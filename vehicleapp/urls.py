from django.urls import path
from . import views
     


urlpatterns = (
    path('', views.index, name="index"),
    path('register/', views.register, name="register"),
    path('admin_home/', views.admin_home, name="admin_home"),
    path('mechhome/', views.mechanichome, name="mechanichome"),
    path('user_home/', views.user_home, name="user_home"),
    path('user_regi/', views.reg_user, name="user_regi"),
    path('login/', views.login, name="login"),
    path('add/', views.add, name="add"),
    path('viewuser/', views.viewuser, name="viewuser"),
    path('update/<int:id>', views.update, name="update"),
    path('delete/<int:id>', views.delete, name="delete"),
    path('viewmechanics/', views.viewmechanics, name="viewmechanics"),
    path('search/', views.search, name="search"),
    path('search_viewmechanics/', views.search_viewmechanics, name="search_viewmechanics"),
    path('request_user/<int:id>', views.request_user, name="request_user"),
    path('send/', views.send, name="send"),
    path('viewrequests/', views.viewrequests, name="viewrequests"),
    path('viewrequests1/', views.viewrequests1, name="viewrequests1"),
    path('reply1/', views.reply1, name="reply1"),
    path('mechreply/', views.mechreply, name="mechreply"),
    path('msgs/<int:pk>',views.msgs,name="msgs"),
    # path('msgs1/<int:pk>', views.msgs1, name="msgs1"),
    path('view_status/', views.view_status, name="view_status"),
    path('update_status/', views.update_status, name="update_status"),
    path('reply/<int:id>', views.reply, name="reply"),
    path('adminreply/', views.adminreply, name="adminreply"),
    path('sendmail/<int:id>', views.sendmail, name="sendmail"),
    path('user_profile/<int:pk>', views.user_profile, name="user_profile"),
    path('mech_profile/<int:pk>', views.mech_profile, name="mech_profile"),
    path('search1/', views.search1, name="search1"),
    path('mech_request/<str:username>', views.mech_request, name="mech_request"),
    path('feedback/', views.feedback, name="feedback"),
    path('pdf/', views.pdf, name="pdf"),
    path('viewfeedback/', views.viewfeedback, name="viewfeedback"),

    #path('changepass/<int:id>',views.changepass,name="changepass"),

)