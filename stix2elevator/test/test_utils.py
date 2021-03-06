# external
import pytest
from stix.indicator import Indicator

# internal
from stix2elevator import convert_stix, utils
from stix2elevator.options import _convert_to_int_list
from stix2elevator.utils import Environment


def test_strftime_with_appropriate_fractional_seconds():
    base_timestamp = "2017-03-29T05:05:05.555Z"
    mili_expected_timestamp = "2017-03-29T05:05:05.555000Z"

    milisecond_timestamp = utils.strftime_with_appropriate_fractional_seconds(base_timestamp, True)
    assert base_timestamp == milisecond_timestamp

    trunc_timestamp = utils.strftime_with_appropriate_fractional_seconds(base_timestamp, False)
    assert mili_expected_timestamp == trunc_timestamp


def test_convert_timestamp_string():
    # Create v1 and v2 indicator, test timestamp pre and post convert_timestamp_call

    # Maybe take a v1 idiom

    # child_timestamp = "2017-03-29T05:05:05.555Z"
    parent_timestamp = "2017-03-29T05:09:09.999Z"
    env = Environment(timestamp=parent_timestamp)
    indicator = Indicator()
    indicator_instance = convert_stix.create_basic_object("indicator", indicator, env)
    assert indicator_instance is not None


@pytest.mark.parametrize("data", [
    [123, 245, 344],
    "123,245,344",
    ["123", "245", 344],
])
def test_convert_int_function(data):
    assert _convert_to_int_list(data) == [123, 245, 344]


@pytest.mark.parametrize("data", [
    "12 3,245,344",
    "212,garbage,33",
    "definitely-not,an_int",
    234,
])
def test_convert_int_function_bad(data):
    with pytest.raises((RuntimeError, ValueError)):
        _convert_to_int_list(data)
