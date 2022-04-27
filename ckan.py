import json
import os
import requests
from dotenv import load_dotenv

from models import Dataset

load_dotenv()


token = os.getenv('CKAN_API_TOKEN')
ckan_site_url = os.getenv('CKAN_SITE_URL')
ckan_host = ckan_site_url[0:-1] if ckan_site_url.endswith('/') else ckan_site_url


def create_dataset(dataset: Dataset):
    response = requests.post('{}/api/3/action/package_create'.format(ckan_host),
                             json=dataset.dict(), headers={'Authorization': token})
    print(json.dumps(response.json(), indent=2))
