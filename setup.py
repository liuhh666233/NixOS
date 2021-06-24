from setuptools import setup, find_packages

setup(
    name='demo-cpu-info',
    version='1.0.0',
    description='This is a python demo package that provides a cpu info app',
    author='liuxb',
    author_email='liuxiaobo666233@gmail.com',
    packages=find_packages(),
    entry_points={
        'console_scripts':[
            'cpu_info = cpu_info.app:main'
        ]
    },
    python_requires = '>=3.6',
)