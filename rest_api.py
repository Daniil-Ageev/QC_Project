import requests


class QcRestApi:

    url = "https://almalmqc1250saastrial.saas.hpe.com/qcbin/"
    url_log = "https://login.software.microfocus.com/msg/actions/doLogin.action"
    site_session = "rest/site-session"

    def __init__(self, login, password):
        self.input_auth = 'username=' + login + '&' + 'password=' + password
        self.__cookies = dict()
        self.__session = requests.session()
        self.__headers = {
            "Content-Type": "application/x-www-form-urlencoded",
            'Host': 'login.software.microfocus.com'
        }
        self.__domain = "DEFAULT_371612180"
        self.__project = "371612180_DEMO"

    def auth(self):
        print("Try to Sign in")
        r = self.__session.post(self.url_log, data=self.input_auth, headers=self.__headers)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.__session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            r = self.__session.post(self.url + self.site_session, headers=self.__headers)
            if 'QCSession' in r.cookies.get_dict():
                self.__session.headers.update({'QCSession': r.cookies.get('QCSession')})
            else:
                return r.status_code
            if 'XSRF-TOKEN' in r.cookies.get_dict():
                self.__session.headers.update({'XSRF-TOKEN': r.cookies.get('XSRF-TOKEN')})
            else:
                return r.status_code
            print("Sign in is successful")
            return r.status_code
        else:
            return r.status_code

    def closing_session(self):
        #Sign out
        print("Try to close a session")
        r = self.__session.delete(self.url + self.site_session, headers=self.__headers)
        if r.status_code == 200:
            print("Session is closed successful ")
            return r.status_code
        else:
            return r.status_code

    def extending_session(self):
        print("Try to extending a session")
        r = self.__session.get(self.url + self.site_session, cookies=self.__cookies, headers=self.__headers)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.__session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            print("Extending successful")
            return r.status_code
        else:
            return r.status_code

    def get_enity(self):
        r = self.__session.get(self.url + 'rest/domains/{0}/projects/{1}/defects/{2}'.
                               format(self.__domain, self.__project, "1"),
                               cookies=self.__cookies, headers=self.__headers)
        #what to do with xml?
