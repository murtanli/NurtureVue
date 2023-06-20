from django.contrib.auth import logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.views import LoginView
from django.http import HttpResponse, request
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import ListView, CreateView, TemplateView, DetailView
from .forms import *
from .models import *
from .utils import *
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin

class HomeView(DataMixin, View):
    def get(self, request, **kwargs):
        c_def = self.get_data()
        context = super().get_data(**kwargs)
        context['active_page'] = 'home'
        context = dict(list(context.items()) + list(c_def.items()))
        return render(request, 'main/home.html', context=context)

class About(DataMixin, View):
    def get(self, request, **kwargs):
        c_def = self.get_data()
        context = super().get_data(**kwargs)
        context['active_page'] = 'about'
        context = dict(list(context.items()) + list(c_def.items()))
        return render(request, 'main/about.html', context=context)

class Contact(DataMixin, View):
    def get(self, request, **kwargs):
        c_def = self.get_data()
        context = super().get_data(**kwargs)
        context['active_page'] = 'contact'
        context = dict(list(context.items()) + list(c_def.items()))
        return render(request, 'main/contact.html', context=context)

"""def login(request):
    context = {
        'active_page': 'login',
        'menu': menu
    }
    return render(request, 'main/Login.html', context=context)"""

class RegisterUser(CreateView, DataMixin):
    form_class = RegisterUserForm
    template_name = 'main/Signup.html'
    success_url = reverse_lazy('home')

    def form_valid(self, form):
        response = super().form_valid(form)
        login(self.request, form.instance)
        return response

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['request'] = self.request
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'signup'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))


"""class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/Signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'signup'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')"""

class LoginUser(DataMixin, LoginView):
    form_class = LoginUserForm
    template_name = 'main/Login.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'login'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('addgrhs')


def logout_user(request):
    logout(request)
    return redirect('login')
"""class RegisterUser(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/Signup.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_data()
        context['active_page'] = 'signup'
        context = dict(list(context.items()) + list(c_def.items()))
        return context"""

"""def signup(request):
    context = {
        'active_page': 'signup',
        'menu': menu,
    }
    return render(request, 'main/Signup.html', context=context)"""

class addgrhs(DataMixin, LoginRequiredMixin, CreateView):
    form_class = AddNewGreenhouse
    template_name = 'main/addgrhs.html'
    success_url = reverse_lazy('home')
    login_url = reverse_lazy('home')
    raise_exception = True
    def get_context_data(self,object_list = None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['active_page'] = 'addgrhs'
        c_def = self.get_data()
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = self.request.user
        profile = Profile.objects.get(user=user)
        form.instance.profile = profile

        return super().form_valid(form)

"""def addgrhs(request):
    if request.method == 'POST':
        form = AddNewGreenhouse(request.POST)
        if form.is_valid():
            try:
                greenhouse.objects.create(**form.cleaned_data)
                return redirect('home')
            except:
                form.add_error(None, 'Error')
    else:
        form = AddNewGreenhouse()

    context = {
        'title': 'Add a Greehouse',
        'active_page': 'addgrhs',
        'menu': menu,
        'form': form,
    }
    return  render(request, 'main/addgrhs.html', context=context)
"""

"""class mainaddgrhs(TemplateView):
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a Greehouse'
        context['active_page'] = 'addgrhs'
        context['menu'] = menu
        return context

    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return render(request, 'main/addgrhs.html', context=context)
    form_class = AddPostForm
    
    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Add a Greehouse'
        context['active_page'] = 'addgrhs'
        context['menu'] = menu
        return context"""

