import allure


def add_html(browser):
    html = browser.driver.page_source
    allure.attach(body=html, name='page_source', attachment_type=allure.attachment_type.HTML, extension='.html')


def add_screenshot(browser):
    png = browser.driver.get_screenshot_as_png()
    allure.attach(body=png, name='screenshot', attachment_type=allure.attachment_type.PNG, extension='.png')


def add_logs(browser):
    log = ''.join(f'{text}\n' for text in browser.driver.get_log(log_type='browser'))
    allure.attach(log, 'browser_logs', allure.attachment_type.TEXT, '.log')


def add_video(browser):
    video_url = 'https://selenoid.autotests.cloud/video/' + browser.driver.session_id + '.mp4'
    html = ("<html><body><video width='100%' height='100%' controls autoplay><source src='"
            + video_url + "' type='video/mp4'></video></body><html>")
    allure.attach(html, 'video_' + browser.driver.session_id, allure.attachment_type.HTML, '.html')
