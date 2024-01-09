from setuptools import find_packages, setup

package_name = 'pl_nouns'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='adam',
    maintainer_email='adam.krawczyk@robotec.ai',
    description='TODO: Package description',
    license='TODO: License declaration',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'dictionary_service = pl_nouns.dictionary_service:main',
            'dictionary_client = pl_nouns.dictionary_client:main',
            'dictionary_test = pl_nouns.dictionary_test:main'
        ],
    },
)
