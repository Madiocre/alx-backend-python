#!/usr/bin/env python3
"""Generic utilities for github org client.
"""
from utils import access_nested_map
import requests
from functools import wraps
from typing import (
    Mapping,
    Sequence,
    Any,
    Dict,
    Callable,
)

nested_map = {"a": {"b": {"c": 1}}}
access_nested_map(nested_map, ["a", "b", "c"])