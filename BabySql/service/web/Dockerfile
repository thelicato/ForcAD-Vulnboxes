FROM php:7.2-apache

RUN docker-php-ext-install mysqli && docker-php-ext-enable mysqli
COPY index.php /var/www/html/index.php
COPY flag_manager.php /var/www/html/flag_manager.php
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]