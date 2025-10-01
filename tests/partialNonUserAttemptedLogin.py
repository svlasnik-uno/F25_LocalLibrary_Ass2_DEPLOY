'''

        try:
            # attempt to find the 'Logout' button - if found, logged in successfully
            elem = driver.find_element(By.XPATH, "/html/body/nav/div/ul/li/form/button")
            print('login successful')
            assert elem.is_displayed()

        except NoSuchElementException:
            print('login unsuccessful - check the username')



'''