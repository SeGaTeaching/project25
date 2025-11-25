from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .forms import MovieForm
from .models import Movie
from django.contrib.auth.models import User

# Create your views here.

# 1. READ (Nur eigene Filme sehen)
@login_required
def movie_list(request):
    if request.user.is_authenticated:
        movies = Movie.objects.filter(created_by=request.user)
    else:
        movies = []
    return render(request, 'movies/movie-list.html', {'movies': movies})

# 1.1 READ DETAIL (NEU)
@login_required
def movie_detail(request, pk):
    # Nur anzeigen, wenn der Film mir gehört
    movie = get_object_or_404(Movie, pk=pk, created_by=request.user)
    return render(request, 'movies/movie-detail.html', {'movie': movie})

# 2. CREATE (Film dem User zuweisen)
@login_required
def movie_create(request):
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            # WICHTIG: commit=False erstellt das Objekt im Speicher, schreibt aber noch nicht in die DB
            movie = form.save(commit=False)
            # Wir setzen den Besitzer manuell auf den aktuell eingeloggten User
            if request.user.is_authenticated:
                movie.created_by = request.user
            else:
                admin = User.objects.filter(is_superuser=True).first()
                # admin = get_object_or_404(User, pk=1)
                movie.created_by = admin
            # Jetzt erst endgültig speichern
            movie.save()
            return redirect('movies:list')
    
    form = MovieForm()
    
    return render(request, 'movies/movie-form.html', {
        'form': form, 
        'title': 'Neuen Film anlegen'
    })
    
# 3. UPDATE (Nur eigene Filme bearbeiten)
@login_required
def movie_edit(request, pk):
    # Sicherheits-Check: Wir suchen den Film UND prüfen gleichzeitig, ob er dem User gehört.
    # Wenn ein anderer User die ID in der URL eingibt, bekommt er einen 404 Fehler.
    movie = get_object_or_404(Movie, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES, instance=movie)
        if form.is_valid():
            form.save()
            return redirect('movies:detail', pk=movie.id)
    else:
        form = MovieForm(instance=movie)
    
    return render(request, 'movies/movie-form.html', {
        'form': form,
        'title': f"{movie.title} bearbeiten"
    })
    

# 4. DELETE (Nur eigene Filme löschen)
@login_required
def movie_delete(request, pk):
    movie = get_object_or_404(Movie, pk=pk, created_by=request.user)
    
    if request.method == 'POST':
        movie.delete()
        return redirect('movies:list')
    
    return render(request, 'movies/delete-confirm.html', {
        'movie': movie
    })