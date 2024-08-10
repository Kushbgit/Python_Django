
from django.urls import path
from App import views

urlpatterns = [
    path('homepage/' ,views.homepage, name='homepage'),
    path('register/', views.Register,name='register'),
    #path('registerdata/', views.Registerdata, name='register'),
    path('aboutpage/' ,views.about, name='aboutpage'),
    path('contact/' ,views.contact, name='contact'),
    # path('registered/' ,views.registered, name='registered'),
    path('landing/' ,views.landing, name='landing')
]
