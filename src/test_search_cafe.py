from base.GooglePage import GooglePage


def test_google_search(browser, load_expected_result, load_locators):
    google_main_page = GooglePage(browser)
    google_main_page.go_to_site()
    google_main_page.enter_word("Mamamia")
    google_main_page.click_on_the_search_button()
    google_main_page.find_elements_by_xpath(load_locators["get_all_links_from_frame"])[0].click()
    element = google_main_page.find_element_by_xpath(load_locators["get_first_found_element"])
    assert element.text == load_expected_result["address"]

