from django.contrib.auth.base_user import BaseUserManager

class UserManager(BaseUserManager):
    
    def create_user(self, phone_no, password=None, **extra_field):
        
        if not phone_no:
            raise ValueError("Phone number is required")
        
        extra_field['email'] = self.normalize_email(extra_field['email'])
        user = self.model(phone_no=phone_no, **extra_field)
        user.set_password(password)
        user.save(using=self._db)  
        
        return user     
    
    
    def create_superuser(self, phone_no, password=None, **extra_field):
        extra_field.setdefault('is_staff', True)
        extra_field.setdefault('is_superuser', True)
        extra_field.setdefault('is_active', True)
        
        if extra_field.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff=True.')
        if extra_field.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')

        
        return self.create_user(phone_no, password, **extra_field)