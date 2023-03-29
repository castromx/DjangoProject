from django.shortcuts import render, get_object_or_404
from django.db.models import F, Sum, Max, Min, Count, Avg , Value

# Create your views here.
from .models import Movie

# Ф-я для відображення всіх елементів бд (фільмів)
def show_all_movie(request):
	# тут використав цикл for для швидкого додавання данних в бд (коли додавав slug щоб кожен запис не перезаписувати, використав цикл)
	# for movie in movies:
	#в змінній movie ми будемо отримувати силки на наші записи
		# movie.save()
		#і все до них спокійно застосовувати метод .save
	# додав вичисляючі поля в бд за допомогою анотації
    movies = Movie.objects.annotate(
    	true_bool=Value(True),
    	false_bool=Value(False),
    	int_field=Value(123),
    	str_field=Value('hello'),
    	new_budget=F('budget')+100,
    	dob_rating_year=F('rating')*F('year')
    	)
    # тут додав ф-ю агрегації
    agg = movies.aggregate(Avg('budget'), Max('rating'), Min('rating'))
    return render(request, 'movie_app/all_movies.html', {
		'movies':movies,
        'agg':agg,
        'total':movies.count()#це приклад ще одного застосування агрегації
	})

# Ф-я для відображення 1 елементу з бд (фільму)
def show_one_movie(request, slug_movie : str):
	movie = get_object_or_404(Movie, slug=slug_movie)
	return render(request, 'movie_app/one_movie.html', {
		'movie':movie
	})
