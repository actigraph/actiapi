from actiapi.v3 import validate_response


def test_study_info(v3_client, v3_study_id):
    info = v3_client.get_study_info(v3_study_id)
    assert info["id"] == 954
    assert info["name"] == "GT9X - CP3 Validation Study"


def test_studies(v3_client):
    info = v3_client.get_studies()
    assert len(info) > 1


def test_metadata(v3_client, v3_study_id):
    metadata = v3_client.get_study_metadata(v3_study_id)
    assert len(metadata) == 2


def test_validate_empty_response(response_404):
    result = validate_response(response_404)
    assert result is None


def test_sleep(v3_client, v3_user, v3_study_id):
    sleep = v3_client.get_sleep_summary(v3_user, v3_study_id)
    assert len(sleep) == 8
    assert sleep[0]["inBedTime"] == "2022-03-30T16:29:00+00:00"


def test_event_marker(v3_client, v3_user, v3_study_id):
    # This test study has no event marker data,
    # so this test merely verifies
    # that the `get_event_markers(.)` method does not
    # crash and returns an empty result.
    result = v3_client.get_event_markers(v3_user, v3_study_id)
    assert len(result) == 0


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


class TestRaw:
    def test_raw(self, v3_client, v3_study_id):
        metadata = v3_client.get_study_metadata(v3_study_id)
        id_ = metadata[0]["id"]
        raw_files = v3_client.get_files(user=id_, study_id=v3_study_id)
        assert len(raw_files) == 0

    def test_raw_between_dates(self, v3_client, v3_study_id):
        metadata = v3_client.get_study_metadata(v3_study_id)
        id_ = metadata[0]["id"]
        raw_files = v3_client.get_files(
            user=id_, study_id=v3_study_id, start="2010-04-14", end="2022-04-15"
        )
        assert len(raw_files) == 0

    def test_raw_before_end(self, v3_client, v3_study_id):
        metadata = v3_client.get_study_metadata(v3_study_id)
        id_ = metadata[0]["id"]
        raw_files = v3_client.get_files(
            user=id_, study_id=v3_study_id, end="2022-04-15"
        )
        assert len(raw_files) == 0

    def test_raw_after_start(self, v3_client, v3_study_id):
        metadata = v3_client.get_study_metadata(v3_study_id)
        id_ = metadata[0]["id"]
        raw_files = v3_client.get_files(
            user=id_, study_id=v3_study_id, start="2022-04-15"
        )
        assert len(raw_files) == 0
