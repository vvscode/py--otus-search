from distutils.core import setup
setup(
  name = 'otus-search',         # How you named your package folder (MyLib)
  packages = ['otus-search'],   # Chose the same as "name"
  version = '0.0.1',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = 'Search links from web',   # Give a short description about your library
  author = 'vvscode',                   # Type in your name
  author_email = 'v.vanchuk@tut.by',      # Type in your E-Mail
  url = 'https://github.com/vvscode/py--otus-search',   # Provide either the link to your github or to your website
  download_url = 'https://github.com/vvscode/py--otus-search/archive/master.zip',    # I explain this later on
  keywords = ['otus', 'vvscode'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests-html',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3.7'      #Specify which pyhton versions that you want to support
  ],
)