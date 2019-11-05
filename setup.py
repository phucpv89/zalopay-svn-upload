from distutils.core import setup
setup(
    name='zpsvnupload',         # How you named your package folder (MyLib)
    packages=['zpsvnupload'],   # Chose the same as "name"
    version='0.1',      # Start with a small number and increase it with every change you make
    # Chose a license from here: https://help.github.com/articles/licensing-a-repository
    license='MIT',
    # Give a short description about your library
    description='SUPPORT UPLOAD FILE TO SVN',
    author='eris mabu',                   # Type in your name
    author_email='phucpv89@gmail..com',      # Type in your E-Mail
    # Provide either the link to your github or to your website
    url='https://github.com/user/reponame',
    # I explain this later on
    download_url='https://github.com/user/reponame/archive/v_01.tar.gz',
    # Keywords that define your package best
    keywords=['ZaloPay', 'SVN'],
    install_requires=[            # I get to this in a second
        'validators',
        'beautifulsoup4',
    ],
    classifiers=[
        'Programming Language :: Python :: 3.7',
    ],
)
