from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields = ["username", "password1", "password2"]

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control mb-2"
        self.fields["password1"].widget.attrs["class"] = "form-control mb-2"
        self.fields["password2"].widget.attrs["class"] = "form-control mb-2"


class LoginForm(AuthenticationForm):

    def __init__(self, request=..., *args, **kwargs):
        super().__init__(request, *args, **kwargs)

        self.fields["username"].widget.attrs.update(
            {"class": "form-control mb-2", "placeholder": "Enter Username"}
        )
        self.fields["password"].widget.attrs.update(
            {"class": "form-control mb-2", "placeholder": "Enter Password"}
        )
