from django.shortcuts import render

# Create your views here.
def posts_list(request):
    return render(request, 'post/post_list.html')
# posts/views.py



def post_list(request):
    return HttpResponse("This is the list of posts.")
