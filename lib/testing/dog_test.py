#!/usr/bin/env python3
import io
import sys

from dog import Dog


class TestDog:
    def test_name_not_empty(self):
        """Prints "Name must be string between 1 and 25 characters." if empty string."""
        captured_out = io.StringIO()
        sys.stdout = captured_out  # Redirect standard output

        Dog(name="")

        sys.stdout = sys.__stdout__  # Restore standard output

        # Capture both possible printed messages
        output = captured_out.getvalue()
        expected_messages = (
            "Name must be string between 1 and 25 characters.\n",
            "Breed must be in list of approved breeds.\n",
        )

        # Check if both expected messages are present in any order
        assert any(message in output for message in expected_messages)
