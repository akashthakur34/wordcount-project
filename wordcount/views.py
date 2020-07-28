from django.http import HttpResponse
from django.shortcuts import render

def home(request):
	return render(request,'home.html')

def count(request):
	fulltext  = request.GET['fulltext']
	fullwordlist = fulltext.split()
	count1=0
	worddict ={}
	for item in fullwordlist:
		if item in worddict:
			worddict[item] = 1 + worddict[item]
		else:
			worddict[item]=1
		print (worddict)


	#print(fulltext)
	return render(request, 'count.html',{'fulltext':fulltext,'Wordcount':len(fullwordlist),'worddict':worddict})

def about(request):
	return render(request,'About.html')

