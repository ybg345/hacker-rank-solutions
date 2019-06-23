# Problem Link: https://www.hackerrank.com/challenges/xml-1-find-the-score/problem
# --------------------------------------------------------------------------------


def get_attr_number(node):
    score = 0
    score +=  len(node.attrib)
    for child in node:
        score += get_attr_number(child)
    return score