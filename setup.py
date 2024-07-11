import setuptools

setuptools.setup(
    name='audio-speech-to-sign-language-converter',
    version='0.1.0',
    description='Python project',
    author='Pallavi Sukre',
    author_email='pallavisukre7667@gmail.com',
    url='https://github.com/jigargajjar55/Audio-Speech-To-Sign-Language-Converter',
    packages=setuptools.find_packages(),
    setup_requires=['nltk', 'joblib','click','regex','sqlparse','setuptools'],
)