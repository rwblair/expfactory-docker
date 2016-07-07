from django.conf.urls import patterns, url
from django.views.generic.base import TemplateView

from expdj import settings
from expdj.apps.experiments.api_views import BatteryAPIList
from expdj.apps.experiments.views import (
    experiments_view, edit_experiment_template, delete_experiment_template,
    add_experiment_template, save_experiment_template, view_experiment,
    preview_experiment, batteries_view, add_battery, edit_battery,
    view_battery, delete_battery, remove_experiment, add_experiment,
    edit_experiment, save_experiment, update_experiment_template,
    remove_condition, preview_battery, serve_battery, serve_battery_anon,
    generate_battery_user, sync, experiment_results_dashboard,
    battery_results_dashboard, dummy_battery ,modify_experiment, intro_battery,
    save_survey_template, add_survey_template, add_game_template,
    save_game_template, enable_cookie_view, change_experiment_order,
    serve_battery_gmail, subject_management
)

urlpatterns = patterns('',

    # Experiment Templates
    url(r'^experiments$', experiments_view, name="experiments"),
    url(r'^experiments/save$',save_experiment_template,name='save_experiment_template'),
    url(r'^experiments/add$',add_experiment_template,name='add_experiment_template'),
    url(r'^experiments/(?P<eid>.+?)/update$',update_experiment_template,name='update_experiment_template'),
    url(r'^experiments/(?P<eid>.+?)/edit$',edit_experiment_template,name='edit_experiment_template'),
    url(r'^experiments/(?P<eid>.+?)/$',view_experiment, name='experiment_details'),
    url(r'^experiments/(?P<eid>.+?)/delete$',delete_experiment_template,name='delete_experiment'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/(?P<eid>.+?)/remove$',remove_experiment,name='remove_experiment'),
    url(r'^experiments/(?P<eid>.+?)/preview$',preview_experiment,name='preview_experiment'),

    # Surveys
    url(r'^surveys/save$',save_survey_template,name='save_survey_template'),
    url(r'^surveys/add$',add_survey_template,name='add_survey_template'),

    # Games
    url(r'^games/save$',save_game_template,name='save_game_template'),
    url(r'^games/add$',add_game_template,name='add_game_template'),


    # Experiments in Batteries
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/add$',add_experiment,name='add_experiment'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/modify$',modify_experiment,name='modify_experiment'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/save$',save_experiment,name='save_experiment'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/(?P<eid>\d+|[A-Z]{8})/customize$',edit_experiment,name='edit_experiment'),
    #url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/results$',experiment_results_dashboard,name='experiment_results_dashboard'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/(?P<eid>\d+|[A-Z]{8})/view$',view_experiment, name='experiment_details'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/(?P<eid>\d+|[A-Z]{8})/order$',change_experiment_order, name='change_experiment_order'),
    url(r'^experiments/(?P<bid>\d+|[A-Z]{8})/(?P<eid>\d+|[A-Z]{8})/remove$',remove_experiment,name='remove_experiment'),
    url(r'^conditions/(?P<bid>\d+|[A-Z]{8})/(?P<eid>\d+|[A-Z]{8})/(?P<cid>\d+|[A-Z]{8})/remove$',remove_condition,name='remove_condition'),

    # Batteries
    url(r'^batteries/$', batteries_view, name="batteries"),
    url(r'^my-batteries/(?P<uid>\d+|[A-Z]{8})/$', batteries_view, name="batteries"),
    url(r'^batteries/new$',edit_battery,name='new_battery'),
    url(r'^batteries/add$',add_battery,name='add_battery'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/edit$',edit_battery,name='edit_battery'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/subjects$',subject_management,name='subject_management'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/user$',generate_battery_user,name='generate_battery_user'),
    #url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/results$',battery_results_dashboard,name='battery_results_dashboard'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/$',view_battery, name='battery_details'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/delete$',delete_battery,name='delete_battery'),

    # Deployment
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/preview$',preview_battery,name='preview_battery'), # intro preview without subid
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/dummy$',dummy_battery,name='dummy_battery'),       # running without subid
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/(?P<userid>\d+|[A-Za-z0-9-]{30,36})/serve$',intro_battery,name='intro_battery'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/(?P<userid>\d+|[A-Za-z0-9-]{30,36})/accept$',serve_battery,name='serve_battery'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/(?P<keyid>\d+|[A-Za-z0-9-]{32})/anon$',serve_battery_anon,name='serve_battery_anon'),
    url(r'^batteries/(?P<bid>\d+|[A-Z]{8})/serve/gmail$',serve_battery_gmail,name='serve_battery_gmail'),
    url(r'^local/(?P<rid>\d+|[A-Z]{8})/$',sync,name='local'),
    url(r'^local/$',sync,name='local'), # local sync of data
    url(r'^cookie/$',enable_cookie_view,name='enable_cookie_view'),

    #  API
    url(r'^api_/battery/$', BatteryAPIList.as_view(), name='battery_api_list'),
)

if settings.DEBUG:
    urlpatterns += patterns('',
        url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
            'document_root': settings.MEDIA_ROOT,
        }),
)
