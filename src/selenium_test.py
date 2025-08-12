from selenium import webdriver

# Пример: открываем браузер и сайт
driver = webdriver.Chrome()  # или Firefox, если используешь GeckoDriver
driver.get("https://example.com")
print(driver.title)
driver.quit()
