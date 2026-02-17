from pathlib import Path

from bs4 import BeautifulSoup

build_dir = Path("_build/html")

for html_file in build_dir.rglob("*.html"):
    print(f"Processing: {html_file}")
    soup = BeautifulSoup(html_file.read_text(), "html.parser")
    modified = False

    # Fix 1: Scrollable regions need tabindex and unique labels
    elements = soup.select("pre.overflow-auto, .overflow-x-auto")
    print(f"  Found {len(elements)} scrollable regions")
    for i, el in enumerate(elements):
        el["tabindex"] = "0"
        el["role"] = "region"
        el["aria-label"] = f"Scrollable content {i + 1}"
        modified = True

    # Fix 2: Navigation landmarks need unique labels
    navs = soup.select("nav.myst-top-nav-bar")
    print(f"  Found {len(navs)} top nav bars")
    for nav in navs:
        nav["aria-label"] = "Site navigation"
        modified = True

    # Fix 3: Search button needs accessible name
    buttons = soup.select("button.myst-search-bar")
    print(f"  Found {len(buttons)} search buttons")
    for btn in buttons:
        btn["aria-label"] = "Search"
        modified = True

    # Fix 4: Skip to content should be in a landmark
    skip_divs = soup.select(".myst-skip-to-article")
    print(f"  Found {len(skip_divs)} skip-to-article divs")
    for skip_div in skip_divs:
        skip_div["role"] = "navigation"
        skip_div["aria-label"] = "Skip links"
        modified = True

    # Fix 5: "Made with MyST" link - remove invalid role, wrap in footer
    links = soup.select("a.myst-made-with-myst")
    print(f"  Found {len(links)} myst-made-with-myst links")
    for link in links:
        # Remove invalid role from link
        if link.get("role"):
            del link["role"]

        # Wrap in footer if not already in one
        if not link.find_parent("footer"):
            wrapper = soup.new_tag("footer")
            wrapper["aria-label"] = "Site credits"
            link.wrap(wrapper)
            modified = True

    # Fix 6: "Made with MyST" span outside landmark
    spans = soup.select("span.self-center.ml-2.text-sm")
    print(f"  Found {len(spans)} self-center spans")
    for span in spans:
        if span.string and "MyST" in span.string:
            # Find parent and ensure it's in a landmark
            parent = span.find_parent(["footer", "nav", "main", "aside", "header"])
            if not parent:
                # Wrap the span's container in a footer
                container = span.parent
                if container and not container.get("role"):
                    container["role"] = "contentinfo"
                    container["aria-label"] = "Site credits"
                    modified = True

    if modified:
        html_file.write_text(str(soup))
        print(f"  ✅ Fixed: {html_file}")
    else:
        print(f"  ⏭️ No changes needed")
