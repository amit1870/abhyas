## UPDATE PACKAGE

### SUBLIME
> "$ wget -qO - https://download.sublimetext.com/sublimehq-pub.gpg | gpg --dearmor | sudo tee /etc/apt/trusted.gpg.d/sublimehq-archive.gpg > /dev/null"
> "$ echo "deb https://download.sublimetext.com/ apt/stable/" | sudo tee /etc/apt/sources.list.d/sublime-text.list"
> $ sudo apt-get update
> $ sudo apt-get install sublime-text

### GENERATE SSH KEYS FOR GIT

> $ ssh-keygen -t ed25519 -C "amitxvf@gmail.com"
> $ cat ~/.ssh/id_ed25519.pub

### MYSQL
> $ systemctl status mysql.service

> $ sudo mysql

> CREATE USER 'dbu_amit'@'localhost' IDENTIFIED WITH mysql_native_password BY 'xxxxxxx';

> GRANT ALL PRIVILEGES ON *.* TO 'dbu_amit'@'localhost' WITH GRANT OPTION;

> FLUSH PRIVILEGES;

> $ mysql -u dbu_amit -p || RUN with password 'xxxx'


### PYTHONANYWHERE

> create virtual env on platform
> $ mkvirtualenv --python /usr/bin/python3.8 vrenv

> path where virtual env will be created
> /home/amitxvf/.virtualenvs/vrenv

> django admin template path
> /home/amitxvf/.virtualenvs/vrenv/lib/python3.8/site-packages/django/contrib/admin/templates

> activate and deactivate virtual env
> $ workon vrenv
> $ deactivate

> source code path
> /home/amitxvf/sitaram

> work dir
> /home/amitxvf

> static dir path
> /home/amitxvf/sitaram/accounts/static

> run migration command for database configuration if git clone/pull done as db.sqlite3 file will be changed.
> python manage.py makemigrations
> python manage.py migrate

> add below content in /var/www/amitxvf_pythonanywhere_com_wsgi.py

### GIT
> checkout a git repo with token
> git clone https://<token>@github.com/<user>/<repo>.git
> git clone https://ghp_b2VYWGWEwKQxAIOIOHe4ivNMsyWtsx0ZGaUY@github.com/amit1870/sitaram.git

### LEARN URLS

> https://www.youtube.com/watch?v=vbQ2bYHxxEA&ab_channel=SyalInfotainment || Git

> https://docs.python-guide.org/ || The Hitchhiker’s Guide to Python!

> https://www.pcloudy.com/blogs/how-to-automate-web-application-testing-with-python-and-selenium/ || Python Selenium Testing

> https://www.guru99.com/software-testing-introduction-importance.html

> https://www.maths.cam.ac.uk/computing/linux/unixinfo/perms || File permission Linux

> https://www.shellscript.sh/ || Shell Script Tutorial

> https://pytest-with-eric.com/ || pytest good tutorial

> https://methodpoet.com/unit-testing-advantages-and-disadvantages/ || testing application/knowledge

>  https://www.bplogix.com/blog/verification-vs-validation-in-software || verification/validation
