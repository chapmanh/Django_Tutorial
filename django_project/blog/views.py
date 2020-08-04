from django.shortcuts import render

posts = [
    {
        'author': 'Haydn',
        'title': 'Test post',
        'content': '#first',
        'date_posted': 'August 02 2020'
    },
    {
        'author': 'Titus',
        'title': 'I am awesome',
        'content': 'The title says it all...',
        'date_posted': 'August 03 2020'
    }
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html', {'title': 'About'})
