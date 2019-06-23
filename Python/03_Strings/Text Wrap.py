# Problem Link: https://www.hackerrank.com/challenges/text-wrap/problem
# ---------------------------------------------------------------------


def wrap(string, max_width):
    text = textwrap.fill(string, max_width)
    return text 