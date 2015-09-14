# Copyright (c) 2015 Uber Technologies, Inc.
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.

#
# Autogenerated by Thrift Compiler (0.9.2)
#
# DO NOT EDIT UNLESS YOU ARE SURE THAT YOU KNOW WHAT YOU ARE DOING
#
#  options string: py:new_style,slots,dynamic
#

from thrift.Thrift import TType, TMessageType, TException, TApplicationException
from ttypes import *
from thrift.Thrift import TProcessor
from thrift.protocol.TBase import TBase, TExceptionBase


class Iface(object):
  def submit(self, span):
    """
    Parameters:
     - span
    """
    pass

  def multi_submit(self, spans):
    """
    Parameters:
     - spans
    """
    pass


class Client(Iface):
  def __init__(self, iprot, oprot=None):
    self._iprot = self._oprot = iprot
    if oprot is not None:
      self._oprot = oprot
    self._seqid = 0

  def submit(self, span):
    """
    Parameters:
     - span
    """
    self.send_submit(span)
    return self.recv_submit()

  def send_submit(self, span):
    self._oprot.writeMessageBegin('submit', TMessageType.CALL, self._seqid)
    args = submit_args()
    args.span = span
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_submit(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = submit_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "submit failed: unknown result");

  def multi_submit(self, spans):
    """
    Parameters:
     - spans
    """
    self.send_multi_submit(spans)
    return self.recv_multi_submit()

  def send_multi_submit(self, spans):
    self._oprot.writeMessageBegin('multi_submit', TMessageType.CALL, self._seqid)
    args = multi_submit_args()
    args.spans = spans
    args.write(self._oprot)
    self._oprot.writeMessageEnd()
    self._oprot.trans.flush()

  def recv_multi_submit(self):
    iprot = self._iprot
    (fname, mtype, rseqid) = iprot.readMessageBegin()
    if mtype == TMessageType.EXCEPTION:
      x = TApplicationException()
      x.read(iprot)
      iprot.readMessageEnd()
      raise x
    result = multi_submit_result()
    result.read(iprot)
    iprot.readMessageEnd()
    if result.success is not None:
      return result.success
    raise TApplicationException(TApplicationException.MISSING_RESULT, "multi_submit failed: unknown result");


class Processor(Iface, TProcessor):
  def __init__(self, handler):
    self._handler = handler
    self._processMap = {}
    self._processMap["submit"] = Processor.process_submit
    self._processMap["multi_submit"] = Processor.process_multi_submit

  def process(self, iprot, oprot):
    (name, type, seqid) = iprot.readMessageBegin()
    if name not in self._processMap:
      iprot.skip(TType.STRUCT)
      iprot.readMessageEnd()
      x = TApplicationException(TApplicationException.UNKNOWN_METHOD, 'Unknown function %s' % (name))
      oprot.writeMessageBegin(name, TMessageType.EXCEPTION, seqid)
      x.write(oprot)
      oprot.writeMessageEnd()
      oprot.trans.flush()
      return
    else:
      self._processMap[name](self, seqid, iprot, oprot)
    return True

  def process_submit(self, seqid, iprot, oprot):
    args = submit_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = submit_result()
    result.success = self._handler.submit(args.span)
    oprot.writeMessageBegin("submit", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()

  def process_multi_submit(self, seqid, iprot, oprot):
    args = multi_submit_args()
    args.read(iprot)
    iprot.readMessageEnd()
    result = multi_submit_result()
    result.success = self._handler.multi_submit(args.spans)
    oprot.writeMessageBegin("multi_submit", TMessageType.REPLY, seqid)
    result.write(oprot)
    oprot.writeMessageEnd()
    oprot.trans.flush()


# HELPER FUNCTIONS AND STRUCTURES

class submit_args(TBase):
  """
  Attributes:
   - span
  """

  __slots__ = [ 
    'span',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.STRUCT, 'span', (Span, Span.thrift_spec), None, ), # 1
  )

  def __init__(self, span=None,):
    self.span = span

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.span)
    return value


class submit_result(TBase):
  """
  Attributes:
   - success
  """

  __slots__ = [ 
    'success',
   ]

  thrift_spec = (
    (0, TType.STRUCT, 'success', (Response, Response.thrift_spec), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value


class multi_submit_args(TBase):
  """
  Attributes:
   - spans
  """

  __slots__ = [ 
    'spans',
   ]

  thrift_spec = (
    None, # 0
    (1, TType.LIST, 'spans', (TType.STRUCT,(Span, Span.thrift_spec)), None, ), # 1
  )

  def __init__(self, spans=None,):
    self.spans = spans

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.spans)
    return value


class multi_submit_result(TBase):
  """
  Attributes:
   - success
  """

  __slots__ = [ 
    'success',
   ]

  thrift_spec = (
    (0, TType.LIST, 'success', (TType.STRUCT,(Response, Response.thrift_spec)), None, ), # 0
  )

  def __init__(self, success=None,):
    self.success = success

  def __hash__(self):
    value = 17
    value = (value * 31) ^ hash(self.success)
    return value

