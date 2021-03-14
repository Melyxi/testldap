# import getpass
# import ldb
# from samba.auth import system_session
# from samba.credentials import Credentials
# from samba.dcerpc import security
# from samba.dcerpc.security import dom_sid
# from samba.ndr import ndr_pack, ndr_unpack
# from samba.param import LoadParm
# from samba.samdb import SamDB
# def main():
#     lp = LoadParm()
#     creds = Credentials()
#     creds.guess(lp)
#     creds.set_username('administrator')
#     creds.set_password('qqqwww12!')
#     samdb = SamDB(url='ldap://10.10.10.101:389', session_info=system_session(),credentials=creds, lp=lp)
#
#     print(samdb)
#     query = "(|(objectclass=user)(objectclass=computer)(objectclass=group))"
#     result = samdb.search('DC=samba,DC=redos', expression=query, scope=ldb.SCOPE_SUBTREE)
#     for item in result:
#         if 'sAMAccountName' in item:
#             print(item['distinguishedName'])
#             print(item['sAMAccountName'])

import ldap
import testldap.settings as set

def main1():
    domain = "SAMBA.REDOS"
    ldap_addr = "ldap://dc.samba.redos"
    ldap_user = "administrator@SAMBA"
    ldap_pass = "qqqwww12!"
    # ad.simple_bind_s("administrator@SAMBA.REDOS", "qqqwww12!")
    ad = ldap.initialize(ldap_addr)
    print(ad , 'wew')
    ldap.set_option(ldap.OPT_REFERRALS, 1)
    ldap.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    auth_tokens = ldap.sasl.gssapi()
    ad.set_option(ldap.OPT_REFERRALS, 0)
    ad.sasl_interactive_bind_s('', auth_tokens)
    print(ad.whoami_s(), "dwdwdwdw")
    # ad.simple_bind_s(ldap_user, ldap_pass)


from ldap3 import Server, Connection, ALL


def main():
    server = Server('ipa.demo1.freeipa.org', use_ssl=True, get_info=ALL)
    conn = Connection(server, 'uid=markus, cn=users, cn=accounts,dc=demo1,dc=freeipa,dc=org', 'dsntuhf', auto_bind=True)

    f = conn.extend.standard.who_am_i()

    print(conn.extend.standard.who_am_i())
    return f


if __name__ == '__main__':
    main()
    main1()
