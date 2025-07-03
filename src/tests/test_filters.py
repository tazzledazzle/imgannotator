# tests/test_filters.py
from pathlib import Path
import pytest
from imgannotator.filters import apply_filter
from PIL import Image
import shutil

FIXTURES_DIR = Path(__file__).parent / "images"


def populate_images(src_dir: Path, dst_dir: Path):
    dst_dir.mkdir(parents=True, exist_ok=True)
    for img in src_dir.iterdir():
        if img.suffix.lower() in {".png", ".jpg", ".jpeg"}:
            shutil.copy(img, dst_dir / img.name)


@pytest.fixture
def images_dir(tmp_path):
    """
    Fixture to create a temporary directory with sample images.
    """
    populate_images(FIXTURES_DIR, tmp_path)
    return tmp_path


def test_apply_filter(tmp_path):
    img_path = tmp_path / "test.jpg"
    Image.new("RGB", (10, 10), color="red").save(img_path)
    apply_filter(str(tmp_path), "BLUR")
    assert img_path.exists()
