# TRUR1300-23
Code for the TRUR1300 Software Development Practices unit 2023-24

# Setting up VS-Code with git

1. From software centre install the `VS Code`
2. From software centre install the `Git` applications

3. Create a repository in GitHub. You should be able to find a `New` button somewhere on the repositories tab.
   1. Tick the `create readme` checkbox.
   2. Set `.gitignore` to `Python`
   3. Set license to GNU  General Public Licence to allow others to share and build on your work (not essential)

4. Copy the URL for the repository. Select the green `<> Code` button and the Local tab. It should be something like

    https://github.com/RichardMorris/FooBar.git

5. Run VS Code
   1. Maybe use the Backup and Sync settings option
  
6. Clone your repository
    1. Select the  Source control icon
    2. Press the clone repository button
    3. Paste in the repository URL
    4. Select a location to store your local copy of the repo. Probably best in the shared N: drive, or in OneDrive, I've created a folder called repos as a sub folder of My Documents.
    5. Press the button ot Open the repository
    6. Tick yes to Trust the author

![vc  code pic 1](https://github.com/RichardMorris/TRUR1300-23/assets/1228002/cac61640-993d-46f6-ad1a-b3e1dfcc7a0d)

6. Set your username and email address
    1. Open the bottom pannel Crtl-J
    2. Select the terminal
    3. Type two lines similar to
```
    git config user.name "Richard Morris"
    git config user.email "rich@singsurf.org"
```

This needs to be done on a per-project basis as we can't write the standard file on Truro computers.
At home you would use the `--global` option for both.

7. Make an edit to the Readme.md file.
    1. You may find the [Markdown Cheetsheet](https://www.markdownguide.org/basic-syntax) useful for this
    2. Ctrl-S to Save

8. Stage the changed file
    1. Open the Source control panel
    2. Click the + next to the Readme.md file
    3. It should then appear under staged changed
   
![Annotation 2023-11-21 115554](https://github.com/RichardMorris/TRUR1300-23/assets/1228002/547c117f-eb0f-4efc-9b35-efe4bc03fb67)

9. Commit the file to local repo
    1. Enter a short diecription of the changes (50 char max)
    2. Press 'Commit' to add the change to the local repo

10. Generate a 'Personal Access Token' -  These are like passwords but with finer grained access.
    1. Go to https://github.com/settings/tokens
    2. Generate a Personal Access Token with the repo scope. 
    3. Copy the generated token
   
11. Press `Sync Changes`
    1. It will ask for github credentials
    2. Select the Token tab and paste in the token
    3. It will ask if you want to sign into github - yes
    4. It will ask if you want to periodically run git fetch - select yes - this can save time with downloading changed repos but does not affect your current repo

12. You now done
    1. Got to the GitHub page to check the repo has been changed.
    2. Its a good idea to commit and sync regularly. Especially if you will be using multiple different machines
