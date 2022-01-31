# Everyone committed this repository
Yes, everyone committed this repository.
# What is?
I got a lot of people to commit and make changes to this repository.
GIT was created for software versioning and GitHub is a platform that supports this versioning using GIT.
Within the GIT in a local repository, you can configure your username and e-mail in each of the commits, in order to control each change. (Go to your repository and a git log!)
So once these changes are pushed to GitHub, Github for some reason takes this email and username information and links it to valid platform users so I can get Linus Torvalds to commit to that repository (without him even having idea of who I am :/ ).
I dont belive it is a vulnerability, its just fun! and can be used for something bad.
# Exploitation
Within this exploration I used this feature of linking valid users and a way to get emails from users inside commits.
I made a python script to clone large repositories and extract valid usernames and emails, then it makes several local changes and finally pushes it to the repository.
The impact of this is to give credibility to repositories by having many important people or people "commit" to them.
I will report this issue to GitHub Team.
# GitHub response:
Because Git is a distributed version control system GitHub must use the commit email address to assign attribution. When you push a repository to GitHub.com it may contain one or more commits, some of which you may not have authored. For example, imagine a scenario where you collaborated with a number of people on a Git repository before you made your first push of that repo to GitHub.com. This push would contain a number of commits from several authors. It would be incorrect to assign all of the commits to the person doing the push, so we use the commit log email addresses to assign attribution on GitHub.com. Each subsequent push to GitHub uses this same logic to assign attribution of commit authors.
In order to verify that commits are made by a specific person, you may consider signing commits using a GPG key: https://help.github.com/articles/signing-commits-using-gpg/. Commit signatures can be used to show commits as verified on GitHub.com and can be used to verify the commits offline.
https://bounty.github.com/ineligible.html#impersonating_a_user_through_git_email_address
