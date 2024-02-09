# automatically generated by the FlatBuffers compiler, do not modify

# namespace: Entities

from .flatbuffers import *
from .flatbuffers.compat import import_numpy
np = import_numpy()

#//////////////
#//////////////
class MeshBufferLocator(object):
    __slots__ = ['_tab']

    @classmethod
    def SizeOf(cls):
        return 16

    # MeshBufferLocator
    def Init(self, buf, pos):
        self._tab = table.Table(buf, pos)

    # MeshBufferLocator
    def Offset(self): return self._tab.Get(number_types.Uint64Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(0))
    # MeshBufferLocator
    def Size(self): return self._tab.Get(number_types.Uint64Flags, self._tab.Pos + number_types.UOffsetTFlags.py_type(8))

def CreateMeshBufferLocator(builder, offset, size):
    builder.Prep(8, 16)
    builder.PrependUint64(size)
    builder.PrependUint64(offset)
    return builder.Offset()
