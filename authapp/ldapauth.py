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
# import testldap.settings as set

# def main1():
#     import ldap
#     con = ldap.initialize('ldaps://185.61.26.170:54732', bytes_mode=False)
#     ldap.set_option(ldap.OPT_X_TLS_REQUIRE_CERT, ldap.OPT_X_TLS_NEVER)
#     con.bind_s('igor', '123Test123')
#
#     results = con.search_s('cn=user,dc=demo1,dc=freeipa, dc=org', ldap.SCOPE_SUBTREE, "(cn=admin)")
#     print(results)
    # domain = "SAMBA.REDOS"
    # ldap_addr = "ldap://dc.samba.redos"
    # ldap_user = "administrator@SAMBA"
    # ldap_pass = "qqqwww12!"
    # # ad.simple_bind_s("administrator@SAMBA.REDOS", "qqqwww12!")
    # ad = ldap.initialize(ldap_addr)
    # print(ad , 'wew')
    # ldap.set_option(ldap.OPT_REFERRALS, 1)
    # ldap.set_option(ldap.OPT_PROTOCOL_VERSION, 3)
    # auth_tokens = ldap.sasl.gssapi()
    # ad.set_option(ldap.OPT_REFERRALS, 0)
    # ad.sasl_interactive_bind_s('', auth_tokens)
    # print(ad.whoami_s(), "dwdwdwdw")
    # # ad.simple_bind_s(ldap_user, ldap_pass)


#from ldap3 import Server, Connection,
from ldap3 import Server, Connection, Tls, SASL, KERBEROS, ALL
import ssl
from ldap3.core.exceptions import LDAPBindError

def main():



    #conn1 = Connection(server1, 'uid=administrator, dc=samba, dc=redos', password='qqqwww12!')

    tls = Tls(validate=ssl.CERT_NONE, version=ssl.PROTOCOL_TLSv1_2)
    server1 = Server('185.61.26.170:54732', get_info=ALL, tls=tls)
    print(server1)
    c = Connection(
        server1, authentication=SASL, sasl_mechanism=KERBEROS)

    c.bind()

    print(c.extend.standard.who_am_i())


    # conn1.bind()
    # print(conn1)
    # f = conn1.extend.standard.who_am_i()
    #print(f)

    server = Server('ipa.demo1.freeipa.org', use_ssl=True, get_info=ALL)
    print(server)
    conn = Connection(server, 'uid=admin, cn=users, cn=accounts, dc=demo1, dc=freeipa,dc=org', 'Secret123', auto_bind=True)


    f = conn.extend.standard.who_am_i()

    print(conn.extend.standard.who_am_i())
    return f


if __name__ == '__main__':
    main()
    # main1()
