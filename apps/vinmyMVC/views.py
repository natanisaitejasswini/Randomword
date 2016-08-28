 from django.shortcuts import render, redirect
import random
import string
def index(request):
	if 'count' not in request.session:
		request.session['count'] = 0
	request.session['count'] += 1
	gen = {
	'random_word': ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(10))
	}
	return render(request,'vinmyMVC/index.html',gen)
def create(request):
	print request.method
	if request.method == "POST":
		return redirect('/')
	else:
		return redirect('/')
def reset(request):
	del request.session['count'] 
	return redirect('/')