# Teaching Computational Linguistics with Jupyter


## Jupyter Day presentation: Language Models

Varada Kolhatkar [ʋəɾəda kɔːlɦəʈkər]

Assistant Professor of Teaching in Computer Science

## Slide settings 

from traitlets.config.manager import BaseJSONConfigManager
from pathlib import Path
path = Path.home() / ".jupyter" / "nbconfig"
cm = BaseJSONConfigManager(config_dir=str(path))
tmp = cm.update(
        "rise",
        {
            "theme": "serif",
            "transition": "fade",
            "start_slideshow_at": "selected",            
            "width": "100%",
            "height": "100%",
            "header": "",
            "footer":"",
            "scroll": True,
            "enable_chalkboard": True,
            "slideNumber": True,
            "center": False,
            "controlsLayout": "edges",
            "slideNumber": True,
            "hash": True,
        }
    )

## Set Altair default size

def theme_vk(*args, **kwargs):
    return {'height': 400,
            'config': {'style': {'circle': {'size': 400},
                                'point': {'size': 30},
                                'square': {'size': 400},
                                },
                       'legend': {'symbolSize': 20, 'titleFontSize': 20, 'labelFontSize': 20}, 
                       'axis': {'titleFontSize': 20, 'labelFontSize': 20}},
            }


## import the libraries 

import pandas as pd
import numpy as np
import IPython
%pylab inline
# pip install git+git://github.com/mgelbart/plot-classifier.git
from plot_classifier import plot_classifier

import matplotlib.pyplot as plt
%matplotlib inline

import numpy as np
import numpy.random as npr


import nltk
nltk.download('punkt')
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import time

from collections import defaultdict
from collections import Counter

import pandas as pd
pd.set_option("display.max_colwidth", 200)

# pip install ipython-autotime
import autotime

from IPython.display import HTML

## Goal 

- To give you a high-level overview of language models.  
- Demonstrate how I use Jupyter notebooks to teach with different modalities.  
    - Text
    - Mathematical equations with latex
    - Images s
    - Code
    - Videos 
    - Interactive websites

%%HTML
<style>
.rendered_html table, .rendered_html th, .rendered_html tr, .rendered_html td {
     font-size: 130%;
}

body.rise-enabled div.inner_cell>div.input_area {
    font-size: 100%;
}

body.rise-enabled div.output_subarea.output_text.output_result {
    font-size: 100%;
}
body.rise-enabled div.output_subarea.output_text.output_stream.output_stdout {
  font-size: 150%;
}
</style>

def display_url(url): 
    """
    Given a url, display it as an iframe. 
    
    Arguments: 
    ----------
    url : str
        The url to be displayed 
    
    Return:
    ----------
    None
    """
    display(HTML("<iframe src=%s width=1000 height=900 allowfullscreen></iframe>"%url))

## Which of the following do you use on everyday basis?

- Hover over the area above screen sharing to see the toolbar/options and click on "Annotate".  
- Select "Stamp" and put your favourite stamps in the appropriate box(s). 

<center>
<img src="images/annotation-exercise.png" height="1400" width="1400">
</center>

### A common component in all these services is **a language model**!! 

## What is a language model? 

A model that computes the probability of a sequence of words or the probability of an upcoming word is called a **language model**.

- Compute the probability of a sentence or a sequence of words.
    - $P(w_1, w_2,\dots,w_t)$
    - P(I have read this book) > P(eye have red this book)

- A related task: What's the probability of an upcoming word? 
    - $P(w_t|w_1,w_2,\dots,w_{t-1})$ 
    - P(book | read this) > P(book | red this)



### Language model examples 

# Gmail smart compose
url = "https://ai.googleblog.com/2018/05/smart-compose-using-neural-networks-to.html"
display_url(url)

## Voice assistant example


<center>
<img src="images/voice-assistant-ex.png" height="1400" width="1400">
</center>

### An example of a state-of-the-art language model
url = "https://www.youtube.com/embed/fZSFNUT6iY8?rel=0&amp;controls=0&amp;showinfo=0"
display_url(url) 

### Language modeling: Why should we care?

Powerful idea in NLP and helps in many tasks.
- Machine translation 
    * P(In the age of data algorithms have the answer) > P(the age data of in algorithms answer the have)
- Spelling correction
    * My office is a 20  <span style="color:red">minuet</span> bike ride from my home.  
        * P(20 <span style="color:blue">minute</span> bike ride from my home) > P(20 <span style="color:red">minuet</span> bike ride from my home)
- Speech recognition 
    * P(<span style="color:blue">I read</span> a book) > P(<span style="color:red">Eye red</span> a book)

### A naive way to calculate probabilities of a sentence

- Calculate probabilities of a sequence by applying chain rule 
- Example: Suppose we want to calculate the probability of the following sequence of words: 

$
\begin{equation}
\begin{split}
P(\textrm{In the age of data algorithms have the answer}) =& P(\textrm{In}) \times P(\textrm{the|In})\\ 
                                              & \times P(\textrm{age|In the}) \times P(\textrm{of|In the age})\\
                                              & \times P(\textrm{data|In the age of})\\
                                              & \times P(\textrm{algorithms|In the age of data}) \\
                                              &  \times P(\textrm{have|In the age of data algorithms}) \\
                                              & \dots 
\end{split}
\end{equation}
$

- How often the exact same long sequences of words occur in text? For example, how often the sequence "In the age of data algorithms have" is likely to occur in your data? 
- The counts will be tiny and the model will be very sparse. 
- <span style="color:red">BAD IDEA!!</span> 

## Markov models of language

**Markov assumption: The future is conditionally independent of the past given present**
<center>
<img src="images/Markov-assumption.png" height="500" width="500">
</center>

- Bigram language model
    
$$
P(\textrm{algorithms|In the age of data}) \approx P(\textrm{algorithms|data})
$$

### Markov model of language (bigram language model)

- Use Markov assumption and calculate the probability of a sequence as follows!
\begin{equation}
\begin{split}
P(\textrm{In the age of data algorithms have the answer}) =& P(\textrm{In}) \times P(\textrm{the|In})\\ 
                                              & \times P(\textrm{age|the})\\
                                              & \times P(\textrm{of|age})\\
                                              & \times P(\textrm{data|of})\\
                                              & \times P(\textrm{algorithms|data}) \\                 
                                              & \times P(\textrm{have|algorithms}) \\                             
                                              & \times P(\textrm{the|have}) \\                                   
                                              & \times P(\textrm{answer|the}) \\                                                                                 
\end{split}
\end{equation}

### Estimating probabilities for the bigram language model

- Example
$$P(\textrm{algorithms|data}) = \frac{Count(\textrm{data algorithms})}{Count(\textrm{data})}$$

### Text generation using Markov models of languaage 

toy_corpus = '''The birds they sang
At the break of day
Start again
I heard them say
Don't dwell on what
Has passed away
Or what is yet to be
Yeah the wars they will
Be fought again
The holy dove
She will be caught again
Bought and sold
And bought again
The dove is never free
Ring the bells (ring the bells) that still can ring
Forget your perfect offering
There is a crack in everything (there is a crack in everything)
That's how the light gets in
We asked for signs
The signs were sent
The birth betrayed
The marriage spent
Yeah the widowhood
Of every government
Signs for all to see
I can't run no more
With that lawless crowd
While the killers in high places
Say their prayers out loud
But they've summoned, they've summoned up
A thundercloud
And they're going to hear from me
Ring the bells that still can ring
Forget your perfect offering
There is a crack, a crack in everything (there is a crack in everything)
That's how the light gets in
You can add up the parts
You won't have the sum
You can strike up the march
There is no drum
Every heart, every heart to love will come
But like a refugee
Ring the bells that still can ring
Forget your perfect offering
There is a crack, a crack in everything (there is a crack in everything)
That's how the light gets in
Ring the bells that still can ring (ring the bells that still can ring)
Forget your perfect offering
There is a crack, a crack in everything (there is a crack in everything)
That's how the light gets in
That's how the light gets in
That's how the light gets in'''

toy_corpus_tokens = nltk.word_tokenize(toy_corpus.lower())

frequencies = defaultdict(Counter)
for i in range(len(toy_corpus_tokens) - 1):
    frequencies[toy_corpus_tokens[i: i + 1][0]][toy_corpus_tokens[i + 1]] += 1
    
freq_df = pd.DataFrame(frequencies).transpose()
freq_df = freq_df.fillna(0)
freq_df

trans_df = freq_df.div(freq_df.sum(axis=1), axis=0)
trans_df

### Generate text using the Markov model above
start_char = 'the'
seq_len = 100
seq = ''
ch = start_char
for i in range(seq_len):    
    seq += " " + ch
    next_char = npr.choice(trans_df.columns.tolist(), p = trans_df.loc[ch,].values.flatten())
    #print('The sampled next character is: ', next_char)
    ch = next_char
print('THE GENERATED SEQUENCE:\n ', seq)    


### In practice the corpus (dataset) is huge. For example, the full Wikipedia or the text available on the entire Internet, or all the New York Times articles from the last 20 years. 

### Considering more history 

- Example: trigrams or four-gram language model
    - Trigram language model
$$
P(\textrm{algorithms|In the age of data}) \approx P(\textrm{algorithms|of data})
$$
    - Four-gram language model
$$
P(\textrm{algorithms|In the age of data}) \approx P(\textrm{algorithms|age of data})
$$


### [Google n-gram viewer](https://books.google.com/ngrams)
 
- All Our N-gram are Belong to You
    - https://ai.googleblog.com/2006/08/all-our-n-gram-are-belong-toyou.html

<blockquote>
Here at Google Research we have been using word n-gram models for a variety
of R&D projects, such as statistical machine translation, speech recognition,
spelling correction, entity detection, information extraction, and others.
That's why we decided to share this enormous dataset with everyone. We
processed 1,024,908,267,229 words of running text and are publishing the
counts for all 1,176,470,663 five-word sequences that appear at least 40
times. There are 13,588,391 unique words, after discarding words that appear
less than 200 times.”
</blockquote>

url = "https://books.google.com/ngrams/"
HTML("<iframe src=%s width=1000 height=800></iframe>"%url)

def plot_ngrams(ngrams, start_year, end_year, corpus, smoothing):
    '''
    Plots ngrams using the Googlr n-gram viewer. 
    
    Parameters:
    ---------------------
    
    ngrams: 
        String with the n-gram to be searched. Words must be separated by spaces.
    start_year: 
        
    end_year: to year
    corpus: corpus to be used (21:Spanish, 15:English, etc. check https://books.google.com/ngrams for more)
    smoothing: number of years to average 
    '''
    ngrams = "+".join(ngrams.split())
    url = ("https://books.google.com/ngrams/graph?content=%s&year_start=%d&year_end=%d&corpus=%d&smoothing=%d"%
          (ngrams, start_year, end_year, corpus, smoothing))
    return HTML("<iframe src=%s width=1000 height=650></iframe>"%url)

#plot_ngrams("data science, databases", 1970, 2019, 21, 3)


## More advanced language models 

- Allow to use more history compared to bigram/trigram/4-gram models 
- Built using deep neural networks using the following techniques 
    - Long-short term memory models 
    - Transformers

## [GPT-3 language model](https://github.com/openai/gpt-3)

- A state-of-the-art language model with 175 billion parameters!!
- Task agnostic and works for many different tasks.   
- Currently very popular (and overhyped)

## Limitations of language models 

- All these complicated models are based on the simple idea of predicting next word given a sequence of words. 
- These models do not have common-sense knowledge or the ability to reason or reflect. 


### Example where the model does reasonably well

Q: How many eyes does a giraffe have?<br>
A: A giraffe has two eyes.

Q: How many legs does a frog have?<br>
A: A frog has four legs.

Q: Are there any animals with three legs?<br>
A: No, there are no animals with three legs.

Q: Why don't animals have three legs?<br>
A: Animals don't have three legs because they would fall over.

[Source](https://lacker.io/ai/2020/07/06/giving-gpt-3-a-turing-test.html)

### Example where the model demonstrates lack of common sense knowledge 

Q: Which is heavier, a mouse or an elephant?<br> 
A: An elephant is heavier than a mouse.

Q: Which is heavier, a mouse or a toaster?<br>
A: A toaster is heavier than a mouse.

Q: Which is heavier, a toaster or a pencil?<br>
A: A pencil is heavier than a toaster.

[Source](https://lacker.io/ai/2020/07/06/giving-gpt-3-a-turing-test.html)


### Beyond language generation 

- The same idea can be used to generate sequences beyond language. 
- Here is an example of generating music: 

url = "https://magenta.tensorflow.org/performance-rnn"
HTML("<iframe src=%s width=1000 height=650></iframe>"%url)

## Summary 



## Resources 

- See [this famous blog](http://karpathy.github.io/2015/05/21/rnn-effectiveness/). 
- [How Do You Know a Human Wrote This?](https://www.nytimes.com/2020/07/29/opinion/gpt-3-ai-automation.html)
