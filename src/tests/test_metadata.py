# tests/test_metadata.py
from pathlib import Path

import pytest
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


def test_embed_metadata(images_dir):

    img_path = FIXTURES_DIR / "test50.jpg"
    assert img_path.exists()
    # embed_metadata(str(tmp_path), "Hello")
    # data = piexif.load(str(img_path))
    # assert data["0th"][piexif.ImageIFD.ImageDescription] == b"Hello"
