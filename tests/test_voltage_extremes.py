def test_voltage_extremes():
    """
    Tests the voltage_extremes function
    """
    try:
        import pytest
        from heart_module.voltage_extremes import voltage_extremes
    except ImportError:
        print("Necessary imports for this test function failed")
        return
    test_data1 = [0, -3, -1.2, 10]
    test_data2 = [1, 3, 2, 5]
    test_data3 = [-3/2, -9, -3, -7, -1]
    test_data4 = []
    test_answer1 = (-3, 10)
    test_answer2 = (1, 5)
    test_answer3 = (-9, -1)
    test_answer4 = (None, None)
    assert test_answer1 == voltage_extremes(test_data1)
    assert test_answer2 == voltage_extremes(test_data2)
    assert test_answer3 == voltage_extremes(test_data3)
    assert test_answer4 == voltage_extremes(test_data4)
    with pytest.raises(TypeError):
        voltage_extremes(5)
    with pytest.raises(TypeError):
        voltage_extremes('abc')
    with pytest.raises(TypeError):
        voltage_extremes({1: 4})
    with pytest.raises(ValueError):
        voltage_extremes(['s', 's'])
    with pytest.raises(ValueError):
        voltage_extremes(['-inf', 5])
    with pytest.raises(ValueError):
        voltage_extremes(['+inf', 5])
    with pytest.raises(ValueError):
        voltage_extremes([float('inf'), 5])
    with pytest.raises(ValueError):
        voltage_extremes([float('-inf'), 5])