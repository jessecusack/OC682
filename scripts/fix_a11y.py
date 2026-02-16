from pathlib import Path

from bs4 import BeautifulSoup

build_dir = Path("_build/html")

for html_file in build_dir.rglob("*.html"):
    soup = BeautifulSoup(html_file.read_text(), "html.parser")
    modified = False

    # Fix 1: Scrollable regions need tabindex and unique labels
    for i, el in enumerate(soup.select("pre.overflow-auto, .overflow-x-auto")):
        if not el.get("tabindex"):
            el["tabindex"] = "0"
            modified = True
        if not el.get("role"):
            el["role"] = "region"
            modified = True
        if not el.get("aria-label"):
            el["aria-label"] = f"Scrollable content {i + 1}"
            modified = True

    # Fix 2: Navigation landmarks need unique labels
    for nav in soup.select("nav.myst-top-nav-bar"):
        if not nav.get("aria-label"):
            nav["aria-label"] = "Site navigation"
            modified = True

    # Fix 3: Search button needs accessible name
    for btn in soup.select("button.myst-search-bar"):
        if not btn.get("aria-label"):
            btn["aria-label"] = "Search"
            modified = True

    # Fix 4: Skip to content should be in a landmark
    for skip_div in soup.select(".myst-skip-to-article"):
        if not skip_div.get("role"):
            skip_div["role"] = "navigation"
            modified = True
        if not skip_div.get("aria-label"):
            skip_div["aria-label"] = "Skip links"
            modified = True

    # Fix 5: Footer content ("Made with MyST") should be in landmark
    for span in soup.select("span.self-center.ml-2.text-sm"):
        if span.string and "MyST" in span.string:
            # Wrap in footer if not already in one
            if not span.find_parent("footer"):
                parent = span.parent
                if parent and not parent.get("role"):
                    parent["role"] = "contentinfo"
                    parent["aria-label"] = "Site credits"
                    modified = True

    if modified:
        html_file.write_text(str(soup))
        print(f"Fixed: {html_file}")
