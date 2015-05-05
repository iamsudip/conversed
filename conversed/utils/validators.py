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
    email = re.match("""^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])$""", emailid)
    if email:
        email_domain = emailid.split('@')[-1]
        if not email_domain:
            return False
        try:
            dns.resolver.query(email_domain, 'MX')
        except dns.resolver.NXDOMAIN:
            return False
        except dns.resolver.NoAnswer:
            return False
        except (dns.resolver.Timeout, dns.resolver.NoNameservers):
            return True
        else:
            return True
    else:
        return False

