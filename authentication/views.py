from django.shortcuts import render, redirect
from django.views import View
from django.views.generic import TemplateView
from django.contrib.auth.views import LoginView, LogoutView
from django.http import HttpRequest, HttpResponse
from django.urls import reverse
from django.contrib import messages

from authentication.forms import  LoginForm, SignUpForm

# Create your views here.


class SignUpView(View):
    template_name = "auth/signup.html"
    page_title = "Create An Account"
    form_class = SignUpForm

    def get(self, request: HttpRequest) -> HttpResponse:
        context = {"title": self.page_title, "form": self.form_class()}
        return render(request, self.template_name, context)

    def post(self, request: HttpRequest) -> HttpResponse:
        form = self.form_class(request.POST)

        if form.is_valid():

            form.save()
            messages.success(request, "User Created successfully")
            return redirect(reverse("homepage"))

        print(form.errors)

        messages.error(request, "Failed to create user")
        context = {"form": form}
        return render(request, self.template_name, context)

class CustomLoginView(LoginView):
    template_name = 'auth/login.html'
    form_class = LoginForm


class LogoutDecisionView(TemplateView):
    template_name = "auth/logout_decision.html"


class CustomLogoutView(LogoutView):
    template_name = "auth/logged_out.html"
