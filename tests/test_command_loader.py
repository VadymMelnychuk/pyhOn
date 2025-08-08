from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from pyhon.command_loader import HonCommandLoader


def test_get_favourite_info_empty_favourite():
    loader = HonCommandLoader(None, None)
    loader._commands = {}
    name, command_name, base = loader._get_favourite_info({})
    assert name == ""
    assert command_name == ""
    assert base is None
