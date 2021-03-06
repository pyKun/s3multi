"""
Static Web Middleware for OpenStack Swift
"""

__all__ = ['version_info', 'version']

#: Version information ``(major, minor, revision)``.
version_info = (0, 1, 0)
#: Version string ``'major.minor.revision'``.
version = '.'.join(map(str, version_info))
