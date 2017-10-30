# Common utility tools

import re

from bmcore.models.voucher_model import VoucherModel


# Function that generates validated string
def gen_val_str(value):

    if value is not None:

        # Remove all chars except the below REGEX
        result = re.sub('[^a-zA-Z0-9]', '', value)

        # Removes whitespaces between strings
        result = "".join(result.lower().split())

        return result

    return None


# Function that checks the existence of an object in a model
def check_obj_exists(model, obj_id, **kwargs):

    name = kwargs.get('name', None)

    _model_name = model.__name__

    _if_exists_text = _model_name + ' already exists'

    _val_name = gen_val_str(name)

    # Validate model with arguments omitting obj_id, if obj_id is not none

    if name is not None:

        if obj_id is None:

            account_exists = model.objects.filter(val_name=_val_name).exists()

            if account_exists:
                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

        elif obj_id is not None:

            account_exists = model.objects.exclude(pk=obj_id).filter(val_name=_val_name).exists()

            if account_exists:

                return {'status': True, 'message': _if_exists_text}

            return {'status': False}

    return ValueError('Cannot check for model existence if arguments are None')


# Function that increment voucher number for a particular voucher type
def increment_voucher(voucher_type):

    model_obj = VoucherModel.objects.get(voucher_template__voucher_type__name=voucher_type)

    model_obj.vch_no += 1

    model_obj.save()

    return model_obj
