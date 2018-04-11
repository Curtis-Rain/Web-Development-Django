from django.shortcuts import render
from .models import Comment


def home_page(request):
    comments = Comment.objects.all()


    if request.method == 'POST':
        user_comment = request.POST.get('comment')
        user_username = request.POST.get("username")

        comment_obj = Comment.objects.create(
            content=user_comment,
            user=user_username
        )


        print(comment_obj.content * 10)
        return render(request, 'blog/home_page.html', {'comments': comments})


    if request.method == "GET":
        return render(request, 'blog/home_page.html', {'comments': comments} )