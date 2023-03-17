from django.urls import path
from . import views


#додав можливість звератись за цифрою і іменем(пізніше силка)
urlpatterns = [
    path('', views.index),#/horoscope/
    #також додав динамічні роути, щоб обробляти роути, в яких деяка частина може змінюватись, і ця частина
    #обробляється автоматично, і переноситься в параметр
    path('<int:sign_zodiac>', views.get_info_about_sign_zodiac_by_numer),
    path('<str:sign_zodiac>', views.get_info_about_sign_zodiac, name='horoscope-name'),#щоб не харкодити, використав ф-ю reverse, а для неї застосував параметр name= в path()

]