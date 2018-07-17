import requests
import xml.etree.ElementTree as ET


class QcRestApi:

    url = "https://almalmqc1250saastrial.saas.hpe.com/qcbin/"
    url_log = "https://login.software.microfocus.com/msg/actions/doLogin.action"
    login = "*****"
    password = "*****"
    cookies = dict()
    site_session = "rest/site-session"
    headers = {
        "Content-Type": "application/x-www-form-urlencoded",
        'Host': 'login.software.microfocus.com',
    }
    log_pas = 'username=' + login + '&' + 'password=' + password
    session = requests.session()

    def auth(self, log_pass):
        #Easy authoriyation
        print("Try to Sign in")
        r = self.session.post(self.url_log, data=log_pass, headers=self.headers)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            r = self.session.post(self.url + self.site_session, headers=self.headers)
            if 'QCSession' in r.cookies.get_dict():
                self.session.headers.update({'QCSession': r.cookies.get('QCSession')})
            else:
                return r.status_code
            if 'XSRF-TOKEN' in r.cookies.get_dict():
                self.session.headers.update({'XSRF-TOKEN': r.cookies.get('XSRF-TOKEN')})
            else:
                return r.status_code
            print("Sign in is successful")
            return r.status_code
        else:
            return r.status_code

    def closing_session(self):
        #Sign out
        print("Try to close a session")
        r = self.session.delete(self.url + self.site_session, headers=self.headers)
        if r.status_code == 200:
            print("Session is closed successful ")
            return r.status_code
        else:
            return r.status_code

    def extending_session(self):
        print("Try to extending a session")
        r = self.session.get(self.url + self.site_session, cookies=self.cookies, headers=self.headers)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            print("Extending successful")
            return r.status_code
        else:
            return r.status_code

    def get_enity(self):
        r = self.session.get(self.url + 'rest/domains/DEFAULT_371612180/projects/371612180_DEMO/defects/',
                             cookies=self.cookies, headers=self.headers)
        #what to do with xml?
