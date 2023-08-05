from selene import browser, have
import configparser

# Read data from the configuration file (config.ini)
config = configparser.ConfigParser()
config.read('config.ini')

# Extract data from the configuration file
email = config.get('credentials', 'email')
password = config.get('credentials', 'password')

# Set a timeout for the browser actions
browser.config.timeout = 8

# This function will run after each test case to close the browser
def teardown_function():
    browser.quit()

# Test case for valid login
def test_valid_login():
    browser.open('https://qa.guru/cms/system/login')

    browser.element('.login-form [name=email]').type(email).press_tab()
    browser.element('[name=password]').type(password).press_enter()

    browser.element('.main-header__login').should(have.text('Личный кабинет'))

# Test case for invalid login with the wrong password
def test_invalid_login_with_wrong_password():
    browser.open('https://qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type(email).press_tab()
    browser.element('[name=password]').type('abrakadabra').press_enter()

    browser.element('.login-form .btn-success').should(have.exact_text('Неверный пароль'))

# Test case for invalid login with an empty password
def test_invalid_login_with_empty_password():
    browser.open('https://qa.guru/cms/system/login')
    browser.element('.login-form [name=email]').type(email).press_enter()

    browser.element('.login-form .btn-success').should(have.exact_text('Не заполнено поле Пароль'))


