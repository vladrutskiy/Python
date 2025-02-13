# ID selection
"""
looks like:  #username
"""

# Class adn other elements selection
"""
to choose class use dot: .hidden
or use it like this: input[name="username"] or input[class="hidden"]
"""

# Combining attributes to find unique element
"""
label[class="bold"][id="username"] - you can add numerous elements in []
"""

# Combining several attributes to find on the page using class and id
"""
we are using label with class and id here
label.bold#username
"""

#  sometimes the id's are dynamic to catch them there are several ways

# if the prefix is stable but the ending is changing 
"""
use ˆ sign  (alt + I) like this: input [idˆ= "dl_lkj_ "]
"""
# if the suffix is stable  
"""
use the $ sign like this: input [id$ = "_df_lku_"]
"""

# if the sub-string is stable 
"""
use * sign like this: input [id* = "_df_lku_"]
"""

# Next sibling selection
"""
looks like: select#month > option + option + option   this will help to select third month.
"""

# Pseudo Classes
""""
Pseudo classes: select#month :first-child 
to select other child you can use select#month :nth-child(7) 
to start selecting from the other side use elect#month :nth-last-child(7)
"""


