from django.shortcuts import render
from django.views import View
from login.models import LoginHelper
# Create your views here.

class loginPage(View):

    def post(self, request):
        LH = LoginHelper()
        username = str(request.POST["username"])
        password = str(request.POST["password"])

        command = ["", username, password]

        try:
            check = LH.login(command)

            if check == 1:
                return "TA homepage"
            if check == 2:
                return "Instructor homepage"
            if check == 3:
                return "Admin homepage"
            if check == 4:
                return "Supervisor homepage"

        except Exception as e:

            return render(request, 'main/index.html', {"message": str(e)})

