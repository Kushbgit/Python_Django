from django.urls import path
from .views import *

urlpatterns = [
    path("stu_info/<int:pk>",Student_detail,name='name'),
    path("stu_list/",student_list,name='student_list')
    #                                                                                                                                               path("student_api/",student_api,name='student_api'),
]