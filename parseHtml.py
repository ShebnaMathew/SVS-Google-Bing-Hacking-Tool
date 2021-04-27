from html.parser import HTMLParser
from html.entities import name2codepoint

class ParseHtml(HTMLParser):

    def __init__(self):
        HTMLParser.__init__(self)
        self.results_tag = False
        self.cite = False
        self.results = []
        self.result = ""
        
    def handle_starttag(self, tag, attrs):
        
        '''
        if tag == 'div':
            for attr in attrs:
                print("     attr:", attr)
                if attr[0] == 'id' and attr[1] == 'b_content':
                    self.results_tag = True
                    print('got it')
        '''
        if tag == 'cite':
            #print("Start tag:", tag)
            self.cite = True
            self.result = ""

    def handle_endtag(self, tag):
        
        if tag == 'cite':
            #print("End tag  :", tag)
            self.cite = False
            self.results.append(self.result)

    def handle_data(self, data):
        
        if self.cite:
            #print("Data     :", data)
            self.result += data

    def get_results(self):
        return self.results

    def is_site_in_results(self, site):
        for each in self.results:
            print("url:", each)
            if site in each:
                return True, each
        return False, ""
            
