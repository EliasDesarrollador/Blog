from django.shortcuts import render
from .models import Post 

# Create your views here.

def home (request) :
    posts =  Post.objects.all().order_by('-fecha')
    return render (request, 'posts/home.html', {'posts' :posts})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'posts/post_detail.html', {'post': post})


def post_create(request):
    from .forms import PostForm
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save()
            # redirigir al detalle del post creado
            from django.shortcuts import redirect
            return redirect('post-detail', post.pk)
    else:
        form = PostForm()

    return render(request, 'posts/post_form.html', {'form': form})