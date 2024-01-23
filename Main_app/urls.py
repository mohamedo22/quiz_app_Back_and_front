from django.urls import path
from .views import *

urlpatterns = [
    path('' , index , name='index_page'),
    path('Log_in_teacher/' , teacher_log_in , name= 'teacher_login_page'),
    path('add_quistions/' , addquistionspage , name='addquistions_page'),
    path('Exam/', doexam , name='exam_page')
]
