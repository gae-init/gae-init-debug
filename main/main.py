# coding: utf-8

from gae_mini_profiler import profiler
from gae_mini_profiler import templatetags
import flask
import flask_debugtoolbar

import config
import util

app = flask.Flask(__name__)
app.config.from_object(config)
app.jinja_env.line_statement_prefix = '#'
app.jinja_env.line_comment_prefix = '##'
app.jinja_env.globals.update(
    check_form_fields=util.check_form_fields,
    is_iterable=util.is_iterable,
    slugify=util.slugify,
    update_query_argument=util.update_query_argument,
  )
toolbar = flask_debugtoolbar.DebugToolbarExtension(app)

import auth
import control
import model
import task

from api import helpers
api_v1 = helpers.Api(app, prefix='/api/v1')

import api.v1


if config.DEVELOPMENT:
  from werkzeug import debug
  app.wsgi_app = debug.DebuggedApplication(app.wsgi_app, evalex=True)
  app.testing = False


###############################################################################
# gae mini profiler
###############################################################################
@app.context_processor
def inject_profiler():
  return dict(profiler_includes=templatetags.profiler_includes())

app = profiler.ProfilerWSGIMiddleware(app)
