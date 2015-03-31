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

from __future__ import absolute_import

import socket
import pytest

from tests.integration.server_manager import TCPServerManager
from tests.integration.server_manager import TChannelServerManager


@pytest.yield_fixture
def tcp_server(random_open_port):
    with TCPServerManager(random_open_port) as manager:
        yield manager


@pytest.yield_fixture
def tchannel_server(random_open_port):
    with TChannelServerManager(random_open_port) as manager:
        yield manager


@pytest.yield_fixture(
    params=[TCPServerManager, TChannelServerManager]
)
def server(request, random_open_port):
    """Run a test against TChannel and TCP.

    This only works in combination with `@pytest.mark.gen_test`.
    """
    manager_class = request.param
    with manager_class(random_open_port) as manager:
        yield manager


@pytest.fixture
def random_open_port():
    """Find and return a random open TCP port."""
    sock = socket.socket(socket.AF_INET)
    try:
        sock.bind(('', 0))
        return sock.getsockname()[1]
    finally:
        sock.close()
