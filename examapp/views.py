from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
import bcrypt
# Create your views here.
def index(request):
    return render(request, 'index.html')

def new_user(request):
    errors = Users.objects.basic_validator(request.POST)


    if len(errors):

        for key, value in errors.items():
            messages.error(request, value)

        print(errors)
        return redirect('/')
    else:
        hash_brown = bcrypt.hashpw(request.POST['password'].encode(), bcrypt.gensalt())
        user = Users.objects.create(name = request.POST['name'], username = request.POST['username'], password = hash_brown.decode('utf-8'))

        request.session['id'] = user.id
        request.session['username']=user.username

        return redirect('/wishlist')

def login(request):
    errors = Users.objects.login_validator(request.POST)
    print(errors)

    if len(errors):

        for key, value in errors.items():
            messages.error(request, value)

        print(errors)
        return redirect('/')
    else:
        user = Users.objects.get(username=request.POST['username'])
        if bcrypt.checkpw(request.POST['password'].encode(), user.password.encode()):
            print("password match")
            request.session['id'] = user.id
            request.session['username']=user.username
            return redirect('/wishlist')
        else:

            print("failed password")
            messages.error(request, "Wrong password")

            return redirect('/')

def logout(request):
    request.session.clear()
    return redirect('/')

def wishlist(request):
    all_items=Items.objects.all()
    added_user=Added.objects.filter(user_id=request.session['id'])
    print(added_user)
    for i in added_user:
        all_items=all_items.exclude(id=i.item_id)

    context={
        'all_items':all_items,
        'added_user':added_user,
    }
    return render(request, 'wishlist.html', context)

def create(request):
    return render(request, 'create.html')

def create_item(request):
    print(request.POST)

    errors = Items.objects.item_validator(request.POST)
    print(errors)
    if len(errors):

        for key, value in errors.items():
            messages.error(request, value)


        print(errors)
        return redirect('/create')

    else:
        new_item=Items.objects.create(product=request.POST['product'], added_by_id= request.session['id'])
        Added.objects.create(item_id=new_item.id, user_id=request.session['id'])
        return redirect('/wishlist')

def added(request, item_id):
    Added.objects.create(item_id=item_id, user_id=request.session['id'])

    return redirect('/wishlist')


def details(request, item_id):
    item = Items.objects.get(id=item_id)
    added_user=Added.objects.exclude(item_id=item_id)

    context = {
        'item': item,
        'added_user': added_user
    }
    return render(request, 'details.html', context)

def delete(request, item_id):
    b = Items.objects.get(id=item_id)
    b.delete()
    return redirect( "/wishlist")

def remove(request, added_id):
    Added.objects.get(id=added_id).delete()
    return redirect( "/wishlist")
