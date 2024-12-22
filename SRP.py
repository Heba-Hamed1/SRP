#The single responsibility principle
#his violates the SRP.
class FileHandler :
    def read_file(self,file_path):
        pass
    
    def write_file(self,file_path,data):
        pass
    
    def process_file(self,data):
        pass
    
    def analyze_data(self,data):
        pass
    
    
class ReportGenerator:
    def generate_report(self,data):
        pass
    
# how we solve this usig SRP 
class FileHandler :
    def read_file(self,file_path):
        pass
    
    def write_file(self,file_path,data):
        pass
    
class DataAnalyze:
    def analyze_data(self,data):
        pass
    
    
class ReportGenerator:
    def generate_report(self,data):
        pass
    