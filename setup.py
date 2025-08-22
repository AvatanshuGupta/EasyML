from setuptools import setup, find_packages

setup(
    name='Neurix',                 
    version='0.1.0',                
    author='Avatanshu Gupta',        
    author_email='avatanshugupta@gmail.com',  
    description='EasyMl is a simple ML utility library with preprocessing, regression, classification, and evaluation tools',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/AvatanshuGupta/EasyML.git', 
    packages=find_packages(),       
    python_requires='>=3.8',      
    install_requires=[            
        'numpy'
        
    ],
    classifiers=[                   
        'Programming Language :: Python :: 3',
        'Operating System :: OS Independent',
    ],
)
