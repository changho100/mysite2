from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, 'nirs/index.html')


def exe_search_html(request):
    
    # html_name = request.POST['html_name']

    html_name = "sample.html"
    
    print(html_name)

    context = { 'html_name' : html_name}
    
    return render(request, 'nirs/html_view.html', context)
