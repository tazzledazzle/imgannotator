# tests/test_filters.py
from imgannotator.filters import apply_filter
from PIL import Image


def test_apply_filter(tmp_path):
    img_path = tmp_path / "test.jpg"
    Image.new("RGB", (10, 10), color="red").save(img_path)
    apply_filter(str(tmp_path), "BLUR")
    assert img_path.exists()
