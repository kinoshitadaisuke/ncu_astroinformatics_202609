#!/usr/bin/env python3

#
# Time-stamp: <2026/09/15 08:46:39 (UT+08:00) daisuke>
#

# importing git module
import git

# main function
def main ():
    # URL of repository
    url_repo = 'https://github.com/astrocatalogs/sne-2010-2014.git'

    # directory name of downloaded repository
    dir_repo = 'osc_2010_2014'

    # downloading repository
    repo = git.Repo.clone_from (url_repo, dir_repo)

# execution of main function
if (__name__ == '__main__'):
    main ()
