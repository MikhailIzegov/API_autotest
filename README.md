## Проект автотестов для 3-ех APIs: reqres.in, catfact.ninja и demowebshop

<!-- Технологии -->

## :gear: Используемые технологии
<p  align="center">
  <code><img width="5%" title="Pycharm" src="images/logo/pycharm.png"></code>
  <code><img width="5%" title="Python" src="images/logo/python.png"></code>
  <code><img width="5%" title="Pytest" src="images/logo/pytest.png"></code>
  <code><img width="5%" title="Requests" src="images/logo/requests.png"></code>
  <code><img width="5%" title="Selene" src="images/logo/selene.png"></code>
  <code><img width="5%" title="Selenium" src="images/logo/selenium.png"></code>
  <code><img width="5%" title="GitHub" src="images/logo/github.png"></code>
  <code><img width="5%" title="Jenkins" src="images/logo/jenkins.png"></code>
  <code><img width="5%" title="Docker" src="images/logo/docker.png"></code>
  <code><img width="5%" title="Selenoid" src="images/logo/selenoid.png"></code>
  <code><img width="5%" title="Allure Report" src="images/logo/allure_report.png"></code>
  <code><img width="5%" title="Allure TestOps" src="images/logo/allure_testops.png"></code>
<!--   <code><img width="5%" title="Jira" src="images/logo/jira.png"></code> -->
  <code><img width="5%" title="Telegram" src="images/logo/tg.png"></code>
</p>

<!-- Описание -->

## :open_book: Описание
В проекте представлены примеры API автоматизации тестирования на Python. 
<p>API тесты на платформе `reqres.in`
<p>API тесты на платформе `catfact.ninja`
<p>API + WEB тесты  на платформе `demowebshop` - демонстрация гибридных тестов WEB и API (например, авторизация через API)
<p>Подключена система отчетности Allure Reports с вложениями (логи, скриншоты, видео и пр.). 
<p>В UI-тестах шаги отображены в виде степов через `with allure.step`
<p>Также по факту прохождения теста отправляется уведомление с результатами в Telegram.
<p>Браузер в UI-тестах запускается удаленно в Selenoid.

## :heavy_check_mark: Кратко
- [x] `API` тесты
- [x] `Гибридные` тесты (API + WEB)
- [x] `Параметризованный` запуск тестов
- [x] Запуск WEB тестов, используя `Jenkins` и `Selenoid`
- [x] `Allure Reports` с вложениями (логи, скриншоты, видео)
- [x] Отправка результатов тестирования в `Telegram`
