from selenium import webdriver
class Test_001:
    def test_credence_001(self):
        driver = webdriver.Chrome()
        driver.maximize_window()
        driver.get("https://credence.in/")
        if driver.title=="Credence":
            driver.save_screenshot('E:\\CT14_NOTES\\Pytest_Class_Demo\\screenshots\\credence.PNG')
            driver.close()
            assert True

        else:
            print('you are at wrong place')
            driver.close()
            assert False

    def test_sum_002(self):
        a=2
        b=4
        sum=a+b
        if sum == 6:
            print('this is sum of a and b :',sum )
            assert True
        else:
            print('sum is not possible')
            assert False

