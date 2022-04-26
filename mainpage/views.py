# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.views.generic import ListView
from django.views.generic.edit import FormView
from django.contrib.messages.views import SuccessMessageMixin

from django.core.mail import send_mail, get_connection
from django.conf import settings

from .forms import ContactForm
from .models import Project

class ProjectListAndFormView(SuccessMessageMixin, ListView, FormView):
    model = Project # data from database
    template_name = 'mainpage/main.html'
    context_object_name = 'list_projects' # name of the var in html template
    queryset = Project.objects.all().order_by("-pub_date")#  list of all projects
    object_list = None

    form_class = ContactForm
    success_url = '/' # After submiting the form keep staying on the same url
    success_message = 'Your Form has been successfully submitted!'

    def form_valid(self, form):
        # This method is called when valid form data has been POSTed.
        cd = form.cleaned_data
        con = get_connection('django.core.mail.backends.console.EmailBackend')
        send_mail(
            cd['name'],
            cd['message'],
            cd.get('email', 'noreply@example.com'),
            ['vlad.moroshan@gmail.com'],
            fail_silently=False
        )
        return super(ProjectListAndFormView, self).form_valid(form)
