import json
from pathlib import Path
from typing import Optional

import typer
from loguru import logger

app = typer.Typer(help="IRATC CLI")


@app.command()
def serve(host: str = "0.0.0.0", port: int = 8000, reload: bool = False):
    """Run the IRATC API server."""
    import uvicorn

    uvicorn.run("iratc.api.main:app", host=host, port=port, reload=reload, factory=False)


@app.command()
def version():
    from iratc import __version__

    typer.echo(__version__)


@app.command()
def echo(path: Optional[Path] = typer.Argument(None, exists=False)):
    """Debug: print file contents or hello."""
    if path and path.exists():
        typer.echo(Path(path).read_text())
    else:
        typer.echo("hello from iratc")


if __name__ == "__main__":
    app()
