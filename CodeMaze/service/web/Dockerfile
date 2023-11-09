FROM php:7.2-apache

RUN && docker-php-ext-install mysqli && docker-php-ext-enable mysqli
COPY index.php /var/www/html/index.php
COPY flag_manager.php /var/www/html/flag_manager.php
RUN cd /usr/local/bin && curl -sS https://getcomposer.org/installer | php && cd /var/www && composer.phar require "twig/twig:1.19.0"
EXPOSE 80

CMD ["/usr/sbin/apache2ctl", "-D", "FOREGROUND"]