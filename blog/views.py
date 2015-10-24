from django.shortcuts import render
from django.utils import timezone
from .models import Postear
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect

def listado_post(request):
    posts = Postear.objects.filter(fecha_publicacion__lte=timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listado_post.html', {'posts': posts})

def detalle_post(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    return render(request, 'blog/detalle_post.html', {'post': post})

def post_nuevo(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_post', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/editar_post.html', {'form': form})

def editar_post(request, pk):
    post = get_object_or_404(Postear, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.autor = request.user
            post.save()
            return redirect('blog.views.detalle_post', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/editar_post.html', {'form': form})
