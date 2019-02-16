from selenium.webdriver.common.by import By


class BookingWidgetLocators(object):
  OPEN_WIDGET          = (By.XPATH, "//*[contains(text(), 'Book now')]")
  ADVANCED_OPTIONS     = (By.XPATH, "//*[contains(text(), 'Advanced Options')]")
  CHECK_AVAILABILITY   = (By.XPATH, "//*[@id='dropdown-book-js']/div/div[3]/input")
  HOTEL_FLIGHT         = (By.XPATH, "//*[contains(text(), 'Hotel + Flight')]")
  INDUSTRY_ID          = (By.CSS_SELECTOR, "div[class*='book-industry-id-content-js show']")
  GUESTS_DEFAULT_VALUE = (By.XPATH, "//*[contains(text(), '2 Guests')]")
  ROOM_DEFAULT_VALUE   = (By.XPATH, "//*[contains(text(), '1 Room')]")
  CALENDAR_CHECK_IN    = (By.CSS_SELECTOR, "[class='md-datepicker-input']")
  CALENDAR_CHECK_OUT   = (By.CSS_SELECTOR, "[aria-label='Check In']")
  CALENDAR_NEXT_MONTH  = (By.CSS_SELECTOR, "[aria-label='Check Out']")
  CALENDAR_DATE        = (By.CSS_SELECTOR, "[class='md-calendar-date-selection-indicator']")
  FLYING_FROM          = (By.CSS_SELECTOR, "[id='airport-autocomplete-js']")

class Common(object):
  CLOSE_COOKIES_NOTIFICATION = (By.CSS_SELECTOR, "[class*=cerrar]")
