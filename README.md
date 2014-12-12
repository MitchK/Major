Major
=====

Major is a light-weight build lifecycle management tool and allows you to create a ```Majorfile```:

```
provision:
  docker:
    image: ubuntu
import:
  git:
    url: $$REPO_URL
    branch: $$BRANCH
dependencies:
  script:
    - pip install -r requirements.txt
test:
  script:
    - python runtests.py
deploy:
  script:
    - python deploy.py
notify:
  github-status:
    accessToken: $$GITHUB_ACCESS_TOKEN
```

Install Major:
```
export MAJOR_PATH=/opt/Major
mkdir $MAJOR_PATH
git clone https://github.com/MitchK/Major.git $MAJOR_PATH
echo "export MAJOR_PATH=$MAJOR_PATH" >> ~/.bash_profile (or .bashrc on Linux)
echo "export PATH=$MAJOR_PATH/bin:$PATH" >> ~/.bash_profile (or .bashrc on Linux)
chmod a+x $MAJOR_PATH/bin/major
source  ~/.bash_profile (or .bashrc on Linux)
major ping
```
