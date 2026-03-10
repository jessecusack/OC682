import glob

import nbformat


def main():
    print("Running pre-build script: Hiding notebook code cells by default...")

    notebooks = glob.glob("**/*.ipynb", recursive=True)

    for nb_path in notebooks:
        if ".ipynb_checkpoints" in nb_path or "_build" in nb_path:
            continue

        try:
            nb = nbformat.read(nb_path, as_version=4)
            modified = False

            for cell in nb.cells:
                if cell.cell_type == "code":
                    # Fetch existing tags
                    tags = cell.metadata.get("tags", [])

                    # If flagged to show, ensure hide-input is NOT there
                    if "show-input" in tags:
                        if "hide-input" in tags:
                            tags.remove("hide-input")
                            cell.metadata["tags"] = tags
                            modified = True
                    # Otherwise, hide it by default
                    else:
                        if "hide-input" not in tags:
                            tags.append("hide-input")
                            cell.metadata["tags"] = tags
                            modified = True

            if modified:
                nbformat.write(nb, nb_path)
                print(f"  -> Updated tags for {nb_path}")

        except Exception as e:
            print(f"Error processing {nb_path}: {e}")

    print("Finished updating notebook tags.")


if __name__ == "__main__":
    main()
