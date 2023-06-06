

# **Automatic code testing and server updating via Github Actions**

For this project, we've brought together three components: GitHub Actions, SSH, and Digital Ocean. GitHub Actions operates as our automatic checker, running tests each time we push new code to our repository. If the tests come back without issues, GitHub Actions moves forward, deploying the code to my new Digital Ocean server - which is a great discovery in itself.

SSH - which stands for Secure Shell - serves as our secure entry point to the Digital Ocean server. It provides a safe and remote login that allows us to execute commands on the server and ensure the smooth deployment of our updates.

Lastly, we have Digital Ocean, a highly scalable cloud infrastructure provider. It's the venue where our Flask application is hosted and managed. Through the interaction of these three components, we can efficiently update and maintain our application in the cloud, ensuring it stays up-to-date and ready for use.

**My challenges:**

- Getting familiar with ssh and Github access codes also took some time. I am now connecting to the digital ocean server with SSH. (The amount of people trying to access 'my’ server is shocking indeed. Since I would like to continue to use this server, I have set up a firewall since..)
- Pytesting - Ideally a Pytest would test the routing/output of the server once it runs, not just the code. I tried to set this up first within Github actions, but found out you cannot really approach a flask server running there. Therefore I came to this current mechanism, which is just testing if the code runs, and if the right requirements are there.
- It was tricky to get the right files and commands on the digital ocean server. This took 11 attempts, before we had the desired notice, indicating the new server [main.py](http://main.py) was updated and running: " Hello, world! = this is the updated version, once again. The code is tested and the flask server is updated." I had to make sure the git pull did not run in problems with file mergers etc, so I decided to deactivate the server first, delete main.py and to do a ‘git reset --hard origin/main’ to make sure the repo get’s pulled without interference.
- Here’s an indication of the YML script I used for the Github Actions (this setup does not need separate .sh files):

```
name: CI/CD Pipeline

on:
  push:
    branches: [ main ]

jobs:
  test:
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Setup Python
        uses: actions/setup-python@v2
        with:
          python-version: 3.8
      - name: Install Dependencies
        run: |
          python -m pip install --upgrade pip
          if [ -f requirements.txt ]; then pip install -r requirements.txt; fi
      - name: Run Tests
        run: pytest main.py

  deploy:
    needs: test
    runs-on: ubuntu-latest
    steps:
      - name: Checkout Code
        uses: actions/checkout@v2
      - name: Setup SSH
        uses: webfactory/ssh-agent@v0.5.0
        with:
          ssh-private-key: ${{ secrets.ZZZ }}
      - name: Deploy
        run: |
          ssh -o StrictHostKeyChecking=no ZZZ@ZZZ <<EOF
          systemctl stop myflaskapp
          cd ~/home/farm/workflow_test
          rm -f main.py
          git fetch --all
          git reset --hard origin/main
          systemctl start myflaskapp
          EOF
```
