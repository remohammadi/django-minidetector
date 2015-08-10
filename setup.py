from distutils.core import Command, setup
import os


class TocTest(Command):
    user_options = []
    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        import os
        import subprocess
        import sys
        try:
            errno = subprocess.call(['tox', '-e', os.getenv('TOX_ENV', 'py27-django18')])
            raise SystemExit(errno)
        except OSError:
            print("please install tox: pip install tox")
            raise SystemExit(2)


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()
 
setup(
    name='minidetector',
    version='1.2',
    description='Django middleware and view decorator to detect phones and small-screen devices',
    long_description = read("README.md"),
    author='metamoof, Chris Drackett, Reza Mohammadi',
    url = "https://github.com/remohammadi/django-minidetector",
    packages = [
        "minidetector",
    ],
    classifiers = [
        "Development Status :: 3 - Alpha",
        "Environment :: Web Environment",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: BSD License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Framework :: Django",
    ],
    cmdclass = {'test': TocTest},
    package_data={'minidetector': ['*.txt']}
)
