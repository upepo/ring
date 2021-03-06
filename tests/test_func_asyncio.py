
import sys
import pytest


if sys.version_info >= (3, 3):
    from ._func_asyncio import *  # noqa

    if sys.version_info >= (3, 5):
        from ._func_async_def import *  # noqa

else:
    @pytest.mark.skip
    def test_this_version_of_python_does_not_support_asyncio():
        pass
