import pandas as pd
import requests
import json
import os
from dotenv import load_dotenv

# Getting the api key from .env
load_dotenv()
API_KEY = os.getenv("RIOT_API_KEY")