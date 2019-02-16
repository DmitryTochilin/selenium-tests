

def test_insert_promocode_from_url_parameter(app):

    value = app.session.random_value()
    app.wd.get(app.base_url + "?some=0&promo={}".format(value))
    app.session.close_cookies_notification()
    app.booking_widget.open_booking_widget()
    app.session.click(app.booking_widget_locators.ADVANCED_OPTIONS)
    app.session.click(app.booking_widget_locators.CHECK_AVAILABILITY)
    app.booking_widget.browser_log_parsing(app, search='Redirecting', value=value)
