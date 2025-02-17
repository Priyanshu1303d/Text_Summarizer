import setuptools

with open("README.md", "r" , encoding="utf-8") as f:
    long_description = f.read()


__version__  = "0.0.0"

REPO_NAME = "Text_Summarizer"
AUTHOR_USER_NAME = "Priyanshu1303d"
AUTHOR_EMAIL = "Priyanshu1303d@gmail.com"
SRC_REPO = "textSummarizer"


setuptools.setup(
    name = REPO_NAME,
    version = __version__,
    author = AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description= "A small python project for nlp app",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url = f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}",
    project_urls ={
        "Bug Tracker" : f"https://github.com/{AUTHOR_USER_NAME}/{SRC_REPO}/issues",
    },
    package_dir={"": "src"},
    packages = setuptools.find_packages(where = "src") 

)