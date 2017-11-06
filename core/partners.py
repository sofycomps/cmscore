from .models import User




class UserManager:
    
    def fetch_all_partners(self):
        
        users = User.objects.all()
        return users