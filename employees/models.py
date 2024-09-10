from django.db import models
from user.models import User


class Worker(models.Model):
    post = models.CharField(max_length=100, verbose_name="Должность")
    worker = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Пользователь",
        related_name="workers",
    )
    director = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Директор")

    def __str__(self):
        return f"{self.post} {self.worker}"

    class Meta:
        db_table = "worker_attrs"
        verbose_name = "Работник"
        verbose_name_plural = "Работники"


class WorkerPermission(models.Model):
    worker = models.ForeignKey(Worker, on_delete=models.CASCADE, verbose_name="Работник")
    right_code = models.CharField(max_length=10, verbose_name="Код разрешения")

    def __str__(self):
        return f"{self.worker} {self.right_code}"

    class Meta:
        db_table = "worker_rights"
        verbose_name = "Права работника"
        verbose_name_plural = "Права работников"


