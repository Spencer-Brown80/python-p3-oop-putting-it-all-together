

class Book:
    def __init__(self, title, page_count):
        self._page_count = page_count
        self.title = title
        
    @property
    def page_count(self):
        return self._page_count
    
    @page_count.setter
    def page_count(self, page_count):
        if isinstance(page_count, int):
            self._page_count = page_count
        else:
            # import ipdb; ipdb.set_trace()  
            print("page_count must be an integer")

    def turn_page(self):
        print("Flipping the page...wow, you read fast!")

        
    
        