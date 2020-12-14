from gensim.models import KeyedVectors
import nltk

# only once!
# Model with tags
# Russian National Corpus and Russian Wikipedia dump of December 2018
rnc_and_wiki_wv = KeyedVectors.load("./initiator-models/rnc-and-wiki.wordvectors")

# Installing NLTK Data (https://www.nltk.org/data.html)
nltk.download('punkt')
nltk.download('universal_tagset')
nltk.download('averaged_perceptron_tagger_ru')
var = nltk.tagset_mapping('ru-rnc', 'universal') == {'!': '.', 'A': 'ADJ', 'C': 'CONJ', 'AD': 'ADV', 'NN': 'NOUN',
                                                     'VG': 'VERB', 'COMP': 'CONJ', 'NC': 'NUM', 'VP': 'VERB',
                                                     'P': 'ADP',
                                                     'IJ': 'X', 'V': 'VERB', 'Z': 'X', 'VI': 'VERB',
                                                     'YES_NO_SENT': 'X',
                                                     'PTCL': 'PRT'}

# END only once!

def get_similarity (text):
    words = nltk.word_tokenize(text)

    words_with_tag = []

    for word in words:
        word_with_tag = nltk.pos_tag([word], tagset='universal', lang='rus')[0]
        words_with_tag.append(word_with_tag[0] + '_' + word_with_tag[1])


    result = get_most_similar(words_with_tag)

    # check each word and find most similarity
    if len(words_with_tag) > 1:
        for word in words_with_tag:
            [result.append(text) for text in get_most_similar(word) if text not in result]

    return result


def get_most_similar(text, pv = 0.5):
    return [(word[0][0:word[0].find('_')]) for word in rnc_and_wiki_wv.most_similar(text) if word[1] >= pv]