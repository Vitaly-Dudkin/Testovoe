from django.contrib.auth.models import AbstractUser
from django.db import models


class Subject(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "subjects"
        verbose_name = "Субъект"
        verbose_name_plural = "Субъекты"


class Country(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "countries"
        verbose_name = "Страна"
        verbose_name_plural = "Страны"


class Filial(models.Model):
    name = models.CharField(max_length=100, verbose_name="Название")

    def __str__(self):
        return self.name

    class Meta:
        db_table = "filials"
        verbose_name = "Филиал"
        verbose_name_plural = "Филиалы"


class User(AbstractUser):
    class StatusChoices(models.TextChoices):
        BOSS = ("boss", "Босс")
        MASTER = ("master", "Мастер")
        FRANCH = ("franch", "Франшиза")

    username = None
    email = models.EmailField(unique=True, verbose_name="Почта")
    phone = models.CharField(
        max_length=35, verbose_name='Номер телефона', null=True, blank=True
    )
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    middle_name = models.CharField(
        max_length=100, verbose_name="Отчество", null=True, blank=True
    )
    reg_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата регистрации")
    status = models.CharField(
        choices=StatusChoices.choices, max_length=10, default=StatusChoices.FRANCH
    )

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    class Meta:
        db_table = "users"
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"


class UserSubject(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE, verbose_name="Субъект")

    class Meta:
        db_table = "users_to_subjects"
        verbose_name = "Пользователь субъекта"
        verbose_name_plural = "Пользователи субъекта"


class UserCountry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    country = models.ForeignKey(Country, on_delete=models.CASCADE, verbose_name="Страна")

    class Meta:
        db_table = "users_to_country"
        verbose_name = "Пользователь страны"
        verbose_name_plural = "Пользователи страны"


class UserFilial(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Пользователь")
    filial = models.ForeignKey(Filial, on_delete=models.CASCADE, verbose_name="Филиал")

    class Meta:
        db_table = "users_to_filials"
        verbose_name = "Пользователь филиала"
        verbose_name_plural = "Пользователи филиала"
