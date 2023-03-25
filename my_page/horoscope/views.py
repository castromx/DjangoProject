from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse



# Create your views here.


zodiac_dict = {
    'Aries': 'Овен - перший знак зодіаку, планета Марс (з 21 березня по 20 квітня).',
    'Taurus': 'Телець - другий знак зодіаку, планета Венера (з 21 квітня по 21 травня).',
    'Gemini': 'Близнюки - третій знак зодіаку, планета Меркурій (з 22 травня по 21 червня).',
    'Cancer': 'Рак - четвертий знак зодіаку, Місяць (з 22 червня по 22 липня).',
    'Leo': "Лев - п'ятий <i>знак зодіаку, Сонце</i> (з 23 липня по 21 серпня)",
    'Virgio': "Дiва - шостий знак зодіаку, планета Меркурій (з 22 серпня по 23 вересня).",
    'Libra': 'Ваги - сьомий знак зодіаку, планета Венера (з 24 вересня по 23 жовтня).',
    'Scorpio': "Скорпіон - восьмий знак зодіаку, планета Марс (з 24 жовтня по 22 листопада)",
    'Saggittarius': "Стрілець - дев'ятий знак зодіаку, планета Юпітер (з 23 листопада по 22 грудня).",
    'Capricorn': 'Козеріг - десятий знак зодіаку, планета Сатурн (з 23 грудня по 20 січня).',
    'Aquarius': 'Водолій - одиннадцятий знак зодіаку, планети Уран і Сатурн (з 21 січня по 19 лютого).',
    'Pisces': 'Риби - дванадцятий знак зодіаку, планети Юпітер (з 20 лютого по 20 березня).'
}


def get_yyyy_converters(request, sign_zodiac):
    return HttpResponse(f'Ви передали число з чотирьох чисел - {sign_zodiac}')


def get_my_float_converters(request, sign_zodiac):
    return HttpResponse(f'Ви передали раціональне число - {sign_zodiac}')


def get_my_date_converters(request, sign_zodiac):
    return HttpResponse(f'Ви передали дату типу - {sign_zodiac}')


def index(request):
    zodiacs = list(zodiac_dict)
    #f"<li><a href='{redirect_path}'>{sign}</a></li>"
    context = {
        'zodiacs' : zodiacs,
        'zodiac_dict': zodiac_dict
    }
    return render(request, 'horoscope/index.html', context)





def get_info_about_sign_zodiac(request, sign_zodiac: str):
    description = zodiac_dict.get(sign_zodiac, 'Неправильний знак зодіаку')

    data = {

        'description': description,
        'sign': sign_zodiac,
        'zodiacs': zodiac_dict


}
    return render(request, 'horoscope/info_zodiac.html', context=data)

def get_info_about_sign_zodiac_by_numer(request, sign_zodiac: int):
    zodiacs = list(zodiac_dict)
    if sign_zodiac > len(zodiacs):
        return HttpResponseNotFound(f'Був переданий неправильний порядковий номер - {sign_zodiac}')
    name_zodiac = zodiacs[sign_zodiac - 1]
    redirect_url = reverse("horoscope-name", args=(name_zodiac, ))
    return HttpResponseRedirect(redirect_url)
