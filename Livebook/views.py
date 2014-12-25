from django.core.urlresolvers import reverse_lazy, reverse
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView, FormView

from Livebook.forms import RegistrationForm
from Livebook.models import Book, Review, News, User


def registration(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            st = form.save(commit=False)  # not saving
            st.save()
            return HttpResponseRedirect(reverse('index'))
        return HttpResponse(form.errors)
    elif request.method == "GET":
        f = RegistrationForm()
        context = {"f": f}
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
        user = User.objects.\
            filter(login=request.POST.get("username", False)).\
            filter(password=request.POST.get("password", False)).first()
        if user:
                return HttpResponseRedirect(reverse('account', kwargs={"user_id": user.id}))
        else:
            return render(request, "Livebook/error.html")


def error(request):
    return render(
        request,
        "Livebook/error.html",

    )


def account(request, user_id):
    user = User.objects.filter(id=user_id).first()
    myRewiews = Review.objects.filter(user=user_id)[:2]
    return render(
        request,
        "Livebook/account.html",
        {
            "user": user,
            "reviews": myRewiews
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