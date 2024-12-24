import fasthtml.components as fhtml


def Page(*, title: str, Child):
    return fhtml.Html(
        fhtml.Head(
            fhtml.Title(f"{title} | MMDb"),
            fhtml.Meta(charset="UTF-8"),
            fhtml.Meta(
                name="viewport", content="width=device-width, initial-scale=1.0"
            ),
            fhtml.Script(src="https://cdn.tailwindcss.com"),
            fhtml.Script(
                src="https://unpkg.com/htmx.org@1.9.6",
                integrity="sha384-FhXw7b6AlE/jyjlZH5iHa/tTe9EpJ1Y55RjcgPbjeWMskSxZt1v9qkxLJWNJaGni",
                crossorigin="anonymous",
            ),
            fhtml.Link(
                rel="stylesheet",
                href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@24,400,0,0",
            ),
        ),
        fhtml.Body(Child, id="body", cls="bg-slate-900 text-white max-h-full"),
    )


def BaseLayout(*, Child, title: str):
    layout = fhtml.Div(
        fhtml.Div(
            fhtml.Div(),  # add button here
            fhtml.Div(
                fhtml.A(
                    "MDNotes",
                    href="/",
                    cls="text-lg",
                ),
                fhtml.Span("/", cls="mx-2"),
                fhtml.H5(title, cls="text-base"),
                cls="dark:text-white font-semibold text-gray-500 dark:text-gray-400 flex flex-row items-center",
            ),
            fhtml.Div(),  # add button here
            cls="h-10 w-full bg-indigo-800 flex flex-row items-center px-4 justify-between",
        ),
        fhtml.Div(Child, cls="h-full w-full flex flex-row items-center"),
        cls="flex flex-col w-full h-full",
    )

    return Page(title=title, Child=layout)


def Home():
    return BaseLayout(
        title="Home",
        Child=fhtml.Div(
            fhtml.H1("MMDb", cls="text-4xl font-bold text-white mb-4"),
            cls="flex flex-col items-center justify-center w-full h-full",
        ),
    )
