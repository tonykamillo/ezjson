#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re, datetime

def encode(o, date_format='%Y/%m/%d', max_depth=3):
    return dump(o, date_format='%Y/%m/%d', max_depth=3)

def decode(json, to_object=False):
    load(json, to_object=False)

def dump(o, date_format='%Y/%m/%d', max_depth=3):
    '''shortcut to Json.encode'''
    return Json.encode(o, date_format, max_depth)

def load(json, to_object=False):
    '''shortcut to Json.decode'''
    return Json.decode(json, to_object)

class Json(object):
    __depth = 0
    __max_depth = None
    __date_format = None

    @classmethod
    def __normalize(self, o):
        '''creates the pairs key/value, in json format, of each attribute of the python object, recursively'''
        json = ''

        if type(o) in (list, tuple):
            json = "[%s]" % ', '.join([str(self.__normalize(i)) for i in o if self.__normalize(i) ])
        elif self.__depth < self.__max_depth and hasattr(o, '__dict__') or type(o) == dict:
            self.__depth += 1
            dic = vars(o) if hasattr(o, '__dict__') else o
            json = "{%s}" % ', '.join( [ "\"%s\":%s" % (k, self.__normalize(v)) for k, v in dic.items() if self.__normalize(v) and not re.match('^_', str(k)) ] )
            self.__depth -= 1
        else:
            json = self.__build_js_values(o)
        return json

    @classmethod
    def __build_js_values(self, v):
        '''builds json atomic values (like number, string, booleans...) from python constants e objects'''
        if type(v) in (bool, int, long, float, str, unicode, datetime.datetime, datetime.date, datetime.time) or v is None:
            if type(v) is bool:
                v = "false" if v is False else "true"
            elif type(v) is long:
                v = int(v)
            elif isinstance(v, basestring):
                if type(v) is unicode: v = v.encode('u8')
                v = "\"%s\"" % v
            elif isinstance(v, datetime.datetime) or isinstance(v, datetime.date) or isinstance(v, datetime.time):
                v = "\"%s\"" % v.strftime(self.__date_format)
            elif v is None:
                v = "null"
            return v
        return False

    @classmethod
    def __build_py_values(self, json):
        '''converts some javascript constants to python constants'''
        json = re.sub('null|undefined', 'None', json)
        json = re.sub('false', 'False', json)
        return re.sub('true', 'True', json)

    @classmethod
    def __d2o(self, dic):
        '''d2o means dictionary to object. this method creates an object from a dict'''
        o = DynaObject()
        for k, v in dic.items():
            if type(v) == dict:
                v = self.__d2o(v)
            setattr(o, k, v)
        return o

    @classmethod
    def encode(self, o, date_format='%Y/%m/%d', max_depth=1):
        '''
        Creates the json. you may specify the date format for attributes of types datetime.datetime, datetime.date or datetime.time.
        Also, its possible specify the max value to depth of the json serialization, in other words, you may decide how far the
        json serialization can achieve. Like objects inside another objects.
        '''
        self.__date_format = date_format
        self.__max_depth = max_depth
        return self.__normalize(o)

    @classmethod
    def decode(self, json, to_object=False):
        '''Create one python object or dictionary from json'''
        dic = eval(self.__build_py_values(json))
        return self.__d2o(dic) if to_object else dic

class DynaObject(object):
    pass

