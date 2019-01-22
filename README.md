# Topic Network - topic modeling with text networks
![alt text](https://img.shields.io/pypi/pyversions/topicnetwork.svg) ![alt text](https://img.shields.io/pypi/l/topicnetwork.svg) ![alt text](https://img.shields.io/pypi/v/topicnetwork.svg)

This package introduces a novel method for topic modeling using community detection in complex networks. The algorithms included in the package first create a network of collocated terms, filters out unimportant words based on centrality measures, and then uses community detection to reveal the topic groups in the network. 

The methods used are language-agnostic, meaning that you can perform the topic modeling on any text in any language. It is an early version, hence there might be performance issues when modeling big corpora. These are to be resolved in upcoming updates.

## Installation

To install the [current version](https://pypi.org/project/topicnetwork/) of the package, use:

```python
pip install topicnetwork
```

## Use

To find the topics, simply use:

```python
import topicnetwork
topics = topicnetwork.find_topics(list_of_strings)
```

For best results, use a text without punctuation and stopwords, and words converted to lowercase. You can perform the cleaning on your English texts with:

```python
text = topicnetwork.clean(list_of_strings)
```

## Notes
Package written and maintained by Michal Pikusa (pikusa.michal@gmail.com)
