import requests
def login(username,password):
    do = requests.post("http://devserver\\settings\\login.php",data={username:username,password:password}))
    return do

