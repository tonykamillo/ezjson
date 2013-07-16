"""
ezjson
-------------

Ezjson (means easy json) is a simple python module to encode and decode json.
The reason by which I did this module, is because i dont like the way as anothers modules, works .
There is some python objects (like datetime.date) that isn't JSON serializable and it often generates errors.
Encode and decode JSON it should be an simple task, like in PHP way.
"""
from setuptools import setup


setup(
    name='ezjson',
    version='1.0',
    url='http://github.com/sacanix/ezjson',
    license='BSD',
    author='Tony Kamillo (Sacanix)',
    author_email='tonysacanix@gmail.com',
    description='Ezjson (means easy json) is a simple python module to encode and decode json.',
    long_description=__doc__,
    # if you would be using a package instead use packages instead
    # of py_modules:
    py_modules=['ezjson'],
    #packages=[],
    #zip_safe=False,
    include_package_data=True,
    platforms='any',
    #install_requires=['python-twitter'],
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ]
)