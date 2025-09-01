from rest_framework.throttling import UserRateThrottle

class TenCallsPerMinute(UserRateThrottle):
    scope = 'ten_per_minute'