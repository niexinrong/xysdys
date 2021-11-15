from django.http import HttpResponse
from XXX.models import huigai

def testdb(request):
	# test1 = huigai(name='ma剑')
	# test1.save()
	# return HttpResponse("<p>添加数据成功</p>")
	test2 = huigai.objects.get(id=1)
	test2.name = 'xinyesu得永生'
	test2.save()

	return HttpResponse('<p>修改成功.hlly,zmzys</p>')