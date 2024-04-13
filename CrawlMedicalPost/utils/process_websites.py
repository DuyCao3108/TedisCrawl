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

class vinmec():
    def __init__(self, inputDict):
        self.inputDict = inputDict
        self.base_url = BASEURL_WEBSITE_TO_CRAWL["vinmec"]
    def create_start_url(self):
        keyword = self.inputDict['keyword']
        start_url = self.base_url + "bai-viet/tim-kiem/?q="

        keyword_splited = keyword.split(" ")
        start_url += keyword_splited[0]

        if len(keyword_splited) <= 1: return start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"%20{character}"
            return start_url

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

        if len(keyword_splited) <= 1: return start_url 
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

        if len(keyword_splited) <= 1: return start_url 
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

        if len(keyword_splited) <= 1: return start_url 
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

        if len(keyword_splited) <= 1: return start_url 
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

        if len(keyword_splited) <= 1: return start_url 
        else:
            for character in keyword_splited[1:]:
                start_url += f"+{character}"
            return start_url
    
def get_query_keyword(from_web, keyword):
    if from_web == "suckhoedoisong":
        keyword_splited = keyword.split(" ")
        query_keyword = ""

        query_keyword += keyword_splited[0]
        
        if len(keyword_splited) <= 1: return query_keyword
        else:
            for character in keyword_splited[1:]:
                query_keyword += f"%20{character}"
            return query_keyword
        
    elif from_web == "vinmec":
        keyword_splited = keyword.split(" ")
        query_keyword = ""

        query_keyword += keyword_splited[0]
        
        if len(keyword_splited) <= 1: return query_keyword
        else:
            for character in keyword_splited[1:]:
                query_keyword += f"%20{character}"
            return query_keyword
