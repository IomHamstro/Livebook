from django.contrib.auth import authenticate, login
from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView

from Livebook.forms import RegistrationProfileForm, RegistrationUserForm
from Livebook.models import Book, Review, News, UserProfile


def registration(request):
    if request.method == "POST":
        form2 = RegistrationUserForm(request.POST, prefix="form2")
        form1 = RegistrationProfileForm(request.POST, prefix="form1")
        if form1.is_valid() and form2.is_valid():
            st1 = form1.save(commit=False)  # not saving
            st2 = form2.save()
            st1.user_id = st2.id
            st1.save()  
            return HttpResponseRedirect(reverse('index'))
        return HttpResponse(form1.errors)
    elif request.method == "GET":
        f1 = RegistrationProfileForm(prefix="form1")
        f2 = RegistrationUserForm(prefix="form2")
        context = {"f1": f1, "f2": f2}
        return render(request, 'Livebook/registration.html', context)


def index(request):
    return render(
        request,
        "Livebook/index.html",
        {
            "books": Book.objects.all()[:4]
        }
    )


def sign_in(request):
    if request.method == "POST":
        user = authenticate(
            username=request.POST["username"],
            password=request.POST["password"]
        )
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse('account'))
        else:
            return HttpResponseRedirect(reverse('error'))
    else:
           return HttpResponseRedirect(reverse('error'))


def error(request):
    return render(
        request,
        "Livebook/error.html",

    )


def account(request):
    user = UserProfile.objects.get(user=request.user)
    my_rewiews = Review.objects.filter(user=user.id)[:2]
    return render(
        request,
        "Livebook/account.html",
        {
            "user": user,
            "reviews": my_rewiews
        }
    )


def rating(request):
    return render(request, "Livebook/rating.html")


class ReviewsView(ListView):
    model = Review
    template_name = "Livebook/reviews.html"
    context_object_name = "reviews"
    paginate_by = 2

    def get_queryset(self):
        qs = Review.objects.order_by("-date")
        return qs


def forum(request):
    return render(request, "Livebook/forum.html")


class NewsView(ListView):
    model = News
    template_name = "Livebook/news.html"
    context_object_name = "news"
    paginate_by = 2

    def get_queryset(self):
        qs = News.objects.order_by("-date")
        return qs


def book(request, id):
    one_book = Book.objects.filter(id=id).first()
    return render(
        request,
        "Livebook/book.html",
        {"book": one_book}
    )


def book_list(request):
    return render(
        request,
        "Livebook/book_list.html",
        {"books": Book.objects.all()[:4]}
    )