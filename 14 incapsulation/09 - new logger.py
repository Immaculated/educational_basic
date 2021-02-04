from datetime import datetime

class Logger():
    
    def __init__(self, fname='log.data', start_time_zero=False):
        self.__fname = fname
        self.start_time_zero = start_time_zero
        self.count = 0
        self.start = None
    
    def config(self, fname, start_time_zero=False):
        self.__fname = fname
        self.start_time_zero = start_time_zero

    def info(self, text):
        self.out_with_tag(text, 'INFO')
    
    def error(self, text):
        self.out_with_tag(text, 'ERROR')
    
    def debug(self, text):
        self.out_with_tag(text, 'DEBUG')
            
    def out_with_tag(self, text, tag):
        if not self.start_time_zero:
            self.simple_log(text, tag)
        elif self.count == 0:
            self.set_start()
            self.start_log()
            self.not_simple_log(text, tag)
            self.count += 1
        else:
            self.not_simple_log(text, tag)

    def simple_log(self, text, tag):
        now = datetime.now()
        with open(self.__fname,'a') as f:
            f.write(tag + ' ' + datetime.strftime(now, "%Y.%m.%d %H:%M:%S ") +  text + '\n')

    def not_simple_log(self, text, tag):
        now = datetime.now() - self.start 
        with open(self.__fname,'a') as f:        
            f.write(tag + ' ' + str(now) + ' ' +  text + '\n')

    def start_log(self):
        now = datetime.now()
        with open(self.__fname,'a') as f:
            f.write('START TIME' + ' ' + datetime.strftime(now, "%Y.%m.%d %H:%M:%S ") + '\n')
    
    def set_start(self):
        self.start = datetime.now()
