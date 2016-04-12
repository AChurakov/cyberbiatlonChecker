from django.db import models

# Create your models here.

class Team(models.Model):
    team_name = models.CharField(max_length=255, verbose_name='Имя команнды')
    att_points = models.FloatField(default=0, verbose_name='Attack points')
    def_points = models.FloatField(default=0, verbose_name='Defense Points')


    class Meta:
        verbose_name = 'Команда'
        verbose_name_plural = 'Команды'

    def __str__(self):
        return self.team_name


class Service(models.Model):
    name_service = models.CharField(max_length='255', verbose_name='Имя Сервиса')
    exploit = models.TextField(default='None', verbose_name='Уязвимость')

    class Meta:
        verbose_name = 'Сервис'
        verbose_name_plural = 'Сервисы'

    def __str__(self):
        return self.name_service


class Task(models.Model):
    name_task = models.CharField(max_length='255', verbose_name='Название Задания')
    text_task = models.TextField(verbose_name='Описание', default='None')
    task_flag = models.CharField(max_length='255', verbose_name='Flag')
    att_points = models.FloatField(default=0, verbose_name='Points')

    class Meta:
        verbose_name = 'Задание'
        verbose_name_plural = 'Задания'

    def __str__(self):
        return self.name_task


class Complete_task(models.Model):
    team_key = models.ForeignKey(Team, verbose_name='Команда')
    task_key = models.ForeignKey(Task, verbose_name='Задание')
    is_done = models.BooleanField(verbose_name='Выполненно')

    class Meta:
        verbose_name = 'Выпоненный'
        verbose_name_plural = 'Выполенные'

    def __str__(self):
        return self.task_key.name_task + ' ' + self.team_key.team_name


class Def_service(models.Model):
    name_service = models.CharField(max_length='255', verbose_name='Название Задания')
    text_service = models.TextField(verbose_name='Описание', default='None')
    service_exploit = models.CharField(max_length='255', verbose_name='Flag')
    def_points = models.FloatField(default=0, verbose_name='Points')

    class Meta:
        verbose_name = 'Защищаемый сервис'
        verbose_name_plural = 'Защищаемые сервисы'

    def __str__(self):
        return self.name_task
