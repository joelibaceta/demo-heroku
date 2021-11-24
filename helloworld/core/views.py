from django.shortcuts import render
from django.views import View

# Create your views here.

class HelloView(View):

    def get(self, request):

        name = request.GET.get("name")
        if name == None:
            name = "Anonymous"

        context = {
            "name": name
        }

        return render(request, 'index.html', context)