import argparse


def noun_phrase_extract(tokens, labels):
    noun_phrases = []
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


def file_noun_phrase_extract(input_file):
    nps = []
    
    with open(input_file, "r") as f_in:
        tokens = []
        labels = []
        for l in f_in:
            l = l.rstrip().split()
            if len(l) == 0:
                np = noun_phrase_extract(tokens, labels)
                nps.append(np)
                tokens = []
                labels = []
            else:
                tokens.append(l[0])
                labels.append(l[1])
        np = noun_phrase_extract(tokens, labels)
        nps.append(np)
    return nps


def eval_metrics(pred_files, origin_files):
    """compute the sentence level evaluation metrics"""

    pred_nps = file_noun_phrase_extract(pred_files)
    # print("preds", pred_nps)
    origin_nps = file_noun_phrase_extract(origin_files)
    # print("origin", origin_nps)
    
    precision = []
    recall = []
    F1 = []
    for pred, origin in zip(pred_nps, origin_nps):
        pred = set(pred)
        origin = set(origin)
        if len(pred) == 0 or len(origin) == 0:
            precision.append(0)
            recall.append(0)
            F1.append(0)
        else:
            p = len(pred.intersection(origin)) / len(pred)
            r = len(pred.intersection(origin)) / len(origin)
            precision.append(p)
            recall.append(r)
            if p == 0 or r == 0:
                F1.append(0)
            else:
                F1.append(2 * p * r / (p + r))
    
    metrics = {
        "precision": round(sum(precision) / len(precision), 2),
        "recall": round(sum(recall) / len(recall), 2),
        "F1": round(sum(F1) / len(F1), 2)
    }

    return metrics




def main():
    parser = argparse.ArgumentParser()

    parser.add_argument("--pred_file", default=None, type=str, required=True,
                        help="The predict data file. Should be the test files for the Pos tagging task.")
    
    parser.add_argument("--origin_file", default=None, type=str, required=False,
                        help="The origin data file. Should be the test files for the Pos tagging task.")
    
    args = parser.parse_args()

    if args.origin_file:
        metrics = eval_metrics(args.pred_file, args.origin_file)
        print(metrics)
    else:
        preds = file_noun_phrase_extract(args.pred_file)
        print(preds)


if __name__ == "__main__":
    main()
