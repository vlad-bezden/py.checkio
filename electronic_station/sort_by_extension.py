"""Sort by Extension

    https://py.checkio.org/en/mission/sort-by-extension/

    You are given a list of files. You need to sort this list by the file extension.
    The files with the same extension should be sorted by name.

    Some possible cases:
    * Filename cannot be an empty string.
    * Files without the extension should go before the files with one.
    * Filename ".config" has an empty extension and a name ".config".
    * Filename "config." has an empty extension and a name "config.".
    * Filename "table.imp.xls" has an extension "xls" and a name "table.imp".
    * Filename ".imp.xls" has an extension "xls" and a name ".imp".

    Input: A list of filenames.
    Output: A list of filenames.
"""

from __future__ import annotations
from typing import Sequence
from dataclasses import dataclass, field


@dataclass(order=True)
class File:
    name: str = field(compare=False)
    ext: str = field(init=False)
    stem: str = field(init=False)

    def __post_init__(self) -> None:
        self.stem, self.ext = (
            (self.name[:idx], self.name[idx + 1 :])
            if (idx := self.name.rindex("."))
            else (self.name, "")
        )

    def __repr__(self):
        return self.name


def sort_by_ext(files: Sequence[str]) -> Sequence[str]:
    return [str(file) for file in sorted(File(name) for name in files)]


if __name__ == "__main__":
    assert sort_by_ext(["1.cad", "1.bat", "1.aa"]) == ["1.aa", "1.bat", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "2.bat"]) == [
        "1.aa",
        "1.bat",
        "2.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".bat"]) == [
        ".bat",
        "1.aa",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.bat", ".aa", ".bat"]) == [
        ".aa",
        ".bat",
        "1.bat",
        "1.cad",
    ]
    assert sort_by_ext(["1.cad", "1.", "1.aa"]) == ["1.", "1.aa", "1.cad"]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", "1.aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        "1.aa.doc",
    ]
    assert sort_by_ext(["1.cad", "1.bat", "1.aa", ".aa.doc"]) == [
        "1.aa",
        "1.bat",
        "1.cad",
        ".aa.doc",
    ]
    print("PASSED!!!")
