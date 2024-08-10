from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators import csrf
import io
from rest_framework.parsers import JSONParser

def student_list(req):
    stu = Student.object.all()
    # print ("Stu =", stu )
    # print ("stu.values()=",stu.values())
    # print ("stu.values_list()=",stu.value_list())
    # print ("stu.values_list(col1,col2)=",stu.values_list('name','roll','city'))
    serializer = StudentSerializer(stu,many=True)
    # print("Serializer =",serializer)
    # print(serializer.data)
    # json_data = JSONRenderer().render(serializer.data)
    # print("Json_data =",json_data)
    # return HttpResponse(json_data,content_type='application/json')
  # whenever we send json data from views then "content_type" must be on application/json
    return JsonResponse(serializer.data,safe=False)   