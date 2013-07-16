#!/usr/bin/env python
#-*- coding:utf-8 -*-

import re, datetime, decimal


def encode(o, date_format='%Y/%m/%d', max_depth=3):
    return dump(o, date_format='%Y/%m/%d', time_format='%H:%M:%S', max_depth=3)


def decode(json, to_object=False):
    return load(json, to_object=False)


def dump(o, date_format='%Y/%m/%d', time_format='%H:%M:%S', max_depth=3):
    '''shortcut to Json.encode'''
    return Json.encode(o, date_format, max_depth)


def load(json, to_object=False):
    '''shortcut to Json.decode'''
    return Json.decode(json, to_object)


class Json(object):
    __depth = 0
    __max_depth = None
    __date_format = ''
    __time_format = ''
    __datetime_format = ''

    @classmethod
    def __normalize(self, o):
        '''creates the pairs key/value, in json format, of each attribute of the python object, recursively'''
        json = ''

        if type(o) in (list, tuple):
            arr = []
            for i in o:
                i = self.__normalize(i)
                if i:
                    arr.append(i)
            json = u'[%s]' % u', '.join(arr)

        elif self.__depth < self.__max_depth and hasattr(o, '__dict__') or type(o) == dict:
            self.__depth += 1
            dic = vars(o) if hasattr(o, '__dict__') else o
            arr = []
            for k, v in dic.items():
                v = self.__normalize(v)
                if v and not re.match('^_', str(k)):
                    arr.append(u'\"%s\":%s' % (k, v))
            json = u'{%s}' % ', '.join(arr)
            self.__depth -= 1
        else:
            json = self.__build_js_values(o)
        return json

    @classmethod
    def __build_js_values(self, v):
        '''builds json atomic values (like number, string, booleans...) from python constants e objects'''
        if type(v) in (bool, int, long, float, str, unicode, decimal.Decimal, datetime.datetime, datetime.date, datetime.time) or v is None:
            if type(v) is bool:
                v = u'false' if v is False else u'true'
            elif type(v) in [long, int]:
                v = u'%s' % int(v)
            elif isinstance(v, decimal.Decimal):
                v = u'%s' % float(v)
            elif isinstance(v, basestring):
                v = addslashes(v)
                v = u'\"%s\"' % unicode(v)
            elif isinstance(v, datetime.datetime):
                v = u'\"%s\"' % v.strftime(self.__datetime_format)
            elif isinstance(v, datetime.date):
                v = u'\"%s\"' % v.strftime(self.__date_format)
            elif isinstance(v, datetime.time):
                v = u'\"%s\"' % v.strftime(self.__time_format)
            elif v is None:
                v = u'null'
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
    def encode(self, o, date_format='%Y/%m/%d', time_format='%H:%M:%S', max_depth=1):
        '''
        Creates the json. you may specify the date format for attributes of types datetime.datetime, datetime.date or datetime.time.
        Also, its possible specify the max value to depth of the json serialization, in other words, you may decide how far the
        json serialization can achieve. Like objects inside another objects.
        '''
        self.__date_format = date_format
        self.__time_format = time_format
        self.__datetime_format = '%s %s' % (date_format, time_format)
        self.__max_depth = max_depth
        out = self.__normalize(o)
        # log.info(out)
        return out

    @classmethod
    def decode(self, json, to_object=False):
        '''Create one python object or dictionary from json'''
        dic = eval(self.__build_py_values(json))
        return self.__d2o(dic) if to_object else dic


def addslashes(string):
    string = unicode(string)
    for char in [u'\\', u'"', u'\'', u'\0']:
        if char in string:
            string = string.replace(char, u'\\%s' % char)
    return string

def removeslashes(string):
    return string.replace('\\\\', '')

class DynaObject(object):
    pass

