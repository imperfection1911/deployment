# ansible плейбук для установки и обновления приложений в wildfly

## Установка.
1. Установить ansible
2. Скопировать sortbykey.py в /usr/lib/python2.7/site-packages/ansible/plugins/filter/sortbykey.py
3. Распаковать плейбук и каталоги в любой удобный каталог.

## Как пользоваться
### Каталоги
В каталоге jars хранятся сборки.
В каталоге templates jinja2 шаблоны конфигов apache
В каталоге vars переменные, необходимые для работы плейбука.
В корне сам плейбук и inventory файл.

### Переменные
Переменные располагаются в файлах в каталоге vars
jboss_path - абсолютный путь к jboss cli
standalone_path - абсолютный путь к standalone.xml
substitutes - словарь для заполнения substitute в конфиге apache.
modules - словарь модулей, контролируемых плейбуком. Имя модуля имеет значение, по нему осуществляется поиск приложения в wildfly.
У каждого модуля есть ключи
jar - имя файла сборки в jars
config - имя конфига apache в templates. Может отсутствовать.
priority - приоритет установки приложения. Приложения с повышеным приоритетом будут установлены первыми.

### Запуск
Например для стенда rel
ansible-playbook -i inventory_rel -e "var_file=rel_modules.yml" deploy.yml
где -i inventory_rel - путь к inventory для REL
-e "var_file=..." путь к файлу с переменными, актуальными для стенда.


