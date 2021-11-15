from django.http import HttpResponse
from django.shortcuts import render
 
def hello(request):
    return HttpResponse("Hello world ! hlly,感谢赞美主耶稣。")

def xysdys(request):
	context = {}
	context['xysdys'] = '信耶稣得永生!wx'
	context['bxysxdy'] = '不信耶稣下地狱'
	return render(request,'hlly.html',context)
