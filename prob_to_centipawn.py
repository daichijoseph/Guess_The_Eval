from math import log, exp

def prob_to_centipawns(w):
    return -log((1-w)/w)/0.00368208

def centipawn_to_prob(cp):
    return (50 + 50*(2/(1 + exp(-0.00368208*cp)) - 1))/100


