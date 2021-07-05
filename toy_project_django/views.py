from django.shortcuts import render

def home(request):
	return render(request, 'index.html')

def result(request):
	username = request.GET['username']
	username = username.upper()
	return render(request, 'result.html',{'user_name': username})
