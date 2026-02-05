import threading
from typing import Any, Callable

import wx

from src.logger import logger


class BackgroundWorker:
    """Runs work in background and handles UI updates safely."""

    def __init__(
        self,
        parent,
        title: str = "Working...",
        message: str = "Please wait.",
    ):
        self.parent = parent
        self.title = title
        self.message = message
        self.busy: wx.BusyInfo | None = None
        self.on_done: Callable[[Any], None] | None = None

    def run(
        self,
        work_func: Callable[[], Any],
        on_done: Callable[[Any], None] | None = None,
    ) -> None:
        """
        Start background work.

        Args:
            work_func: Function to run in background
            on_done: Callback when done (receives result)
        """
        self.busy = wx.BusyInfo(
            f"{self.title}\n{self.message}",
            parent=self.parent,
        )

        self.on_done = on_done

        thread = threading.Thread(target=self._do_work, args=(work_func,))
        thread.daemon = True
        thread.start()

    def _do_work(self, work_func: Callable[[], Any]) -> None:
        """Run the actual work (background thread)."""
        try:
            result = work_func()
        except Exception as e:
            result = e

        wx.CallAfter(self._finish, result)

    def _finish(self, result: Any) -> None:
        """Close popup and call user's callback (UI thread)."""
        if self.busy:
            del self.busy

        if self.on_done:
            self.on_done(result)

    def runBackgroundTesk(self, func, *args, on_done=None, **kwargs):
        """
        Runs a given function in the background.

        Parameters
        ----------
        func : callable
            Function to execute in the background.
        *args : tuple
            Positional arguments for func.
        on_done : callable, optional
            Optional callback that gets executed when the task finishes.
        **kwargs : dict
            Keyword arguments for func.
        """

        def work_func():
            # Work safely inside background thread
            return func(*args, **kwargs)

        def default_on_done(result):
            # You can adapt this to update UI, log, etc.
            print(f"[{self.title}] Task completed.")
            print("Result:", result)

        # Run the worker (assuming your existing BackgroundWorker supports this)
        self.run(work_func=work_func, on_done=on_done or default_on_done)
