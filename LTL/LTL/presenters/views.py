import datetime

from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect
from django.views.generic import View

from LTL.presenters import forms



class GetStartedView(View):

    template_name = 'presenters/welcome.html'

    def get(self, request):

        form = forms.ProfileForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        #TODO image
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            #TODO redirect to scheduling
            return redirect('/')

        return render(request, self.template_name, {'form': form})


class CreateTalk(View):

    template_name = 'presenters/create_talk.html'

    def get(self, request):
        when = datetime.datetime(
            int(request.GET['year']),
            int(request.GET['month']),
            int(request.GET['day']),
            int(request.GET['hour']),
            int(request.GET['minute']))
        form = forms.TalkForm(initial={'when': when})
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = forms.TalkForm(request.POST)
        if form.is_valid():

            #TODO make sure slot isn't taken
            #TODO lock time slot to prevent race conditions

            talk = form.save(commit=False)
            talk.presenter = request.user
            talk.save()

            return redirect(reverse('talk_prep'))

        return render(request, self.template_name, {'form': form})


class TalkPrep(View):

    template_name = 'presenters/talk_prep.html'

    def get(self, request):
        return render(request, self.template_name)

