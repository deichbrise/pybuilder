#!/usr/bin/env python

from setuptools import setup
from setuptools.command.install import install as _install

class install(_install):
    def pre_install_script(self):
        pass

    def post_install_script(self):
        pass

    def run(self):
        self.pre_install_script()

        _install.run(self)

        self.post_install_script()

if __name__ == '__main__':
    setup(
        name = 'pybuilder',
        version = '0.12.0.dev20180116151215',
        description = 'An extensible, easy to use continuous build tool for Python',
        long_description = 'PyBuilder is a build automation tool for python.\n\nPyBuilder is a software build tool written in pure Python which mainly targets Python applications.\nIt is based on the concept of dependency based programming but also comes along with powerful plugin mechanism that\nallows the construction of build life cycles similar to those known from other famous build tools like Apache Maven.\n',
        author = 'Alexander Metzner, Maximilien Riehl, Michael Gruber, Udo Juettner, Marcel Wolf, Arcadiy Ivanov, Valentin Haenel',
        author_email = 'alexander.metzner@gmail.com, max@riehl.io, aelgru@gmail.com, udo.juettner@gmail.com, marcel.wolf@me.com, arcadiy@ivanov.biz, valentin@haenel.co',
        license = 'Apache License',
        url = 'http://pybuilder.github.io',
        scripts = ['scripts/pyb'],
        packages = [
            'pybuilder',
            'pybuilder.pluginhelper',
            'pybuilder.plugins',
            'pybuilder.plugins.python'
        ],
        namespace_packages = [],
        py_modules = [],
        classifiers = [
            'Programming Language :: Python',
            'Programming Language :: Python :: Implementation :: CPython',
            'Programming Language :: Python :: Implementation :: PyPy',
            'Programming Language :: Python :: 2',
            'Programming Language :: Python :: 2.7',
            'Programming Language :: Python :: 3',
            'Programming Language :: Python :: 3.4',
            'Programming Language :: Python :: 3.5',
            'Programming Language :: Python :: 3.6',
            'Programming Language :: Python :: 3.7',
            'Development Status :: 4 - Beta',
            'Environment :: Console',
            'Intended Audience :: Developers',
            'License :: OSI Approved :: Apache Software License',
            'Topic :: Software Development :: Build Tools',
            'Topic :: Software Development :: Quality Assurance',
            'Topic :: Software Development :: Testing'
        ],
        entry_points = {
            'console_scripts': ['pyb_ = pybuilder.cli:main']
        },
        data_files = [],
        package_data = {
            'pybuilder': ['LICENSE']
        },
        install_requires = [
            'pip~=9.0',
            'setuptools~=36.5',
            'tailer~=0.4',
            'tblib',
            'wheel~=0.30'
        ],
        dependency_links = [],
        zip_safe = True,
        cmdclass = {'install': install},
        keywords = '',
        python_requires = '!=3.0,!=3.1,!=3.2,!=3.3,<3.8,>=2.7',
        obsoletes = [],
    )
