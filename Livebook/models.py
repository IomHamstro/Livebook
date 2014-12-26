from django.contrib.auth import models
from django.contrib.auth.models import User
from django.db import models
from django.db.models import OneToOneField


class UserProfile(models.Model):
    email = models.EmailField()
    name = models.TextField()
    surname = models.TextField()
    birthday = models.DateField()
    address = models.TextField()
    information = models.TextField()
    hobby = models.TextField()
    # avatar = models.ImageField(upload_to="/user/avatar")
    books = models.ManyToManyField('Book')
    user = OneToOneField(User)


class Author(models.Model):
    name = models.TextField()
    biography = models.TextField()


class Genre(models.Model):
    type = models.CharField(max_length=255)



class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author)
    date = models.IntegerField()
    publishing = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    cover = models.ImageField(upload_to="books/covers")
    annotation = models.TextField()
    # my_marks = models.IntegerField()
    # submitDate = models.DateField(auto_now=True)



class Comment(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    

class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateField()
    positive = models.BooleanField()


class News(models.Model):
    title = models.TextField()
    text = models.TextField()
    date = models.DateField()


class Section(models.Model):
    name = models.TextField()


class Theme(models.Model):
    name = models.TextField()
    author = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    date = models.DateField(auto_now_add=True)


class Message(models.Model):
    theme = models.ForeignKey(Theme)
    author = models.ForeignKey(User)
    text = models.TextField()


class UserFiles(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to="/user/files")


class Rating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    value = models.SmallIntegerField()
