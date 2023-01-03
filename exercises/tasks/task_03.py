from exercises.tasks.resource_03 import open_kiwi_website


# Sidebar actions (expanding options, verifying visibility of items)
def test_sidebar_actions_work_as_expected(page):
    # 1. On the Kiwi.com website hit the right sidebar hamburger button
    # 1.1. Open the kiwi.com website
    open_kiwi_website(page)

    # 1.2. Hit the right sidebar hamburger button
    page.click("[data-test=]")
    page.wait_for_selector("[data-test=][aria-hidden=]", state="")

    # 2. Verify a sidebar with the "Manage your trips, set up price alerts, use Kiwi.com Credit, and get personalized
    # support." text appears
    expected_sidebar_text = ""
    current_sidebar_text = page.locator("[data-test=] [class*=]").first.inner_text()
    assert "???" == "???"

    # 3. Hit the Discover button
    page.click("")

    # 4. Verify the Discover button expands into a dropdown/slide of items
    assert page.is_visible("")

    # 5. Verify the Subscribe to newsletter button is displayed
    assert page.is_visible("")

    # 6. Verify the Stories button is displayed
    assert page.is_visible("")

    # 7. Hit the Subscribe to newsletter button
    page.click("")

    # 8. Verify the sidebar disappears
    page.wait_for_selector("[data-test=][aria-hidden=]", state="")

    # 9. Verify a modal with the "Subscribe to the Kiwi.com newsletter" heading is displayed
    page.wait_for_selector("[class*=]", state="")
    assert page.is_visible("")

    # 10. Verify the modal can be closed by hitting the cross button in its top right corner
    page.click("")
    page.wait_for_selector("[class*=]", state="")