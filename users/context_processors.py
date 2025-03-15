from django.contrib.auth.models import User

def get_user(request):
    if  request.user.is_authenticated:
        user = request.user
    else:
        user = None
    context = {"user":user,}
    return context