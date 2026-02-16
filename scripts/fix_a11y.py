from pathlib import Path

from bs4 import BeautifulSoup

build_dir = Path("_build/html")

for html_file in build_dir.rglob("*.html"):
    soup = BeautifulSoup(html_file.read_text(), "html.parser")

    modified = False
    for el in soup.select("pre.overflow-auto, .overflow-x-auto"):
        if not el.get("tabindex"):
            el["tabindex"] = "0"
            el["role"] = "region"
            modified = True

    if modified:
        html_file.write_text(str(soup))
        print(f"Fixed: {html_file}")
