### Thamara Project - Frontend

We have prepared the frontend part as a draft version, all pages are static html and they run under `flask` driven by `python`

For a full deployment, you need to follow the following steps:

- Download python from [this link](https://www.python.org/ftp/python/3.8.6/python-3.8.6-amd64.exe) then install it

- Remember to check the option for addind python executables to system PATH

- Download the script `get-pip.py` from [here](https://bootstrap.pypa.io/get-pip.py) `pip`

- Open command prompt and go to the directory you save the `get-pip.py` file

- run this command: `python get-pip.py`

> If your command prompt can't python as an executable command, then you need to add the path for example `C:\Python38` and the path `C:\Python38\Scripts` manually to the PATH in the environmental variables

- As `pip` command is installed, then run this `pip install flask`

> if your command prompt didn't recognize `pip` as an internal or external command, then you may need to re-install it again from the previous command

- Now everything is done!, you need to go to the Thamara project folder (after you cloned the repo) from the command prompt, then run the app `python server.py`

- The app is running locally and you can easily access it from browser following [this link](http://127.0.0.1/)

- You may add any fake `username` and `password`, then click on sign-in button

> - **NOTE:** if you want to integrate the `html` pages in your backend environment, you need to know that all pages are designed following inheritance, so we have a master template and each page extends (inherits) from the master (each page starts with a tag to inherits from master `{% extends 'base.html' %}`)
>  
> - So to get a full `html` page you need to replace the content enclosed by the tag (e.g. `{% block page_header %}`) with its reference in the master template, after replacing all tags you may save the corresponding file as a full html to be used by your backend code
> 
> - You can also change the style of the included tags to fit the style of tags of the backend structure you have, this way you save the inherited hierarchical structure.