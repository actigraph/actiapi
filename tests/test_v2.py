def test_metadata(v2_client, v2_study_id):
    metadata = v2_client.get_study_metadata(v2_study_id)
    assert len(metadata) == 2


def test_daily(v2_client, v2_study_id):
    metadata = v2_client.get_study_metadata(v2_study_id)
    id_ = metadata[0]["Id"]
    daily = v2_client.get_daily_summary(id_)
    assert len(daily) == 3
    assert daily[0].keys() == {
        "Date",
        "Bouts",
        "Calories",
        "Cutpoints",
        "AxisXCounts",
        "AxisYCounts",
        "AxisZCounts",
        "Epochs",
        "MVPA",
        "Steps",
        "TotalMinutes",
        "WearFilteredBouts",
        "WearFilteredCalories",
        "WearFilteredCutPoints",
        "WearFilteredAxisXCounts",
        "WearFilteredAxisYCounts",
        "WearFilteredAxisZCounts",
        "WearFilteredMVPA",
        "WearFilteredSteps",
        "WearMinutes",
        "AwakeWearMinutes",
    }
