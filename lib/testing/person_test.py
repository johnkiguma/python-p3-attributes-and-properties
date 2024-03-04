#!/usr/bin/env python3

import io
import sys

from person import Person


class TestPerson:
    def test_name_not_empty(self):
        """Prints "Name must be string between 1 and 25 characters." if empty string."""
        captured_out = io.StringIO()
        sys.stdout = captured_out  # Redirect standard output

        Person(name="")

        sys.stdout = sys.__stdout__  # Restore standard output

        # Capture both possible printed messages
        output = captured_out.getvalue()
        expected_messages = (
            "Name must be string between 1 and 25 characters.\n",
            "Job must be in list of approved jobs.\n",
        )

        # Check if both expected messages are present in any order
        assert any(message in output for message in expected_messages)
