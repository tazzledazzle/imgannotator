# tests/test_metadata.py
import os
import tempfile
from imgannotator.metadata import embed_metadata
from PIL import Image
import piexif


def test_embed_metadata(tmp_path):
    img_path = tmp_path / "test.jpg"
    Image.new("RGB", (10, 10)).save(img_path)
    embed_metadata(str(tmp_path), "Hello")
    data = piexif.load(str(img_path))
    assert data["0th"][piexif.ImageIFD.ImageDescription] == b"Hello"
