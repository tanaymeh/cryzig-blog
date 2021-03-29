# Cryzig Blog

Welcome to Cryzig! It's a simple blogging platform that I'm making while learning FastAPI. It's written in Pure Python 3.6 and it uses Barebones.css for front-end.

Just like all matters in life, it is a work-in-progress. Currently, I have made it use Local Persistent Storage, which means that any blog that I make using this platform will be stored in form of `.json` file in the `data/` folder.

I am, although thinking of changing this to mongodb or sqlalchemy in the future, but it is what it is for now.

If you like my project, please star it!

Also, here's a Screenshot of how it looks for the time being, since I haven't deployed it yet (it's not complete!).

![](ss.png)

# Trying it out

If you still want to run it, follow the below sequence:

* Install the dependencies by navigating to the project root and then running the below command in Terminal/CMD:

```shell
pip install -r requirements.txt
```

* After that's done, type the following piece of command in the same Terminal/CMD window:

```shell
uvicorn main:app --reload
```

Now you will see a lot of lines popping in (starting with Green colored words). If you see any errors, please open an issue repo.

* Now you should navigate to [127.0.0.1:8000](http://127.0.0.1:8000)

You should probably see the app running a front page similar to the screenshot above.

If you come across any errors or bugs, please open an issue.

I hope you found this app useful!
