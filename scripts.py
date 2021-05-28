import random
from datacenter.models import Schoolkid, Mark, Chastisement, Lesson, Commendation


def get_schoolkid(name):
    return Schoolkid.objects.filter(full_name__contains=name).get()


def fix_marks(schoolkid):
    marks = Mark.objects.filter(points__in=[2, 3], schoolkid=schoolkid)
    for mark in marks:
        mark.points = 5
        mark.save()


def remove_chastisements(schoolkid):
    Chastisement.objects.filter(schoolkid=schoolkid).delete()


def create_commendation(schoolkid, subject, **kwargs):
    commendations = [
        'Молодец!',
        'Отлично!',
        'Хорошо!',
        'Гораздо лучше, чем я ожидал!',
        'Ты меня приятно удивил!',
        'Великолепно!',
        'Прекрасно!',
        'Ты меня очень обрадовал!',
        'Именно этого я давно ждал от тебя!',
        'Сказано здорово – просто и ясно!',
        'Ты, как всегда, точен!',
        'Очень хороший ответ!',
        'Талантливо!',
        'Ты сегодня прыгнул выше головы!',
        'Я поражен!',
        'Уже существенно лучше!',
        'Потрясающе!',
        'Замечательно!',
        'Прекрасное начало!',
        'Так держать!',
        'Ты на верном пути!',
        'Здорово!',
        'Это как раз то, что нужно!',
        'Я тобой горжусь!',
        'С каждым разом у тебя получается всё лучше!',
        'Мы с тобой не зря поработали!',
        'Я вижу, как ты стараешься!',
        'Ты растешь над собой!',
        'Ты многое сделал, я это вижу!',
        'Теперь у тебя точно все получится!'
        ]
    text = random.choice(commendations)
    lesson = Lesson.objects.filter(year_of_study=schoolkid.year_of_study, group_letter=schoolkid.group_letter,
                                   subject__title__contains=subject).order_by('?').first()
    date = kwargs.get('commendation_date', lesson.date)
    Commendation.objects.create(text=text, created=date, schoolkid=schoolkid, subject=lesson.subject,
                                teacher=lesson.teacher)
