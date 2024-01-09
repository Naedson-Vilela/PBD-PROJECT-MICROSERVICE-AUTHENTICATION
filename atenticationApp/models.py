from django.db import models

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

