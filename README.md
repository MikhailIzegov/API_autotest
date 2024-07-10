## Проект автотестов для 3-ех APIs: reqres.in, catfact.ninja и demowebshop

<!-- Технологии -->

## :gear: Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pycharm/pycharm-original.svg"></code>
  <code><img width="5%" title="Python" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original.svg"></code>
  <code><img width="5%" title="Pytest" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/pytest/pytest-original.svg"></code>
  <code><img width="5%" title="Poetry" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/poetry/poetry-original.svg"></code>
  <code><img width="5%" title="Requests" src="images/logo/requests.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/github/github-original.svg"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/docker/docker-original.svg"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
<!--   <code><img width="5%" title="Jira" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/jira/jira-original-wordmark.svg"></code> -->
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

## :open_book: Описание
В проекте представлены примеры API автоматизации тестирования на Python.
  
API тесты на платформе `reqres.in`  
  
API тесты на платформе `catfact.ninja`  
  
API + WEB тесты  на платформе `demowebshop` - демонстрация гибридных тестов WEB и API (например, авторизация через API)  
  
Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео и пр.)   
  
В UI-тестах шаги отображены в виде степов через `with allure.step`  
  
Также по факту прохождения теста отправляется уведомление с результатами в Telegram.  
  
Браузер в UI-тестах запускается удаленно в Selenoid.  

## :heavy_check_mark: Кратко
- [x] `API` тесты
- [x] `Гибридные` тесты (API + WEB)
- [x] `Параметризованный` запуск тестов
- [x] Запуск WEB тестов, используя `Jenkins` и `Selenoid`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Отправка результатов тестирования в `Telegram`

<!-- Тест кейсы -->

## :heavy_check_mark: Что проверяют API тесты (reqres.in, catfact.ninja)

- [x] Создание новой сущности/пользователя
- [x] Обновление сущности/пользователя
- [x] Удаление сущности/пользователя
- [x] Регистрация новой сущности/пользователя

## :heavy_check_mark: Что проверяют WEB тесты (demowebshop)
- [x] Авторизация через UI
- [x] Авторизация через API без фикстуры с помощью авторизационной куки
- [x] Добавление товара в корзину через API (POST-запрос)
- [x] Добавление товара в корзину через API с помощью модели
- [x] Добавление товара в корзину через API с помощью модели и сессии (`from requests import sessions`)

<!-- Jenkins -->

## <img width="5%" title="Jenkins" src="images/logo/jenkins.png"> Запуск тестов из Jenkins

Для запуска тестов из Jenkins:
1. Нажмите кнопку "Собрать с параметрами"

<p><img src="images/screenshots/Jenkins_build_with_params.jpg" alt="Jenkins"/></p>

2. Выберите параметры

<p><img src="images/screenshots/Jenkins_choose_tests.jpg" alt="Jenkins"/></p>

3. Нажмите "Собрать"

<!-- Отчеты -->

## :bar_chart: Отчеты о прохождении тестов доступны в Allure

> При локальном запуске введите в командной строке: 
```bash
allure serve 
```

### <img width="3%" title="Allure" src="images/logo/allure_report.png"> Allure

#### Примеры отображения тестов

<img src="images/screenshots/Allure_test_results.jpg" alt="Allure"/>

#### Во вкладке Graphs можно посмотреть графики о прохождении тестов, по их приоритезации, по времени прохождения и др.

<img src="images/screenshots/Allure_graphs.jpg" alt="Allure"/>

### <img width="2.5%" title="Telegram" src="images/logo/tg.png"> Telegram

Настроена отправка отчета в Telegram

<img src="images/screenshots/Telegram_notifications.jpg" alt="Telegram"/>
