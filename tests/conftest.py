from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

import allure
import pytest
from playwright.sync_api import expect

from test_data.users import TestUsers
from utils.config import Config

if TYPE_CHECKING:
    from playwright.sync_api import Page, Playwright


@pytest.fixture()
def config():
    return Config()


@pytest.fixture(scope="function")
def browser_page(playwright: Playwright, config: Config) -> Page:  # noqa
    expect.set_options(timeout=config.EXPECT_TIMEOUT)

    with playwright.chromium.launch(headless=config.HEADLESS) as browser:
        with browser.new_context(
            base_url=f"{config.BASE_URL}/",
        ) as context:
            context.tracing.start(screenshots=True, snapshots=True, sources=True)
            page = context.new_page()
            yield page  # noqa

            trace_file = config.root_path / "tracing" / f"trace_{uuid.uuid4()}.zip"
            context.tracing.stop(path=trace_file)

    allure.attach.file(trace_file, name="trace", extension="zip")


@pytest.fixture()
def get_page(browser_page):
    def _get_page(page_class):
        return page_class(browser_page)

    return _get_page


@pytest.fixture()
def users() -> type[TestUsers]:
    return TestUsers
