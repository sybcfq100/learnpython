class Tree:
    """ abstract base class representing a tree structure. """
    # ------------------- nested position class ------------------
    class Position:
        """ an abstract representing the location of a single element. """
        def element(self):
            """ return the element stored at this position. """
            raise NotImplementedError("must be implemented by subclass")
        
        def __eq__(self, other):
            """ return True if other is a Position representing the same location. """
            raise NotImplementedError("must be implemented by subclass")
        
        def __ne__(self, other):
            """ return True if other does not represent the same location. """
            return not (self == other)
    # ------------------- abstract methods that concrete subclass must support ------------------
    def root(self):
        """ return the root Position of the tree (or None if empty) """
        raise NotImplementedError("must be implemented by subclass")
    
    def parent(self, p):
        """ return the Position representing p's parent (or None if p is root) """
        raise NotImplementedError("must be implemented by subclass")
    
    def num_children(self, p):
        """ return the number of children that Position p has """
        raise NotImplementedError("must be implemented by subclass")
    
    def __len__(self):
        """return the total number of elements in the tree. """
    raise NotImplementedError("must be implemented by subclass")

    def is_root(self, p):
        """ return True if Position p represents the root of the tree """
        return self.root() == p
    
    def is_leaf(self, p):
        """ return True if Position p does not have any children """
        return self.num_children(p) == 0
    
    def is_empty(self):
        """ return True if the tree is empty """
        return len(self) == 0

    def depth(self, p):
        """ return the number of levels separating Position p from the root """
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height1(self):
        """ return the height of the tree """
        return max(self.depth(p) for p in self.positions() if self.is_leaf(p))
    
    def _height2(self, p):
        """ return the height of the subtree rooted at Position p """
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.children(p))
    