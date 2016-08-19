from django.shortcuts import render
from django.utils import timezone
from django.shortcuts import render, get_object_or_404
from django.shortcuts import redirect
from .forms import PostForm
from .models import Post

# Create your views here.
def post_list(request):
    posts = Post.objects.filter(data__lte=timezone.now()).order_by('-id')
    return render(request, 'financeiro/post_list.html', {'posts': posts})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'financeiro/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.usuario = request.user
            post.data = timezone.now()
            post.save()
            return redirect('financeiro.views.post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'financeiro/post_edit.html', {'form': form})