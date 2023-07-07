from django.http import HttpResponse
from django.shortcuts import render, redirect

from .forms import MovieUpdateForm
from . models import movielist

# Create your views here.
def index(request):
    movies=movielist.objects.all()
    context={
        'movielist':movies
    }
    return render(request,'index.html',context)
def detail(request,movie_id):
    movieDetails=movielist.objects.get(id=movie_id)
    return render(request,'detail.html',{'movieDetails':movieDetails})
def add_movie(request):
    if request.method=="POST":
        name=request.POST['moviename']
        desc = request.POST['desc']
        year = request.POST['year']
        img = request.FILES['img']
        movie=movielist(name=name,desc=desc,year=year,img=img)
        movie.save()
        return redirect('/')
    return render(request,'add_movie.html')

def update_movie(request,movie_id):
    movie=movielist.objects.get(id=movie_id)
    form=MovieUpdateForm(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request, 'update_movie.html',{'form':form,'movie':movie})

def delete_movie(request,movie_id):
    if request.method == "POST":
       movie = movielist.objects.get(id=movie_id)
       movie.delete()
       return redirect('/')
    return render(request, 'delete_movie.html')