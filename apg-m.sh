name=apg-m
mail=""
err_detection()
{
    if [ ! $? -eq 0 ];then
        err_message=` cat /sh/logs/${name}${date}.log |grep ERROR `
        if [ -z ${err_message} ];then
            err_message=` tail -1 /sh/logs/${name}${date}.log `
        fi  
        echo "执行失败！错误信息为： ${err_message}。"
        pkill tail
        exit
    fi  
}
if [ ! -e "/sh/logs/${name}${date}.log" ]; then
  touch "/sh/logs/${name}${date}.log"
fi
tail -f /sh/logs/${name}${date}.log &
exec &>>/sh/logs/${name}${date}.log
SVN_URL=https://192.168.1.11:443/svn/src/gold
SVN_PSWD=123456
SVN_USER=test1
SVN_LOCAL_URL=/tmp/${name}
rm -rf /tmp/${name}
svn --username $SVN_USER --password $SVN_PSWD checkout $SVN_URL $SVN_LOCAL_URL
err_detection
cd /tmp/${name}/gold-parent
mvn clean package -DskipTests -Ptest
err_detection
expect <<EOF
set timeout -1
spawn ssh m
expect "*#"
        send "systemctl stop tomcat\r"
        send "cd /data/tomcat/webapps\r"
        send "rm -rf *\r"
        send "scp 192.168.2.2:/tmp/apg-m/gold-managers/target/gold-managers.war .\r"
        send "systemctl start tomcat.service\r"
        send "systemctl status -l tomcat.service\r"     
    send "exit\r"
expect eof
EOF
pkill tail
echo "此邮件为系统自动发送，请勿回复，如有问题请联系运维人员，谢谢！" | mail -s "${environment} ${name} ${edition}部署完成！" ${mail}
