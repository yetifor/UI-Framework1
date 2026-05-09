from urllib.parse import quote, urlsplit, urlunsplit


def embed_credentials_in_url(url: str, username: str, password: str) -> str:
    parsed_url = urlsplit(url)
    credentials = f"{quote(username, safe='')}:{quote(password, safe='')}"
    host = parsed_url.hostname or ""

    if parsed_url.port is not None:
        host = f"{host}:{parsed_url.port}"

    if host:
        netloc = f"{credentials}@{host}"
    else:
        cleaned_netloc = parsed_url.netloc.lstrip("@")
        netloc = f"{credentials}@{cleaned_netloc}"

    return urlunsplit(
        (
            parsed_url.scheme,
            netloc,
            parsed_url.path,
            parsed_url.query,
            parsed_url.fragment,
        )
    )
