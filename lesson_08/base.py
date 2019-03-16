class base():
    def __init__(self,driver):
        self.driver = driver
     #id
    def by_id(self,element):
        return  self.driver.find_element_by_id(element)
    #name
    def by_name(self,element):
        return self.driver.find_element_by_name(element)
    #xpath
    def by_xpath(self,element):
        return  self.driver.find_element_by_xpath(element)
    #css
    def by_css(self,element):
        return  self.driver.find_element_by_css_selector(element)
    #url
    def dr_url(self):
        return self.driver.current_url
