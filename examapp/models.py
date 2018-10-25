from __future__ import unicode_literals
from django.db import models
from datetime import datetime

import re
# Create your models here.

now = str(datetime.now())

class UserManager(models.Manager):
    def basic_validator(self, postData):


        errors = {}

        if len(postData["name"]) < 3:
            errors["name"] = "name is required"
        elif Users.objects.filter(name = postData["name"]):
            errors["name"] = "Great one, but it's already taken!"

        if len(postData["username"]) < 3:
            errors["username"] = "username is required"
        elif Users.objects.filter(username = postData["username"]):
            errors["username"] = "Great one, but it's already taken!"

        if len(postData['password']) < 8:
            errors['password'] = "password is required"
        if postData['pw_confirm'] != postData['password']:
            errors['password'] = "Hey, these passwords don't match!!"
        return errors


    def login_validator(self, postData):

        print("POSTDATA is", postData)

        errors = {}

        if len(postData["username"]) < 3:
            errors["username"] = "username is required"
        elif not Users.objects.filter( username = postData["username"]):
            errors["username"] = "Username not found, please register!"

        if len(postData['password']) < 8:
            errors['password'] = "password is required"
        return errors

class ItemManager(models.Manager):

    def item_validator(self, postData):
        errors = {}

        if len(postData['product']) < 3:
            errors['product'] = "should be more than 3 characters!"
        return errors

class Users(models.Model):
    name = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = UserManager()

class Items(models.Model):
    product = models.CharField(max_length=255)
    action = models.CharField(max_length=255)
    added_by = models.ForeignKey(Users, related_name="items", on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)

    objects = ItemManager()

class Added(models.Model):
    user = models.ForeignKey(Users, related_name="added_user", on_delete = models.CASCADE)
    item = models.ForeignKey(Items, related_name="added_item", on_delete = models.CASCADE)
