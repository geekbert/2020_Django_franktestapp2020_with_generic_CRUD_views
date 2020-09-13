# GIT HUB GENERIC SYNC PROCESS

1 on Windows, download and install Git 
2 in Directory ...., launch git bash and perform 'git init' 
SKIP: 3 git clone https://github.com/geekbert/ARISRepositoryAPI.git (Cloning into existing directory only allowed if directory is empty) 
3 BETTER: git remote add origin https://.... 
3 BETTER: git pull origin master (that way downloaded git directory into existing directory that is not empty)
NOTE: git pull origin master anyways always recommended if there were changes on origin master repository newer than local repo 4 git add ARIS_API.html (warning: LF replaced by CLRF) -> can fix by: git config core.autocrlf true 5 git commit -m 'message/reason/audit story' 6 git push origin master (fatal: origin does not appear to be git repo) 7 git remote add origin https://... 8 git push origin master (rejected: failed to push some refs to https://... 9 git pull origin master (works, but does not help) 10 git pull origin master --allow-unrelated-histories (-> this fixed it - appears to put README.md into same directory, as opposed to sub-folder 11 git push origin master (works now) 12 git status 13 NOTE: to view changes to file in github, go to file, then history - very cool
