# tests/test_main.py
import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


# removes repetitive code for making POST requests in tests

def post(route, a, b):
    return client.post(route, json={"a": a, "b": b})


# /add endpoint tests

def test_add_basic():
    r = post("/add", 2, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 5.0}

def test_add_floats():
    r = post("/add", 2.5, 1.5)
    assert r.status_code == 200
    assert r.json() == {"result": 4.0}

def test_add_negatives():
    r = post("/add", -2, -3)
    assert r.status_code == 200
    assert r.json() == {"result": -5.0}

def test_add_invalid_input():
    r = client.post("/add", json={"a": "foo", "b": 3})
    assert r.status_code == 400
    assert "error" in r.json()


# /subtract endpoint tests

def test_subtract_basic():
    r = post("/subtract", 5, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 2.0}

def test_subtract_negative_result():
    r = post("/subtract", 3, 5)
    assert r.status_code == 200
    assert r.json() == {"result": -2.0}

def test_subtract_floats():
    r = post("/subtract", 5.5, 2.0)
    assert r.status_code == 200
    assert r.json() == {"result": 3.5}

def test_subtract_invalid_input():
    r = client.post("/subtract", json={"a": 5, "b": None})
    assert r.status_code == 400
    assert "error" in r.json()


# /multiply endpoint tests

def test_multiply_basic():
    r = post("/multiply", 2, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 6.0}

def test_multiply_by_zero():
    r = post("/multiply", 5, 0)
    assert r.status_code == 200
    assert r.json() == {"result": 0.0}

def test_multiply_floats():
    r = post("/multiply", 2.5, 4)
    assert r.status_code == 200
    assert r.json() == {"result": 10.0}

def test_multiply_negatives():
    r = post("/multiply", -2, 3)
    assert r.status_code == 200
    assert r.json() == {"result": -6.0}

def test_multiply_invalid_input():
    r = client.post("/multiply", json={"a": 2})
    assert r.status_code == 400
    assert "error" in r.json()


# /divide endpoint tests

def test_divide_basic():
    r = post("/divide", 6, 3)
    assert r.status_code == 200
    assert r.json() == {"result": 2.0}

def test_divide_float_result():
    r = post("/divide", 5.5, 2)
    assert r.status_code == 200
    assert r.json() == {"result": 2.75}

def test_divide_negative():
    r = post("/divide", -6, 3)
    assert r.status_code == 200
    assert r.json() == {"result": -2.0}

def test_divide_by_zero():
    r = post("/divide", 5, 0)
    assert r.status_code == 400
    assert r.json() == {"error": "Cannot divide by zero!"}

def test_divide_invalid_input():
    r = client.post("/divide", json={"a": "bar", "b": 2})
    assert r.status_code == 400
    assert "error" in r.json()


# / (root) endpoint tests 

def test_root_returns_200():
    r = client.get("/")
    assert r.status_code == 200