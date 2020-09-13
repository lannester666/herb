#/bin/bash
cd realtime_images
python tcpImageServer.py &
jobs | echo
echo "1"
cd ..
python manage.py runserver 0.0.0.0:8080 &
jobs | echo
echo "2"
