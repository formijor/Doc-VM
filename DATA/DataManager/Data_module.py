'''
Created on 10 jul. 2021

@author: Jorge
'''


class DataQuery():
    def __init__(self):
        self.DataRead = DataRead()
        self.DataWrite = DataWrite()
    

class DataRead():
    def __init__(self):
        pass
    
    def get_all_docs(self):
        pass
    
    def get_doc(self, doc_id):
        pass
    
    def search_doc(self, dato):
        pass
    
    
class DataWrite():
    def __init__(self):
        pass
    
    def create_new_doc(self, datos):
        pass
    
    def delete_doc(self, doc_id):
        pass
    
    def update_doc(self, doc_id, data):
        pass
    
    def modify_doc(self, doc_id, data):
        pass