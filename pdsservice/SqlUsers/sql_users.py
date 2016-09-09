# -*- coding: utf-8 -*-
"""
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
#
# Author: Sunnepah

import logging
from pdsservice import settings

from common.util.remote import RemoteSql

rsql = RemoteSql(settings.VIRTUOSO_HOST)

log = logging.getLogger(__name__)


class VirtuosoSqlUsers():

    def __init__(self):
        pass

    def create_new_user(self, username):
        try:
            print "Entering create_new_user"
            password = 'secret'
            result = rsql.execute_virtuoso_sql("DB.DBA.USER_CREATE('" + username + "', '" + password + "')")
            if result:
                return True

            return False
        except Exception as e:
            print e.message

    def grant_user_permissions(self, username):
        select_perm = rsql.execute_virtuoso_sql('GRANT SPARQL_SELECT TO "' + username + '"')
        update_perm = rsql.execute_virtuoso_sql('GRANT SPARQL_UPDATE TO "' + username + '"')
        sponge_perm = rsql.execute_virtuoso_sql('GRANT SPARQL_SPONGE TO "' + username + '"')

        if select_perm and update_perm and sponge_perm:
            rsql.execute_virtuoso_sql("DB.DBA.RDF_DEFAULT_USER_PERMS_SET('" + username + "', 0)")
            return True

        return False

    def set_user_permission_on_personal_graph(self, graph, username):
        rsql.execute_virtuoso_sql("DB.DBA.RDF_GRAPH_USER_PERMS_SET('" + graph + "','" + username + "', " + str(3) + ")")

