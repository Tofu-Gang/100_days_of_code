import unittest
from os import getcwd, sep, walk, chdir
from os.path import basename, normpath
from typing import Tuple

from utils import extract_day_number_from_dir_name, prefix_day_number_with_zeroes, _get_src_directories, \
                   _get_implemented_days
from constants import SRC_DIR_NAME


########################################################################################################################

def _get_src_directories_for_tests() -> Tuple[str, ...]:
    """
    Collect the directories names in a different way from the function utils.get_src_directories()
    (utils.get_src_directories() uses os.listdir, this function used in tests uses os.walk).

    :return: a sorted tuple of directories names in the src folder
    """

    # collect directories names in src folder
    directories = []
    # save the original working directory, chdir changes are global
    original_cwd = getcwd()
    chdir("..")

    for root, dirs, _ in walk(getcwd() + sep + SRC_DIR_NAME):
        for name in dirs:
            if basename(normpath(root)) == SRC_DIR_NAME:
                # collect directory name only if it is in the src folder
                directories.append(name)

    # go back to the original working directory
    chdir(original_cwd)
    # make the list a sorted tuple
    return tuple(sorted(directories))


########################################################################################################################

class TestUtils(unittest.TestCase):

    def test_extract_day_number_from_dir_name(self) -> None:
        """
        Test the utils.extract_day_number_from_dir_name() function. Compare its result with mocked source directory name
        for every valid day number between 1 and 100 (both inclusive); they should be equal.
        """

        for i in range(1, 101):
            tested_day_number = extract_day_number_from_dir_name(
                "day_" + prefix_day_number_with_zeroes(str(i)) + "_example_project")
            self.assertEqual(tested_day_number, i)

########################################################################################################################

    def test_prefix_day_number_with_zeroes(self) -> None:
        """
        Test the utils.prefix_day_number_with_zeroes() function. Compare its result for every number between 1 and 100
        (both inclusive) with a result of a different way of prefixing the number (with a format string); they should be
        equal.
        """

        for i in range(1, 101):
            self.assertEqual(prefix_day_number_with_zeroes(str(i)), "{:03d}".format(i))

########################################################################################################################

    def test_get_src_directories(self) -> None:
        """
        Test the utils._get_src_directories() function. Compare its result in a form of a sorted tuple to the result of
        the function get_src_directories_for_tests() from this module; they should be equal.
        """

        # get the result of the tested function and the names collected in this test; make them both a sorted tuple and
        # test their equality
        self.assertEqual(_get_src_directories_for_tests(), tuple(sorted(_get_src_directories())))

########################################################################################################################

    def test_get_implemented_days(self) -> None:
        """
        Test the utils._get_implemented_days() function. Compare its result in a form of a sorted tuple to the result
        of the function _get_src_directories_for_tests() from this module, after applying the same map() as in the
        tested function; they should be equal.
        """

        self.assertEqual(
            tuple(sorted(map(extract_day_number_from_dir_name, _get_src_directories_for_tests()))),
            tuple(sorted(_get_implemented_days())))


########################################################################################################################

if __name__ == '__main__':
    unittest.main()

########################################################################################################################
