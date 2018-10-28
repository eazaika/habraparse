from setuptools import setup, find_packages
from os.path import join, dirname

setup(
    name='habraparser',
    version='1.0',
    packages=find_packages(),
    long_description=open(join(dirname(__file__), 'README.rst')).read(),
    install_requires=[
        'asn1crypto==0.24.0',
        'attrs==18.2.0',
        'Automat==0.7.0',
        'BTrees==4.5.1',
        'cffi==1.11.5',
        'constantly==15.1.0',
        'cryptography==2.3.1',
        'cssselect==1.0.3',
        'ExtensionClass==4.4',
        'habradata==1.0',
        'habraparse==1.0',
        'hyperlink==18.0.0',
        'idna==2.7',
        'incremental==17.5.0',
        'lxml==4.2.5',
        'mongo==0.2.0',
        'MultiMapping==4.1',
        'parsel==1.5.1',
        'persistent==4.4.3',
        'pyasn1-modules==0.2.2',
        'pycparser==2.19',
        'PyDispatcher==2.0.5',
        'PyHamcrest==1.9.0',
        'pymongo==3.7.2',
        'pyOpenSSL==18.0.0',
        'queuelib==1.5.0',
        'Scrapy==1.5.1',
        'service-identity==17.0.0',
        'six==1.11.0',
        'transaction==2.4.0',
        'Twisted==18.9.0',
        'w3lib==1.19.0',
        'zc.lockfile==1.3.0',
        'ZConfig==3.3.0',
        'zdaemon==4.2.0',
        'ZEO==5.2.0',
        'ZODB==5.5.1',
        'ZODB3==3.11.0',
        'zodbpickle==1.0.2',
        'zope.interface==4.6.0'
    ],
    entry_points={
        'console_scripts':
            ['startparse = habraparser.spiders.HabrSpider:startparse']
    }
)
