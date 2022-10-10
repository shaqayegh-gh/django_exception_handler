
from django.conf import settings
PersianErrorCodes = settings.PersianErrorCodes

persianEnglishErrorCodesDict = dict(
    sample_error={'has_attribute': False, 'farsi_detail_attrs': 'این یک خطای نمونه می باشد', 'farsi_detail': 'این یک خطای نمونه می باشد'},
    token_not_valid={'has_attribute': False, 'farsi_detail_attrs': 'token نامعتبر می باشد', 'farsi_detail': 'token نامعتبر می باشد'},
    invalid_input={'has_attribute': True, 'farsi_detail_attrs': 'attrs وارد شده نامعتبر است', 'farsi_detail': 'مقدار وارد شده نامعتبر است'},
    unique_together={'has_attribute': True, 'farsi_detail_attrs': 'attrs با این مشخصات قبلا ساخته شده است', 'farsi_detail': 'آیتم با این مشخصات قبلا ساخته شده است'},
    unique={'has_attribute': True, 'farsi_detail_attrs': 'attrs وارد شده تکراری است', 'farsi_detail': 'مقدار وارد شده تکراری است'},
    error={'has_attribute': False, 'farsi_detail_attrs': 'مشکلی در سرور به وجود آمده است', 'farsi_detail': 'مشکلی در سرور به وجود آمده است'},
    required={'has_attribute': True, 'farsi_detail_attrs': 'وارد کردن گزینه attrs اجباری می باشد', 'farsi_detail': 'وارد کردن فیلد اجباری می باشد'},
    blank={'has_attribute': True, 'farsi_detail_attrs': 'وارد کردن گزینه attrs اجباری می باشد', 'farsi_detail': 'وارد کردن فیلد اجباری می باشد'},
    invalid_choice={'has_attribute': True, 'farsi_detail_attrs': 'attrs انتخابی جزء گزینه ها نمی باشد', 'farsi_detail': 'آیتم انتخابی جزء گزینه ها نمی باشد'},
    not_found={'has_attribute': False, 'farsi_detail_attrs': 'صفحه مورد نظر یافت نشد', 'farsi_detail': 'صفحه مورد نظر یافت نشد'},
    does_not_exist={'has_attribute': True, 'farsi_detail_attrs': 'attrs انتخابی وجود ندارد', 'farsi_detail': 'این گزینه وجود ندارد'},
    null={'has_attribute': True, 'farsi_detail_attrs': 'گزینه attrs نمی تواند خالی باشد', 'farsi_detail': 'این گزینه نمی تواند خالی باشد'},
    min_length={'has_attribute': True, 'farsi_detail_attrs': 'اندازه attrs وارد شده کمتر از حد مجاز است', 'farsi_detail': 'اندازه مقدار وارد شده کمتر از حد مجاز است'},
    max_length={'has_attribute': True, 'farsi_detail_attrs': 'اندازه attrs وارد شده بیشتر از حد مجاز است', 'farsi_detail': 'اندازه مقدار وارد شده بیشتر از حد مجاز است'},
    starts_with={'has_attribute': True, 'farsi_detail_attrs': 'attrs وارد شده اشتباه است', 'farsi_detail': 'مقدار وارد شده اشتباه است'},
    incorrect_otp_code={'has_attribute': False, 'farsi_detail_attrs': 'کد وارد شده اشتباه است', 'farsi_detail': 'کد وارد شده اشتباه است'},
    phone_number_user_not_exist={'has_attribute': False, 'farsi_detail_attrs': 'حساب کاربری با شماره تلفن وارد شده یافت نشد',
                                 'farsi_detail': 'حساب کاربری با شماره تلفن وارد شده یافت نشد'},
    not_authenticated={'has_attribute': False, 'farsi_detail_attrs': 'برای انجم درخواست به حساب کاربری خود وارد شوید',
                       'farsi_detail': 'برای انجم درخواست به حساب کاربری خود وارد شوید'},
)

persianEnglishErrorCodesDict.update(PersianErrorCodes)
