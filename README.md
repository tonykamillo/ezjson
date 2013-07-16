ezjson
======

Ezjson (means easy json) is a simple python module to encode and decode json.
The reason by which I did this module, is because i dont like the way as anothers modules, works .
There is some python objects (like datetime.date) that isn't JSON serializable and it often generates errors.
Encode and decode JSON it should be an simple task, like in PHP way.


##Usage
```python
import ezjson as json

#Encoding
dumped = json.dump(a_object)
#or
encoded = json.encode(a_object)

#------------------------------------

#Decoding
loaded = json.load(dumped) 
#or
decoded = json.decode(encoded)

```

##Functions
**dump(python_data, date_format='%Y/%m/%d', max_depth=3)**

- *python_data*: the python data to be converted to json
- *date_format*: format of dates will be formated
- *max_depth*: refer to how deep the recursion can reach

    Returns a unicode of the encoded json. 

**encode(python_data, date_format='%Y/%m/%d', max_depth=3)**

   Alias to dump function

**load(json, to_object=False)**

- *json*: The json that will be loaded as a python data
- *to_object*: If True returns a python object. 

Returns a dict as default data or a python object if to_object is True.

**decode(json, to_object=False)**

Alias to load function

##Installation

```bash
$ pip install ezjson
```

or download/clone the package and

```bash
$ python setup install
```


