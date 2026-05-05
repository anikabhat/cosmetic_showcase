from email.mime import message
from urllib import request
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from django.shortcuts import redirect
from hello.forms import ReviewForm
from hello.models import Review
from django.views.generic import ListView

class HomeListView(ListView):
    """Renders the home page, with a list of all reviews."""
    model = Review

    def get_context_data(self, **kwargs):
        context = super(HomeListView, self).get_context_data(**kwargs)
        return context

def about(request):
    return render(request, "hello/about.html")
def contact(request):
    return render(request, "hello/contact.html")


def hello_there(request, name):
    print(request.build_absolute_uri()) #optional
    return render(
        request,
        'hello/hello_there.html',
    {
        'name': name,
        'date': datetime.now()
    }
)
def submit_review(request):
    form = ReviewForm(request.POST or None)

    if request.method == "POST":
      if form.is_valid():
        review = form.save(commit=False)
        review.log_date = datetime.now()
        review.save()
        return redirect("home")
    else:
        return render(request, "hello/submit_review.html", {"form": form}
)