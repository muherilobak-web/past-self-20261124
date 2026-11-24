"""Two Lines to Your Past Self.

Writes one fixed two-line text to /output/entry.txt:
a warning to the writer's past self about one specific
moment, and why that moment mattered.
"""

import os
from pathlib import Path

TEXT = (
    "Pick up the phone that Tuesday evening in March when Grandma calls, "
    "because she will not call again tomorrow.\n"
    "You let it ring to voicemail and meant to call back, and the goodbye "
    "you kept saving for tomorrow never got said."
)


def main() -> None:
    output_dir = Path(os.environ.get("OUTPUT_DIR", "/output"))
    output_dir.mkdir(parents=True, exist_ok=True)
    (output_dir / "entry.txt").write_text(TEXT, encoding="utf-8")


if __name__ == "__main__":
    main()
