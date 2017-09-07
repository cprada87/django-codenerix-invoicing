# -*- coding: utf-8 -*-
#
# django-codenerix-pos
#
# Copyright 2017 Centrologic Computational Logistic Center S.L.
#
# Project URL : http://www.codenerix.com
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from django import forms
from django.utils.translation import ugettext_lazy as _

from codenerix.forms import GenModelForm
from codenerix.widgets import MultiStaticSelect

from codenerix_invoicing.models_sales import SalesOrder
from codenerix_invoicing.models_purchases import PAYMENT_DETAILS_CARD
from .models_cash import CashDiary, CashMovement


class CashDiaryForm(GenModelForm):
    class Meta:
        model = CashDiary
        exclude = ['user', ]

    def __groups__(self):
        return [
            (
                _('Point of Sales'), 12,
                ['pos', 12],
            ), (
                _('Opened'), 12,
                ['opened_user', 4],
                ['opened_date', 4],
                ['opened_amount', 4],
            ), (
                _('Closed'), 12,
                ['closed_user', 4],
                ['closed_date', 4],
                ['closed_amount', 4],
            )
        ]

    @staticmethod
    def __groups_details__():
        return [
            (
                _('Point of Sales'), 12,
                ['pos', 12],
            ), (
                _('Opened'), 12,
                ['opened_user', 4],
                ['opened_date', 4],
                ['opened_amount', 4],
            ), (
                _('Closed'), 12,
                ['closed_user', 4],
                ['closed_date', 4],
                ['closed_amount', 4],
            )
        ]


class CashMovementForm(GenModelForm):
    order = forms.ModelMultipleChoiceField(
        queryset=SalesOrder.objects.all(),
        label=_('Orders'),
        required=False,
        widget=MultiStaticSelect(
            attrs={'manytomany': True, }
        )
    )

    class Meta:
        model = CashMovement
        exclude = ['user', ]

    def __groups__(self):
        return [
            (
                _('Details'), 12,
                ['order', 6],
                ['pos_slot', 6],
                ['kind', 6],
                ['kind_card', 6],
                ['date_movement', 6],
                ['amount', 6],
            )
        ]

    @staticmethod
    def __groups_details__():
        return [
            (
                _('Details'), 12,
                ['user', 6],
                ['order', 6],
                ['pos_slot', 6],
                ['kind', 6],
                ['kind_card', 6],
                ['date_movement', 6],
                ['amount', 6],
            )
        ]

    def clean(self):
        cleaned_data = super(CashMovementForm, self).clean()
        kind = cleaned_data.get('kind', None)
        kind_card = cleaned_data.get('kind_card', None)
        if kind == PAYMENT_DETAILS_CARD and kind_card is None:
            self.add_error('kind_card', _('Kind card is required'))
