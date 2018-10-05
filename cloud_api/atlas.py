from cloud_api import CoreApi
'''
    TODO: need to populate all the APIs
    TODO: do we need generator objects for the base structures
'''


class WhiteListEntry(object):
    pass


class DatabaseUser(object):
    pass


class Organization(object):
    pass


class OrganizationUser(object):
    """
    TODO: is this really needed or is there a basic user we can create?
    """
    pass


class Group(object):
    """
    TODO: A project is a group ....
    """
    pass


class Invoice(object):
    pass


class AtlasApi(CoreApi):
    """
    TODO: look to include the request parameters
    TODO: - pageNum
    TODO: - itemsPerPage
    TODO: - pretty
    TODO: - envelope
    """
    def __init__(
            self,
            api_url='https://cloud.mongodb.com/api/atlas/v1.0',
            api_usr='',
            api_token=''
    ):
        """
        :param api_url:
        :param api_usr:
        :param api_token:
        """
        super(AtlasApi, self).__init__(api_url, api_usr, api_token)
        self.logger.debug('use the atlas api structure')

    def get_project_ip_whitelists(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-get-all/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/whitelist'.format(gid))

    def get_project_ip_whitelist(self, gid, wl_entry):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-get-one-entry/

        :param gid:
        :param wl_entry:
        :return:
        """
        return self._get('/groups/{}/whitelist/{}'.format(gid, wl_entry))

    def add_whitelist_entries(self, gid, wl_entries):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-add-one/

        :param gid:
        :param wl_entries:
        :return:
        """
        return self._post('/groups/{}/whitelist'.format(gid), wl_entries)

    def update_ip_whitelist_entries(self, gid, wl_entries):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-update-one/

        TODO: NOTICE we are using plural! there can be one but must always be an array even if one!
        TODO: Capture this is in the documentation!
        TODO: this is the same as adding! are the responses the same ....

        :param gid:
        :param wl_entries:
        :return:
        """
        return self._post('/groups/{}/whitelist'.format(gid), wl_entries)

    def delete_ip_whitelist_entry(self, gid, wl_entry):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-delete-one/

        :param gid:
        :param wl_entry:
        :return:
        """
        return self._delete('/groups/{}/whitelist/{}'.format(gid, wl_entry))

    def get_db_users(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-get-all-users/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/databaseUsers'.format(gid))

    def get_db_user(self, gid, user):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-get-single-user/

        :param gid:
        :param user:
        :return:
        """
        return self._get('/groups/{}/databaseUsers/admin/{}'.format(gid, user))

    def create_db_user(self, gid, user):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-create-a-user/

        :param gid:
        :param user:
        :return:
        """
        return self._post('/groups/{}/databaseUsers'.format(gid), user)

    def update_db_user(self, gid, username, user):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-update-a-user/

        :param gid:
        :param username:
        :param user:
        :return:
        """
        return self._patch('/groups/{}/databaseUsers/admin/{}'.format(gid, username), user)

    def delete_db_user(self, gid, user):
        """
        https://docs.atlas.mongodb.com/reference/api/database-users-delete-a-user/

        :param gid:
        :param user:
        :return:
        """
        return self._delete('groups/{}/databaseUsers/admin/{}'.format(gid, user))

    def get_clusters(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-all/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/clusters'.format(gid))

    def get_cluster(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-one/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}'.format(gid, c_name))

    def get_cluster_process_args(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-get-advanced-configuration-options/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/processArgs'.format(gid, c_name))

    def create_cluster(self, gid, cluster):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-create-one/

        :param gid:
        :param cluster:
        :return:
        """
        return self._post('/groups/{}/clusters'.format(gid), cluster)

    def modify_cluster(self, gid, c_name, cluster):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-modify-one/

        :param gid:
        :param c_name:
        :param cluster:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}'.format(gid, c_name), cluster)

    def modify_cluster_process_args(self, gid, c_name, cluster):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-modify-advanced-configuration-options/

        :param gid:
        :param c_name:
        :param cluster:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}/processArgs'.format(gid, c_name), cluster)

    def delete_cluster(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/clusters-delete-one/

        :param gid:
        :param c_name:
        :return:
        """
        return self._delete('/groups/{}/clusters{}'.format(gid, c_name))

    def get_global_cluster(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-retrieve-namespaces/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/globalWrites'.format(gid, c_name))

    def add_global_cluster_managed_namespace(self, gid, c_name, global_ns):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-add-namespace/

        :param gid:
        :param c_name:
        :param global_ns:
        :return:
        """
        return self._post(
            '/groups/{}/clusters/{}/globalWrites/managedNamespaces'.format(gid, c_name),
            global_ns
        )

    def delete_global_cluster_managed_namespace(self, gid, c_name, db, collection):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-delete-namespace/

        :param gid:
        :param c_name:
        :param db:
        :param collection:
        :return:
        """
        return self._delete(
            '/groups/{}/clusters/{}/globalWrites/managedNamespaces?db={}&collection={}'.format(
                gid,
                c_name,
                db,
                collection
            )
        )

    def add_global_cluster_zone_mappings(self, gid, c_name, zones):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-add-customzonemapping/

        :param gid:
        :param c_name:
        :param zones:
        :return:
        """
        return self._post('/groups/{}/clusters/{}/globalWrites/customZoneMapping'.format(gid, c_name), zones)

    def delete_global_cluster_zone_mapping(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/global-clusters-delete-customzonemappings/

        :param gid:
        :param c_name:
        :return:
        """
        return self._delete('/groups/{}/clusters/{}/globalWrites/customZoneMapping'.format(gid, c_name))

    def request_verification_group_ldap_config(self, gid, l_conf):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-request-verification/

        :param gid:
        :param l_conf:
        :return:
        """
        return self._post('/groups/{}/userSecurity/ldap/verify'.format(gid), l_conf)

    def status_of_group_ldap_verification(self, gid, rid):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-verification-status/

        :param gid:
        :param rid:
        :return:
        """
        return self._get('/groups/{}/userSecurity/ldap/verify/{}'.format(gid, rid))

    def save_group_ldap_config(self, gid, l_conf):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-save/

        :param gid:
        :param l_conf:
        :return:
        """
        return self._patch('/groups/{}/userSecurity'.format(gid), l_conf)

    def get_group_ldap_config(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-get-current/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/userSecurity'.format(gid))

    def delete_group_ldap_user_dn_mapping(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/ldaps-configuration-remove-usertodnmapping/

        :param gid:
        :return:
        """
        return self._delete('/groups/{}/userSecurity'.format(gid))

    def get_cluster_snapshots(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-get-all/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/snapshots'.format(gid, c_name))

    def get_cluster_snapshot(self, gid, c_name, sid):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-get-one/

        :param gid:
        :param c_name:
        :param sid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/snapshots/{}'.format(gid, c_name, sid))

    def change_cluster_snapshot_expiration(self, gid, c_name, sid, snapshot):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-change-expiration/

        :param gid:
        :param c_name:
        :param sid:
        :param snapshot:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}/snapshots/{}'.format(gid, c_name, sid), snapshot)

    def delete_cluster_snapshot(self, gid, c_name, sid):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshots-delete-one/

        :param gid:
        :param c_name:
        :param sid:
        :return:
        """
        return self._delete('/groups/{}/clusters/{}/snapshots/{}'.format(gid, c_name, sid))

    def get_cluster_snapshot_schedule(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshot-schedule-get/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/snapshotSchedule'.format(gid, c_name))

    def update_cluster_snapshot_schedule(self, gid, c_name, schedule):
        """
        https://docs.atlas.mongodb.com/reference/api/snapshot-schedule-patch/

        :param gid:
        :param c_name:
        :param schedule:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}/snapshotSchedule'.format(gid, c_name), schedule)

    def get_cluster_cp_snapshots(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-get-all/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backup/snapshots'.format(gid, c_name))

    def get_cluster_cp_snapshot(self, gid, c_name, sid):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-get-one/

        :param gid:
        :param c_name:
        :param sid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backup/snapshots/{}'.format(gid, c_name, sid))

    def delete_cluster_cp_snapshot(self, gid, c_name, sid):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-delete-one/

        :param gid:
        :param c_name:
        :param sid:
        :return:
        """
        return self._delete('/groups/{}/clusters/{}/backup/snapshots/{}'.format(gid, c_name, sid))

    def get_cluster_cp_snapshot_restore_jobs(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-get-all/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backup/restoreJobs'.format(gid, c_name))

    def get_cluster_cp_snapshot_restore_job(self, gid, c_name, jid):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-get-one/

        :param gid:
        :param c_name:
        :param jid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backup/restoreJobs/{}'.format(gid, c_name, jid))

    def create_cluster_cp_snapshot_restore_job(self, gid, c_name, restore_job):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-create-one/

        :param gid:
        :param c_name:
        :param restore_job:
        :return:
        """
        return self._post('/groups/{}/clusters/{}/backup/restoreJobs'.format(gid, c_name), restore_job)

    def cancel_cluster_cp_snapshot_restore_job(self, gid, c_name, jid):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-restore-jobs-delete-one/

        :param gid:
        :param c_name:
        :param jid:
        :return:
        """
        return self._delete('/groups/{}/clusters/{}/backup/restoreJobs/{}'.format(gid, c_name, jid))

    def get_cluster_cp_snapshot_schedule(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-schedule-get-all/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backup/schedule'.format(gid, c_name))

    def update_cluster_cp_snapshot_schedule(self, gid, c_name, schedule):
        """
        https://docs.atlas.mongodb.com/reference/api/cloud-provider-snapshot-schedule-modify-one/

        :param gid:
        :param c_name:
        :param schedule:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}/backup/schedule'.format(gid, c_name), schedule)

    def get_cluster_backup_checkpoints(self, gid, c_name):
        """
        https://docs.atlas.mongodb.com/reference/api/checkpoints-get-all/

        :param gid:
        :param c_name:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backupCheckpoints'.format(gid, c_name))

    def get_cluster_backup_checkpoint(self, gid, c_name, cid):
        """
        https://docs.atlas.mongodb.com/reference/api/checkpoints-get-one/

        :param gid:
        :param c_name:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/backupCheckpoints/{}'.format(gid, c_name, cid))

    def get_group_cloud_containers(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-containers-list/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/containers'.format(gid))

    def get_group_cloud_container(self, gid, cid):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-container/

        :param gid:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/containers/{}'.format(gid, cid))

    def create_group_cloud_container(self, gid, container):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-create-container/

        :param gid:
        :param container:
        :return:
        """
        return self._post('/groups/{}/containers'.format(gid), container)

    def update_group_cloud_container(self, gid, cid, container):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-update-container/

        :param gid:
        :param cid:
        :param container:
        :return:
        """
        return self._patch('/groups/{}/containers/{}'.format(gid, cid), container)

    def get_group_peer_conns(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-connections-list/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/peers'.format(gid))

    def get_group_peer_conn(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-get-connection/

        :param gid:
        :param pid:
        :return:
        """
        return self._get('/groups/{}/peers/{}'.format(gid, pid))

    def create_group_peer_conn(self, gid, peer):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-create-peering-connection/

        :param gid:
        :param peer:
        :return:
        """
        return self._post('/groups/{}/peers'.format(gid), peer)

    def update_group_peer_conn(self, gid, pid, peer):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-update-peering-connection/

        :param gid:
        :param pid:
        :param peer:
        :return:
        """
        return self._patch('/groups/{}/peers/{}'.format(gid, pid), peer)

    def delete_group_peer_conn(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/vpc-delete-peering-connection/

        :param gid:
        :param pid:
        :return:
        """
        return self._delete('/groups/{}/peers/{}'.format(gid, pid))

    def delete_user_api_key(self, uid, kid):
        """
        https://docs.atlas.mongodb.com/reference/api/delete-api-key/

        :param uid:
        :param kid:
        :return:
        """
        return self._delete('/users/{}/keys/{}'.format(uid, kid))

    def get_group_processes(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/processes-get-all/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/processes'.format(gid))

    def get_group_process(self, gid, host, port):
        """
        https://docs.atlas.mongodb.com/reference/api/processes-get-one/

        :param gid:
        :param host:
        :param port:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}'.format(gid, host, port))

    def get_group_process_measures(self, gid, host, port):
        """
        https://docs.atlas.mongodb.com/reference/api/process-measurements/

        :param gid:
        :param host:
        :param port:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}/measurements'.format(gid, host, port))

    def get_group_process_dbs(self, gid, host, port):
        """
        https://docs.atlas.mongodb.com/reference/api/process-databases/

        :param gid:
        :param host:
        :param port:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}/databases'.format(gid, host, port))

    def get_group_process_db_measures(self, gid, host, port, dbid):
        """
        https://docs.atlas.mongodb.com/reference/api/process-databases-measurements/

        :param gid:
        :param host:
        :param port:
        :param dbid:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}/databases/{}/measurements'.format(gid, host, port, dbid))

    def get_group_process_disks(self, gid, host, port):
        """
        https://docs.atlas.mongodb.com/reference/api/process-disks/

        :param gid:
        :param host:
        :param port:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}/disks'.format(gid, host, port))

    def get_group_process_disk_measures(self, gid, host, port, disk):
        """
        https://docs.atlas.mongodb.com/reference/api/process-disks-measurements/

        :param gid:
        :param host:
        :param port:
        :param disk:
        :return:
        """
        return self._get('/groups/{}/processes/{}:{}/disks/{}/measurements'.format(gid, host, port, disk))

    def get_group_host_log(self, gid, host, logname):
        """
        TODO: need to test downloading the file
        https://docs.atlas.mongodb.com/reference/api/logs/

        :param gid:
        :param host:
        :param logname:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/logs/{}'.format(gid, host, logname))

    def get_group_process_pa_namespaces(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-namespaces-get-all/

        :param gid:
        :param pid:
        :return:
        """
        return self._get('/groups/{}/processes/{}/performanceAdvisor/namespaces'.format(gid, pid))

    def get_group_process_pa_indexes(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-existing-indexes-get-all/

        :param gid:
        :param pid:
        :return:
        """
        return self._get('/groups/{}/processes/{}/performanceAdvisor/existingIndexes'.format(gid, pid))

    def get_group_process_pa_slow_queries(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-get-slow-query-logs/

        :param gid:
        :param pid:
        :return:
        """
        return self._get('/groups/{}/processes/{}/performanceAdvisor/slowQueryLogs'.format(gid, pid))

    def get_group_process_suggested_indexes(self, gid, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/pa-suggested-indexes-get-all/

        :param gid:
        :param pid:
        :return:
        """
        return self._get('/groups/{}/processes/{}/performanceAdvisor/suggestedIndexes'.format(gid, pid))

    def get_group_audit_log(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/auditing-get-auditLog/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/auditLog'.format(gid))

    def configure_group_audit_log(self, gid, audit):
        """
        https://docs.atlas.mongodb.com/reference/api/auditing-set-auditLog/

        :param gid:
        :param audit:
        :return:
        """
        return self._patch('/groups/{}/auditLog'.format(gid), audit)

    def get_group_enc_at_rest_config(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/get-configuration-encryptionatrest/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/encryptionAtRest'.format(gid))

    def configure_group_enc_at_rest(self, gid, enc_at_rest):
        """
        https://docs.atlas.mongodb.com/reference/api/enable-configure-encryptionatrest/

        :param gid:
        :param enc_at_rest:
        :return:
        """
        return self._patch('/groups/{}/encryptionAtRest'.format(gid), enc_at_rest)
