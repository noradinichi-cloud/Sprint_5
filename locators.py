from selenium.webdriver.common.by import By


class MainPageLocators:
    # Кнопка «Войти в аккаунт» на главной странице
    LOGIN_ACCOUNT_BUTTON = (By.XPATH, "//button[text()='Войти в аккаунт']")
    # Кнопка «Личный кабинет» в шапке сайта
    PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//p[text()='Личный Кабинет']")
    # Кнопка «Конструктор» в шапке сайта
    CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")
    # Логотип «Stellar Burgers» в шапке сайта
    LOGO_BUTTON = (By.XPATH, "//div[contains(@class, 'AppHeader_header__logo')]")
    # Вкладка «Булки» в конструкторе
    BUNS_TAB = (By.XPATH, "//span[text()='Булки']/parent::div")
    # Вкладка «Соусы» в конструкторе
    SAUCES_TAB = (By.XPATH, "//span[text()='Соусы']/parent::div")
    # Вкладка «Начинки» в конструкторе
    FILLINGS_TAB = (By.XPATH, "//span[text()='Начинки']/parent::div")
    # Кнопка «Оформить заказ» (появляется на главной после успешного входа)
    ORDER_BUTTON = (By.XPATH, "//button[text()='Оформить заказ']")


class RegisterPageLocators:
    # Поле ввода «Имя» на странице регистрации
    NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")
    # Поле ввода «Email» на странице регистрации
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода «Пароль» на странице регистрации
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка «Зарегистрироваться» на странице регистрации
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")
    # Сообщение об ошибке при вводе некорректного пароля (менее 6 символов)
    PASSWORD_ERROR_TEXT = (By.XPATH, "//p[text()='Некорректный пароль']")
    # Ссылка «Войти» внизу формы регистрации
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class LoginPageLocators:
    # Заголовок «Вход» на странице авторизации
    LOGIN_HEADER = (By.XPATH, "//h2[text()='Вход']")
    # Поле ввода «Email» на странице входа
    EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")
    # Поле ввода «Пароль» на странице входа
    PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")
    # Кнопка «Войти» на странице входа
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Войти']")


class ForgotPasswordPageLocators:
    # Ссылка «Войти» на странице восстановления пароля
    LOGIN_LINK = (By.XPATH, "//a[text()='Войти']")


class ProfilePageLocators:
    # Ссылка «Профиль» в меню личного кабинета
    PROFILE_LINK = (By.XPATH, "//a[text()='Профиль']")
    # Кнопка «Выход» в личном кабинете
    LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")
