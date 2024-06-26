import secrets

from django.contrib.auth.forms import PasswordResetForm
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, FormView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject='Подтверждение почты',
            message=f'Перейти по ссылке для подтверждения почты {url}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)

    @staticmethod
    def email_verification(request, token):
        user = get_object_or_404(User, token=token)
        user.is_active = True
        user.save()
        return redirect(reverse('users:login'))


class UserResetPasswordView(FormView):
    model = User
    form_class = PasswordResetForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        email = form.cleaned_data['email']
        random_password = secrets.token_hex(16)
        for user in form.get_users(email):
            user.set_password(random_password)
            user.save()
        send_mail(
            subject='Password reset',
            message=f'Hello your password {random_password}',
            from_email=EMAIL_HOST_USER,
            recipient_list=[email],
        )

        return super().form_valid(form)
