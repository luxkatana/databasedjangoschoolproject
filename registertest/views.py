from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest
from django.contrib.auth.forms import UserCreationForm



def register_view(request: HttpRequest) -> HttpResponse:
	if  request.method == "POST":
		validation = UserCreationForm(request.POST)
		if validation.is_valid():
			validation.save()
		return redirect("/")
	else:
		form = UserCreationForm()
		return render(request, "registration/register.html", {"form": form})




def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, "registertest/home.html", {"user": request.user})