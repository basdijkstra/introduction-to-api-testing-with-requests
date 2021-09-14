### Installation
Ensure you have a recent version of Python (preferably 3.7 or newer) installed and configured as your interpreter.

Run `pip install -r requirements.txt` from the project root to install the dependencies (`pytest` and `requests`).

### Running the tests
Running the tests is as easy as running `pytest <test_file.py>` from the project root, e.g.

`pytest answers.py`

yielding the following output:

```text
================================= test session starts =========================
platform win32 -- Python 3.8.3, pytest-6.2.5, py-1.10.0, pluggy-1.0.0
rootdir: C:\Git\introduction-to-api-testing-with-requests
collected 10 items                                                                                                                                                           

answers.py ..........                                                    [100%]

================================== 10 passed in 1.29s =========================
```