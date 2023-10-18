from django.shortcuts import render
from datetime import datetime


# Create your views here.
def vmware(request):

    date = datetime.today().strftime('%Y-%m-%d')

    context = { 'html_file' : '/static/facts/vmware' + '/' + date + '/esx-all.html', 'date' : date, 'count' : 0, }

    return render(request, 'nirs/vmware_view.html', context)


def exe_search_vmware(request):

    # html_file = '/static' + '/facts' + '/vmware' + '/' + request['date'] + '/sample.html'

    platform = 'vmware'
    date = request.POST['date']
    
    context = { 'html_file' : '/static/facts/' + platform + '/' + date + '/esx-all.html', 'date' : date, 'count' : 1, }
    
    return render(request, 'nirs/vmware_view.html', context)
