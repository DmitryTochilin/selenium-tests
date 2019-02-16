class BookingWidget:

    def __init__(self, app):
        self.app = app

    def open_booking_widget(self):
        self.app.wd.find_element(*self.app.booking_widget_locators.OPEN_WIDGET).click()

    def browser_log_parsing(self, app, search, value):
        result = _not_found = object()
        log = app.wd.get_log('browser')
        for entry in log:
            if ('%s' % search) in entry['message']:
                result = entry['message']
                assert ('Promo={}'.format(value) in result)
                print(result)
        if result is _not_found:
            raise ValueError("'%s' is not found in browser log" % search)
