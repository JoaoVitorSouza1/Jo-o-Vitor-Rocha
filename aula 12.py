import pyrebase



config = {

    "apiKey": "AIzaSyBqLBA8kfIKCjcv-h6lRHIMylQxBsStNBE",

    "authDomain": "clientes-28e4a.firebaseapp.com",

    "databaseURL": "https://clientes-28e4a.firebaseio.com",

    "storageBucket": "clientes-28e4a.appspot.com"

    }

    

firebase = pyrebase.initialize_app(config)