# Pyth Stack

## Components
- Python + FastHTML
- Tailwind
- HTMX

## Dependencies
Managed by `uv`

## Linter
```sh
    uvx ruff
```

### Fuck ruff
```sh
uvx ruff format . && uvx ruff check . --fix && uvx ruff check . --select I --fix
```

## Typecheck
```sh
    npx pyright
```

## How to run
Before running be sure to add all required environment variables (see [env example](.env.example)) 

- serve: `mmdb serve`
