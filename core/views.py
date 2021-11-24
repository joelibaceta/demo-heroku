from django.shortcuts import render
from django.views import View

# Create your views here.

class HelloView(View):

    def get(self, request):

        name = request.GET.get("name")
        last_name = request.GET.get("lastname")
        if name == None:
            name = "Anonymous"
        if last_name == None:
            last_name = ""

        context = {
            "name": name,
            "last_name": last_name
        }

        return render(request, 'index.html', context)