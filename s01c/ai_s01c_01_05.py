#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:35:12 (UT+08:00) daisuke>
#

# importing git module
import git

# main function
def main ():
    # URL of repository
    url_repo = 'https://github.com/astronexus/HYG-Database.git'

    # directory name of downloaded repository
    dir_repo = 'hyg'

    # downloading repository
    repo = git.Repo.clone_from (url_repo, dir_repo)

# execution of main function
if (__name__ == '__main__'):
    main ()
