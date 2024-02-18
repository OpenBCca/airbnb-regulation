### Import policy from policy object
class PolicyResults:
    """The policy results contain the policy and result of whether it is violated (bool)
    [
      {policy A : "True"},
      {policy B: "False"}
    ]
    """

    def __init__(self, violation_results: list[dict]):
        self.violation_results = violation_results

    """ Retrieve results from running a policy
    policy : a method in Policy class 
    """

    def get_violation_result_from(self, *policy_method):
        result = {}
        result[policy_method.__name__] = policy_method
        self.violation_results.append(result)
        return result
