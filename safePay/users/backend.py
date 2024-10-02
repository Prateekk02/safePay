from django.contrib.auth.backends import BaseBackend
from .models import CustomUser

class PhoneNoBackend(BaseBackend):
    def authenticate(self, request, phone_no=None, password=None, **kwargs):
        try:
            user = CustomUser.objects.get(phone_no=phone_no)
        except CustomUser.DoesNotExist:
            return None

        
        if user.check_password(password):
            return user
        return None
    
    def get_user(self, user_id):
        try:
            return CustomUser.objects.get(pk=user_id)
        except CustomUser.DoesNotExist
            return None