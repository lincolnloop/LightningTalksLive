from django.shortcuts import render, redirect
from django.views.generic import View

from LTL.presenters import forms



class GetStartedView(View):

    template_name = 'welcome.html'

    def get(self, request):

        form = forms.ProfileForm()
        return render(request, 'welcome.html', {'form': form})

    def post(self, request):
        #TODO image
        form = forms.ProfileForm(request.POST)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = request.user
            profile.save()

            #TODO redirect to scheduling
            return redirect('/')

        return render(request, 'welcome.html', {'form': form})
