import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def pytest_addoption(parser):
    parser.addoption('--language', action='store', default=None,
                     help="Choose language: ru or en or fr")


@pytest.fixture(scope="function")
def browser(request):
    null = None
    user_language = request.config.getoption("language")

    if user_language != null:
        options = Options()
        options.add_experimental_option('prefs', {'intl.accept_languages': user_language})
        browser = webdriver.Chrome(options=options)
    else:
        raise pytest.UsageError("--language should be ru or en or fr")
    yield browser
    print("\nquit browser..")
    browser.quit()