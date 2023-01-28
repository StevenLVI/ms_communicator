cd ../devops && docker-compose -f localhost.yml down && docker-compose -f localhost.yml up -d
sleep 2
python ../manage.py makemigrations && python ../manage.py migrate
sleep 1
python ../manage.py runserver
