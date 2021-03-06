#-*-coding: utf8-*-


"""
mailgun api parameters

usage:

    >>> from mailgun.parameter import Message
    >>> message = Message()
    >>> message.add_from("foo@bar.com")
    >>> message.add_to("to", "to@bar.com")
    >>> message.generate()
"""

from .event import Event
from .message import Message


__all__ = [
    'Event',
    'Message'
]