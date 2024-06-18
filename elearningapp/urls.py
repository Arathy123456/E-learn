"""Elearn URL Configuration

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
from django.conf.urls.static import static
from django.conf import settings
from .import views

urlpatterns = ([
    path('admin/', admin.site.urls),
    path('',views.indexpage,name='indexpage'),
    path('user_registration',views.user_registration,name='user_registration'),
    path('login',views.log,name='login'),
    path('user_home',views.user_home,name='user_home'),
    path('logout',views.logout1,name='logout'),
    path('course_registration',views.registration_course,name='course_registration'),
    path('python_home',views.python_home,name='python_home'),
    path('course_reg',views.course,name='course_reg'),
    path('booking',views.booking,name='booking'),
    path('flutter',views.flutter_home,name='flutter'),
    path('mearn',views.mearnstack_home,name='mearn'),
    path('digital',views.digital_home,name='digital'),
    path('datascience',views.datascience,name='datascience'),
    path('three_day',views.three_day,name='three_day'),
    path('payment',views.payment_details,name='payment'),
    path('trainer_reg',views.trainer_registration,name='trainer_reg'),
    path('trainer_login',views.trainer_login,name='trainer_login'),
    path('trainer_home',views.trainer_home,name='trainer_home'),
    path('videocall',views.videocall,name='videocall'),
    path('user_video',views.user_video_access,name='user_video'),
    path('user_profile',views.user_profile,name='user_profile'),
    path('admin1',views.admin_log,name='admin1'),
    path('interview',views.interview_register1,name='interview'),
    path('resume',views.resume,name='resume'),
    path('certificates',views.certificate1,name='certificates'),
    path('interview_video',views.interview_section_video,name='interview_video'),
    path('userview',views.viewuser,name='userview'),
    path('viewcourse',views.viewreg,name='viewcourse'),
    path('viewbook', views.viewpay,name='viewbook'),
    path('certificateview',views.certificates_view,name='certificateview'),
    path('3day_admin',views.three_day_admin,name='3day_admin'),
    path('destroy',views.destroy,name='destroy'),
    path('placement',views.placement,name='placement'),
    path('placement_page',views.placementpg,name='placement_page'),
    path('placementreg',views.placement_reg,name='placementreg'),
    path('viewplacement',views.viewplacement,name='viewplacement'),
    path('admin_lock/<id>',views.admin_lock),
    path('unlock1/<id>',views.unlock_viewpay),
    path('reject/<id>',views.del_viewpay),
    path('trainer_view',views.trainer_view,name='trainer_view'),
    path('lock_view',views.lock_view,name='lock_view'),
    path('interview_reg',views.interview_register,name='interview_reg'),


])