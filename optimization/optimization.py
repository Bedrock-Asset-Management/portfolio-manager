from abc import ABC, abstractmethod

class Optimization(ABC):
    @abstractmethod
    def optimize(self, portfolio):
        pass
    from abc import ABC, abstractmethod

class Optimization(ABC):
    """
    Abstract base class for optimization algorithms.
    All optimization strategies should inherit from this class and implement the optimize method.
    """

    @abstractmethod
    def optimize(self, *args, **kwargs):
        """
        Perform optimization based on the specific algorithm.
        Parameters:
            *args, **kwargs: Flexible arguments to support diverse optimization needs.
        Returns:
            Any: Optimization result, typically an array of optimized weights or parameters.
        """
        pass
