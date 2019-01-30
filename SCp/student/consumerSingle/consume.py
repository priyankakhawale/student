import requests
class StudentREST:
    BASE_URI='http://localhost:8000/api/v1/'

    def geStudent(self,cid):
        response=requests.get(url=StudentREST.BASE_URI+str(cid))
        print(response.status_code)
        return response.json()

    def getAllStudent(self):
        response=requests.get(url=StudentREST.BASE_URI)
        print(response.status_code)
        print(response.json())
        return response.json()

    def addStudent(self,cust):
        response=requests.post(url=StudentREST.BASE_URI,json=cust)
        print(response.status_code)
        return response.json()

if __name__ == '__main__':
    s=StudentREST()
    s.getAllStudent()