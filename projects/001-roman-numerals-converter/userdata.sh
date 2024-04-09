touch userdata.sh
vim userdata.sh
#! /bin/bash
yum update -y
yum install python3 -y
yum install python3-pip -y
pip3 install flask
yum install git -y
FOLDER="https://raw.githubusercontent.com/okti3535/testproject001/main/001-roman-numerals-converter/templates"
cd /home/ec2-user
wget -P templates ${FOLDER}/index.html
wget -P templates ${FOLDER}/result.html
wget https://raw.githubusercontent.com/okti3535/testproject001/main/001-roman-numerals-converter/Instructor_Solution/CLI/userdata.sh
wget https://raw.githubusercontent.com/okti3535/testproject001/main/001-roman-numerals-converter/Instructor_Solution/app/roman-numerals-converter-app.py
python3 roman-numerals-converter-app.py