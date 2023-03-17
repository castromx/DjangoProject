from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound, HttpResponseRedirect
from django.urls import reverse

# Create your views here.



zodiac_dict = {
	'Aries': 'Овен - перший знак зодіаку, планета Марс (з 21 березня по 20 квітня).',
	'Taurus': 'Телець - другий знак зодіаку, планета Венера (з 21 квітня по 21 травня).',
	'Gemini': 'Близнюки - третій знак зодіаку, планета Меркурій (з 22 травня по 21 червня).',
	'Cancer': 'Рак - четвертий знак зодіаку, Місяць (з 22 червня по 22 липня).',
	'Leo': "Лев - п'ятий знак зодіаку, Сонце (з 23 липня по 21 серпня)",
	'Virgio': "Дiва - шостий знак зодіаку, планета Меркурій (з 22 серпня по 23 вересня).",
	'Libra': 'Ваги - сьомий знак зодіаку, планета Венера (з 24 вересня по 23 жовтня).',
	'Scorpio': "Скорпіон - восьмий знак зодіаку, планета Марс (з 24 жовтня по 22 листопада)",
	'Saggittarius': "Стрілець - дев'ятий знак зодіаку, планета Юпітер (з 23 листопада по 22 грудня).",
	'Capricorn': 'Козеріг - десятий знак зодіаку, планета Сатурн (з 23 грудня по 20 січня).',
	'Aquarius': 'Водолій - одиннадцятий знак зодіаку, планети Уран і Сатурн (з 21 січня по 19 лютого).',
	'Pisces': 'Риби - дванадцятий знак зодіаку, планети Юпітер (з 20 лютого по 20 березня).'
}



#поки що HTML кодом користуватись не буду, тому використаю теги
def index(request):
	zodiacs = list(zodiac_dict)
	li_elements = ''
	for sign in zodiacs:
		redirect_path = reverse("horoscope-name", args=(sign, ))#тут також реалізував ф-ю reverse
		li_elements += f"<li><a href='{redirect_path}'>{sign}</a></li>"#опрацюємо кожному значенню відповіду силку
		#<li> - тег для таблиці, <a href> -  тег для посилання який ми беремо з ф-ї reverse для імені з словника zodiac_dict
	#запхаємо це в список order list <ol> - тегами
	response = f"""
	<ol>
	    {li_elements}
	</ol>
	"""
	return HttpResponse(response)

#параметри з динамічного роута, наша ф-я також приймає
def get_info_about_sign_zodiac(request, sign_zodiac: str):#використовується для відображення сторінки з описом знака зодіаку на основі назви знака (параметр sign_zodiac).
	description = zodiac_dict.get(sign_zodiac, None)
	if description:
		return HttpResponse(f'<h2>{description}</h2>')#також вирішив застосувати теги, та збільшив шрифт тегами для заголовку <h2>
	else:
		return HttpResponseNotFound(f'Невідомий знак зодіаку - {sign_zodiac}')#якщо знак не знайдено, повертається код помилки 404, та самому клінту повідомлення з f-рядка
		

def get_info_about_sign_zodiac_by_numer(request, sign_zodiac: int):#використовується для відображення сторінки з описом знака зодіаку на основі його порядкового номера 
	zodiacs = list(zodiac_dict)
	if sign_zodiac> len(zodiacs):
		return HttpResponseNotFound(f'Був переданий неправильний порядковий номер - {sign_zodiac}')
	name_zodiac = zodiacs[sign_zodiac-1]
	redirect_url = reverse("horoscope-name", args=(name_zodiac, ))#і тут реалізував ф-ю reverse щоб автоматизувати перехід(вона вибудовує нам адрес)
	return HttpResponseRedirect(redirect_url)

