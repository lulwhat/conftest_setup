import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/"

def test_guest_can_add_product_to_basket(browser):
	browser.get(link)
	time.sleep(3)
	assert browser.find_element_by_css_selector(".btn-add-to-basket") \
		!= None, "No button"