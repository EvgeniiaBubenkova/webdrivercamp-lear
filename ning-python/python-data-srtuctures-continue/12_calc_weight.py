#!/usr/bin/python3
def calc_weight(list_=[]):
    if not list_:
        return 0

    weighted_sum = sum(score * weight for score, weight in list_)
    total_weight = sum(weight for score, weight in list_)
    
    return weighted_sum / total_weight

if __name__=="__main__":
    list_ = [(3, 2), (5, 9), (7, 7)]
    # = ((3 * 2) + (5 * 9) + (7 * 7)) / (2 + 9 + 7)
    result = calc_weight(list_)
    print(f"Weight: {result:0.2f}")
