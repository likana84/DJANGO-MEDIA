from django.shortcuts import render, get_object_or_404, redirect 
from .models import Post
from .forms import CommentForm

# Create your views here.
def index(request):
      posts = Post.objects.all()
      return render(request, 'blog/index.html',{'posts': posts})

def post_detail(request, slug):
      post = get_object_or_404(Post, slug=slug)  # Fetch post by slug or return 404, preventing errors/crash
      if request.method == 'POST':
            form=CommentForm(request.POST) # Bind data from request to form
            if form.is_valid():
                  comment = form.save(commit=False) # Create comment object but don't save to DB yet
                  comment.post = post  # Associate comment with the current post
                  comment.save()  # Now save the comment to the database
                  return redirect('post_detail', slug=slug)  # Redirect to the same post detail page
      else:
            form = CommentForm()  # Create an unbound form for GET request
                  
      return render(request, 'blog/post_detail.html', {
            'post': post,
            'form': form,})


