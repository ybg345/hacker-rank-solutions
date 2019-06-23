# Problem Link: https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem
# ------------------------------------------------------------------------------------------------------


def wrapper(f):
    def fun(l):
        # complete the function
        f("+91 %s %s" % (t[-10:-5], t[-5:]) for t in l)
    return fun

# http://simeonfranklin.com/blog/2012/jul/1/python-decorators-in-12-steps/

