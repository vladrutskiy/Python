# General XPATH rules
"""
Xpath=//tagname[@Attribute="value"]
/html/body/div/h1
/html/body/div[18]/div/div/form/div[1]/div[1]/input

Absolute xpath: /html/body/div[18]/div/div/form/div[1]/div[1]/input
/html/body/div[@class="w3-top"]/div[@id="myNavbar"]/a[@href="#projects"]

Relative xpath: //tagname[@Attribute="value"]

"""

# ID or class selection
"""
//*[@id="about"]  //*[@class="firstname"] //span[@id="nameError"]
"""

# Combining several attributes
"""
//input[@id="name"][@name="name"][@placeholder="John"] 

/html/body/div[@class="w3-top"]/div[@id="myNavbar"]/a[@href="#projects"]
"""

