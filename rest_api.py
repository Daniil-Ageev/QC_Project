import requests
import json


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
        self.domain = "DEFAULT_371612180"
        self.project = "371612180_DEMO"

    def sign_in(self):
        """Sign in function.

        Login and password from self.input_auth

        Returns:
            Status code from request.

        """

        print("Try to Sign in")
        r = self.__session.post(self.url_log, data=self.input_auth, headers=self.__headers)
        print(self.__session.cookies)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.__session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            print(self.__session.cookies)
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
        """Sign out function that close connection.

        Returns:
            Status code from request.
        
        """

        print("Try to close a session")
        r = self.__session.delete(self.url + self.site_session, headers=self.__headers)
        if r.status_code == 200:
            print("Session is closed successful ")
            return r.status_code
        else:
            return r.status_code

    def extending_session(self):
        """Extending connection function.

        Returns:
            Status code from request.

        """

        print("Try to extending a session")
        r = self.__session.get(self.url + self.site_session, cookies=self.__cookies, headers=self.__headers)
        if 'LWSSO_COOKIE_KEY' in r.cookies.get_dict():
            self.__session.headers.update({'LWSSO_COOKIE_KEY': r.cookies.get('LWSSO_COOKIE_KEY')})
            print("Extending successful")
            return r.status_code
        else:
            return r.status_code

    def get_entity(self):
        """Get entity from defects.

        Returns:
            Status code from request.

        """
        r = self.__session.get(self.url + 'rest/domains/{0}/projects/{1}/defects/{2}'
                               .format(self.domain, self.project, "1"),
                               cookies=self.__cookies, headers=self.__headers)
        print(r.content)
        return r.status_code

    def create_defect(self):
        js = """{
    "data": [
        {
            "type": "defect",
            "name": "Willoughby dissaffected with Marianne",
            "description": "Refuses to acknowledge her.",
            "priority": "4-Very High",
            "detected-by": "steves",
            "severity": "2-Medium",
            "creation-time": "20148-07-19"
        }
    ]
}
        """
        j = json.dumps([
        {
            "type": "defect",
            "name": "Willoughby dissaffected with Marianne",
            "description": "Refuses to acknowledge her.",
            "priority": "4-Very High",
            "detected-by": "steves",
            "severity": "2-Medium",
            "creation-time": "2018-07-19"
        }
    ])

        jso = {
            "Fields": [
            {
               "Name": "detected-by",
               "Value": "henry_tilney"
            },
            {
               "Name": "creation-time",
               "Value": "2010-03-02"
            },
            {
               "Name": "severity",
               "Value": "2-Medium"
            },
            {
               "Name": "name",
               "Value": "Returned value not does not match value in database."
            }]
        }

        self.__session.headers.update({'Content-Type': 'application/json'})
        self.__session.headers.update({'Accept': 'application/json'})

        r = self.__session.post(self.url + 'rest/domains/{0}/projects/{1}/defects'
                                .format(self.domain, self.project), data=json.dumps(jso))
        print(r.status_code)
        #print(r.text)

