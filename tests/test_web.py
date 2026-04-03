"""Tests for calculator_app.web Flask application."""

import json

import pytest

from calculator_app.web import app


@pytest.fixture()
def client():
    """Return a Flask test client with testing mode enabled."""
    app.config["TESTING"] = True
    with app.test_client() as c:
        yield c


class TestIndexRoute:
    def test_get_returns_200(self, client) -> None:
        response = client.get("/")
        assert response.status_code == 200

    def test_get_returns_html(self, client) -> None:
        response = client.get("/")
        assert b"<!DOCTYPE html>" in response.data or b"<!doctype html>" in response.data.lower()

    def test_content_type_is_html(self, client) -> None:
        response = client.get("/")
        assert "text/html" in response.content_type


class TestCalculateRoute:
    # --- happy path ---

    def test_addition(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "3+4"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        data = response.get_json()
        assert data["result"] == pytest.approx(7.0)

    def test_subtraction(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "10-3"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == pytest.approx(7.0)

    def test_multiplication(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "6*7"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == pytest.approx(42.0)

    def test_division(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "9/3"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == pytest.approx(3.0)

    def test_float_operands(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "1.5+2.5"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == pytest.approx(4.0)

    def test_expression_with_spaces(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "8 / 2"}),
            content_type="application/json",
        )
        assert response.status_code == 200
        assert response.get_json()["result"] == pytest.approx(4.0)

    def test_response_contains_result_key(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "1+1"}),
            content_type="application/json",
        )
        assert "result" in response.get_json()

    # --- error cases ---

    def test_division_by_zero_returns_400(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "5/0"}),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert "error" in response.get_json()

    def test_division_by_zero_error_message(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "5/0"}),
            content_type="application/json",
        )
        data = response.get_json()
        assert "zero" in data["error"].lower()

    def test_invalid_expression_returns_400(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "not-an-expression"}),
            content_type="application/json",
        )
        assert response.status_code == 400
        assert "error" in response.get_json()

    def test_missing_expression_key_returns_400(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"foo": "bar"}),
            content_type="application/json",
        )
        assert response.status_code == 400

    def test_empty_body_returns_400(self, client) -> None:
        response = client.post(
            "/calculate",
            data="",
            content_type="application/json",
        )
        assert response.status_code == 400

    def test_non_json_content_type_returns_400(self, client) -> None:
        response = client.post(
            "/calculate",
            data="expression=1+1",
            content_type="application/x-www-form-urlencoded",
        )
        assert response.status_code == 400

    def test_error_response_has_error_key(self, client) -> None:
        response = client.post(
            "/calculate",
            data=json.dumps({"expression": "abc/xyz"}),
            content_type="application/json",
        )
        data = response.get_json()
        assert "error" in data
        assert "result" not in data
