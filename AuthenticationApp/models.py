from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, Group, Permission


class UserManager(BaseUserManager):
    use_in_migration = True

    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError('Email is Required')
        user = self.model(email=self.normalize_email(email), **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_active', True)

        if extra_fields.get('is_staff') is not True:
            raise ValueError('Superuser must have is_staff = True')
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser = True')

        return self.create_user(email, password, **extra_fields)


from django.contrib.auth.models import AbstractUser

class UserData(AbstractUser):
    username = None
    name = models.CharField(max_length=100, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    date_joined = models.DateTimeField(auto_now_add=True)
    is_admin = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # Adicione related_name='user_data_groups'
    # groups = models.ManyToManyField(Group, blank=True, related_name='user_data_groups')
    #
    # # Adicione related_name='user_data_permissions'
    # user_permissions = models.ManyToManyField(Permission, blank=True, related_name='user_data_permissions')

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=255)
    acess_key = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Service'
        verbose_name_plural = 'Services'



class User(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'Users'
        verbose_name_plural = 'Users'


class Group(models.Model):
    group_name = models.CharField(max_length=255)
    service_id = models.ForeignKey(Service, related_name='groups', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Group'
        verbose_name_plural = 'Groups'

class Permission(models.Model):
    name = models.CharField(max_length=255)
    ativo = models.BooleanField(default=True)
    group_id = models.ForeignKey(Group, related_name='permissios', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Permission'
        verbose_name_plural = 'Permissions'

class UserService(models.Model):
    user_id = models.ForeignKey(User, related_name='userServices', on_delete=models.CASCADE)
    service_id = models.ForeignKey(Service, related_name='serviceUsers', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'UserService'
        verbose_name_plural = 'UserServices'

class UserGroup(models.Model):
    user_id = models.ForeignKey(User, related_name='userGroups', on_delete=models.CASCADE)
    group_id = models.ForeignKey(Group, related_name='groupsUser', on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'UserGroup'
        verbose_name_plural = 'UserGroups'

