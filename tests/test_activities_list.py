def test_get_activities_returns_expected_structure(client):
    # Arrange
    expected_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    data = response.json()

    # Assert
    assert response.status_code == 200
    assert expected_activity in data
    assert "description" in data[expected_activity]
    assert "schedule" in data[expected_activity]
    assert "max_participants" in data[expected_activity]
    assert "participants" in data[expected_activity]
