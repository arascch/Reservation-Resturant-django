from django.shortcuts import render , get_object_or_404
from .models import Blog , Tag , Category , Comments
from .forms import CommentForm
from django.core.paginator import Paginator


# Create your views here.

def blog_list(request):
    blogs = Blog.objects.all()
    paginator = Paginator(blogs, 2)
    page_number = request.GET.get('page')
    blogs = paginator.get_page(page_number)

    context = {
        "blogs" : blogs,

    }

    return render(request , "blog/blog_list.html" , context)

def blog_detail(request , id):
    blog = Blog.objects.get(id=id)
    tags = Tag.objects.all().filter(blogs=blog)
    recent = Blog.objects.all().order_by("created")[:5]
    category = Category.objects.all()
    comments = Comments.objects.all().filter(blog=blog)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            nname = form.cleaned_data['name']
            nemail = form.cleaned_data['email']
            nmessage = form.cleaned_data['message']

            ncomment = Comments(blog=blog , name= nname , email = nemail , message= nmessage)
            ncomment.save()

    context = {
        "blog" : blog,
        "tags": tags,
        "recents":recent,
        "category":category,
        "comments": comments,
    }

    return render(request , "blog/blog_detail.html" , context)

def blog_tag(request , tag):
    blogs = Blog.objects.filter(tags__slug= tag)
    context = {
        "blogs":blogs
    }
    return render(request , "blog/blog_list.html" , context)

def blog_category(request , category):
    blogs = Blog.objects.filter(category__slug=category)
    context = {
        "blogs": blogs
    }
    return render(request, "blog/blog_list.html", context)
