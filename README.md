# Topic Network - topic modeling with text networks
![alt text](https://img.shields.io/pypi/pyversions/topicnetwork.svg) ![alt text](https://img.shields.io/pypi/l/topicnetwork.svg)

This package builds a text network out of a list of strings, picks the most important words on the basis of betweenness centrality measure, and performs community detection to group the words into topic networks and return the groups. The methods used are language-agnostic, meaning that you can perform the topic modeling on any text in any language.
The package uses NetworkX to build the network and perform the necessary calculations. 

## Usage

To install the [current version](https://pypi.org/project/topicnetwork/) of the package, use::

```python
pip install topicnetwork
```

To find the topics, simply use::

```python
import topicnetwork
topics = topicnetwork.find_topics(list_of_strings)
```

For best results, use a text without punctuation and stopwords, and words converted to lowercase. You can perform the cleaning on your English texts with:

```python
text = topicnetwork.clean(list_of_strings)
```

Package written and maintained by Michal Pikusa (pikusa.michal@gmail.com)
