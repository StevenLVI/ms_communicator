cd ../devops && docker-compose -f testing.yml down && docker-compose -f testing.yml up -d && cd ..
sleep 2
python manage.py test -v3