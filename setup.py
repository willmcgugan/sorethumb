from distutils.core import setup

from sorethumb import __version__ as VERSION

classifiers = ["Framework :: Django",
               "Intended Audience :: Developers",
               "License :: OSI Approved :: BSD License",
               "Programming Language :: Python",
               "Topic :: Software Development :: Libraries :: Python Modules",
               ]

setup(
      name = 'sorethumb',
      packages = ['sorethumb',
                  'sorethumb.templatetags',
                  'sorethumb.filters'],
      version = VERSION,
      description = 'Thumbnail image processing, with Django integration',
      author = 'Will McGugan',
      author_email = "will@willmcgugan.com",
      url = 'http://code.google.com/p/sorethumb',
      download_url = 'http://code.google.com/p/sorethumb/downloads/list',
      classifiers = classifiers,
      maintainer = "Will McGugan",
      maintainer_email = "will@willmcgugan.com"
)
