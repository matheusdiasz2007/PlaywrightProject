from time import sleep
from playwright.sync_api import sync_playwright


with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)

    page = browser.new_page()
    page.goto('http://localhost:8000/')

    page.locator('#username').fill('pylive')
    page.locator('#password').fill('pylive004')
    page.locator('xpath=//button[@class="btn btn-primary"]').click()

    page.locator('xpath=//i[@class="bi bi-truck fs-4"]').click()

    page.locator('xpath=//i[@class="bi bi-plus"]').click()

    page.locator('#id_name').fill('Positivo do Brasil LTDA')
    page.locator('#id_description').fill('Marca boa de Notebooks #confia')
    page.locator('xpath=//button[@class="btn btn-primary"]').click()

    sleep(10)

    browser.close()
