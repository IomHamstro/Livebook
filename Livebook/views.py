from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render

from Livebook.forms import LoginForm


def index(request):
    return render(
        request,
        "Livebook/index.html",
        {
            # "books": Book.objects.order_by("-submitDate").all()[:4]
        }
    )


def sign_in(request):
    if request.POST:
        f = LoginForm(request.POST)
        if f.is_valid():
            user = authenticate(
                username=f.cleaned_data["username"],
                password=f.cleaned_data["password"]
            )
            if user:
                login(request, user)
                return HttpResponseRedirect(reverse('account'))
            else:
                return HttpResponseRedirect(reverse('index'))
    else:
        f = LoginForm()
        context = {"f": f}
        if request.GET.has_key("next"):
            context["next"] = request.GET["next"]
        return render(request, "Livebook/index.html", context)


def account(request):
    return render(
        request,
        "Livebook/account.html",

    )


def rating(request):
    return render(request, "Livebook/rating.html")


def reviews(request):
    return render(request, "Livebook/reviews.html")


def forum(request):
    return render(request, "Livebook/forum.html")


def news(request):
    return render(request, "Livebook/news.html")