import pytest
from hospital_triage_priority import process_triage_wards, monitor_oxygen_manifolds

# Example test case:
def test_single_normal_patient():
    wards = [
        {
            "is_accepting": True,
            "tier": "general",
            "icu_standby": False,
            "patients": [{"spo2": 98, "hr": 72, "unconscious": False}]
        }
    ]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 10
    assert result["status"] == "TRIAGE_STABLE"

# TODO: Add test cases to achieve 90-100% on both Line and Branch coverage!

def test_invalid_wards():
    import pytest
    with pytest.raises(ValueError):
        process_triage_wards("invalid", 10)


def test_negative_acuity_score():
    import pytest
    with pytest.raises(ValueError):
        process_triage_wards([], -1)


def test_empty_wards():
    result = process_triage_wards([], 10)
    assert result == {
        "acuity_score": 0,
        "status": "NO_URGENT_CASES",
    }


def test_non_accepting_ward():
    wards = [{
        "is_accepting": False,
        "patients": [{"spo2": 80, "hr": 130}],
        "icu_standby": True,
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0
    assert result["status"] == "NO_URGENT_CASES"


def test_invalid_patient_vitals():
    wards = [{
        "is_accepting": True,
        "patients": [
            {"spo2": 0, "hr": 70},
            {"spo2": 98, "hr": 0},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0
    assert result["status"] == "NO_URGENT_CASES"


def test_unconscious_general_patient():
    wards = [{
        "is_accepting": True,
        "tier": "general",
        "patients": [{"unconscious": True}],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 100
    assert result["status"] == "TRIAGE_STABLE"


def test_unconscious_outpatient():
    wards = [{
        "is_accepting": True,
        "tier": "outpatient",
        "patients": [{"unconscious": True}],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 0
    assert result["status"] == "NO_URGENT_CASES"


def test_critical_vitals():
    wards = [{
        "is_accepting": True,
        "patients": [
            {"spo2": 89, "hr": 75},
            {"spo2": 98, "hr": 121},
        ],
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 120


def test_icu_standby():
    wards = [{
        "is_accepting": True,
        "patients": [],
        "icu_standby": True,
    }]
    result = process_triage_wards(wards, 10)
    assert result["acuity_score"] == 25


def test_ward_alert():
    wards = [{
        "is_accepting": True,
        "patients": [{"spo2": 0}] * 5,
    }]
    result = process_triage_wards(wards, 10)
    assert result["status"] == "WARD_ALERT"


def test_no_sensor_data():
    assert monitor_oxygen_manifolds([]) == "NO_DATA"


def test_pressure_failure():
    assert monitor_oxygen_manifolds([[3.5, 3.0]]) == "PRESSURE_FAILURE"


def test_pressure_recovers():
    assert monitor_oxygen_manifolds([[3.5, 4.0, 3.5]]) == "PRESSURE_NORMAL"


def test_normal_pressure():
    assert monitor_oxygen_manifolds([[4.0, 4.5, 5.0]]) == "PRESSURE_NORMAL"
