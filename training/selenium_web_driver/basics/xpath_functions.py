# Used to find dynamic web elements Xpath function "starts-with"
"""
//tagname[starts-with(@attribute,'value')]

/html/body/div[@class="w2-content w2-container w2-border w2-border-radius-20"]/div[@class="icon-container "]/div[@class="icons "]/div[@class="icon-wrapper" ]
"""

# to find dynamic web elements use "contains" function
"""
syntax is:
//tagname[contains(@attribute,"value")]

/html/body/div[@id="projects"]/div/div/div/p/i[contains(@class,'fa')]
"""

# to find dynamic elements using contains
"""
syntax is:
//tagname[contains(@attribute,"value")]

//button[contains(@id,"342")] actual search button at our Salesforce page
"""

# to find an element with exact text match use text function
"""
syntax is:
//tagname[text()='value']

//div[text()="New"][@title="New"]
"""

# To find an element using more that one attribute use "and" & "or" functions
"""
//tagname[@attribute1="value1" and @attribute2="value2"]
//tagname[@attribute1="value1" or @attribute2="value2"]

//a[@title="New" or @title="Intelligence View" and @role="button"]

"""

# xpath axes methods to find elements (parent, child, self, sibling, ancestor, descendant)
"""
//tagname[@attribute="value"]//parent::tagname
//tagname[@attribute="value"]//child::tagname
//tagname[@attribute="value"]//self::tagname
//tagname[@attribute="value"]//sibling::tagname
//tagname[@attribute="value"]//ancestor::tagname
//tagname[@attribute="value"]//descendant::tagname 

"""

# ID selection
"""
"""

# ID selection
"""
"""