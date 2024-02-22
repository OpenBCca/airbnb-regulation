from abc import ABC, abstractmethod


class Policy(ABC):
    """Interface for policy object"""

    @abstractmethod
    def evaluate(self) -> bool:
        """Abstract method to evaluate the policy"""
        pass

    def get_policy_name(self) -> str:
        """Get policy name from object class name"""
        return self.__class__.__name__
