def test_unregister_succeeds_for_existing_participant(client):
    # Arrange
    activity_name = "Chess Club"
    existing_email = "michael@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": existing_email}
    )

    # Assert
    assert response.status_code == 200
    assert response.json()["message"] == f"Unregistered {existing_email} from {activity_name}"

    updated_activity = client.get("/activities").json()[activity_name]
    assert existing_email not in updated_activity["participants"]


def test_unregister_fails_for_unknown_activity(client):
    # Arrange
    activity_name = "Unknown Activity"
    email = "someone@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Activity not found"


def test_unregister_fails_for_non_participant(client):
    # Arrange
    activity_name = "Chess Club"
    email_not_in_activity = "notenrolled@mergington.edu"

    # Act
    response = client.delete(
        f"/activities/{activity_name}/participants", params={"email": email_not_in_activity}
    )

    # Assert
    assert response.status_code == 404
    assert response.json()["detail"] == "Student not found in this activity"


def test_unregister_fails_when_email_query_is_missing(client):
    # Arrange
    activity_name = "Chess Club"

    # Act
    response = client.delete(f"/activities/{activity_name}/participants")

    # Assert
    assert response.status_code == 422
    assert "detail" in response.json()
