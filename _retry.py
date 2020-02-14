from retry import retry


@retry(exceptions=Exception, tries=5, jitter=1)
def test_fail(text):
    """
    Raises Exception for the retry
    Retry 5 times
    Add 1 second on every retry

    """
    print("inside test function")
    raise Exception(text)


test_fail("What are you try to fail?")
