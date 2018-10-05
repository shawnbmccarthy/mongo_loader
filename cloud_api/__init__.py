import requests
import logging
from requests.auth import HTTPDigestAuth
from cloud_api.errors import ApiError

_VERSION_MAJOR = 0
_VERSION_MINOR = 1
_VERSION_RELEASE = 'BEFORE_ALPHA'


class BaseApi:
    """

    """
    def __init__(self, api_url, api_usr, api_token):
        """

        :param api_url:
        :param api_usr:
        :param api_token:
        """
        self.logger = logging.getLogger(__name__)
        self.api_url = api_url
        self.api_usr = api_usr
        self.api_token = api_token
        self.logger.info('api client setup: %s' % self.api_url)

    def _get(self, resource, params=None):
        """
        :param resource:
        :param params:
        :return:
        """
        self.logger.debug('attempting to read(GET) resource: %s' % resource)
        response = requests.get(
            str('{}{}'.format(self.api_url, resource)),
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )

        self._validate_response(response, resource, 'GET')
        return response.json()

    def _patch(self, resource, data, params=None):
        response = requests.patch(
            '{}{}'.format(self.api_url, resource),
            json=data,
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'PATCH')
        return response.json()

    def _post(self, resource, data, params=None):
        """
        :param resource: resource to create
        :param data: json data structure
        :param params:
        :return:
        """
        self.logger.debug('attempting to create(POST) resource: %s' % resource)
        response = requests.post(
            str('{}{}'.format(self.api_url, resource)),
            json=data,
            params=params,
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'POST')
        return response.json()

    def _put(self, resource, data):
        pass

    def _delete(self, resource):
        self.logger.debug('attempting to delete(DELETE) resource: %s' % resource)
        response = requests.delete(
            str('{}{}'.format(self.api_url, resource)),
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, resource, 'DELETE')
        return response.json()

    def _validate_response(self, response, resource, method):
        """
        :param response:
        :return:
        """
        if response.status_code < 200 or response.status_code > 299:
            r = response.json()
            self.logger.error('api call(%s) failed for %s, status code: %d' % (method, resource, response.status_code))
            self.logger.error('reason:%s, detail:%s' % (r['reason'], r['detail']))
            raise ApiError('{}({}): {}'.format(r['reason'], response.status_code, r['detail']), response.status_code)
        self.logger.debug('valid response found')

    def get_from_link(self, link):
        """
        TODO: can we reduce this code to the _get! or vice versa _get builds a link!
        :param link:
        :return:
        """
        self.logger.debug('attempting to read for linked resource: %s' % link['href'])
        response = requests.get(
            link['href'],
            auth=HTTPDigestAuth(username=self.api_usr, password=self.api_token)
        )
        self._validate_response(response, link['href'], 'LINK')
        return response.json()


class CoreApi(BaseApi):
    """
    """
    def __init__(self, api_url, api_usr, api_token):
        super(CoreApi, self).__init__(api_url, api_usr, api_token)

    def get_api_info(self, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/root/
        https://docs.cloudmanager.mongodb.com/reference/api/root/

        :param kwargs: envelope & pretty
        :return:
        """
        return self._get('/', params=kwargs)

    def get_orgs(self, **kwargs):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-all/

        :return:
        """
        return self._get('/orgs', params=kwargs)

    def get_org(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-one/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-one/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}'.format(oid))

    def create_org(self, org):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-create-one/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-create-one/

        :param org:
        :return:
        """
        return self._post('/orgs', org)

    def rename_org(self, oid, org):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-rename/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-rename/

        The documentation shows POST in cloud documentation but the example has patch!

        :param oid:
        :param org:
        :return:
        """
        return self._patch('/orgs/{}'.format(oid), org)

    def delete_org(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-delete-one/

        :param oid:
        :return:
        """
        return self._delete('/orgs/{}'.format(oid))

    def get_org_groups(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all-projects/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-all-projects/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}/groups'.format(oid))

    def get_org_users(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-users-get-all-users/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-all-users/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}/users'.format(oid))

    def get_teams(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-get-all/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}/teams'.format(oid))

    def get_team(self, oid, tid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-one-by-id/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-get-one-by-id/

        :param oid:
        :param tid:
        :return:
        """
        return self._get('/orgs/{}/teams/{}'.format(oid, tid))

    def get_team_by_name(self, oid, t_name):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-one-by-name/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-get-one-by-name/

        :param oid:
        :param t_name:
        :return:
        """
        return self._get('/orgs/{}/teams/byName/{}'.format(oid, t_name))

    def get_users_of_team(self, oid, tid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-get-all-users/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-get-all-users/

        :param oid:
        :param tid:
        :return:
        """
        return self._get('/orgs/{}/teams/{}/users'.format(oid, tid))

    def create_team(self, oid, team):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-create-one/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-create-one/

        :param oid:
        :param team:
        :return:
        """
        return self._post('/orgs/{}/teams'.format(oid), team)

    def rename_team(self, oid, tid, team):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-rename-one/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-rename-one/

        :param oid:
        :param tid:
        :param team:
        :return:
        """
        return self._patch('/orgs/{}/teams/{}'.format(oid, tid), team)

    def add_users_to_team(self, oid, tid, users):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-add-user/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-add-user/

        :param oid:
        :param tid:
        :param users:
        :return:
        """
        return self._post('/orgs/{}/teams/{}/users'.format(oid, tid), users)

    def remove_user_from_team(self, oid, tid, uid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-remove-user/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-remove-user/

        :param oid:
        :param tid:
        :param uid:
        :return:
        """
        return self._delete('/orgs/{}/teams/{}/users/{}'.format(oid, tid, uid))

    def delete_team(self, oid, tid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-delete-one/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-delete-one/

        :param oid:
        :param tid:
        :return:
        """
        return self._delete('/orgs/{}/teams/{}'.format(oid, tid))

    def remove_team(self, oid, tid):
        """
        https://docs.atlas.mongodb.com/reference/api/teams-remove-from-project/
        https://docs.cloudmanager.mongodb.com/reference/api/teams/teams-remove-from-project/

        :param oid:
        :param tid:
        :return:
        """
        return self._delete('/groups/{}/teams/{}'.format(oid, tid))

    def get_projects(self):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/get-all-groups-for-current-user/

        groups & projects are synonymous terms

        :return:
        """
        return self._get('/groups')

    def get_project(self, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-one/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/get-one-group-by-id/

        groups & projects are synonymous terms

        :param pid:
        :return:
        """
        return self._get('/groups/{}'.format(pid))

    def get_project_by_name(self, p_name):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-one-by-name/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/get-one-group-by-name/

        :param p_name:
        :return:
        """
        return self._get('/groups/byName/{}'.format(p_name))

    def get_project_teams(self, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/project-get-teams/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/project-get-teams/

        :param pid:
        :return:
        """
        return self._get('/groups/{}/teams'.format(pid))

    def create_project(self, project):
        """
        https://docs.atlas.mongodb.com/reference/api/project-create-one/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/create-one-group/

        :param project:
        :return:
        """
        return self._post('/groups', project)

    def delete_project(self, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/project-delete-one/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/delete-one-group/

        :param pid:
        :return:
        """
        return self._delete('/groups/{}'.format(pid))

    def assign_teams_to_project(self, pid, teams):
        """
        https://docs.atlas.mongodb.com/reference/api/project-add-team/
        https://docs.cloudmanager.mongodb.com/reference/api/groups/project-add-team/

        :param pid:
        :param teams:
        :return:
        """
        return self._post('/groups/{}/teams'.format(pid), teams)

    def get_user_by_id(self, uid):
        """
        https://docs.atlas.mongodb.com/reference/api/user-get-by-id/
        https://docs.cloudmanager.mongodb.com/reference/api/user-get-by-id/

        :param uid:
        :return:
        """
        return self._get('/users/{}'.format(uid))

    def get_user_by_name(self, name):
        """
        https://docs.atlas.mongodb.com/reference/api/user-get-one-by-name/
        https://docs.cloudmanager.mongodb.com/reference/api/user-get-by-name/

        :param name:
        :return:
        """
        return self._get('/users/byName/{}'.format(name))

    def create_user(self, user):
        """
        https://docs.atlas.mongodb.com/reference/api/user-create/
        https://docs.cloudmanager.mongodb.com/reference/api/user-create/

        :param user:
        :return:
        """
        return self._post('/users', user)

    def update_user(self, uid, user):
        """
        https://docs.atlas.mongodb.com/reference/api/user-update/
        https://docs.cloudmanager.mongodb.com/reference/api/user-update/

        :param uid:
        :param user:
        :return:
        """
        return self._patch('/users/{}'.format(uid), user)

    def get_user_api_whitelists(self, uid):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-api/
        https://docs.cloudmanager.mongodb.com/reference/api/whitelist-get-for-current-user/

        :param uid:
        :return:
        """
        return self._get('/users/{}/whitelist'.format(uid))

    def get_user_api_whitelist(self, uid, addr):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-api/
        https://docs.cloudmanager.mongodb.com/reference/api/whitelist-get-for-ip-address/

        :param uid:
        :param addr:
        :return:
        """
        return self._get('/users/{}/whitelist/{}'.format(uid, addr))

    def add_user_api_whitelist(self, uid, addrs):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-api/
        https://docs.cloudmanager.mongodb.com/reference/api/whitelist-add-entries/

        :param uid:
        :param addrs:
        :return:
        """
        return self._post('/users/{}/whitelist'.format(uid), addrs)

    def delete_user_api_whitelist(self, uid, addr):
        """
        https://docs.atlas.mongodb.com/reference/api/whitelist-api/
        https://docs.cloudmanager.mongodb.com/reference/api/whitelist-delete-entry/

        :param uid:
        :param addr:
        :return:
        """
        return self._delete('/users/{}/whitelist/{}'.format(uid, addr))

    def get_user_api_keys(self, uid):
        """
        https://docs.atlas.mongodb.com/reference/api/api-key-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/api-key/api-key-get-all/

        :param uid:
        :return:
        """
        return self._get('/users/{}/keys'.format(uid))

    def create_user_api_key(self, uid, key):
        """
        https://docs.atlas.mongodb.com/reference/api/create-api-key/
        https://docs.cloudmanager.mongodb.com/reference/api/api-key/create-api-key/

        :param uid:
        :param key:
        :return:
        """
        return self._post('/users/{}/keys'.format(uid), key)

    def toggle_user_api_key(self, uid, kid, key):
        """
        https://docs.atlas.mongodb.com/reference/api/enable-disable-api-key/
        https://docs.cloudmanager.mongodb.com/reference/api/api-key/enable-disable-api-key/

        :param uid:
        :param kid:
        :param key:
        :return:
        """
        return self._patch('/users/{}/keys/{}'.format(uid, kid), key)

    def enable_user_api_key(self, uid, kid):
        return self.toggle_user_api_key(uid, kid, {'enabled': True})

    def disable_user_api_key(self, uid, kid):
        return self.toggle_user_api_key(uid, kid, {'enabled': False})

    def get_invoices(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-all-invoices/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-all-invoices/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}/invoices'.format(oid))

    def get_invoice(self, oid, iid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-one-invoice/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-one-invoice/

        :param oid:
        :param iid:
        :return:
        """
        return self._get('/org/{}/invoices/{}'.format(oid, iid))

    def get_pending_invoices(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/organization-get-pending-invoices/
        https://docs.cloudmanager.mongodb.com/reference/api/organizations/organization-get-pending-invoices/

        :param oid:
        :return:
        """
        return self._get('/org/{}/invoices/pending'.format(oid))

    def get_all_group_alerts(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-get-all-alerts/
        https://docs.cloudmanager.mongodb.com/reference/api/alerts-get-all-alerts/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/alerts'.format(gid))

    def get_group_alert(self, gid, aid):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-get-alert/
        https://docs.cloudmanager.mongodb.com/reference/api/alerts-get-alert/

        :param gid:
        :param aid:
        :return:
        """
        return self._get('/groups/{}/alerts/{}'.format(gid, aid))

    def ack_group_alert(self, gid, aid, ack):
        """
        https://docs.atlas.mongodb.com/reference/api/alerts-acknowledge-alert/

        :param gid:
        :param aid:
        :param ack:
        :return:
        """
        return self._patch('/groups/{}/alerts/{}'.format(gid, aid), ack)

    def get_group_alert_configs(self, gid):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-all-configs/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-get-all-configs/

        :param gid:
        :return:
        """
        return self._get('/groups/{}/alertConfigs'.format(gid))

    def create_group_alert_config(self, gid, alert_config):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-create-config/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-create-config/

        :param gid:
        :param alert_config:
        :return:
        """
        return self._post('/groups/{}/alertConfigs'.format(gid), alert_config)

    def get_group_alert_config(self, gid, aid):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-config/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-get-config/

        :param gid:
        :param aid:
        :return:
        """
        return self._get('/groups/{}/alertConfigs/{}'.format(gid, aid))

    def update_group_alert_config(self, gid, aid, alert_config):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-update-config/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-update-config/

        :param gid:
        :param aid:
        :param alert_config:
        :return:
        """
        return self._put('/groups/{}/alertConfigs/{}'.format(gid, aid), alert_config)

    def toggle_group_alert_config(self, gid, aid, toggle):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-enable-disable-config/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-enable-disable-config/

        :param gid:
        :param aid:
        :param toggle:
        :return:
        """
        return self._patch('/groups/{}/alertConfigs/{}'.format(gid, aid), toggle)

    def enable_group_alert_config(self, gid, aid):
        return self.toggle_group_alert_config(gid, aid, {'enabled': True})

    def disable_group_alert_config(self, gid, aid):
        return self.toggle_group_alert_config(gid, aid, {'enabled': False})

    def delete_group_alert_config(self, gid, aid):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-delete-config/
        https://docs.cloudmanager.mongodb.com/reference/api/alert-configurations-delete-config/

        :param gid:
        :param aid:
        :return:
        """
        return self._delete('/groups/{}/alertConfigs/{}'.format(gid, aid))

    def get_open_alerts_for_group_alert_config(self, gid, aid):
        """
        https://docs.atlas.mongodb.com/reference/api/alert-configurations-get-open-alerts/

        :param gid:
        :param aid:
        :return:
        """
        return self._get('/groups/{}/alertConfigs/{}/alerts'.format(gid, aid))

    def get_org_events(self, oid):
        """
        https://docs.atlas.mongodb.com/reference/api/events-orgs-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/events/get-all-events-for-org/

        :param oid:
        :return:
        """
        return self._get('/orgs/{}/events'.format(oid))

    def get_org_event(self, oid, eid):
        """
        https://docs.atlas.mongodb.com/reference/api/events-orgs-get-one/
        https://docs.cloudmanager.mongodb.com/reference/api/events/get-one-event-for-org/

        :param oid:
        :param eid:
        :return:
        """
        return self._get('/orgs/{}/events/{}'.format(oid, eid))

    def get_project_events(self, pid):
        """
        https://docs.atlas.mongodb.com/reference/api/events-projects-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/events/get-all-events-for-project/

        :param pid:
        :return:
        """
        return self._get('/groups/{}/events'.format(pid))

    def get_project_event(self, gid, eid):
        """
        https://docs.atlas.mongodb.com/reference/api/events-projects-get-one/
        https://docs.cloudmanager.mongodb.com/reference/api/events/get-one-event-for-project/

        :param pid:
        :param eid:
        :return:
        """
        return self._get('/groups/{}/events/{}'.format(gid, eid))

    def get_cluster_restore_jobs(self, gid, c_name, batch_id=''):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-get-all/
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/get-all-restore-jobs-for-one-cluster/

        :param gid:
        :param c_name:
        :param batch_id:
        :return:
        """
        req = '/groups/{}/clusters/{}/restoreJobs'.format(gid, c_name)

        if batch_id != '':
            req = '{}?batchId={}'.format(req, batch_id)

        return self._get(req)

    def get_cluster_restore_job(self, gid, c_name, jid):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-get-one/
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/get-one-single-restore-job-for-one-cluster/

        :param gid:
        :param c_name:
        :param jid:
        :return:
        """
        return self._get('/groups/{}/clusters/{}/restoreJobs/{}'.format(gid, c_name, jid))

    def create_cluster_restore_job(self, gid, c_name, job):
        """
        https://docs.atlas.mongodb.com/reference/api/restore-jobs-create-one/
        https://docs.cloudmanager.mongodb.com/reference/api/restorejobs/create-one-restore-job-for-one-cluster/

        :param gid:
        :param c_name:
        :param job:
        :return:
        """
        return self._post('/groups/{}/clusters/{}/restoreJobs'.format(gid, c_name), job)
