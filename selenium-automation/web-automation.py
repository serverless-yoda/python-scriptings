from selenium import webdriver

# driver can be found here: https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/
edge_browser = webdriver.Edge('./msedgedriver')
edge_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')
assert "Selenium Easy" in edge_browser.title

show_message_button = edge_browser.find_element_by_class_name('btn-default')
print(show_message_button.get_attribute('innerHTML'))

assert "Show Message" in edge_browser.page_source
user_message= edge_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('selenium')


show_message_button.click()
display_message = edge_browser.find_element_by_id('display')
assert 'selenium' in display_message.text

