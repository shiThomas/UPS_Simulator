from django.db.models import Q
from django.shortcuts import render, redirect, get_object_or_404
from myapp.models import package, survey
from django.views import generic
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib import messages
from .forms import UserRegisterForm, UserUpdateForm, ProfileUpdateForm
from django.core.mail import send_mail
from django.views.generic.edit import UpdateView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.contrib import messages

from django.core.mail import send_mail


# Create your views here.
def index(request):
    package_list = package.objects.all()
    num_package = package_list.count()
    context = {
        'num_package': num_package,
    }
    query = request.GET.get("q")
    if query:
        packageid_list = package.objects.filter(package_id__icontains = query)
        num_package = packageid_list.count()


        if num_package is not 0:
            pack = package.objects.all().filter(package_id=query)

            dest_x = pack.values_list('destination_x')[0][0]
            dest_y = pack.values_list('destination_y')[0][0]
            status = pack.values_list('package_status')[0][0]
            context = {
                'package_id':query,

                'dest_x': dest_x,
                'dest_y': dest_y,
                'num_package': num_package,
                'status': status,
            }
    return render(request, 'index.html', context=context)


class PackageListView(LoginRequiredMixin, generic.ListView):
    model = package

    def get_queryset(self):
        return package.objects.filter(owner=self.request.user)

    paginate_by = 10

class PackageDetailView(LoginRequiredMixin,generic.DetailView):
    model = package

class PackageUpdate(LoginRequiredMixin,UpdateView):
    model = package
    fields = ['destination_x','destination_y']


class SurveyCreate(LoginRequiredMixin,CreateView):
    model = survey
    fields =['package_id','satisfied','content']
    initial = {'Arrival_Time': '05/01/2018 12:00'}

    def form_valid(self, form):

        return super().form_valid(form)

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            messages.success(request, f'Account created for {username}!')
            send_mail(
                'Register Success',
                'Your account has been created successfully.',
                'UPS',
                [email],
                fail_silently=False,
            )
            return redirect('login')

    else:
        form = UserRegisterForm()

    return render(request, 'registration/signup.html', {'form': form})


@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST,
                                   request.FILES,
                                   instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request, f'Your account has been updated!')
            return redirect('profile')

    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, 'registration/profile.html', context)
