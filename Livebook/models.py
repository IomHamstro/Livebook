from django.db import models


class User(models.Model):
    login = models.CharField(max_length=255)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    name = models.TextField()
    surname = models.TextField()
    birthday = models.DateField()
    address = models.TextField()
    information = models.TextField()
    hobby = models.TextField()
    avatar = models.ImageField(upload_to="/user/avatar")
    books = models.ManyToManyField('Book')

    def __str__(self):
        return " : ".join([self.login, self.email, self.password, self.name, self.surname, str(self.birthday),
                           self.address, self.information, self.hobby, self.avatar.name])


class Author(models.Model):
    name = models.TextField()
    biography = models.TextField()

    def __str__(self):
        return " : ".join([self.name, self.biography])


class Genre(models.Model):
    type = models.CharField(max_length=255)

    def __str__(self):
        return self.type


class Book(models.Model):
    name = models.TextField()
    author = models.ForeignKey(Author)
    date = models.DateField()
    publishing = models.CharField(max_length=255)
    genres = models.ManyToManyField(Genre)
    cover = models.ImageField(upload_to="books/covers")
    annotation = models.TextField()
    my_marks = models.IntegerField()
    submitDate = models.DateField(auto_now=True)

    def __str__(self):
        return " : ".join([self.name, self.author.name, self.date, self.publishing, self.genre.type, self.cover.name,
                           self.annotation])


class Comment(models.Model):
    book = models.ForeignKey(Book)
    author = models.ForeignKey(User)
    date = models.DateField(auto_now_add=True)
    text = models.TextField()
    
    def __str__(self):
        return " : ".join([self.book.name, self.author.name, str(self.date), self.text])


class Review(models.Model):
    book = models.ForeignKey(Book)
    user = models.ForeignKey(User)
    text = models.TextField()
    date = models.DateField()
    positive = models.BooleanField()

    def __str__(self):
        return " : ".join([self.book.name, self.user.name, self.text, str(self.date)])


class Section(models.Model):
    name = models.TextField()

    def __str__(self):
        return self.name


class Theme(models.Model):
    name = models.TextField()
    author = models.ForeignKey(User)
    section = models.ForeignKey(Section)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return " : ".join([self.name, str(self.scored), str(self.missed)])


class Message(models.Model):
    theme = models.ForeignKey(Theme)
    author = models.ForeignKey(User)
    text = models.TextField()

    def __str__(self):
        return " : ".join([self.theme.name, self.author.name, self.text])


class UserFiles(models.Model):
    user = models.ForeignKey(User)
    file = models.FileField(upload_to="/user/files")

    def __str__(self):
        return " : ".join([self.user.name, self.file.name])


class Rating(models.Model):
    user = models.ForeignKey(User)
    book = models.ForeignKey(Book)
    value = models.SmallIntegerField()

    def __str__(self):
        return " : ".join([self.user.name, self.book.name, str(self.rating)])