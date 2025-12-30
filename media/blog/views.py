from django.shortcuts import render, get_object_or_404 
from .models import Post

# Create your views here.
def index(request):
      posts = Post.objects.order_by('-created_at')
      return render(request, 'blog/index.html',{'posts': posts})

def post_detail(request, slug):
      post = get_object_or_404(Post, slug=slug)  # Fetch post by slug or return 404, preventing errors/crash
      return render(request, 'blog/post_detail.html', {'post': post})



