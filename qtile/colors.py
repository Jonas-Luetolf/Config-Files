from typing import Sequence


class QtileColorScheme:
    def __init__(self, colors: Sequence[str]) -> None:
        if len(colors) < 4:
            raise ValueError("colors length should be at least 4")
        self.colors = colors

    def __getitem__(self, n: int):
        return self.colors[n]

    @property
    def backgroundColor(self):
        return self.colors[0]

    @property
    def foregroundColor(self):
        return self.colors[1]

    @property
    def foregroundColorTwo(self):
        return self.colors[2]

    @property
    def workspaceColor(self):
        return self.colors[3]


NORD = QtileColorScheme(
    [
        "#2e3440",
        "#d8dee9",
        "#3b4252",
        "#5e81ac",
        "#88c0d0",
        "#a3be8c",
        "#d08779",
        "#b48ead",
        "#a3be8c",
        "#bf616a",
        "#ebcb8b",
    ]
)
