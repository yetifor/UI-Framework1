import logging
from collections.abc import Callable

from playwright.sync_api import Dialog, Page

from logger import LOGGER_NAME

logger = logging.getLogger(LOGGER_NAME)


class PageActions:
    def __init__(self, page: Page) -> None:
        self.page = page

    def goto(self, url: str) -> None:
        logger.info(f"PageActions: goto '{url}'")
        self.page.goto(url)

    def expect_new_page(self):
        logger.info("PageActions: expect new page")
        return self.page.context.expect_page()

    def bring_to_front(self) -> None:
        logger.info("PageActions: bring page to front")
        self.page.bring_to_front()

    def wait_for_load_state(self, state: str | None = None) -> None:
        logger.info(f"PageActions: wait for load state '{state}'")
        self.page.wait_for_load_state(state)

    def close_page(self) -> None:
        logger.info("PageActions: close page")
        self.page.close()

    def run_and_accept_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: accept dialog")
        return self._handle_dialog(action, mode="accept")

    def run_and_dismiss_alert(self, action: Callable[[], None]) -> str:
        logger.info("PageActions: dismiss dialog")
        return self._handle_dialog(action, mode="dismiss")

    def run_and_accept_prompt(
            self,
            action: Callable[[], None],
            prompt_text: str,
    ) -> str:
        logger.info("PageActions: accept prompt")
        return self._handle_dialog(action, mode="accept", prompt_text=prompt_text)

    def _handle_dialog(
            self,
            action: Callable[[], None],
            mode: str,
            prompt_text: str | None = None,
    ) -> str:
        logger.info("PageActions: expect dialog")
        message = ""

        def handle_dialog(dialog: Dialog) -> None:
            nonlocal message
            message = dialog.message
            logger.info(f"PageActions: dialog '{dialog.type}' with message '{message}'")
            if mode == "dismiss":
                dialog.dismiss()
                return

            if prompt_text is None:
                dialog.accept()
                return

            dialog.accept(prompt_text)

        self.page.once("dialog", handle_dialog)
        action()

        if not message:
            raise RuntimeError("Expected dialog was not shown")

        return message
