import os
from pathlib import Path


def get_data_path(*path: str | os.PathLike) -> str:
    return os.fspath(Path(__file__).parent.joinpath("data", *path))

def get_relative_data_path(caller_path: str | os.PathLike, *path: str | os.PathLike) -> str:
    data_path = Path(__file__).parent.joinpath("data", *path)
    return os.fspath(data_path.relative_to(Path(caller_path).parent))
