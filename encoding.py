#!/usr/bin/env python
# coding: utf-8

# In[2]:


b = [45,147, 128, 53, 44, 32, 112, 108, 101, 97, 115, 101, 148,45]
s = bytes(b)
print(s)


# In[3]:


print(s.decode('cp1252'))


# In[4]:


print(s.decode('iso-8859-1'))


# In[5]:


print(len(s.decode('cp1252')))


# In[6]:


print(len(s.decode('iso-8859-1')))


# In[9]:


def make_alnum_sample(out, codec, n):
    for x in range(n):
        try:
            u = chr(x)
            if u.isalnum():
                b = u.encode(codec)
                out.write(b)
        except:
                # skip u if codec cannot represent it
                print('pass')
                pass
    out.write(b'\n')


# In[10]:


codecs = ['ascii', 'cp437', 'cp858', 'cp1252', 'iso-8859-1', 'macroman', 'utf-8', 'utf-16']
for codec in codecs:
    with open('%s_alnum.txt' % codec, mode='wb') as out:
        make_alnum_sample(out, codec, 512)


# In[14]:


def stream_non_ascii_snippets(s, n_before = 15, n_after = 15):
    """
    s is a byte string possibly containing non-ascii characters
    n_before and n_after specify a window size
    this function is a generator for snippets
    containing the n_before bytes before a non-ascii character,
    the non-ascii byte itself, and the n_after bytes that follow it.
    """
    for idx, c in enumerate(s):
        if c> 127:
            start = max(idx - n_before, 0)
            end = idx + n_after + 1
            yield(s[start:end])


# In[ ]:





# In[12]:


CODECS = ['cp858', 'cp1252', 'macroman']
def test_codecs(s, codecs = CODECS):
    """
    prints the codecs that can decode s to a Unicode string
    and those unicode strings
    """
    max_len = max(map(len, codecs))
    for codec in codecs:
        try:
            u = s.decode(codec)
            print(codec.rjust(max_len) + ': ' + u)
        except:
            pass


# In[15]:


b = [45, 147, 128, 53, 44, 32, 112, 108, 101, 97, 115, 101, 148, 45]
s = bytes(b)
test_codecs(next(stream_non_ascii_snippets(s)))


# In[16]:


from collections import defaultdict
from operator import itemgetter


# In[17]:


def get_non_ascii_byte_counts(s):
    """
    returns {code point: count}
    for non-ASCII code points
    """
    counts = defaultdict(int)
    for c in s:
        if c > 127:
            counts[c] += 1
    return counts


# In[21]:


def stream_targeted_non_ascii_snippets(s, target_byte, n_before = 15, n_after = 15):
    """
    s is a byte string possibly containing non-ascii characters
    target_byte is code point
    n_before and n_after specify a window size
    
    this function is a generator for snippets containing the n_before bytes
    before target_byte, target_byte itself, and the n_after bytes that follow it.
    """
    for idx, c in enumerate(s):
        if c == target_byte:
            start = max(idx - n_before, 0)
            end = idx + n_after + 1
            yield(s[start:end])


# In[ ]:





# In[19]:


sorted(get_non_ascii_byte_counts(s).items(), key = itemgetter(1,0), reverse = True)


# In[22]:


it = stream_targeted_non_ascii_snippets(s, 148, n_before=6)
test_codecs(next(it))


# In[23]:


# Ex 4-7. Normarlizing text from Py


# In[24]:


with open('macroman_alnum.txt', mode = 'rb') as f:
    print(f.readline())


# In[25]:


with open('macroman_alnum.txt', mode = 'rb') as f:
    print(f.readline().decode('macroman'))


# In[26]:


with open('macroman_alnum.txt', encoding = 'macroman') as f:
    print(f.readline())


# In[27]:


import urllib


# In[28]:


urllib.parse.urlencode({'eqn': '1+2==3'})


# In[32]:


s = 'www.example.com/text?eqn=1%2B2%3D%3D3'
urllib.parse.unquote(s)


# In[36]:


import html


# In[ ]:





# In[37]:


s = '<script>//Do Some Évîl</script>'
encoded = html.escape(s).encode('ascii', 'xmlcharrefreplace').decode('ascii')
print(encoded)


# In[38]:


print(html.unescape(encoded))


# In[39]:


ss = html.escape(encoded).encode('ascii', 'xmlcharrefreplace').decode('ascii')
ss = html.escape(ss).encode('ascii', 'xmlcharrefreplace').decode('ascii')
print(ss)


# In[40]:


while len(ss) != len(html.unescape(ss)):
    ss = html.unescape(ss)
    print(ss)


# In[41]:


import io
import csv


# In[42]:


s = io.StringIO('''Name, Job Description
"Bolton, Michael ""Mike""","""Programmer"
Bolton, Michael "Mike", Programmer''')


# In[44]:


list(map(len, [line.split(',') for line in s]))


# In[45]:


s.seek(0)
list(map(len, csv.reader(s)))


# In[46]:


s.seek(0)
data = [row for row in csv.reader(s)]


# In[47]:


data[1][0]


# In[48]:


data[2][0]


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




