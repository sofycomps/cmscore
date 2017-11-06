import string
from django.db import models
import uuid # Required for unique book instances
from datetime import date
from django.core.mail import send_mail
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.base_user import AbstractBaseUser
from django.utils.translation import ugettext_lazy as _

class Currency(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter a the Currency name(e.g. US Dollar, Euro, Rupees, etc.)")
    code = models.CharField(max_length=5, help_text="Currency Code(e.g. USD, INR, etc.)")
    sign = models.CharField(max_length=5, help_text="Curency Sign")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
class Account(models.Model):
    name = models.TextField(blank=True, null=True)
    type = models.TextField(blank=True, null=True)
    currency = models.ForeignKey(Currency, blank=True, null=True)
    status = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
    expiry_date = models.DateTimeField(auto_now_add=False, null=True, blank=True)
    organization = models.TextField(blank=True, null=True)    
    address1 = models.TextField(blank=True, null=True)    
    address2 = models.TextField(blank=True, null=True)    
    city = models.TextField(blank=True, null=True)    
    postal_zip = models.TextField(blank=True, null=True)    
    state = models.TextField(blank=True, null=True)    
    country = models.TextField(blank=True, null=True)    
    contact_name = models.TextField(blank=True, null=True)    
    contact_mobile = models.TextField(blank=True, null=True)
    contact_phone = models.TextField(blank=True, null=True)   
    contact_email = models.TextField(blank=True, null=True)    

    created = models.DateTimeField(auto_now_add=True, editable=False)    
    modified = models.DateTimeField(auto_now_add=True, editable=False)    
    created_by = models.TextField(blank=True, null=True)    
    modified_by = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Account"

class Project(models.Model):
    name = models.TextField(blank=True, null=True)
    bookstore_url = models.TextField(blank=True, null=True)
    is_active = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
    currency = models.ForeignKey(Currency, blank=True, null=True)

    def __unicode__(self):
        return str(self.name)

    class Meta:
        verbose_name = "Project"


class Permissions(models.Model):
   permission = models.TextField(blank=True, null=True) 
   fk_project  = models.ForeignKey(Project, blank=False, null=False)
   can_create_docs  = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
   can_delete_docs  = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
   can_modify_docs  = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
   can_publish_docs  = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")
   can_update_account  = models.SmallIntegerField(default=0, help_text="0|Inactive 1|Active")

   def __unicode__(self):
        return str(self.permission)

   class Meta:
        verbose_name = "Permission"
   
class User(AbstractBaseUser):
    UID = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID")
    username = models.CharField(_('username'), unique=True, max_length=100)
    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=100, blank=True)
    last_name = models.CharField(_('last name'), max_length=100, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    avatar = models.ImageField(upload_to='static/avatars/', null=True, blank=True)
    fk_account = models.ForeignKey(Account, blank=False, null=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = [first_name]

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    def get_full_name(self):
        '''
        Returns the first_name plus the last_name, with a space in between.
        '''
        full_name = '%s %s' % (self.first_name, self.last_name)
        return full_name.strip()

    def get_short_name(self):
        '''
        Returns the short name for the user.
        '''
        return self.first_name

    def email_user(self, subject, message, from_email=None, **kwargs):
        '''
        Sends an email to this User.
        '''
        send_mail(subject, message, from_email, [self.email], **kwargs)


class Genre(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a book genre (e.g. Science Fiction, French Poetry etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name
        
        
class Language(models.Model):
    """
    Model representing a Language (e.g. English, French, Japanese, etc.)
    """
    name = models.CharField(max_length=200, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")
    code = models.CharField(max_length=5, help_text="Enter a the book's natural language (e.g. English, French, Japanese etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name


        
class Document(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    fk_project  = models.ForeignKey(Project, blank=False, null=False)
      # Foreign Key used because book can only have one author, but authors can have multiple books
      # Author as a string rather than object because it hasn't been declared yet in file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    isbn = models.CharField('ISBN',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    genre = models.ManyToManyField(Genre, help_text="Select a genre for this book")
      # ManyToManyField used because Subject can contain many books. Books can cover many subjects.
      # Subject declared as an object because it has already been defined.
    imprint = models.CharField(max_length=200)
    language = models.ForeignKey('Language', on_delete=models.SET_NULL, null=True)

    location = models.TextField(max_length=1000, help_text="Document location") 
    
    created = models.DateTimeField(auto_now_add=True, editable=False)    
    modified = models.DateTimeField(auto_now_add=True, editable=False)    
    created_by = models.TextField(blank=True, null=True)    
    modified_by = models.TextField(blank=True, null=True)
  
    def display_genre(self):
        """
        Creates a string for the Genre. This is required to display genre in Admin.
        """
        return ', '.join([ genre.name for genre in self.genre.all()[:3] ])
        display_genre.short_description = 'Genre'
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
        

class BookInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    book = models.ForeignKey('Document', on_delete=models.SET_NULL, null=True) 
    imprint = models.CharField(max_length=200)
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s (%s)' % (self.id,self.book.title)
        
