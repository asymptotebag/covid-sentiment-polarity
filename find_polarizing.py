from statistics import variance

ATTN_THRESHOLD = 0.1  # min(abs(min(attns)), abs(max(attns))) > threshold to be included
NUM_CONTROVERSIAL = 50  # how many of our top variance words to consider "controversial"

corpus_attns = {  # is this the format?
    'apple' : [0.15,0.21,-0.04,0.1],
    'bear' : [-0.2,-0.8,0.2],
    'crayon' : [0.002,0.03,-0.07],
}

corpus_variances = []  # store (word, var) tuples
for word, attns in corpus_attns.items():
    mina, maxa = min(attns), max(attns)
    # attns have to both straddle 0 AND have sufficient room around 0
    if (mina < 0 and maxa > 0) and min(abs(mina), maxa) > ATTN_THRESHOLD:
        corpus_variances.append((word, variance(attns)))
print(len(corpus_variances))  # how many did we get rid of?
corpus_variances.sort(key=lambda x:x[1], reverse=True)  # sort by decreasing variance
print(corpus_variances[:NUM_CONTROVERSIAL])