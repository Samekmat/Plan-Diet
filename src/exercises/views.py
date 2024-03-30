from django.core.paginator import PageNotAnInteger, EmptyPage, Paginator
from django.shortcuts import render
from django.views import View

from exercises.models import Exercise


class ExerciseView(View):
    def get(self, request, id):
        exercise = Exercise.objects.get(pk=id)
        return render(request, 'exercises/exercise.html', {'exercise': exercise})


class ExerciseListView(View):
    def get(self, request):
        exercises = Exercise.objects.all()
        paginator = Paginator(exercises, 18)
        page = request.GET.get('page', 1)
        try:
            pages = paginator.page(page)
        except PageNotAnInteger:
            pages = paginator.page(1)
        except EmptyPage:
            pages = paginator.page(paginator.num_pages)

        return render(request, 'exercises/exercise_list.html', {'exercises': exercises, 'pages': pages})
