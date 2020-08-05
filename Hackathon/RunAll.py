import sys
from GlobalVar import Max
# insert at 1, 0 is the script path (or '' in REPL)
sys.path.insert(1, '/Users/test/Documents/python/Py_Programs/Hackathon/Deaths')
Countries = 'Germany,France' 
days = Max
import GetFiles
from WriteDeaths import full
full(days)
from ReadDeaths import full
full(days)
from ManageFiles import full
full()
from Countries import full
full(Countries)
from UI import full
full()