from setuptools import setup

def readme():
    with open('README.md') as f:
        return f.read()

setup(name='topicnetwork',
      version='0.1.3',
      description='Topic modeling with text networks',
      long_description=readme(),
      long_description_content_type="text/markdown",
      classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Topic :: Text Processing :: Linguistic',
      ],
      keywords='topic network community detection',
      url='http://github.com/michal_pikusa/topic-network',
      author='Michal Pikusa',
      author_email='pikusa.michal@gmail.com',
      license='MIT',
      packages=['topicnetwork'],
      install_requires=[
          'networkx',
          'nltk'
      ],
      include_package_data=True,
      zip_safe=False)