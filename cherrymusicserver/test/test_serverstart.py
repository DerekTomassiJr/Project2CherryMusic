from cherrymusicserver import browsersetup
import pytest


def testServerStart():
    try:
        browsersetup.configureAndStartCherryPy(8080)
    except:
        pytest.fail("Cherry Music Server Didn't Start Properly")
