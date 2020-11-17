# TopicModelingProject

## ECS 189L Project
## Austin, Katya, Raghav, Viswaas, & Zeke

### Files:
- *get_data_equarterly.py*: collect text data for *Eugenics Quarterly*
- *get_data_ereview.py*:    collect text data for *Eugenics Review*
- *get_data_socbio.py*:     collect text data for *Social Biology*
- *data_gathering.py*:      aggregate all preprocessed journal data

### Problemos at hand:
- text is cut of for some articles, and badly
- need to decide: deal with what we got or attempt to convert pdf to txt better
- if deal with what got, can use pyspellchecker (levenshtein distance) to complete/fix words with missing chars or special chars
- if improve, use pdfminer or pdftotext or something else

### equarterly todo:
- method of pdf to text: encoding of text bc there are special chars
- discarding numbers and garbage data (especially from tables/visuals)
- how to deal with typos and rand special chars: maybe use algo to guess most likely word (string edit distance)
- dealing with random breaks in paragraphs (including mid-word) with table data and page nums in between
- remove "Downloaded by [] at X:XX XX Month XXXX" that occurs every so often
- remove html?
- remove dashes in words during breaks

