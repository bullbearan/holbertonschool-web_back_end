#!/usr/bin/env python3
"This is a line of text"
from parameterized import parameterized
import unittest
from unittest import mock
from utils import access_nested_map, get_json, memoize


class TestAccessNestedMap(unittest.TestCase):
    "This is a line of text"
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expect):
        "This is a line of text"
        self.assertEqual(access_nested_map(nested_map, path), expect)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b"))
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        "This is a line of text"
        with self.assertRaises(KeyError) as error:
            access_nested_map(nested_map, path)
        self.assertEqual(error.exception.args[0], path[-1])


class TestGetJson(unittest.TestCase):
    "This is a line of text"
    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @mock.patch('test_utils.get_json')
    def test_get_json(self, url, payload, mock):
        "This is a line of text"
        mock.return_value = payload
        res = get_json(url)
        self.assertEqual(res, payload)


class TestMemoize(unittest.TestCase):
    "This is a line of text"
    def test_memoize(self):
        "This is a line of text"
        class TestClass:

            def a_method(self):
                return 42

            @memoize
            def a_property(self):
                return self.a_method()
        with mock.patch.object(TestClass, "a_method") as mock_method:
            TestClass.a_property
            TestClass.a_property
            mock_method.assert_called_once
