import logging
import os
from datetime import date

class Logger:
   __instance = None
   log_path = "log"

   @staticmethod 
   def getInstance():
      if Logger.__instance == None:
         Logger()
      return Logger.__instance

   def __init__(self):
      if Logger.__instance is None:
         Logger.__instance = self
         # get current root path
         project_root_path = os.path.abspath(os.path.join(os.path.dirname(__file__),".."))
         # log path
         log_path = project_root_path + '/' + self.log_path + '/'
         # create folder if not  exists
         if not os.path.exists(log_path):
            os.makedirs(log_path)
         # generate file name
         log_file_name = log_path + date.today().strftime("%b-%d-%Y") + '.log'
         # generate file mode: write if not exists or red if already created
         log_file_mode = 'a' if os.path.isfile(log_file_name) else 'w'
         # config logging
         logging.basicConfig(
            format = '%(asctime)s - %(levelname)s - %(message)s', 
            datefmt = '%d-%b-%y %H:%M:%S', 
            filename = log_file_name, 
            level=logging.DEBUG, filemode = log_file_mode
         )

         self.log = logging