# ./init_remote_git.sh root@139.59.162.184 CAB prodserver
#
# Executes:
# ssh root@139.59.162.184 'git init CAB.git/;cd CAB.git;git config receive.denyCurrentBranch updateInstead'
# git remote add prodserver root@139.59.162.184:CAB.git
# git push prodserver master
# scp -r ssh root@139.59.162.184:CAB.git/

ssh $1 "git init $2.git/;cd $2.git/;git config receive.denyCurrentBranch updateInstead"
git remote add $3 $1:$2.git
git push $3 master
scp -r backend/.ssh-deploy-keys/ $1:$2.git/backend/.ssh-deploy-keys/
