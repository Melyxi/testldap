#!/usr/bin/python
# -*- coding: utf-8 -*-
import getpass
import ldb
from samba.auth import system_session
from samba.credentials import Credentials
from samba.dcerpc import security
from samba.dcerpc.security import dom_sid
from samba.ndr import ndr_pack, ndr_unpack
from samba.param import LoadParm
from samba.samdb import SamDB

lp = LoadParm()
creds = Credentials()
creds.guess(lp)
creds.set_username('administrator')
creds.set_password('qqqwww12!')
samdb = SamDB(url='ldap://185.61.26.170:54732', session_info=system_session(),credentials=creds, lp=lp)

query = "(|(objectclass=user)(objectclass=computer)(objectclass=group))"
result = samdb.search('DC=samba,DC=redos', expression=query, scope=ldb.SCOPE_SUBTREE)
for item in result:
    if 'sAMAccountName' in item:
        print(item['distinguishedName'])
        print(item['sAMAccountName'])

