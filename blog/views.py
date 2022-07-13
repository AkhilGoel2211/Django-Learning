import imp
from turtle import title
from django.shortcuts import render
from .models import Post

# from django.http import HttpResponse

# Create your views here.

# posts = [
#     {
#         "author": "Akhil Goel",
#         "title": "Blog Post 1",
#         "content": "First Post content",
#         "date_posted": "12 July 2022",
#     },
#     {
#         "author": "Aaryan Garg",
#         "title": "Blog Post 2",
#         "content": "Second Post content",
#         "date_posted": "13 July 2022",
#     },
# ]


def home(request):
    context = {"posts": Post.objects.all()}
    return render(request, "blog/home.html", context)


def about(request):
    return render(request, "blog/about.html", {"title": "About"})
