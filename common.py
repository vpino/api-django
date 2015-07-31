#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import deb822
import urllib
import urllib2
import re
import gzip

def list_items(path=None, dirs=True, files=True):
    """

    Lists items under a given path (non-recursive, unnormalized).

    :param path: a string containing a path.
    :param dirs: if False, no directories will be included in the result.
    :param files: if False, no files will be included in the result.
    :return: a list of items under the given path (non-recursive).
    :rtype: a list.

    """
    assert path
    assert type(path) == str
    return [f for f in os.listdir(path)
            if (os.path.isdir(os.path.join(path, f)) and dirs)
            or (os.path.isfile(os.path.join(path, f)) and files)]


def create_cache(repository_root, branch, cache_dir_path):
    """

    Creates the cache and all other necessary directories to organize the
    control files pulled from the repository.

    :param repository_root: url of the repository from which the control files
                            files will be pulled.
    :param cache_dir_path: path where the cache will be created.

    """

    if not os.path.isdir(cache_dir_path):
        os.makedirs(cache_dir_path)

    release_path = os.path.join(repository_root, 'dists', branch, 'Release')
    try:
        md5list = deb822.Release(urllib.urlopen(release_path)).get('MD5sum')
    except urllib2.URLError, e:
        pass
        #logger.warning('Could not read release file in %s, error code #%s' % (release_path, e.code))
    else:
        for control_file_data in md5list:
            if re.match('[\w]*-?[\w]*/binary-(i386|amd64)/Packages.gz$', control_file_data['name']):
                component, architecture, _ = control_file_data['name'].split('/')
                remote_file = os.path.join(repository_root, 'dists',
                                           branch, control_file_data['name'])
                local_name = '_'.join([branch, component,
                                       architecture.replace('binary-', '')])
                f = os.path.join(cache_dir_path, local_name + '.gz')

                if not os.path.isfile(f):
                    try:
                        urllib.urlretrieve(remote_file, f)
                    except urllib2.URLError, e:
                        pass
                        #logger.error('Could not get %s, error code #%s' % (remote_file, e.code))
                else:
                    if md5Checksum(f) != control_file_data['md5sum']:
                        os.remove(f)
                        try:
                            urllib.urlretrieve(remote_file, f)
                        except urllib2.URLError, e:
                            pass
                            #logger.error('Could not get %s, error code #%s' % (remote_file, e.code))

def get_deps(file):
    control_file = deb822.apt_pkg.TagFile(open(file))
    for section in control_file:
        if not section.has_key('Package'):
            next
        if section.has_key('Depends'):
            clean_deps = []
            for dep in section.get('Depends').split(","):
                clean_deps.append(dep.strip())
            return clean_deps


def check_deps(cache_dir_path, deps_list):
    control_files = list_items(cache_dir_path, False, True)
    for control_file in control_files:
        name, _ = control_file.split(".")
        branch, comp, _ = name.split("_")
        control_file_path = os.path.join(cache_dir_path, control_file)
        for paragraph in deb822.Packages.iter_paragraphs(gzip.open(control_file_path, 'r')):
            if paragraph.get('Package') in deps_list:
                deps_list.remove(paragraph.get('Package'))
            if paragraph.has_key('Provides'):
                for prov in paragraph.get('Provides').split(","):
                    if prov.strip() in deps_list:
                        deps_list.remove(prov.strip())

    if not deps_list:
        print "Las dependencias estan satisfechas"
    else:
        print deps_list

def main():

    cache_path = "/home/fran/cache"

    repo_url = 'http://10.16.106.224/debian'
    #repo_url = 'http://debian.cantv.net/debian'

    branch = 'jessie'

    create_cache(repo_url, branch, cache_path)

    depends = get_deps('control')

    check_deps(cache_path, depends)

main()