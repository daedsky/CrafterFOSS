from enum import StrEnum


class AppInfo(StrEnum):
    VERSION = '0.0.2'
    THEME_MODE_KEY = 'io.crafter.CrafterFOSS.ThemeMode'
    THEME_COLOR_KEY = 'io.crafter.CrafterFOSS.ThemeColor'
    LICENSE_AGREED_KEY = 'io.crafter.CrafterFOSS.LICENSE_AGREED'
    STORAGE_PERMS_DENIED = 'io.crafter.CrafterFOSS.StoragePermsDenied'
    PRIVACY_POLICY_URL = 'https://github.com/daedsky/CrafterFOSS/blob/master/docs/privacy_policy.md'
    APP_LICENSE_URL = 'https://github.com/daedsky/CrafterFOSS/blob/master/LICENSE'
    GIT_REPO_URL = 'https://github.com/daedsky/CrafterFOSS'
