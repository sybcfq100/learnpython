class Vector:
    """ represent a vector in a multidimensional space."""

    def __init__(self, d):
        """ create a vector of dimension d """
        self._coords = [0] * d

    def __len__(self):
        """ return the dimension of the vector """
        return len(self._coords)

    def __getitem__(self, j):
        """ return the j-th coordinate of the vector """
        return self._coords[j]

    def __setitem__(self, j, val):
        """ set the j-th coordinate of the vector to given value """
        self._coords[j] = val

    def __add__(self, other):
        """ return the sum of two vectors """
        if len(self) != len(other):
            raise ValueError("dimensions must agree")
        result = Vector(len(self))
        for j in range(len(self)):
            result[j] = self[j] + other[j]
        return result

    def __eq__(self, other):
        """ return True if vector has same coordinates as other """
        return self._coords == other._coords

    def __ne__(self, other):
        """ return True if vector differs from other """
        return not self == other

    def __str__(self):
        """ return the vector as a string """
        return "<" + str(self._coords)[:]+">"


v = Vector(5)
v[1] = 23
v[-1] = 45
print(v)
u = v + [1, 0, 3, 4, 0]
print(u)
total = sum(v)
print(total)
