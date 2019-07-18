from django.shortcuts import render
from django.http import HttpResponse
from django.core.urlresolvers import reverse
# Create your views here.

# 必须要传一个参数,一般命名为request
def funcA(request):
    return HttpResponse("this is a test response")

def funcB(request, year, month):
    return HttpResponse("this is a test response{0}{1}".format(year, month))

def rev(request):
    return HttpResponse(reverse('name'))