

def test_default_value(app):

    app.main_page.open_main_page()
    app.session.response_code()
    app.booking_widget.open_booking_widget()
    app.session.assert_element_is_selected(app, locator=app.booking_widget_locators.GUESTS_DEFAULT_VALUE)
    app.session.assert_element_is_selected(app, locator=app.booking_widget_locators.ROOM_DEFAULT_VALUE)
