class MainPage:

    def __init__(self, app):
        self.app = app

    def open_main_page(self):
        self.app.wd.get(self.app.base_url)