# Набор скриптов для работы с электронным дневником

Данный набор скриптов позволяет редактировать электронный дневник учащихся школы,
исправлять все двойки и тройки на пятёрки, удалять замечания и добавлять похвалы.
Скрипты работают в интерактивной консоли Django shell, в проекте сайта электронного 
дневника школы. Необходимо следуя [инструкции](https://github.com/devmanorg/e-diary/blob/master/README.md)
репозитория Электронный дневник школы, развернуть проект сайта локально с подключенной
готовой БД. Не забываем про создание [виртуального окружения](https://docs.python.org/3/library/venv.html).  

Когда сервер запущен и сайт доступен, скопируйте файл `scripts.py` в корневую папку 
проекта сайта.

### Запуск Django shell

  1. Откройте терминал
  1. Перейдите в корневой каталог проекта сайта
  1. Выполните команду:
```
python manage.py shell
```

Консоль запущена:
<a href="https://ibb.co/3dkvHgd"><img src="https://i.ibb.co/fFQ97jF/2-u-Tvan-Tx.png" alt="2-u-Tvan-Tx" border="0"></a>

### Описание скриптов

* `get_schoolkid` - Возвращает объект `schoolkid`, который необходим для работы других 
скриптов. При вызове необходимо указать аргументом фамилию и имя ученика. 
* `fix_marks` - Принимает объект `schoolkid` в качестве аргумента. Исправляет двойки и
тройки на пятёрки.  
* `remove_chastisements` - Принимает объект `schoolkid` в качестве аргумента. Удаляет
замечания от учителей.  
* `create_commendation` - Принимает объекты `schoolkid` и название предмета в качестве
аргумента. Выбирает случайный урок по указанному предмету и добавляет похвалу от 
  учителя с датой выбранного урока. Также после указания предмета можно передать
  необязательным аргументом дату похвалы в формате «гг/мм/дд».

### Использование скриптов

Для начало импортируем все скрипты одной командой:
```
from scripts import get_schoolkid, fix_marks, remove_chastisements, create_commendation
```
Создаём объект `schoolkid`:
```
schoolkid = get_schoolkid("Фролов Иван")
```
Если программа ругается на то, что найдено несколько одинаковых учеников, можно 
ввести ещё и отчество (например Фролов Иван Григорьевич).

Исправляем двойки и тройки на пятёрки:
```
fix_marks(schoolkid)
```
Удаляем замечания учителей:
```
remove_chastisements(schoolkid)
```
Добавляем похвалу по музыке со случайной датой:
```
create_commendation(schoolkid, "Музыка")
```
Добавляем похвалу по краеведению с конкретной датой:
```
create_commendation(schoolkid, "Краеведение", date='19-01-04')
```
### Цели проекта

Код написан в учебных целях — это урок в курсе по Python и веб-разработке на сайте [Devman](https://dvmn.org).
