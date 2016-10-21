'''
Created on 2016-10-20

@author: Martin Foo
'''

import getpass
from github import Github

def has_contributor(repo, login):
    for cont in repo.get_contributors():
        if cont.login == login:
            return True

    return False

if __name__ == '__main__':
    userId = raw_input("Input your github user: ")
    print 'user:', userId
    pswdStr = getpass.getpass("Password: ")
    print 'Got your password, pls waiting ...'

    # First create a Github instance:
    g = Github(userId, pswdStr)

    for star in g.get_user().get_starred():
        print star.full_name

    # Then play with your Github objects:
    for repo in g.get_user().get_repos():
        # print repo.fork
        if repo.fork == True:
            print repo #, repo.source == repo.parent
            if not has_contributor(repo, userId):
                print repo.full_name, repo.source
                # if repo.name in ['51-android', '010_template_for_android', 'aacplayer-android']:
                g.get_user().add_to_starred(repo.source)
                print repo.delete()
