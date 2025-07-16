import os
import re
from pathlib import Path
from typing import Union, List

from utils.driver_manager import DriverManager
from utils.logger import Logger

counter = 0

def get_current_test_name():
    test_full_name = os.environ.get('PYTEST_CURRENT_TEST')
    return re.search('::(\w+)\s', test_full_name).group(1)


def verify(check: Union[List[bool], bool], f_msg, p_msg=''):
    global counter
    driver = DriverManager().driver
    logger = Logger("Verification")
    if isinstance(check, bool):
        check = [check]
    assert all(check), f_msg
    evidence_path = Path(f"./test_results/evidences/{get_current_test_name()}/evidence_{counter}.png")
    if not evidence_path.parent.exists():
        evidence_path.parent.mkdir(parents=True)
    driver.save_screenshot(evidence_path)
    counter += 1
    logger.info(f'Verified: {p_msg} ({evidence_path})')

