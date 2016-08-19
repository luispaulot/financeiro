from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(data__lte=timezone.now()).order_by('-data')
    return render(request, 'financeiro/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'financeiro/post_detail.html', {'post': post})