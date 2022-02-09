from phonenumbers import (
    NumberParseException,
    PhoneNumberFormat,
    PhoneNumberType,
    format_number,
    is_valid_number,
    number_type,
    parse as parse_phone_number,
)
from pydantic import BaseModel, EmailStr, constr, validator

MOBILE_NUMBER_TYPES = PhoneNumberType.MOBILE, PhoneNumberType.FIXED_LINE_OR_MOBILE
RUSSIAN_COUNTRY_CODE = 7


class CreateUser(BaseModel):
    first_name: constr(min_length=4, max_length=50, strip_whitespace=True)
    last_name: constr(min_length=4, max_length=50, strip_whitespace=True)
    phone_number: constr(max_length=50, strip_whitespace=True) = None
    email: EmailStr

    @validator("phone_number")
    def check_phone_number(cls, v):
        if v is None:
            return v

        try:
            n = parse_phone_number(v, "GB")
        except NumberParseException as e:
            raise ValueError("Please provide a valid mobile phone number") from e

        if not is_valid_number(n) or number_type(n) not in MOBILE_NUMBER_TYPES:
            raise ValueError("Please provide a valid mobile phone number")

        return format_number(n,
                             PhoneNumberFormat.NATIONAL if n.country_code == RUSSIAN_COUNTRY_CODE else PhoneNumberFormat.INTERNATIONAL)


class DeleteUser(BaseModel):
    email: EmailStr


class UpdateUser(BaseModel):
    first_name: constr(min_length=4, max_length=50, strip_whitespace=True)
    last_name: constr(min_length=4, max_length=50, strip_whitespace=True)
    phone_number: constr(max_length=50, strip_whitespace=True) = None
    email: EmailStr

    @validator("phone_number")
    def check_phone_number(cls, v):
        if v is None:
            return v

        try:
            n = parse_phone_number(v, "GB")
        except NumberParseException as e:
            raise ValueError("Please provide a valid mobile phone number") from e

        if not is_valid_number(n) or number_type(n) not in MOBILE_NUMBER_TYPES:
            raise ValueError("Please provide a valid mobile phone number")

        return format_number(n,
                             PhoneNumberFormat.NATIONAL if n.country_code == RUSSIAN_COUNTRY_CODE else PhoneNumberFormat.INTERNATIONAL)
