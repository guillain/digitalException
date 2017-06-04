VERSION="1.2.0"
USER='guillain'

add(){
  echo "add: ${1}, comment: ${2}"
  git add -f "${1}"
  git commit -m "${2}" "${1}"
}

add run "Shell run script"
add git.sh "Git comiter"
add README.md "Readme file"
add LICENSE "License file"
add requirements.txt "List of Python requirement"
add digitalException.wsgi "WSGI script"
add doc/scrum.md "Scrum follow up"
add doc/install.md "Doc for installation"
add doc/workflow.png "Picture related to the workflow"
add doc/chatbot.png "Picture related to the Cisco Spark chatbot"
add doc/button.png "Picture related to the bt.tn/Sigfox button"
add conf/settings.cfg.default "Default application setting file"
add conf/apache.conf.default "Default apache conf file"
add conf/apache-secure.conf.default "Default apache secure conf file"
add conf/mysql.sql "MySQL structure"
add digitalException/__init__.py "App init"
add digitalException/ciscoSpark.py "Main script"
add digitalException/pyCiscoSpark.py "Cisco Spark lib"
add digitalException/tools.py "Extra tools"

git commit -m "prepare for ${VERSION}"
git push

