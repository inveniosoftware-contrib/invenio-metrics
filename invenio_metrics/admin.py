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

"""Admin interface to metrics."""

from __future__ import absolute_import, print_function

from flask_admin.contrib.sqla import ModelView

from .models import ResourceUsage


def _(x):
    """Identity function for string extraction."""
    return x


class ResourceUsageModelView(ModelView):
    """Resource usage admin interface."""

    can_create = False
    can_edit = False
    can_delete = False

    column_list = (
        'object_type', 'object_id', 'metric', 'value', 'modified',
    )

    column_filters = ['object_type', 'metric']

    column_searchable_list = ['object_type', 'object_id', 'metric']

    column_default_sort = ('modified', True)


resourceusage_adminview = dict(
    modelview=ResourceUsageModelView,
    model=ResourceUsage,
    category=_('Metrics'))
