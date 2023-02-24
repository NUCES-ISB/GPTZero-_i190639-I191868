"""
This code a slight modification of perplexity by hugging face
https://huggingface.co/docs/transformers/perplexity

Both this code and the orignal code are published under the MIT license.

by Burhan Ul tayyab and Nicholas Chua
"""

from model import GPT2PPL

# initialize the model
model = GPT2PPL()

sentence = "Another reason for Lays' success is its marketing strategies. The brand has employed various marketing campaigns over the years that have helped it to increase its brand recognition and attract new customers. One of the most successful marketing campaigns was the Do Us A Flavor campaign, which was first launched in the United States in 2012. The campaign encouraged customers to submit their ideas for new chip flavors, and the winning flavor was added to the Lays product line. The campaign was so successful that it was later launched in other countries, such as Canada, the United Kingdom, and Australia."

model(sentence)
