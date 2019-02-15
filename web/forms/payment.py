#!/usr/bin/env python
# -*- coding:utf-8 -*-
from django.forms import ModelForm, Form
from web import models


class PaymentForm(ModelForm):
    class Meta:
        model = models.Payment   #(该字段必须为 model  数据库中表)
        fields = "__all__"         # 所有字段

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label    # label 提示信息

        # 这里应该优化，如果客户多了，一个一个去选很麻烦
        self.fields['customer'].empty_label = "请选择客户"


class PaymentUserForm(ModelForm):
    class Meta:
        model = models.Payment
        exclude = ['customer',]     # 排除字段

    def __init__(self, *args, **kwargs):
        super(PaymentUserForm, self).__init__(*args, **kwargs)

        for name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
            field.widget.attrs['placeholder'] = field.label
