CREATE USER 'django_user'@'%' IDENTIFIED BY 'password';
GRANT ALL PRIVILEGES ON agendausm.* TO 'django_user'@'%';
GRANT SUPER ON *.* TO 'django_user'@'%';
GRANT SYSTEM_VARIABLES_ADMIN ON *.* TO 'django_user'@'%';
FLUSH PRIVILEGES;
