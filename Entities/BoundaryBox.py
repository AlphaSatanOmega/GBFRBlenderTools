# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Entities

from .flatbuffers import *
from .flatbuffers.compat import import_numpy
np = import_numpy()

class BoundaryBox(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 24

    # BoundaryBox
    def Init(self, buf, pos):
        self._tab = table.Table(buf, pos)

    # BoundaryBox
    def Min(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 0)
        return obj

    # BoundaryBox
    def Max(self, obj):
        obj.Init(self._tab.Bytes, self._tab.Pos + 12)
        return obj


def CreateBoundaryBox(builder, min_x, min_y, min_z, max_x, max_y, max_z):
    builder.Prep(4, 24)
    builder.Prep(4, 12)
    builder.PrependFloat32(max_z)
    builder.PrependFloat32(max_y)
    builder.PrependFloat32(max_x)
    builder.Prep(4, 12)
    builder.PrependFloat32(min_z)
    builder.PrependFloat32(min_y)
    builder.PrependFloat32(min_x)
    return builder.Offset()