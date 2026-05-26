from PIL import Image
import os

root = os.path.dirname(os.path.abspath(__file__))

jobs = [
    # (src, dst, max_width, quality)
    ("header.png", "img/header.webp", 1600, 78),
    ("header.png", "img/header.jpg",  1600, 82),
    ("liveandforgive3.png", "img/cover.webp", 1000, 82),
    ("liveandforgive3.png", "img/cover.jpg",  1000, 85),
    ("star.png", "img/star.webp", 1000, 82),
    ("star.png", "img/star.jpg",  1000, 85),
]

os.makedirs(os.path.join(root, "img"), exist_ok=True)

for src, dst, max_w, q in jobs:
    src_path = os.path.join(root, src)
    dst_path = os.path.join(root, dst)
    im = Image.open(src_path)
    if im.mode in ("RGBA", "P"):
        im = im.convert("RGB")
    w, h = im.size
    if w > max_w:
        new_h = int(h * max_w / w)
        im = im.resize((max_w, new_h), Image.LANCZOS)
    fmt = "WEBP" if dst.endswith(".webp") else "JPEG"
    im.save(dst_path, fmt, quality=q, method=6 if fmt == "WEBP" else None, optimize=(fmt == "JPEG"), progressive=(fmt == "JPEG"))
    print(f"{dst}: {os.path.getsize(dst_path)//1024} KB ({im.size[0]}x{im.size[1]})")
