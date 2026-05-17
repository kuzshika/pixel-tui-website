from base64 import b64encode
from pathlib import Path

html = Path("index.html").read_text(encoding="utf-8")

logo = b64encode(Path("assets/icon-192.png").read_bytes()).decode("ascii")
favicon = b64encode(Path("favicon.png").read_bytes()).decode("ascii")
og = b64encode(Path("assets/icon-512.png").read_bytes()).decode("ascii")

html = html.replace("/assets/pixel-tui-logo.jpg", f"data:image/png;base64,{logo}")
html = html.replace("/favicon.png", f"data:image/png;base64,{favicon}")
html = html.replace("/assets/icon-192.png", f"data:image/png;base64,{favicon}")
html = html.replace("/assets/og-image.jpg", f"data:image/png;base64,{og}")

Path("index.github.html").write_text(html, encoding="utf-8")
