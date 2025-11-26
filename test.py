import os
from dotenv import load_dotenv

load_dotenv()

debug = bool(os.environ.get('DEBUG'))
print(debug, type(debug))

