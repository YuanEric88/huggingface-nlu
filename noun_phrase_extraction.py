import argparse


def noun_phrase_extract(tokens, labels):
    tokens = []
    labels = []
    noun_phrases = []
    with open(input_file, "r") as f_in:
        for l in f_in:
            l = l.rstrip().split()
            tokens.append(l[0])
            labels.append(l[1])
    pos = 0
    while pos < len(labels):
        cur_pos = pos
        if labels[pos] in ["NN", "NNS", "NP", "NPS"]:
            noun_phrase = tokens[pos]
            if labels[pos] in ["NP", "NPS"]:
                npos = pos+1
                while npos < len(labels) and labels[npos] in ["NP", "NPS", "CD"]:
                    noun_phrase = " ".join([noun_phrase, tokens[npos]])
                    npos += 1
                noun_phrases.append(noun_phrase)
                pos = npos
            elif labels[pos] in ["NN", "NNS"]:
                noun_phrase = tokens[pos]
                prev = pos-1
                # concantenate CD/JJ/JJS/NP/NPS with noun phrase
                if prev >= 0 and labels[prev] in ["CD", "JJ", "JJS", "NP", "NPS"]:
                    noun_phrase = " ".join([tokens[prev], noun_phrase])
                npos = pos+1
                while npos < len(labels) and labels[npos] in ["NN", "NNS", "CD"]:
                    noun_phrase = " ".join([noun_phrase, tokens[npos]])
                    npos += 1
                noun_phrases.append(noun_phrase)
                pos = npos
        if pos == cur_pos:
            pos += 1
    
    return noun_phrases


def eval_metrics(pred_files, origin_files=None):
    """compute the evaluation metrics"""

    pred_nps = []
    if origin_files:
        origin_nps = []
    # First deal with predict_files.
    pred_labels = []
    pred_tokens = []
    with open(predict_files, "r") as f_in:
        pred_label = []
        pred_token = []
        for l in f_in:
            l = l.rstrip().split()
            tokens.append(l[0])
            labels.append(l[1])


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_file", default=None, type=str, required=True,
                        help="The input data file. Should be the test files for the Pos tagging task.")
    
    args = parser.parse_args()

    noun_phrases = noun_phrase_extract(args.data_file)
    
    print(noun_phrases)


if __name__ == "__main__":
    main()
