import requests
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_data(animal_name):
    """
    Fetches the animals data for the animal 'animal_name'.
    Returns: a list of animals, each animal is a dictionary:
    {
        'name': ...,
        'taxonomy': {
            ...
        },
        'locations': [
            ...
        ],
        'characteristics': {
            ...
        }
    }
    """
    api_key = os.getenv('API_KEY')
    
    if not api_key:
        raise ValueError("API_KEY environment variable is not set")
        
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': api_key})
    
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None 