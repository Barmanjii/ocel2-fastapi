# Main Pythons Imports
import re
from collections.abc import Mapping

UNDERSCORE_RE = re.compile(r"(?<=[^\-_])[\-_]+[^\-_]")


def camelize_for_request(str_or_iter: list | dict) -> list | dict:
    """
    Camelize the keys in the request body. Used in PUT and POST calls and also models

    Args:
        str_or_iter (list | dict): Input schema in list or dict or json format

    Returns:
        list | dict: Camelized output
    """

    def _process_keys(str_or_iter: list | dict) -> list | dict:
        """
        Camelize the list object
        Args:
            str_or_iter (list | dict): Take input from the camelize_for_request as in list of dict

        Returns:
            list | dict: if str_or_iter is list then it will recursively calls iteself, if dict then return dict
        """
        if isinstance(str_or_iter, list):
            return [_process_keys(k) for k in str_or_iter]
        return str_or_iter

    def _is_none(_in: list) -> list:
        """
        Checks if the input is None

        Args:
            _in (list): Input list

        Returns:
            _in : Empty string if None, else the input is returned with white-space removed
        """
        return "" if _in is None else re.sub(r"\s+", "", str(_in))

    if isinstance(str_or_iter, (list, Mapping)):
        return _process_keys(str_or_iter)

    s = _is_none(str_or_iter)
    if s.isupper() or s.isnumeric():
        return str_or_iter

    if len(s) != 0 and not s[:2].isupper():
        s = s[0].lower() + s[1:]

    return UNDERSCORE_RE.sub(lambda m: m.group(0)[-1].upper(), s)
