"""Tests for updatedata command."""

from io import StringIO

from django.core.management import call_command
from django.core.management.base import BaseCommand

from eat_better.management.commands.updatedata import Command


def test_class():
    """Test that Command class exists and is a subclass of BaseCommand."""
    assert Command()
    assert issubclass(Command, BaseCommand)


def test_out():
    """Test the output of the command."""
    out = StringIO()
    call_command("updatedata", stdout=out)
    assert "Updating database..." in out.getvalue()
    assert "Database is up to date !" in out.getvalue()

