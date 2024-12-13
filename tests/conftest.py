# Uses pytest hooks to display messages when tests are run
def pytest_runtest_protocol(item, nextitem):
    print(f"Running test: {item.name}")
    return None


def pytest_runtest_makereport(item, call):
    if call.when == "call":
        if call.excinfo is None:
            print(f"Test {item.name} PASSED")
        else:
            print(f"Test {item.name} FAILED")
