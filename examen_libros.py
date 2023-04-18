from Examen_libros import collection
import json


def read_titulos(id=None):
    if id is not None:
        query = {"_id": id}
        document = collection.find_one(query)
        print(document)
    else:
        documents = collection.find()
        for document in documents:
            print(document)


def create_titulo(json_titulo):
    result = collection.insert_one(json_employees)
    print(result.inserted_id)


def update_titulos(id, json_titulos_update):
    query = {"_id": id}
    new_values = {"$set": json_titulo_update}
    result = collection.update_one(query,values)
    print(result.modified_count)