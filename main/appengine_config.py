import os
import sys
sys.path.insert(0, 'libx')

if os.environ.get('SERVER_SOFTWARE', '').startswith('Google App Engine'):
  sys.path.insert(0, 'lib.zip')
else:
  import re
  from google.appengine.tools.devappserver2.python import stubs
  re_ = stubs.FakeFile._skip_files.pattern.replace('|(?:^lib/.*)|', '|')
  re_ = re.compile(re_)
  stubs.FakeFile._skip_files = re_
  sys.path.insert(0, 'lib')


def gae_mini_profiler_should_profile_production():
  from google.appengine.api import users
  return users.is_current_user_admin()
