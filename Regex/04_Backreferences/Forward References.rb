# Problem Link: https://www.hackerrank.com/challenges/forward-references/problem
# ------------------------------------------------------------------------------


Regex_Pattern = '^(\2tic|(tac))+$'

=begin
Explanation:
-----------

* Condition 1: S consists of tic or tac. 
Explanation: So regex is either - tic|tac or, tac|tic. What we should choose between these two depends on the second and third condition. 

* Condition 2: tic should not be immediate neighbour of itself.
* Condition 3: The first tic must occur only when tac has appeared at least twice before.
Explanation: If we choose regex tic|tac instead of tac|tac and fulfilled condition 3 first then the regex will be like - (\2tic|(tac)). 
    Here in the first group it tries to match group 2. But group 2 is not still available.So it goes into the OR section and matched tac. Now tac our group 2. 
    Because of tac in group 2 our group 1 becomes \2tic => tactic. So total group 1 becomes (\2tic|(tac)) => tactic|tac.
Thus our second and third condition fulfilled at the same time by choosing tic|tac instead of tac|tic and making tac as first group. 

=end