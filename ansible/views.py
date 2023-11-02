from django.shortcuts import render
from datetime import datetime


# Create your views here.
def vmware(request):

    date = '2023-10-18'

    context = { 'html_file' : '/static/facts/vmware' + '/' + date + '/esx-all.html', 'date' : date, 'count' : 0, }

    return render(request, 'ansible/vmware_view.html', context)


def exe_search_vmware(request):

    # html_file = '/static' + '/facts' + '/vmware' + '/' + request['date'] + '/sample.html'

    platform = 'vmware'
    date = '2023-10-18'
    
    context = { 'html_file' : '/static/facts/' + platform + '/' + date + '/esx-all.html', 'date' : date, 'count' : 1, }
    
    return render(request, 'ansible/vmware_view.html', context)


def exceldown(request):
   
    return render(request, 'ansible/exceldown.html')
