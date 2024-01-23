from django.shortcuts import render , redirect , HttpResponseRedirect
from .models import *
from datetime import *
from django.contrib import messages
from django.core.mail import send_mail
from django.conf import settings
def index(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        check = "false"
        try:
            user = students.objects.get(email=email, password=password)
            if user:
                check = "true"
                send_mail("New log in" , "There is a new log in success to your account in 'Quiz app'" , settings.EMAIL_HOST_USER , [email], fail_silently=False)
                return HttpResponseRedirect(f'/Exam/?student_email={email}')
        except students.DoesNotExist:
                check = "false"
                send_mail("New log in" , "There is a new log in Failed to your account in 'Quiz app'" , settings.EMAIL_HOST_USER , [email], fail_silently=False)
                return render(request, 'Log_in_student.html', {'check': check})
    return render(request, 'Log_in_student.html')
def teacher_log_in(request):
    if request.method == 'POST':
       name = request.POST.get('username')
       password = request.POST.get('password')
       check = "false"
       try:
            user = teacher.objects.get(name = name, password = password)
            if user:
                check = "true"
                return redirect(addquistionspage)
       except teacher.DoesNotExist:
                check = "false"
                return render(request, 'Log_in_teacher.html', {'check': check})
    return render(request , 'Log_in_teacher.html')
def addquistionspage(request):
    all_student = students.objects.all()
    if request.method == 'POST':
        try:
            delete_i = request.POST.get('delete')
            if delete_i == "delete":
                quistions.objects.all().delete()
                return render(request , 'add_quistions.html' , {'proccess': 'deleteall'})
            else:
                quistion = request.POST.get('q1')
                answer1 = request.POST.get('choose1')
                answer2 = request.POST.get('choose2')
                answer3 = request.POST.get('choose3')
                right_answer = request.POST.get('rightchoose')
                data = quistions(quistion = quistion , first_answer = answer1, second_answer = answer2 , third_answer = answer3 , right_answer = right_answer)
                try:
                    data.save()
                    return render(request , 'add_quistions.html' , {'proccess': 'addprocess'})
                except:
                    return render(request , 'add_quistions.html' , {'proccess': 'notadd'})
        except:
            return render(request, 'add_quistions.html', {'proccess': 'false'})
    return render(request , 'add_quistions.html' ,{'proccess': ' ' , 'students' : all_student})
def doexam(request):
    all_quistions = quistions.objects.all()
    email = request.GET.get('student_email')
    user = students.objects.filter(email=email).first()
    if request.method == 'POST':
        score = request.POST.get('score')
        user.exam_result = score
        user.save()
    return render(request , 'home.html' , {'quistions':all_quistions , 'user':user})