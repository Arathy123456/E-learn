# from _pydatetime import timedelta
# from datetime import timezone

from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

# from .forms import CourseForm
from .models import Userregistrations, course_registration, registration1, course_data, payment, trainer_reg, \
    certificates, placementreg,interview_reg


# from.models import *

def indexpage(request):
    return render(request, 'indexpage1.html')


def user_registration(request):
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        photo = request.FILES.get('image1')

        password1 = request.POST['pass1']
        password2 = request.POST['pass2']

        # Perform basic validation
        if password1 == password2:
            if User.objects.filter(username=username):
                messages.error(request, 'Username Exists! Try another Username...')
                return redirect('user_registration')
            else:
                if User.objects.filter(email=email):
                    return HttpResponse(request, 'Email Is Already Taken! Try Another One... ')
                    return redirect('user_registration')
                else:
                    user = User.objects.create_user(username=username, email=email, password=password1)
                    user.save()
                    # reg = Userregistrations()
                    # reg.username = username
                    # reg.email = email
                    # reg.Password = password1
                    # reg.save()
                    data = Userregistrations.objects.create(username=username, email=email, Password=password1,
                                                            user_photo=photo)
                    data.save()
                    # log(request,user)
                    messages.success(request, 'You have successfully Registered')
                    return redirect(log)
        else:
            print('Password Did Not Matched!...')
            return redirect('user_registration')
    else:
        return render(request, 'Userregistration.html')


def log(request):
    #   if request.user.is_authenticated:
    #      messages.warning(request, "You are already logged in")
    #     return redirect(user_home)
    if request.method == 'POST':
        name = request.POST.get('user')
        passwd = request.POST.get('pass')
        user = authenticate(username=name, password=passwd)
        list = ["learning", "learn"]

        if user is not None:
            login(request, user)
            messages.success(request, 'Logged in Successfully!')
            return redirect(user_home)
        elif name == list[0] and passwd == list[1]:
            return redirect(admin_log)
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect(log)
    return render(request, 'login.html')


def user_home(request):
    return render(request, 'userhome.html')


def python_home(request):
    return render(request, 'pythonhome.html')


def course(request):
    if request.user.is_authenticated:
        return render(request, 'coursereg1.html')
    else:
        return redirect(log)


def flutter_home(request):
    return render(request, 'flutterhome.html')


def digital_home(request):
    return render(request, 'digitalhm.html')


def mearnstack_home(request):
    return render(request, 'mearnhm.html')


def datascience(request):
    return render(request, 'datasciencehm.html')


def registration_course(request):
    if request.method == 'POST':
        user = request.user.username
        full_name = request.POST['names']
        gmail = request.POST['uemail']
        contact = request.POST['phone']
        courses = request.POST['course']
        quali = request.POST['quali']
        # image = request.FILES.get('img')
        data = registration1.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,
                                            Qualification=quali)
        data.save()
        return redirect('booking')

    return render(request, 'coursereg1.html')


def booking(request):
    bookings = registration1.objects.get(name=request.user)
    if request.method == 'POST':

        user_id = request.user.id
        user_name = request.user.username
        user1 = request.POST['uname']

        user = User.objects.filter(id=user_id)
        prof = registration1.objects.filter(name=user_name)
        book = registration1.objects.get(id=prof)
        # booked = registration1.objects.get(course=)
        #      booked = registration1.objects.get(course=course_data.course_name)
        if prof:
            return render(request, 'coursepay.html', {'bookings': bookings})

    return render(request, 'coursepay.html', {'bookings': bookings})


def payment_details(request):
    if request.method == 'POST':
        full_name = request.POST['names']
        gmail = request.POST['uemail']
        contact = request.POST['phone']
        courses = request.POST['course']
        amount = request.POST['amount']
        pay = request.POST['pay']
        data = payment.objects.create(name=full_name, gmail=gmail, phoneno=contact, course=courses,
                                      amount=amount, payment_id=pay)
        data.save()
    return render(request, 'coursepay.html')


def three_day(request):
    try:
        user_detail = registration1.objects.get(name=request.user)
        return render(request, '3daytrial.html', {'user_detail': user_detail})
    except registration1.DoesNotExist:
        return render(request, '3dayregister.html')


def trainer_registration(request):
    if request.method == 'POST':
        name = request.POST['name']
        gmail = request.POST['mail']
        contact = request.POST['phone']
        photo = request.FILES['image']
        password1 = request.POST['pass']
        existing_users = trainer_reg.objects.filter(name=name)

        if existing_users.exists():
            messages = "user name is already exists"
        else:

            trainer = trainer_reg.objects.create(name=name, email=gmail, phoneno=contact, trainerphoto=photo,
                                                 password=password1)
            trainer.save()
            # messages = "Successfully Registered"
            return redirect('trainer_login')

    return render(request, 'trainerreg.html')


def trainer_login(request):
    if request.method == 'POST':
        name = request.POST['name']
        password = request.POST['pass']
        user = trainer_reg.objects.filter(name=name, password=password)

        if user is not None:
            # slogin(request, user)
            messages.success(request, 'Logged in Successfully!')

            return redirect('trainer_home')
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('trainer_login')

    return render(request, 'trainerlog.html')


def trainer_home(request):
    return render(request, 'trainerhome.html')


def videocall(request):
    user_name = request.user.username
    return render(request, 'WEB_UIKITS.html')


def logout1(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect(indexpage)


# Create your views here.
def user_video_access(request):
    try:
        user_detail = payment.objects.get(name=request.user)
        return render(request, 'WEB_UIKITS.html')
    except payment.DoesNotExist:
        messeges = "you have not booked  course"
        return redirect(user_profile)


def user_profile(request):
    # bookings = Userregistrations.objects.get(username=request.user)
    try:
        bookings = registration1.objects.get(name=request.user)
        if bookings:
            return render(request, 'Userprofile.html', {'bookings': bookings})
        else:
            return redirect(user_home)

    except:
        return redirect(user_home)


def admin_log(request):
    return render(request, 'admin1.html')


def interview_register1(request):
    lock1 = payment.objects.filter(status='Unlock')
    if lock1:
        return render(request, 'interview register.html')
    else:
        return redirect('user_profile')


def resume(request):
    lock1 = payment.objects.filter(status='Unlock')
    if lock1:
        return render(request, 'WEB_UIKITS.html')
    else:
        return redirect('user_profile')


def certificate1(request):
    if request.method == 'POST':
        name = request.POST['names']
        sslc = request.POST.get('image1')
        plus2 = request.POST.get('plus2')
        degree = request.POST.get('degree')
        certifi = certificates.objects.create(name=name, sslc=sslc, plus_two=plus2, degree=degree)
        certifi.save()
    return render(request, 'certificates.html')


def interview_section_video(request):
    try:
        user_detail = interview_reg.objects.get(name=request.user)
        return render(request, 'WEB_UIKITS.html')
    except interview_reg.DoesNotExist:

        return redirect(interview_register1)


def viewuser(request):
    d = Userregistrations.objects.all()
    return render(request, 'adminuserview.html', {'data': d})


def viewreg(request):
    d = registration1.objects.all()
    return render(request, 'adminregview.html', {'data': d})


def viewpay(request):
    d = payment.objects.all()
    return render(request, 'adminbooked.html', {'data': d})


def trainer_view(request):
    d = trainer_reg.objects.all()
    return render(request, 'trainerview.html', {'data': d})


def certificates_view(request):
    c = certificates.objects.all()
    return render(request, 'admin_certificate_view.html', {'data': c})


def three_day_admin(request):
    if payment.amount == 500:
        d = payment.objects.get(amount=500)
        return render(request, 'admin_3day'.html, {'data': d})
    return render(request, 'admin_3day.html')


def destroy(request, id):
    try:
        user_detail = payment.objects.get(id=id)
        user_detail.delete()
    except payment.DoesNotExist:
        return redirect(viewpay)


def placement(request):
    lock1 = payment.objects.filter(status='Unlock')
    if lock1:
        return render(request, 'placement.html')
    else:
        return redirect('user_profile')


#   try:
#      user_detail = payment.objects.get(name=request.user)
#      return render(request, 'placement.html')
#  except payment.DoesNotExist:
#     return redirect(user_profile)


def placementpg(request):
    return render(request, 'placementreg.html')


def placement_reg(request):
    if request.method == 'POST':
        full_name = request.POST['name']
        gmail = request.POST['mail']
        contact = request.POST['phone']
        cv = request.FILES['image']
        pos = request.POST['position']
        quali = request.POST['quali']
        data = placementreg.objects.create(name=full_name, gmail=gmail, phoneno=contact, cv=cv, position=pos,
                                           Qualification=quali)
        data.save()
    return render(request, 'placementreg.html')


def viewplacement(request):
    d = placementreg.objects.all()
    return render(request, 'adminplacement.html', {'data': d})


def unlock_viewpay(request, id):
    payment.objects.filter(pk=id).update(status='Unlock')
    return redirect(videocall)


def viewpay(request):
    d = payment.objects.all()
    return render(request, 'adminbooked.html', {'data': d})


def del_viewpay(request, id):
    payment.objects.filter(pk=id).delete()
    return redirect(viewpay)


def unlock_viewpay(request, id):
    payment.objects.filter(pk=id).update(status='Unlock')
    # payment.save()
    return redirect(viewpay)


def lock_view(request):
    try:
        user1 = payment.objects.get(name=request.user)
        lock1 = payment.objects.filter(status='Unlock')
        if lock1:
            return redirect('videocall')
        else:
            return redirect('user_profile')
    except:
        return redirect('user_profile')


def admin_lock(request, id):
    payment.objects.filter(pk=id).update(status='Lock')
    return redirect(viewpay)

def interview_register(request):
    if request.method == 'POST':
        full_name = request.POST['names']
        gmail = request.POST['uemail']
        contact = request.POST['phone']
        course= request.POST['course']
        quali = request.POST['quali']
        data =interview_reg.objects.create(name=full_name, email=gmail, phoneno=contact,course=course,
                                           Qualification=quali)
        data.save()
    return render(request,'interview register.html')