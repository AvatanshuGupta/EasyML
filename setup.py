from setuptools import setup, find_packages

setup(
    name='EasyML',                  # Package name (unique on PyPI)
    version='0.1.0',                 # Initial version
    author='Avatanshu Gupta',        # Your name
    author_email='avatanshugupta@gmail.com',  
    description='EasyMl is a simple ML utility library with preprocessing, regression, classification, and evaluation tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AvatanshuGupta/EasyML.git',  # Optional: GitHub repo
    packages=find_packages(),         # Automatically finds all packages
    python_requires='>=3.8',         # Minimum Python version
    install_requires=[               # Dependencies
        'numpy'
        
    ],
    classifiers=[                    # Optional, helps PyPI categorize your package
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
)
