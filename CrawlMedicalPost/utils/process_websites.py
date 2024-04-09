from utils.constant import BASEURL_WEBSITE_TO_CRAWL

class ntLongChau():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["nhathuoclongchau"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"

        return start_url

class vinMec():
    pass

class helloBacsi():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["hellobacsi"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"

        return start_url
    
class medlatec():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["medlatec"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url + "/tim-kiem-thong-tin?keyword="

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"%20{character}"
        
        start_url+= "&type=bai-viet"

        return start_url

class suckhoedoisong():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["suckhoedoisong"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url + "/tim-kiem.htm?keywords="

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"%20{character}"

        return start_url
    
class tamanhhospital():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["tamanhhospital"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url + "/?s="

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"

        return start_url
    
class youmed():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["youmed"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"

        return start_url
    
class doctortuan():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["doctortuan"]

    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url + "/search?query="

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"

        return start_url
    
