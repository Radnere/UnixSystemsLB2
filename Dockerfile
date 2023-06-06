FROM tomcat:11.0.0

ADD webSocket.war /user/local/tomcat/webapps/

EXPOSE 8080

ENTRYPOINT ["catalina.sh", "run"]