from django.shortcuts import render
from django.utils import timezone
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(data__lte=timezone.now()).order_by('data')
    return render(request, 'financeiro/post_list.html', {'posts': posts})