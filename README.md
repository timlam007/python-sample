# Sources with Dockerfile to assemble the docker image.
Python Sample App

Run the App Locally without docker

Step 1: Clone the code
git clone https://github.com/timlam007/python-sample

Step 2: Install dependencies
The application uses the psutil and Flask, Plotly, boto3 libraries. Install them using pip:
pip install -r requirements.txt

Step 3: Run the application
To run the application, navigate to the root directory of the project and execute the following command:
python helloworld.py

-------------------------------------------------------------------------------------------------------------------------------------
D:\projects\tekton\python-sample>git pull .

D:\projects\tekton\python-sample>notepad helloworld.py

D:\projects\tekton\python-sample>git status

D:\projects\tekton\python-sample>git add .

D:\projects\tekton\python-sample>git commit -m "Tim Changed"

 1 file changed, 1 insertion(+), 1 deletion(-)

D:\projects\tekton\python-sample>git push

To https://github.com/timlam007/python-sample
   cb61dc5..564c83d  master -> master


D:\projects\tekton\python-sample>docker build .


docker run -it -p 5000:5000 bfa7505009804f55fff0220749b0f12fdc00224d0137a8738f07014cf38f45e5
