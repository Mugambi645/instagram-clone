from django.shortcuts import render

# Create your views here.
#home view
def index(request):
    return render(request, "home/index.html", {})

class PostCreateView(LoginRequiredMixin, CreateView):
    """
    view class to create post
    """
    model = Post
    fields = "__all__"
    template_name = 'gallery/post_form.html'

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


def post(request, pk):
    """
    View to handle post model
    Args:
    Pk - Primary Key,an unique way to identify an object uniquely in relational database systems
    """
    post = Post.objects.get(pk=pk)
    user = request.user
    form = CommentForm()
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = Comment(author= user,content=form.cleaned_data["description"],post=post)
            comment.save()

    comments = Comment.objects.filter(post=post).order_by('-date_posted')
    context = {
        "post": post,
        "comments": comments,
        "form": form,
    }

    return self.get(self, request, pk, context)


