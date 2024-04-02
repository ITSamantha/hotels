# Приложение для бронирования комнат в отеле


## Требования
  - Для комнат должны быть поля: номер/название, стоимость за сутки, количество мест.
  - Пользователи должны уметь фильтровать и сортировать комнаты по цене, по количеству мест.
  - Пользователи должны уметь искать свободные комнаты в заданном временном интервале.
  - Пользователи должны уметь забронировать свободную комнату.
  - Суперюзер должен уметь добавлять/удалять/редактировать комнаты и редактировать записи о бронях через админ панель Django.
  - Брони могут быть отменены как самим юзером, так и суперюзером.
  - Пользователи должны уметь регистрироваться и авторизовываться (логиниться).
  - Чтобы забронировать комнату пользователи должны быть авторизованными. Просматривать комнаты можно без логина. Авторизованные пользователи должны видеть свои брони.


## Стек
  - Django;
  - DRF;
  - СУБД предпочтительно PostgreSQL, но не обязательно. Главное не SQLite;
  - При необходимости можно добавлять другие библиотеки.

## Дополнительно
  - Автотесты;
  - Аннотации типов;
  - Линтер;
  - Автоформатирование кода;
  - Документация к API;
  - Инструкция по запуску приложения

# Используемый стек

  - Django
  - DRF
  - PostgreSQL

    
# Сборка

Данное приложение развернуто в Docker для удобства проверки. Для сборки приложения необходимо установить Docker. 
Для удобства проверки все миграции в приложении запускаются и создаются автоматически, а также БД заполняется тестовыми данными с помощью фикстур.
Для сборки приложения необходимо выполнить следующие действия.

  1. Склонировать репозиторий:
     
     ```
     git clone https://github.com/ITSamantha/hotels
     ```
     
  3. Выполнить build в директории приложения с помощью следующей команды:
     
     ```
    docker compose build --no-cache
     ```
     
  3. Для запуска приложения необходимо выполнить следующую команду:
     
     ```
    docker compose up
     ```
     
  Далее необходимо создать суперюзера.
