# OC682

The site is [live via pages](jessecusack.github.io/OC682). 

# Development notes

## For collaborators

Clone this repository and use uv to create the development environment. 

```
uv sync
uv run nbstripout --install
```

## Stripping note book outputs

We don't want to clog git with figure outputs. 

```
uv add --dev nbstripout
uv run nbstripout --install
git config --get filter.nbstripout.clean  # Verify
```

