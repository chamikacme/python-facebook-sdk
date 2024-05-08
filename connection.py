import facebook as fb
import os
from dotenv import load_dotenv

load_dotenv()
access_token = os.getenv('PAGE_ACCESS_TOKEN')

pageApi = fb.GraphAPI(access_token)