from cloud_api import CoreApi


class CloudApi(CoreApi):
    """
    """
    def __init__(
            self,
            api_url='https://cloud.mongodb.com/api/public/v1.0',
            api_usr='',
            api_token=''
    ):
        """
        :param api_url:
        :param api_usr:
        :param api_token:
        """
        super(CloudApi, self).__init__(api_url, api_usr, api_token)
        self.logger.debug('use the cloud manager api structure')

    def get_group_by_agent_api_key(self, agent_api_key):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/groups/get-one-group-by-agent-api-key/

        :param agent_api_key:
        :return:
        """
        return self._get('/groups/byAgentApiKey/{}'.format(agent_api_key))

    def get_users_in_group(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/groups/get-all-users-in-one-group/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/users'.format(gid))

    def add_users_to_projects(self, gid, users):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/groups/add-users-to-one-group/

        :param gid:
        :param users:
        :return:
        """
        return self._post('/groups/{}/users'.format(gid), users)

    def change_project_name(self, gid, project):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/groups/change-one-group-name/

        :param gid:
        :param project:
        :return:
        """
        return self._patch('/groups/{}'.format(gid), project)

    def remove_user_from_project(self, gid, uid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/groups/remove-one-user-from-one-group/

        :param gid:
        :param uid:
        :return:
        """
        return self._delete('/groups/{}/users/{}'.format(gid, uid))

    def get_all_hosts(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/get-all-hosts-in-group/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/hosts'.format(gid))

    def get_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/get-one-host-by-id/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}'.format(gid, hid))

    def get_host_by_name(self, gid, name, port):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/get-one-host-by-hostname-port/

        :param gid:
        :param name:
        :param port:
        :return:
        """
        return self._get('/groups/{}/hosts/byName/{}:{}'.format(gid, name, port))

    def monitor_host(self, gid, host):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/create-one-host/

        :param gid:
        :param host:
        :return:
        """
        return self._post('/groups/{}/hosts'.format(gid), host)

    def update_monitoring_for_host(self, gid, hid, conf):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/update-one-host/

        :param gid:
        :param hid:
        :param conf:
        :return:
        """
        return self._patch('/groups/{}/hosts/{}'.format(gid, hid), conf)

    def stop_monitoring_on_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/hosts/delete-one-host/

        :param gid:
        :param hid:
        :return:
        """
        return self._delete('/groups/{}/hosts/{}'.format(gid, hid))

    def get_disks_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/disks-get-all/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/disks'.format(gid, hid))

    def get_disk_for_host(self, gid, hid, partition_name):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/disk-get-one/

        :param gid:
        :param hid:
        :param partition_name:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/disks/{}'.format(gid, hid, partition_name))

    def get_dbs_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/databases-get-all-on-host/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/databases'.format(gid, hid))

    def get_db_for_host(self, gid, hid, dbname):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/database-get-by-name/

        :param gid:
        :param hid:
        :param dbname:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/databases/{}'.format(gid, hid, dbname))

    def get_all_clusters(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/clusters/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/clusters'.format(gid))

    def get_cluster(self, gid, cid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/clusters/

        :param gid:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}'.format(gid, cid))

    def udate_cluster(self, gid, cid, cluster):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/clusters/

        The only property that you may modify is the clusterName

        :param gid:
        :param cid:
        :param cluster:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}'.format(gid, cid))

    def get_agents(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/agents-get-all/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/agents'.format(gid))

    def get_agent_by_type(self, gid, type):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/agents-get-by-type/

        :param gid:
        :param type:
        :return:
        """
        return self._get('/groups/{}/agents/{}'.format(gid, type))

    def create_agent_api_key(self, gid, desc):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/agentapikeys/create-one-agent-api-key/

        :param gid:
        :param desc:
        :return:
        """
        return self._post('/groups/{}/agentapikeys'.format(gid), desc)

    def get_api_keys(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/agentapikeys/get-all-agent-api-keys-for-project/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/agentapikeys'.format(gid))

    def remove_api_key(self, gid, kid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/agentapikeys/delete-one-agent-api-key/

        :param gid:
        :param kid:
        :return:
        """
        return self._delete('/groups/{}/agentapikeys/{}'.format(gid, kid))

    def host_measurements(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/measures/get-host-process-system-measurements/
        https://docs.cloudmanager.mongodb.com/reference/api/measures/get-measurement-types/
        https://docs.cloudmanager.mongodb.com/reference/api/measures/measurement-types/

        TODO: required query parameters
        TODO: combine 2 api's in one call as params are different

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/measurements'.format(gid, hid))

    def get_disk_measurements(self, gid, hid, partition_name):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/measures/get-disk-measurements/

        :param gid:
        :param hid:
        :param partition_name:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/disks/{}/measurements'.format(gid, hid, partition_name))

    def get_db_measurements(self, gid, hid, dbname):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/measures/get-database-measurements/

        :param gid:
        :param hid:
        :param dbname:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/databases/{}/measurements'.format(gid, hid, dbname))

    def get_maintenance_windows(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/maintenance-windows/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/maintenanceWindows'.format(gid))

    def get_maintenance_window(self, gid, mid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/maintenance-windows/

        :param gid:
        :param mid:
        :return:
        """
        return self._get('/groups/{}/maintenanceWindows/{}'.format(gid, mid))

    def create_maintenance_window(self, gid, maintenance_window):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/maintenance-windows/

        :param gid:
        :param maintenance_window:
        :return:
        """
        return self._post('/groups/{}/maintenanceWindows'.format(gid), maintenance_window)

    def update_maintenance_window(self, gid, mid, maintenance_window):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/maintenance-windows/

        :param gid:
        :param mid:
        :param maintenance_window:
        :return:
        """
        return self._patch('/groups/{}/maintenanceWindows/{}'.format(gid, mid), maintenance_window)

    def delete_maintenance_window(self, gid, mid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/maintenance-windows/

        :param gid:
        :param mid:
        :return:
        """
        return self._delete('/groups/{}/maintenanceWindows/{}'.format(gid, mid))

    def get_slow_queries_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/performance-advisor/get-slow-queries/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/performanceAdvisor/slowQueryLogs'.format(gid, hid))

    def get_suggested_indexes_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/performance-advisor/get-suggested-indexes/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/performanceAdvisor/suggestedIndexes'.format(gid, hid))

    def get_namespaces_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/performance-advisor/pa-namespaces-get-all/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/performanceAdvisor/namespaces'.format(gid, hid))

    def get_indexes_for_host(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/performance-advisor/pa-existing-indexes-get-all/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/performanceAdvisor/existingIndexes')

    def get_backup_configs(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/backup/get-all-backup-configs-for-group/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/backupConfigs'.format(gid))

    def get_backup_config(self, gid, bid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/backup/get-one-backup-config-by-cluster-id/

        :param gid:
        :param bid:
        :return:
        """
        return self._get('/groups/{}/backupConfigs/{}'.format(gid, bid))

    def update_backup_config(self, gid, bid, config):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/backup/update-backup-config/

        :param gid:
        :param bid:
        :param config:
        :return:
        """
        return self._patch('/groups/{}/backupConfigs/{}'.format(gid, bid), config)

    def get_snapshot_schedule(self, gid, cid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/backup/get-snapshot-schedule/

        :param gid:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/backupConfigs/{}/snapshotSchedule'.format(gid, cid))

    def update_snapshot_schedule(self, gid, cid, config):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/backup/update-one-snapshot-schedule-by-cluster-id/

        :param gid:
        :param cid:
        :param config:
        :return:
        """
        return self._patch('/groups/{}/backupConfigs/{}/snapshotSchedule'.format(gid, cid), config)

    def get_cluster_snapshots(self, gid, cid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/get-all-snapshots-for-one-cluster/

        :param gid:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/snapshots'.format(gid, cid))

    def get_cluster_snapshot(self, gid, cid, sid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/get-one-snapshot-for-one-cluster/

        :param gid:
        :param cid:
        :param sid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/snapshots/{}'.format(gid, cid, sid))

    def update_snapshot_expiry(self, gid, cid, sid, conf):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/change-expiry-for-one-snapshot/

        :param gid:
        :param cid:
        :param sid:
        :param conf:
        :return:
        """
        return self._patch('/groups/{}/clusters/{}/snapshots/{}'.format(gid, cid, sid), conf)

    def remove_snapshot_from_cluster(self, gid, cid, sid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/remove-one-snapshot-from-one-cluster/

        :param gid:
        :param cid:
        :param sid:
        :return:
        """
        return self._delete('/groups/{}/clusters/{}/snapshots/{}'.format(gid, cid, sid))

    def get_config_srv_snapshots(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/get-all-snapshots-for-config-server/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/snapshots'.format(gid, hid))

    def get_config_srv_snapshot(self, gid, cid, sid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/snapshots/get-one-snapshot-for-config-server/

        :param gid:
        :param cid:
        :param sid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/snapshots/{}'.format(gid, cid, sid))

    def get_cluster_checkpoints(self, gid, cid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/checkpoints/

        :param gid:
        :param cid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/checkpoints'.format(gid, cid))

    def get_cluster_checkpoint(self, gid, cid, chkptid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/checkpoints/

        :param gid:
        :param cid:
        :param chkptid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/checkpoints/{}'.format(gid, cid, chkptid))

    def get_config_srv_restore_jobs_sccc(self, gid, hid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/get-all-restore-jobs-for-one-sccc-config-server/

        :param gid:
        :param hid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/restoreJobs'.format(gid, hid))

    def get_config_srv_restore_job_sccc(self, gid, hid, jid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/get-one-single-restore-job-for-one-sccc-config-server/

        :param gid:
        :param hid:
        :param jid:
        :return:
        """
        return self._get('/groups/{}/hosts/{}/restoreJobs/{}'.format(gid, hid, jid))

    def create_config_srv_restore_job_sccc(self, gid, hid, conf):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/create-one-restore-job-for-one-sccc-config-server/

        :param gid:
        :param hid:
        :param jid:
        :param conf:
        :return:
        """
        return self._post('/groups/{}/hosts/{}/restoreJobs'.format(gid, hid), conf)

    def get_automation_config(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/automation-config/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/automationConfig'.format(gid))

    def update_automation_config(self, gid, conf):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/automation-config/

        :param gid:
        :param conf:
        :return:
        """
        return self._put('/groups/{}/automationConfig'.format(gid), conf)

    def update_monitoring_config(self, gid, conf):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/automation-config/

        :param gid:
        :param conf:
        :return:
        """
        return self._put('/groups/{}/automationConfig/monitoringAgentConfig'.format(gid), conf)

    def update_backup_config(self, gid, conf):
        """
        return self._put('/groups/{}/automationConfig'.format(gid), conf)

        :param gid:
        :param conf:
        :return:
        """
        return self._put('/groups/{}/automationConfig/backupAgentConfig'.format(gid), conf)

    def get_automation_status(self, gid):
        """
        https://docs.cloudmanager.mongodb.com/reference/api/automation-status/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/automationStatus'.format(gid))
