

def test_calendar(app):

    app.main_page.open_main_page()
    app.booking_widget.open_booking_widget()
    app.session.click(app.booking_widget_locators.CALENDAR_CHECK_IN)
    app.session.click(app.booking_widget_locators.CALENDAR_DATE)
    app.session.click(app.booking_widget_locators.CALENDAR_CHECK_OUT)
    app.session.click(app.booking_widget_locators.CALENDAR_DATE)
    app.session.click(app.booking_widget_locators.CHECK_AVAILABILITY)
    app.session.response_code()
