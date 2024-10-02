from django.shortcuts import render

def blog_list(request):
    return render(request, 'aclanApp_02/blog_list.html')

def blog_post(request):
    return render(request, 'aclanApp_02/blog_post.html')

def about(request):
    return render(request, 'aclanApp_02/about.html')