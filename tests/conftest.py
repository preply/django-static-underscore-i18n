import shutil
import pytest


@pytest.fixture
def cleandir(request, settings):
    def teardown():
        shutil.rmtree(settings.STATIC_UNDERSCORE_I18N_ROOT)
    request.addfinalizer(teardown)
