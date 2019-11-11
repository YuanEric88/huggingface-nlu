import argparse


def noun_phrase_extract(input_file):
    tokens = []
    labels = []
    noun_phrases = []
    with open(input_file, "r") as f_in:
        for l in f_in:
            l = l.rstrip().split()
            tokens.append(l[0])
            labels.append(l[1])
    pos = 0
    while i < len(labels):
        if labels[i] in ["NN", "NNS", "NP", "NPS"]:
            noun_phrase = labels[i]
            if labels[i] in ["NP", "NPS"]:
                npos = i+1
                while npos < len(labels) and labels[npos] in ["NP", "NPS"]:
                    noun_phrase = " ".join([noun_phrase, labels[npos]])
                    npos += 1
                noun_phrases.append(noun_phrase)
                i = npos
            elif labels[i] in ["NN", "NNS"]:
                noun_phrase = labels[i]
                prev = i-1
                # concantenate CD/JJ/JJS/NP/NPS with noun phrase
                if prev >= 0 and labels[prev] in ["CD", "JJ", "JJS", "NP", "NPS"]:
                    noun_phrase = " ".join([labels[prev], noun_phrase])
                npos = i+1
                while npos < len(labels) and labels[npos] in ["NN", "NNS"]:
                    noun_phrase = " ".join([noun_phrase, labels[npos]])
                    npos += 1
                noun_phrases.append(noun_phrase)
                i = npos
    
    return noun_phrases


def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--data_file", default=None, type=str, required=True,
                        help="The input data file. Should be the test files for the Pos tagging task.")
    
    args = parser.parse_args()

    noun_phrases = noun_phrase_extract(args.data_file)
    
    print(noun_phrases)


if __name__ == "__main__":
    main()
