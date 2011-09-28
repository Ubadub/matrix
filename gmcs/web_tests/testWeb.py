from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re, os

class AllPagesEmptyChoices(unittest.TestCase):
    '''Check that all the pages load with an empty choices file'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://uakari.ling.washington.edu/matrix/test/matrix.cgi"
        self.verificationErrors = []
    
    def test_all_pages_empty_choices(self):
        driver = self.driver
        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("General Information").click()
        try: self.assertEqual("General Information", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Number").click()
        driver.find_element_by_link_text("Number").click()
        self.assertEqual("Number", driver.find_element_by_css_selector("h2").text)
#        except AssertionError as e: self.verificationErrors.append(str(e))
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.back()
        driver.find_element_by_link_text("Word Order").click()
        try: self.assertEqual("Word Order", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.back()
        driver.find_element_by_link_text("Person").click()
        try: self.assertEqual("Person", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Gender").click()
        try: self.assertEqual("Gender", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Case").click()
        try: self.assertEqual("Case", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Direct-inverse").click()
        try: self.assertEqual("Direct-inverse", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Tense, Aspect and Mood").click()
        try: self.assertEqual("Tense, Aspect and Mood", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Other Features").click()
        try: self.assertEqual("Other Features", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Sentential Negation").click()
        try: self.assertEqual("Sentential Negation", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Coordination").click()
        try: self.assertEqual("Coordination", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Matrix Yes/No Questions").click()
        try: self.assertEqual("Matrix Yes/No Questions", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Argument Optionality").click()
        try: self.assertEqual("Argument Optionality", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Lexicon").click()
        try: self.assertEqual("Lexicon", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Test Sentences").click()
        try: self.assertEqual("Test Sentences", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
#        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_link_text("Test by Generation Options").click()
        try: self.assertEqual("Test by Generation Options", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

class AllPagesJamamadiChoices(unittest.TestCase):
    '''Check thatt all the pages load with a valid choices file'''
    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.implicitly_wait(30)
        self.base_url = "http://uakari.ling.washington.edu/matrix/test/matrix.cgi"
        self.verificationErrors = []
    
    def test_all_pages_jamamadi_choices(self):
        driver = self.driver
        driver.get("http://uakari.ling.washington.edu/matrix/test/matrix.cgi")
        driver.find_element_by_name("choices").clear()
        driver.find_element_by_name("choices").send_keys(os.path.abspath("./gmcs/web_tests/web_choices/Jamamadi_choices.txt"))
        driver.find_element_by_css_selector("form[name=\"choices_form\"] > p > input[type=\"submit\"]").click()
        driver.find_element_by_link_text("General Information").click()
        try: self.assertEqual("General Information", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Word Order").click()
        driver.find_element_by_link_text("Word Order").click()
        try: self.assertEqual("Word Order", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Number").click()
        try: self.assertEqual("Number", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Person").click()
        try: self.assertEqual("Person", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Gender").click()
        try: self.assertEqual("Gender", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Case").click()
        try: self.assertEqual("Case", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Direct-inverse").click()
        try: self.assertEqual("Direct-inverse", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Tense, Aspect and Mood").click()
        try: self.assertEqual("Tense, Aspect and Mood", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Other Features").click()
        try: self.assertEqual("Other Features", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Sentential Negation").click()
        try: self.assertEqual("Sentential Negation", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Coordination").click()
        try: self.assertEqual("Coordination", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Matrix Yes/No Questions").click()
        try: self.assertEqual("Matrix Yes/No Questions", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Argument Optionality").click()
        try: self.assertEqual("Argument Optionality", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Lexicon").click()
        try: self.assertEqual("Lexicon", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Test Sentences").click()
        try: self.assertEqual("Test Sentences", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
        driver.back()
        driver.find_element_by_link_text("Test by Generation Options").click()
        try: self.assertEqual("Test by Generation Options", driver.find_element_by_css_selector("h2").text)
        except AssertionError as e: self.verificationErrors.append(str(e))
    
    def is_element_present(self, how, what):
        try: self.driver.find_element(by=how, value=what)
        except NoSuchElementException, e: return False
        return True
    
    def tearDown(self):
        self.driver.quit()
        self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":
    unittest.main()
