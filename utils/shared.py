from typing import Any 
from datetime import datetime, timezone, date
import enum


def preprocess_search_params(
        search_params: dict[str, Any]) -> tuple[dict[str, str], dict[str, str], dict[str, str]]:
    """Preprocess search parameters for quering the database.
    Integer-valued fields are not supported.

    Args:
        search_params (dict): The search parameters

    Returns:
        tuple[dict[str, str], dict[str, str], dict[str, str]]: The search dictionaries containing other type values, string-valued
        search dictionary and date-valued search dictionary.
        Format: `(string-valued dictionary, date-valued dictionary)`
    """
    str_search_dict = dict()
    datetime_search_dict = dict()
    other_types_search_dict = dict()
    for field_name, value in search_params.items():
        # do not include fields whose values are None
        if value is None:
            continue
        # format values appropriately
        elif any([
            isinstance(value, enum.Enum),
            isinstance(value, bool),
            isinstance(value, int),
            isinstance(value, float),
        ]):
            other_types_search_dict[field_name] = value
        # prepare values of date and/or time format
        elif any([isinstance(value, date), isinstance(value, datetime)]):
            datetime_search_dict[field_name] = value.date(
            ) if isinstance(value, datetime) else value
        # prepare values of other types (only string are expected)
        else:
            str_search_dict[field_name] = f"%{value}%"
    # return the preprocessed search parameters
    return str_search_dict, other_types_search_dict, datetime_search_dict