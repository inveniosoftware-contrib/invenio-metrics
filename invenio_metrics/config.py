# -*- coding: utf-8 -*-
#
# This file is part of Invenio.
# Copyright (C) 2015 CERN.
#
# Invenio is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Invenio is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Invenio; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Configuration for metrics module."""

from __future__ import absolute_import, print_function

METRICS_PUBLISH_METRICS = []
"""Determine which metrics to publish."""

#
# XSLS related variables.
#
METRICS_XSLS_API_URL = "http://xsls-dev.cern.ch"
"""XSLS API endpoint."""

METRICS_XSLS_SERVICE_ID = None
"""XSLS service id."""

METRICS_XSLS_EMAIL = None
"""Email address to send to XSLS."""

METRICS_XSLS_WEBPAGE = None
"""Website to send to XSLS."""

METRICS_XSLS_AVAILABILITY = None
"""Import path to callable that will compute an availability value (0-100).

The callable must take one argument which is the ServiceDocument that will
be sent to the XSLS service.

See http://itmon.web.cern.ch/itmon/recipes/how_to_create_a_service_xml.html
"""
