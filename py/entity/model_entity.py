# -*- coding:utf-8 -*-

#model实例
class Model:

    def __init__(self, model_name,model_no,model_factory,model_size,model_texture,model_document):

        self.__model_name = model_name
        self.__model_no = model_no
        self.__model_factory = model_factory
        self.__model_size = model_size
        self.__model_texture = model_texture
        self.__model_document = model_document



    def __str__(self):
        return ' '.join((self.__model_name,self.__model_no,self.__model_factory,self.__model_size,self.__model_texture,self.__model_document))


    def get_model_name(self):
        return self.__model_name
    def set_model_name(self, model_name):
        self.__model_name = model_name

    def get_model_no(self):
        return self.__model_no


    def get_model_factory(self):
        return self.__model_factory
    def set_model_factory(self, model_factory):
        self.__model_factory = model_factory


    def get_model_size(self):
        return self.__model_size
    def set_model_size(self, model_size):
        self.__model_size = model_size



    def get_model_texture(self):
        return self.__model_texture
    def set_model_texture(self, model_texture):
        self.__model_texture = model_texture


    def get_model_document(self):
        return self.__model_document
    def set_model_document(self, model_document):
        self.__model_document = model_document

