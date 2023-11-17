# TRUR1300-23
Code for the TRUR1300 Software Development Practices unit 2023-24

# Setting up VS-Code with git

1. From software centre install the `VS Code` and `Git` applications.

2. Create a repository in GitHub. You should be able to find a `New` button somewhere on the repositories tab. It will be easier if you tick the `create readme` checkbox. Set .gitignore to Python may help. 

3. Copy the URL for the repository. Select the green `<> Code` button and the Local tab. It should be something like

    https://github.com/RichardMorris/FooBar.git

4. Run VS Code

5. 

5. Set your username and email address

Open the terminal at the bottom and type two lines similar to 

    git config user.name "Richard Morris"
    git config user.email "rich@singsurf.org"

This needs to be done on a per-project basis as we can't write the standard file on Truro computers.
At home you would use the `--global` option for both.



In the Source control tab hover over the file you want to change, and press +, this stages the file ready to be committed.

Add a brief description of the change in source control.

Press the Commit button, this updates the local git repository. 

Press Sync Changes to send your changes upto github. 

It will ask for some check on cedentials. Well use a Personal Access Token with the repo scope. These are like passwords but with finer grained access.

Go to https://github.com/settings/tokens 

Generate a Personal Access Token with the repo scope. 




