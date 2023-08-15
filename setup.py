from setuptools import setup, find_packages

setup(
    name='tax-resolution-chatbot-plugin',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'flask',
        'openai',
    ],
    author='Sami Abdullah',
    author_email='samiabd2304@gmail.com',
    description='A plugin for integrating a Tax Resolution Chatbot using GPT-3.5',
    keywords='chatbot tax resolution GPT-3.5 plugin',
    url='https://github.com/your-username/tax-resolution-chatbot-plugin', # URL to the repository (if applicable)
)
