# This file is part of the Reproducible Open Benchmarks for Data Analysis
# Platform (ROB).
#
# Copyright (C) [2019-2020] NYU.
#
# ROB is free software; you can redistribute it and/or modify it under the
# terms of the MIT License; see LICENSE file for more details.

"""Helper methods to access configuration parameters. Following the
Twelve-Factor App methodology all configuration parameters are maintained in
environment variables.

The name of methods that provide access to values from environment variables
are in upper case to emphasize that they access configuration values that are
expected to remain constant throughout the lifespan of a running application.
"""

import os

from flowserv.config.api import API_BASEDIR


"""Environment variables that contain configuration parameters for the Web
API.
"""
# Directory path for API logs
ROB_WEBAPI_LOG = 'ROB_WEBAPI_LOG'
# Maximum size of uploaded files (in bytes)
ROB_WEBAPI_CONTENTLENGTH = 'ROB_WEBAPI_CONTENTLENGTH'


# -- Helper methods to access configutation parameters ------------------------

def LOG_DIR():
    """Get the logging directory for the Web API from the respective
    environment variable 'ROB_WEBAPI_LOG'. If the variable is not set a
    sub-folder 'log' in the API base directory use used as the default.

    Returns
    -------
    string
    """
    log_dir = os.environ.get(ROB_WEBAPI_LOG)
    # If the variable is not set create a sub-folder in the API base directory
    if log_dir is None:
        log_dir = os.path.join(API_BASEDIR(), 'log')
    return os.path.abspath(log_dir)


def MAX_CONTENT_LENGTH():
    """Get the maximum size for uploaded files from the respective environment
    variable 'ROB_WEBAPI_CONTENTLENGTH'. If the variable is not set the
    default value that is equal to 16MB is used.

    Returns
    -------
    string

    Raises
    ------
    ValueError
    """
    value = os.environ.get(ROB_WEBAPI_CONTENTLENGTH)
    if value is None:
        # If the variable is not set use a default of 16MB
        return 16 * 1024 * 1024
    else:
        # Convert the value to integer. This may raise a value error
        return int(value)
