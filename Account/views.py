from django.shortcuts import render
from django.views import View
from Account.models import Account
# Create your views here.


class Home(View):
    def get(self, request):
        a = Account()
        a.accountName = "What"
        a.accountName = "no"
        return render(request, "index.html", {"a": a, "b": []})

    def post(self, request):
        a = Account()
        a.accountName = str(request.POST["name"])
        a.accountEmail = str(request.POST["email"])
        a.accountTitle = str(request.POST["title"])
        a.accountHP = str(request.POST["phone"])
        a.accountAddress = str(request.POST["address"])
        a.save()
        b = list(Account.objects.all())  #objects.filter() cascade delete
        return render(request, "index.html", {"a": a, "b": b})
