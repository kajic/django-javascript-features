from setuptools import setup, find_packages

setup(
    name="django-javascript-features",
    version="0.1",
    description="Helps initalizing javascript modules on the pages that need them",
    long_description=open('README.rst').read(),
    author='Robert Kajic',
    author_email='robert@kajic.com',
    url='https://github.com/kajic/django-javascript-features',
    download_url='https://github.com/kajic/django-javascript-features/django-javascript-features/downloads',
    license="MIT",
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,  # because we're including media that Django needs
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],
)
