import importlib

import medrag.config as config


def test_chunk_size_from_environment(monkeypatch):
    monkeypatch.setenv("MEDRAG_CHUNK_SIZE", "500")   # prepare
    importlib.reload(config)                          # run config.py again
    assert config.CHUNK_SIZE == 500                   # check
    assert isinstance(config.CHUNK_SIZE, int)