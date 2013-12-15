#
# Switch2bill-common
#
# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
#
# Copyright (C) 2011-2013 Star2Billing S.L.
#
# The Initial Developer of the Original Code is
# Arezqui Belaid <info@star2billing.com>
#
from utils import Choice
from django.utils.translation import ugettext_lazy as _


class EXPORT_CHOICE(Choice):
    CSV = 'csv', _('csv').upper()
    XLS = 'xls', _('xls').upper()
    JSON = 'json', _('json').upper()
