from ckan import create_dataset, create_resource
from models import Dataset, Resource


def main():
    """ Crear conjunto de datos """
    # d = Dataset(
    #     name='el-dataset',
    #     title="El dataset",
    #     private=False,
    #     owner_org='datasketch',
    #     author="David Daza",
    #     author_email="david@datasketch.co",
    #     maintainer="David Daza",
    #     maintainer_email="david@datasketch.co",
    #     notes="Notas sobre el conjunto de datos"
    # )
    # create_dataset(dataset=d)
    """ Crear recurso con archivo """
    # r = Resource(
    #     package_id='el-dataset',
    #     name="El recurso",
    #     upload='/path/to/file.csv'
    # )
    # create_resource(resource=r)
    """ Crear recurso con url """
    # r = Resource(
    #     package_id='el-dataset',
    #     name="El recurso",
    #     url='https://datosabiertos.bogota.gov.co/dataset/e8bbee49-fa9f-46d2-a357-3846db5a737e/resource/40ffd4bb-a09d-47e5-8d92-5f0c5dde65c5/download/parques_urbanos.csv'
    # )
    # create_resource(resource=r)
    pass


if __name__ == '__main__':
    main()
