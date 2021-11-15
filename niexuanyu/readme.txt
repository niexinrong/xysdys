docker-compose run achievements django-admin.py startproject achievements ./achievements



django.db.utils.OperationalError: (1045, 'Plugin caching_sha2_password could not be loaded: /usr/lib/x86_64-linux-gnu/mariadb19/plugin/caching_sha2_password.so: cannot open shared object file: No such file or directory')


打开cmd：
mysql -uroot -p 

进入mysql依次执行下面语句

ALTER USER 'root'@'localhost' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER; #修改加密规则 

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root'; #修改密码加密策略 

flush privileges; #刷新权限

重置密码：
alter user 'root'@'localhost' identified by 'root';



 docker-compose build

docker-compose up
后台运行
docker-compose up -d
------------------------------------------------------------------------按以下来：----------------
第一步：-------------------------
docker-compose build
第二步：-------------------------
docker-compose up
第三步：-------------------------
从docker 进入数据库
mysql -uroot -p 

进入mysql依次执行下面语句

ALTER USER 'root'@'localhost' IDENTIFIED BY 'root' PASSWORD EXPIRE NEVER; #修改加密规则 

ALTER USER 'root'@'%' IDENTIFIED WITH mysql_native_password BY 'root'; #修改密码加密策略 

flush privileges; #刷新权限

alter user 'root'@'localhost' identified by 'root';#重置密码：

exit;#退出mysql
exit;#退出容器

第四步：-------------------------------
ctrl+c 停止服务
docker-compose up 
如果连不上数据库，多重复第四步。
或使用docker ,把WEB停一下，再重启WEB
-----------------------------------------------------------------------结束
docker tag com-dj3-mysql_achievements niexinrong/com-dj3-mysql:hlly-sucess-20211109
docker push niexinrong/com-dj3-mysql:hlly-sucess-20211109

