import os
import shutil
from typing import List

import attr


@attr.s(slots=True)  # pragma: no mutate
class ExecutionContext:
    """Storage for the current context of the execution."""

    hypothesis_output: List[str] = attr.ib(factory=list)  # pragma: no mutate
    workers_num: int = attr.ib(default=1)  # pragma: no mutate
    show_errors_tracebacks: bool = attr.ib(default=False)  # pragma: no mutate
    endpoints_processed: int = attr.ib(default=0)  # pragma: no mutate
    current_line_length: int = attr.ib(default=0)  # pragma: no mutate
    terminal_size: os.terminal_size = attr.ib(factory=shutil.get_terminal_size)  # pragma: no mutate
