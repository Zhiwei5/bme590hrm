def test_json_add():
    """
    Tests the json_add function
    """
    try:
        import pytest
        from heart_module.json_add import json_add
        import json
        from pprint import pprint
    except ImportError:
        print("Necessary imports for this test function failed")
        return

    test_mean_hr_bpm = 1
    test_voltage_extremes = (2, 7)
    test_duration = 30
    test_num_beats = 30
    test_beats = [1, 2, 3]
    test_info = 'test.csv'
    # (mean_hr_bpm, voltage_extremes, duration, num_beats, beats, info):
    json_add(test_mean_hr_bpm, test_voltage_extremes, test_duration,
             test_num_beats, test_beats, test_info)

    data = json.load(open('test.json'))
    pprint(data)
    assert data['mean_hr_bpm'] == 1
    assert data['voltage_extremes'] == [2, 7]
    assert data['duration'] == 30
    assert data['num_beats'] == 30
    assert data['beats'] == [1, 2, 3]
