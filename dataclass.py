from dataclasses import dataclass
from dataclasses import field
from dataclasses import InitVar
import pandas as pd
import random
import math


@dataclass
class DataClass(object):
    # hidden attribute
    attr_0: InitVar[int] = 81
    # initialized attribute
    attr_1: int = 0
    attr_2: float = 0.
    attr_3: str = 'undefined'
    attr_4: list = field(default_factory=list)
    # generated attribute
    attr_5: float = field(init=False)

    @property
    def attr_5(self) -> float:
        return math.sqrt(abs(self._attrHidden))

    @attr_5.setter
    def attr_5(self, _): pass

    def __post_init__(self, attr_0):
        self._attrHidden = attr_0

    @classmethod
    def create(cls):
        return cls(
            # attr_0=random.randint(-1e3, 1e3),
            # attr_1=random.randint(-1e6, 1e6),
            attr_2=random.random(),
            attr_3=random.choice(['h', 'e', 'l', 'o']),
            attr_4=random.choices(range(100, 999), k=3)
        )


if __name__ == '__main__':
    objects = [DataClass.create() for _ in range(100)]
    df = pd.DataFrame(objects)

    print(df)
