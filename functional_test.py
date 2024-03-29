# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import unittest

class NewVisitor(unittest.TestCase):
    def setUp(self):
        self.browser=webdriver.Firefox()
        self.browser.implicitly_wait(3)
    
    def tearDown(self):
        self.browser.quit()
        
    def test_can_start_a_list_and_retrieve_it_laster(self):
        self.browser.get('http://localhost:8000')
        
        self.assertIn('to-do',self.browser.title)
        head_text=self.browser.find_element_by_tag_name('h1').text
        self.assertIn('to-do',head_text)
        
        inputbox=self.browser.find_element_by_id("id_new_item")
        self.assertEqual(
                inputbox.get_attribute("placeholder"),
                'Enter a to_do item')
        inputbox.send_keys('buy peacock feathers')
        inputbox.send_keys(Keys.ENTER)
        
        table=self.browser.find_element_by_id('id_list_table')
        rows=table.find_elements_by_tag_name('tr')
        self.assertTrue(
                any(rows.text=='1: Buy peacock feathers' for row in rows),
                "New to_do item did not appear in tables"
                )
         
        self.fail('finish the test!')
        
if __name__=='__main__':
    unittest.main(warnings='ignore')

#browser = webdriver.Firefox()
#browser.get('http://localhost:8000')
#assert 'to-do' in browser.title
