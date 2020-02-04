import requests
import base64
import yarl


class qtestmanager:
    def __init__(self, api_endpoint, username, password, api_end):
        self.api_endpoint = api_endpoint
        self.username = username
        self.password = password
        self.api_end = api_end


    def get_access_token(self):
        data = {'grant_type':"password",
              'username':self.username,
              'password':self.password,}
        url = yarl.URL(self.api_endpoint)
        post_domain = ((url.host).split('.')[0])
        domain = (str(post_domain)+':')
        request = requests.post(url = self.api_endpoint,data=data, headers={"Authorization" : "Basic "+(base64.b64encode(domain.encode()).decode())})
        access_token_data = request.text
        decode_access_token_data= ("%s"%access_token_data).lstrip("{").rstrip("}")
        access_token = decode_access_token_data.split(',')
        self.x = access_token[0].split(':')[1]

    def get_projects(self):
        request = requests.get(url = self.api_end,headers={"Authorization":"bearer "+self.x.strip('""')})
        print(request.text)

# qtest_username_get
# email_id
# password
# qtest_username_get
c=qtestmanager(qtest_username_post,email_id,password,qtest_username_get)
c.get_access_token()
c.get_projects()
