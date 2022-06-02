#!/usr/bin/python
import sys
import pytest

"""
Pueden utilizar este script para ejecutar los tests dentro de Thonny.
(ejecutenló como otro programa)
"""

if __name__ == "__main__":
    sys.path.append("src")
    sys.exit(pytest.main())
