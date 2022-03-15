from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import views as auth_views, login

# Create your views here.
from django.urls import reverse_lazy
from django.views import generic as generic_views


class HomePageView(generic_views.TemplateView):
    template_name = 'index.html'


class UserRegisterView(generic_views.CreateView):
    # form_class = forms.UserRegistrationForm
    form_class = UserCreationForm
    template_name = 'register.html'
    success_url = reverse_lazy('index')

    # overwriting the form_valid method to login user directly after registering
    def form_valid(self, form):
        result = super().form_valid(form)
        # user => self.object
        # request => self.request
        login(self.request, self.object)
        return result


class UserLoginView(auth_views.LoginView):
    template_name = 'login.html'

    # overwriting the success url method to check if next is in the request.
    def get_success_url(self):
        next = self.request.GET.get('next', None)
        if next:
            return next
        return reverse_lazy('index')


class UserLogoutView(auth_views.LogoutView):
    template_name = 'logout.html'
