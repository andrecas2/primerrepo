from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404


def listado(request):
    posts = Post.objects.filter(fecha_publicacion__lte = timezone.now()).order_by('fecha_publicacion')
    return render(request, 'blog/listar.html', {'posts': posts})
