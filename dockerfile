FROM tomcat:9

LABEL maintainer="hippo"

ADD ./target/my-app.war /usr/local/tomcat/webapps/

EXPOSE 8080

CMD ["catalina.sh", "run"]