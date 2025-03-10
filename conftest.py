import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def pytest_addoption(parser):
    parser.addoption('--browser_name', action='store', default=None,
                     help="Choose browser: chrome or firefox")

    parser.addoption('--language', action='store', default='en',
                     help="Choose language: '--language=en' or '--language=ru'")

@pytest.fixture(scope="function")
def r_browser(request):
    browser_name = request.config.getoption("browser_name")
    user_language = request.config.getoption("language")

    options = Options()
    options.add_experimental_option(
        'prefs', {'intl.accept_languages': user_language})

    options_firefox = Options()
    options_firefox.set_preference("intl.accept_languages", user_language)

    r_browser = None
    if browser_name == "chrome":
        print("\nstart chrome browser for test..")
        r_browser = webdriver.Chrome(options=options)
    elif browser_name == "firefox":
        print("\nstart firefox browser for test..")
        r_browser = webdriver.Firefox(options=options_firefox)
    else:
        raise pytest.UsageError("--browser_name should be chrome or firefox")
    yield r_browser
    print("\nquit browser..")
    r_browser.quit()
