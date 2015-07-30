import os
import deb822
import urllib
import urllib2
import re

def readconfig(filename, options=[], conffile=False, strip_comments=True):
    """

    Reads a file whether if is a data or configuration file and returns
    its content in a dictionary or a list.

    :param filename: path to the file.
    :param options: a list of aditional options.
    :param conffile: if True then the result will be a dictionary else the
                     result will be a list.
    :param strip_comments: if True then the comments in the file will be
                           deleted.
    :return: a Dictionary or a List.
    :rtype: ``dict`` ``list``

    .. versionadded:: 0.1

    """

    try:
        f = urllib.urlopen(filename) # No estoy seguro si esto sea una buena idea
    except:
        f = open(filename)

    if conffile:
        options = {}
    else:
        options = []

    for line in f:
        line = line.replace('\n', ' ')
        line = line.replace('\t', ' ')
        if '#' in line and strip_comments:
            line, comment = line.split('#', 1)
        if '=' in line and conffile:
            option, value = line.split('=', 1)
            options[option.strip()] = value.strip()
        elif line and not conffile:
            options.append(line.strip())

    f.close()
    return options


def create_cache(repository_root, cache_dir_path):
    """

    Creates the cache and all other necessary directories to organize the
    control files pulled from the repository.

    :param repository_root: url of the repository from which the control files
                            files will be pulled.
    :param cache_dir_path: path where the cache will be created.

    """

    if not os.path.isdir(cache_dir_path):
        os.makedirs(cache_dir_path)

    branches = (branch.split()
                for branch in readconfig(os.path.join('distributions')))
    
    for name, release_path in branches:
        release_path = os.path.join(repository_root, release_path)
        try:
            md5list = deb822.Release(urllib.urlopen(release_path)).get('MD5sum')
        except urllib2.URLError, e:
            logger.warning('Could not read release file in %s, error code #%s' % (release_path, e.code))
        else:
            for control_file_data in md5list:
                #if re.match('[\w]*-?[\w]*/[\w]*-[\w]*/Packages.gz$', control_file_data['name']):
                if re.match('[\w]*-?[\w]*/binary-(i386|amd64)/Packages.gz$', control_file_data['name']):
                    component, architecture, _ = control_file_data['name'].split('/')
                    remote_file = os.path.join(repository_root, 'dists',
                                               name, control_file_data['name'])
                    local_name = '_'.join([name, component,
                                           architecture.replace('binary-', '')])
                    f = os.path.join(cache_dir_path, local_name + '.gz')

                    if not os.path.isfile(f):
                        try:
                            urllib.urlretrieve(remote_file, f)
                        except urllib2.URLError, e:
                            logger.error('Could not get %s, error code #%s' % (remote_file, e.code))
                    else:
                        if md5Checksum(f) != control_file_data['md5sum']:
                            os.remove(f)
                            try:
                                urllib.urlretrieve(remote_file, f)
                            except urllib2.URLError, e:
                                logger.error('Could not get %s, error code #%s' % (remote_file, e.code))

def main():
    create_cache('http://10.16.106.224/debian', '/home/fran/cache')

main()