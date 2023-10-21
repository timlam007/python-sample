# Sources with Dockerfile to assemble the docker image.
Python Sample App

git clone https://github.com/timlam007/python-sample

python helloworld.py


D:\projects\tekton\python-sample>git pull .

D:\projects\tekton\python-sample>notepad helloworld.py

D:\projects\tekton\python-sample>git status

D:\projects\tekton\python-sample>git add .

D:\projects\tekton\python-sample>git commit -m "Tim Changed"


[master 564c83d] Tim Changed
 1 file changed, 1 insertion(+), 1 deletion(-)

D:\projects\tekton\python-sample>git push
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 20 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (3/3), 300 bytes | 300.00 KiB/s, done.
Total 3 (delta 2), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (2/2), completed with 2 local objects.
To https://github.com/timlam007/python-sample
   cb61dc5..564c83d  master -> master


D:\projects\tekton\python-sample>docker build .


docker run -it -p 5000:5000 bfa7505009804f55fff0220749b0f12fdc00224d0137a8738f07014cf38f45e5
