from django.shortcuts import render


posts = [
    {
        "author": "Sanjaa",
        "title": "Forum Post 1",
        "content": "First forum post content",
        "date_posted": "August 27, 2018"
    },
    {
        "author": "User2",
        "title": "Forum Post 2",
        "content": "Second forum post content",
        "date_posted": "August 28, 2018"
    }
]


def home(request):
    context = {
        "posts": posts
    }
    return render(request, "forum/home.html", context)


def about(request):
    return render(request, "forum/about.html", {"title":"About"})

