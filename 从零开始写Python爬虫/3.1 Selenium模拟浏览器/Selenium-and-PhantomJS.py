
# coding: utf-8

# In[215]:


from selenium import webdriver


# In[216]:


from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


# In[217]:


from selenium.webdriver.common.action_chains import ActionChains


# In[218]:


dcap = dict(DesiredCapabilities.PHANTOMJS)  #设置userAgent


# In[219]:


# dcap["phantomjs.page.settings.loadImages"] = False


# In[220]:


dcap["phantomjs.page.settings.userAgent"] = ("Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36")


# In[221]:


browser = webdriver.PhantomJS(executable_path=r"D:\phantomjs\bin\phantomjs.exe",desired_capabilities=dcap)


# In[222]:


browser.set_window_size(1440, 900)


# In[223]:


url = 'https://www.baidu.com'


# In[224]:


url_pilz = 'https://www.pilz.com/zh-CN'


# In[225]:


browser.get(url_pilz)


# In[226]:


browser.implicitly_wait(3)


# In[227]:


agent = browser.execute_script("return navigator.userAgent")


# In[228]:


agent


# In[229]:


button = browser.find_element_by_class_name("togglesearch")


# In[230]:


button.click()


# In[231]:


text = browser.find_element_by_id("search--desktop--field")


# In[232]:


text.clear()


# In[233]:


text.send_keys('multi')


# In[234]:


button = browser.find_element_by_class_name("btn-primary")


# In[235]:


button.click()


# In[236]:


browser.current_url


# In[240]:


results = browser.find_elements_by_class_name('result')


# In[243]:


for result in results:
    if '.pdf' in result.get_attribute('href'):
        print(result.get_attribute('href'))

