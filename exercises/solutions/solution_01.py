# Navigate to the Kiwi.com website and verify the "Book cheap flights other sites simply can’t find." text is displayed.
def test_navigate_to_kiwi(page):
    # 1. Open the kiwi.com website
    page.goto("https://www.kiwi.com/en/")

    # 2. Accept cookies by clicking the appropriate button
    page.click("[data-test='CookiesPopup-Accept']")

    # 2. Assert the expected text is displayed
    assert page.is_visible("text=Book cheap flights other sites simply can’t find.")
