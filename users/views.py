import logging
from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout

logger = logging.getLogger('django')  # Django log tizimi


def get_client_ip(request):
    """Foydalanuvchi IP manzilini olish uchun yordamchi funksiya"""
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        return x_forwarded_for.split(',')[0]
    return request.META.get('REMOTE_ADDR')


class LoginView(View):
    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        ip = get_client_ip(request)  # IP manzilni olamiz
        username = request.POST.get('username')

        logger.info(f"LOGIN ATTEMPT: IP={ip}, USERNAME={username}")  # IP va loginni logga yozamiz

        user = authenticate(
            username=username,
            password=request.POST['password']
        )
        if user is not None:
            login(request, user)
            return redirect("bolimlar")
        return redirect("login")


def logout_view(request):
    logout(request)
    return redirect('login')
