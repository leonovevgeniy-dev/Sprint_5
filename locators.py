from selenium.webdriver.common.by import By


# ===== ГЛАВНАЯ СТРАНИЦА =====
# Заголовок страницы
PAGE_TITLE = (By.XPATH, "//h1[text()='Соберите бургер']")

# Кнопка "Войти в аккаунт" на главной
LOGIN_BUTTON_MAIN = (By.XPATH, "//button[text()='Войти в аккаунт']")

# Кнопка "Личный кабинет"
PERSONAL_ACCOUNT_BUTTON = (By.XPATH, "//a[@href='/account']")

# Навигация
CONSTRUCTOR_BUTTON = (By.XPATH, "//p[text()='Конструктор']")  # Кнопка "Конструктор"
LOGO_BUTTON = (By.CLASS_NAME, "AppHeader_header__logo__2D0X2")  # Логотип Stellar Burgers

# Разделы конструктора
BUNS_SECTION = (By.XPATH, "//span[text()='Булки']/parent::div")  # Раздел "Булки"
SAUCES_SECTION = (By.XPATH, "//span[text()='Соусы']/parent::div")  # Раздел "Соусы"
FILLINGS_SECTION = (By.XPATH, "//span[text()='Начинки']/parent::div")  # Раздел "Начинки"

# Активный раздел конструктора
ACTIVE_SECTION = (By.XPATH, "//div[contains(@class, 'tab_tab_type_current')]")


# ===== СТРАНИЦА ВХОДА =====
# Поле ввода Email
EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле ввода пароля
PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

# Кнопка "Войти"
LOGIN_SUBMIT_BUTTON = (By.XPATH, "//button[text()='Войти']")

# Ссылка "Зарегистрироваться"
REGISTER_LINK = (By.XPATH, "//a[@href='/register']")

# Ссылка "Восстановить пароль"
FORGOT_PASSWORD_LINK = (By.XPATH, "//a[@href='/forgot-password']")


# ===== СТРАНИЦА РЕГИСТРАЦИИ =====
# Поле ввода имени
NAME_INPUT = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

# Поле ввода email
REGISTER_EMAIL_INPUT = (By.XPATH, "//label[text()='Email']/following-sibling::input")

# Поле ввода пароля
REGISTER_PASSWORD_INPUT = (By.XPATH, "//label[text()='Пароль']/following-sibling::input")

# Кнопка "Зарегистрироваться"
REGISTER_BUTTON = (By.XPATH, "//button[text()='Зарегистрироваться']")

# Ссылка "Войти"
REGISTER_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")

# Ошибка некорректного пароля
PASSWORD_ERROR = (By.XPATH, "//p[contains(@class, 'input__error')]")


# ===== СТРАНИЦА ВОССТАНОВЛЕНИЯ ПАРОЛЯ =====
# Ссылка "Войти" на странице восстановления
FORGOT_LOGIN_LINK = (By.XPATH, "//a[@href='/login']")


# ===== ЛИЧНЫЙ КАБИНЕТ =====
# Поле "Имя" в профиле
PROFILE_NAME = (By.XPATH, "//label[text()='Имя']/following-sibling::input")

# Поле "Логин" (email) в профиле
PROFILE_EMAIL = (By.XPATH, "//label[text()='Логин']/following-sibling::input")

# Кнопка "Выход"
LOGOUT_BUTTON = (By.XPATH, "//button[text()='Выход']")