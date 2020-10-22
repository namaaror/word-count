from django.http import HttpResponse
from django.shortcuts import render
import operator

def homepage(request):
    return render(request, 'home.html')

def count(request):
    data = request.GET['fulltext']
    datalist = data.split()

    worddict = {}
    for word in datalist:
        if word in worddict:
            worddict[word] += 1
        else:
            worddict[word] = 1

    sorted_list = sorted(worddict.items(), key=operator.itemgetter(1), reverse=True)

    return render(request, 'count.html', {'fulltext': data, 'counter': len(datalist),
                    'worddict': sorted_list})