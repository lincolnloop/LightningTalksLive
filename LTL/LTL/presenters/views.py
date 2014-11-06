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

        form = forms.TalkForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):

        form = forms.TalkForm(request.POST)
        if form.is_valid():
            talk = form.save(commit=False)
            talk.presenter = request.user
            talk.save()
        print form.errors
        return render(request, self.template_name, {'form': form})


