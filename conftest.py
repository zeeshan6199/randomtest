import pytest,os,datetime,pathlib
from playwright.sync_api import Page
from pages.loginpage import LoginPage
from dotenv import load_dotenv

load_dotenv()


@pytest.fixture(autouse=True)
def _page_defaults(page:Page):
    page.set_default_timeout(10000)
    page.set_default_navigation_timeout(15000)
    yield

# ------------------------------
# ARTIFACTS ON FAILURE
# ------------------------------
@pytest.hookimpl(hookwrapper=True, tryfirst=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    rep = outcome.get_result()
    setattr(item, "rep_" + rep.when, rep)

@pytest.fixture(autouse=True)

def _artifacts_on_failure(page, request):
    yield
    if hasattr(request.node, "rep_call") and request.node.rep_call.failed:
        ts = datetime.now().strftime("%Y%m%d-%H%M%S")
        name = f"{request.node.name}-{ts}"
        out = pathlib.Path("artifacts")
        out.mkdir(exist_ok=True)
        page.screenshot(path=out / f"{name}.png", full_page=True)
        html = page.content()
        (out / f"{name}.html").write_text(html, encoding="utf-8")



@pytest.fixture()
def logged_in(page:Page):
    loginpage=LoginPage(page)
    loginpage.goto(os.getenv("base_url"))

    loginpage.loginaction(os.getenv("e_username"),os.getenv("e_password"))
    return page