import nltk


def preprocess_batch(sentences, postag,stopword):
    processed_sentences = []
    for text in sentences:
        pos_removal = [tag[0] for tag in nltk.pos_tag(text.split()) if tag[1] in postag]
        processed_sentence = " ".join(
            [i for i in text.split(" ") if i not in stopword]
        )
        processed_sentences.append(processed_sentence)
    return processed_sentences
