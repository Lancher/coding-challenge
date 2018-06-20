# LEETCODE@ 251. Flatten 2D Vector
#
# --END--


class Vector2D(object):
    def __init__(self, vec2d):
        self.vec2d = vec2d
        self.vec = []

    def next(self):
        if not self.vec:
            while self.vec2d and not self.vec:
                self.vec = self.vec2d.pop(0)
        return self.vec.pop(0)

    def hasNext(self):
        if self.vec:
            return True
        else:
            while self.vec2d and not self.vec:
                self.vec = self.vec2d.pop(0)
            return bool(self.vec)
