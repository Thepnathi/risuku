# NewsAPI.org
from dotenv import load_dotenv
from pathlib import Path
import os
import requests

load_dotenv(verbose=True)
env_path = Path('.') / '.env'

API_KEY = os.getenv("GOOGLE_API_KEY")

def results(request, question_id):
    response = f"You are looking at results of question %s"
    return HttpResponse(response % question_id)

def latest_news(request, question_id): 
    url = (f'http://newsapi.org/v2/top-headlines?country=us&apiKey={API_KEY}')
    response = request.get(url)
    assert 0 <= len(response) <= 25
    return response

