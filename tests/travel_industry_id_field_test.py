

def test_travel_industry_id_field(app):

    app.main_page.open_main_page()
    app.booking_widget.open_booking_widget()
    app.session.click(app.booking_widget_locators.ADVANCED_OPTIONS)
    assert(app.wd.find_element(*app.booking_widget_locators.INDUSTRY_ID).is_displayed())
    app.session.click(app.booking_widget_locators.HOTEL_FLIGHT)
    app.session.assert_is_not_displayed(locator=app.booking_widget_locators.INDUSTRY_ID)
