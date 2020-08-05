import sys
from GlobalVar import Max
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/test/Documents/python/Py_Programs/Hackathon/Deaths')
Countries = 'Germany,France' 
days = Max
import GetFiles
from Format import full
full(days)
from SpitProvinces import full
full(days)
from ManageFiles import full
full()
from UI import full
full()