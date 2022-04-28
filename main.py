from ckan import create_dataset, create_resource
from models import Dataset, Resource


def main():
    """ Crear recurso con url """
    # r = Resource(
    #     package_id='el-dataset',
    #     name="El recurso",
    #     upload='/Users/ddazal/Desktop/mtcars.csv'
    # )
    # create_resource(resource=r)
    """ Crear conjunto de datos sin recursos """
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
    pass


if __name__ == '__main__':
    main()
