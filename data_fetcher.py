import requests


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
    api_url = f'https://api.api-ninjas.com/v1/animals?name={animal_name}'
    response = requests.get(api_url, headers={'X-Api-Key': 'XL3dO8k9/+HKpwX1qvA4zg==CHisXjRa9dlCb83o'})
    
    if response.status_code == requests.codes.ok:
        return response.json()
    else:
        return None 