#!/usr/bin/env python
# _*_ coding:utf-8 _*

"""
@author:    Rubén Hortas Astariz <http://rubenhortas.blogspot.com>
@contact:   rubenhortas at gmail.com
@github:    http://githug.com/rubenhortas/
@license:   CC BY-NC-SA 3.0 <http://creativecommons.org/licenses/by-nc-sa/3.0/>
@file:      Messages.py
"""


class message:
    """
    Class message
        Stores and displays an information (or error) message.
    """
    msg = None
    msg_type = None

    def __init__(self, msg_type, msg):
        """
        __init__(self, msg_type, msg)
            Stores and displays a message.
        Args:
            - msg_type: (string) Type of the message.
                        - information
                        - error
            - msg: (string) Messages.
        """
        self.msg_type = msg_type
        self.msg = msg
        self.print_msg()

    def print_msg(self):
        """
        print_msg(self)
            Displays the message in a nice format.
        """
        if self.msg_type == 'error':
            print tag.error + color.bold_red + 'Error: ' + color.end \
                + self.msg
        else:
            print tag.info_msg + color.bold_green + 'INFO: ' \
                + color.end + self.msg
