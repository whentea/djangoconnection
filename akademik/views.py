#from django.shortcuts import render

# Create your views here.

from akademik.models import UserModel, StatusModel
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
# Create your views here.
def index(request):
    data = {}
    return render(request,"akademik/index.html",data)


def create(request):
    nilai1 = StatusModel(mk ="bahasa indonesia", votes=90)
    nilai2 = StatusModel(mk ="bahasa inggris", votes=72)
    nilai3 = StatusModel(mk ="bahasa arab", votes=69)
    nilai4 = StatusModel(mk ="bahasa jawa", votes=81)

    nilais = [nilai1, nilai2, nilai3, nilai4]

    user = UserModel(nama="Wahyu", tgl=datetime.datetime.now(), nilais=nilais)
    user.save()

    user = UserModel(nama="Wenty", tgl=datetime.datetime.now(),
                     nilais=nilais)
    user.save()

    return HttpResponseRedirect(reverse("mhs:show"))


def show(request):
    data = {}
    p = UserModel.objects.all()
    data["users"] = p
    return render(request, "mhs/show.html", data)


def delete(request, document_id):
    UserModel.objects.filter(id=document_id).delete()
    return HttpResponseRedirect(reverse("mhs:show"))
