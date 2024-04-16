WARNING!!!

- Create an demo amazon Linux 2023 EC2 instance then First check the aws version

```bash
aws --version
```

- Write your credentials using this command
```bash
aws configure #cli kullanabilmek icin kendimizi aws e tanitmak icin
```

- or Assign a role with AdministratorFullAccess Policy. It is best practice to use IAM role rather than using AWS credentials

1. Create Security Group

```bash
aws ec2 create-security-group \
    --group-name aynur_roman_numbers_sec_grp\
    --description "This Sec Group is to allow ssh and http from anywhere"
```

- We can check the security Group with these commands
```bash # burda sec grubun bilgilerini getiriyoruz
aws ec2 describe-security-groups --group-names aynur_roman_numbers_sec_grp
```

2. Create Rules of security Group #kurallarini belirliyelim

```bash
aws ec2 authorize-security-group-ingress \
    --group-name aynur_roman_numbers_sec_grp \
    --protocol tcp \
    --port 22 \
    --cidr 0.0.0.0/0

aws ec2 authorize-security-group-ingress \
    --group-name aynur_roman_numbers_sec_grp \
    --protocol tcp \
    --port 80 \
    --cidr 0.0.0.0/0


```

3. After creating security Groups, We'll create our EC2 which has latest AMI id. to do this, we need to find out latest AMI with AWS system manager (ssm) command

- This command is to run querry to get latest AMI ID
```bash # guncel ami numarasini cekelim
aws ssm get-parameters --names /aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64 --query 'Parameters[0].[Value]' --output text
```

- We can assign this latest AMI id output to the LATEST_AMI environmental variable and use in our CLI command 

``` #guncel olani latest e atadik
(LATEST_AMI=xxxxxxxxxxxxxxxx)
```
- or we can directly fetch the last version via  using "resolve:ssm". We keep going with using "resolve:ssm" option. 

- in home directory of Ec2 create a userdata.sh file with following

```
touch userdata.sh
nano userdata.sh

#! /bin/bash
dnf update -y
dnf install python3 -y
dnf install python3-pip -y
pip3 install flask
dnf install git -y
FOLDER="https://raw.githubusercontent.com/Aynuur/aws-projects/master/projects/001-roman-numerals-converter/templates" #github tan index raw i al
cd /home/ec2-user
wget -P templates ${FOLDER}/index.html
wget -P templates ${FOLDER}/result.html
wget https://raw.githubusercontent.com/Aynuur/aws-projects/master/projects/001-roman-numerals-converter/roman-numerals-converter-app.py #app.py nin rawini al
python3 roman-numerals-converter-app.py
```
- As for the student who use his/her own local terminal, they need to show the absulete path of userdata.sh file

- Now we can run the instance with CLI command. (Do not forget to create userdata.sh under "/home/ec2-user/" folder before run this command)

```bash
aws ec2 run-instances --image-id ami-051f8a213df8bc089 --count 1 --instance-type t2.micro --key-name ottoaws9 --security-groups roman_numbers_sec_grp1 --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=roman_numbers}]' --user-data file:///Users/ODG/Desktop/git_dir/osvaldo-cw/porfolio_lesson_plan/week_6/CLI_solution/userdata.sh

or

aws ec2 run-instances \
    --image-id ami-051f8a213df8bc089 \
    --count 1 \
    --instance-type t2.micro \
    --key-name aynur-new-key \
    --security-groups aynur_roman_numbers_sec_grp \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=roman_numbers}]'\
    --user-data file:///home/ec2-user/userdata.sh
```
#eger instance olusursa public ip yi al bak uygulama calisiyor mu
- To see the each instances Ip we'll use describe instance CLI command
```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=roman_numbers"
```

- You can run the query to find Public IP and instance_id of instances:
```bash
aws ec2 describe-instances --filters "Name=tag:Name,Values=roman_numbers" --query 'Reservations[].Instances[].PublicIpAddress[]'
#insatance id i getirdi
aws ec2 describe-instances --filters "Name=tag:Name,Values=roman_numbers" --query 'Reservations[].Instances[].InstanceId[]'
```

- To delete instances
```bash 
aws ec2 terminate-instances --instance-ids #buraya yukarda gelen instance id yi yaz termnt et
aws ec2 terminate-instances --instance-ids <We have already learned this id with query on above>
```
- To delete security groups
```bash
aws ec2 delete-security-group --group-name aynur_roman_numbers_sec_grp1
```
