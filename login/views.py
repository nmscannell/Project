from django.shortcuts import render
from django.views import View
from login.models import LoginHelper
# Create your views here.


class loginPage(View):

    def get(self, request):
        return render(request, 'loginscreen.html')

    def post(self, request):
        LH = LoginHelper()
        username = str(request.POST["username"])
        password = str(request.POST["password"])

        commandlist = ["", username, password]

        try:
            check = LH.login(commandlist)

            if check == 1:
                LH.logout()
                return render(request, 'loginscreen.html', {"message": "Ta login"})
            if check == 2:
                LH.logout()
                return render(request, 'loginscreen.html', {"message": "Instructor login"})
            if check == 3:
                LH.logout()
                return render(request, 'loginscreen.html', {"message": "Admin login"})
            if check == 4:
                LH.logout()
                return render(request, 'loginscreen.html', {"message": "Supervisor login"})

        except Exception as e:

            return render(request, 'loginscreen.html', {"message": str(e)})

