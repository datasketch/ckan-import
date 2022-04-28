import json
import os
import requests
from dotenv import load_dotenv

from models import Dataset, Resource

load_dotenv()

token = os.getenv('CKAN_API_TOKEN')
ckan_site_url = os.getenv('CKAN_SITE_URL')
ckan_host = ckan_site_url[0:-1] if ckan_site_url.endswith('/') else ckan_site_url
headers = {'Authorization': token}


def create_dataset(dataset: Dataset):
    response = requests.post(
        '{}/api/3/action/package_create'.format(ckan_host),
        json=dataset.dict(),
        headers=headers
    )
    print(json.dumps(response.json(), indent=2))


def create_resource(resource: Resource):
    if not resource.upload and not resource.url:
        raise SystemExit(
            'Neither a resource url nor a upload file was specified'
        )

    if resource.url:
        response = requests.post(
            '{}/api/3/action/resource_create'.format(ckan_host),
            json=resource.dict(),
            headers=headers
        )
    else:
        response = requests.post(
            '{}/api/3/action/resource_create'.format(ckan_host),
            json=resource.dict(),
            headers=headers,
            files=[('upload', open(resource.upload))]
        )
    print(json.dumps(response.json(), indent=2))
