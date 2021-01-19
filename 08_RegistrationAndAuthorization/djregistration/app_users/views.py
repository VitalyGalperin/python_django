from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.views.generic import DetailView, FormView

from .forms import ExtendedRegisterForm
from .models import Profile
from django.contrib.auth.views import LoginView, LogoutView


class Login2View(LoginView):
    template_name = 'users/login.html'


class Logout2View(LogoutView):
    # template_name = 'users/logout.html'
    next_page = '/'


class Registration2View(FormView):
    template_name = 'users/register.html'
    success_url = '/'
    form_class = ExtendedRegisterForm

    def form_valid(self, form):
        user = form.save()
        city = form.cleaned_data['city']
        phone = form.cleaned_data['phone']
        Profile.objects.create(
            user=user,
            city=city,
            phone=phone,
        )
        username = form.cleaned_data['username']
        raw_password = form.cleaned_data['password1']
        user = authenticate(username=username, password=raw_password)
        login(self.request, user)
        return super(Registration2View, self).form_valid(form)


class AccountView(DetailView):
    model = User

    def get(self, request, *args, **kwargs):
        return render(request, 'users/account.html')

# _________  Not used. notes ____________
# from django.contrib.auth.decorators import permission_required
# from django.contrib.auth.forms import UserCreationForm
# from django.core.exceptions import PermissionDenied
#
# @permission_required
# def vacancy_list(request):
#     vacancies =Vacancy.objects.all()
#     return render(request, 'vacancy/edit_account.html', {'vacancy_list': vacancies})
#
#
# def vacancy_list(request):
#     if not request.user.has_perm(app_news.view_news): # <app>.<action>_<object_name>
#         raise PermissionDenied()
#     vacancy =Vacancy.objects.all()
#     return render(request, 'vacancy/edit_account.html', {'vacancy_list': vacancy})
#
#
# def base_register_view(request):
#     if request.method == 'POST':
#         form = UserCreationForm(request.POST)
#         if form.is_valid():
#             form.save()
#             username = form.cleaned_data['username']
#             raw_password = form.cleaned_data['password1']
#             user = authenticate(username=username, password=raw_password)
#             login(request, user)
#             return redirect('/')
#     else:
#         form = UserCreationForm()
#     return render(request, 'users/register.html', {'form': form})



