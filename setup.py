from setuptools import setup, find_packages

setup(
    name='ofd-viewer',
    version='0.1.0',
    author='Your Name',
    author_email='your.email@example.com',
    description='A simple OFD document viewer with a GUI.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/ofd-viewer',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'tkinter',
        'ofd-parser'
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)