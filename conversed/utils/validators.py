#!/usr/bin/env python

import dns.resolver
import re

__all__ = ['validate']

def validate(emailid):
    """
    Validator to confirm an email address is likely to be valid because its
    domain exists and has an MX record.

    :param str message: The email address that needs validation.
    """
    email = re.match("^[a-zA-Z][\w\.-]*[a-zA-Z0-9]@[a-zA-Z][\w\.-]*[a-zA-Z0-9]\.[a-zA-Z][a-zA-Z\.]*[a-zA-Z]$", emailid)
    if email:
        email_domain = emailid.split('@')[-1]
        if not email_domain:
            return 1
        try:
            dns.resolver.query(email_domain, 'MX')
        except dns.resolver.NXDOMAIN:
            return 1
        except dns.resolver.NoAnswer:
            return 1
        except (dns.resolver.Timeout, dns.resolver.NoNameservers):
            return None
    else:
        return 1

