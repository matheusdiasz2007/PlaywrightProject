<<<<<<< HEAD
from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme='dark',
        **p.devices['iPhone 14'],
    )
    page = context.new_page()
    page.goto('https://matheusdiasz2007.github.io/Portfolio-Site/')
    print(page.title())

    sleep(60)

    browser.close()
=======
from playwright.sync_api import sync_playwright
from time import sleep

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    context = browser.new_context(
        color_scheme='dark',
        **p.devices['iPhone 14'],
    )
    page = context.new_page()
    page.goto('https://matheusdiasz2007.github.io/Portfolio-Site/')
    print(page.title())

    sleep(60)

    browser.close()
>>>>>>> 45d172c (add)
