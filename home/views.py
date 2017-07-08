from django.shortcuts import render

# Create your views here.
def index(request):
	noticias = [
		{'title':"Buscar x en google", 'link':"https://www.google.com/search?q=x&oq=x&aqs=chrome.0.69i59l2j69i60j35i39j0l2.103j0j7&sourceid=chrome&ie=UTF-8"},
		{'title':"noticia NYT", 'link':"https://www.nytimes.com/2017/07/07/world/europe/trump-putin-g20.html?hp&action=click&pgtype=Homepage&clickSource=story-heading&module=a-lede-package-region&region=top-news&WT.nav=top-news"}
	]
	return render(request, 'home/index.html', {'noticias':noticias})
