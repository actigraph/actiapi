def test_metadata(v3_client, v3_study_id):
    metadata = v3_client.get_study_metadata(v3_study_id)
    assert len(metadata) == 2


def test_minutes(v3_client, v3_study_id):
    metadata = v3_client.get_study_metadata(v3_study_id)
    id_ = metadata[0]["id"]
    minutes = v3_client.get_minute_summary(id_, v3_study_id)
    assert len(minutes) == 3208
    assert minutes[0].keys() == {
        "subjectId",
        "timestampUtc",
        "minuteSummarySettingsId",
        "activityMonitorSerial",
        "studyId",
        "isWear",
        "isSleep",
        "x",
        "y",
        "z",
        "vectorMagnitude",
        "steps",
        "mets",
        "calories",
        "staudenmayerCutPointsMinuteAggregations",
    }


def test_daily(v3_client, v3_study_id):
    metadata = v3_client.get_study_metadata(v3_study_id)
    id_ = metadata[0]["id"]
    daily = v3_client.get_daily_summary(id_, v3_study_id)
    assert len(daily) == 3
    assert daily[0].keys() == {
        "id",
        "studyId",
        "dailyStatisticsSettingId",
        "subjectId",
        "date",
        "siteId",
        "activityMonitorSerials",
        "epochAggregation",
        "staudenmayerAggregations",
        "uwfAggregation",
        "hildebrandMetCalorieAggregation",
        "firstEpochDateTimeUtc",
        "lastEpochDateTimeUtc",
        "firstEpochDateTimeLocal",
        "lastEpochDateTimeLocal",
    }


def test_raw(v3_client, v3_study_id):
    metadata = v3_client.get_study_metadata(v3_study_id)
    id_ = metadata[0]["id"]
    raw_files = v3_client.get_files(user=id_, study_id=v3_study_id)
    assert len(raw_files) == 0
