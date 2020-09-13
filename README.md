# GIT HUB GENERIC SYNC PROCESS

1 on Windows, download and install Git 
2 in Directory ...., launch git bash and perform 'git init' 
If Windows Directory empty: 3 git clone https://github.com/geekbert/ARISRepositoryAPI.git (Cloning into existing directory only allowed if directory is empty) 
If Windows Directory not empty: git remote add origin https://.... 
4 git pull origin master (downloads git directory into existing directory even if not empty)
(NOTE: git pull origin master anyways always recommended if there were changes on origin master repository newer than local repo)  
5 git add * 
6 git commit -m 'message/reason/audit story' 
7 git push origin master  
8 git status 
9 NOTE: to view changes to file in github, go to file, then history - very cool
