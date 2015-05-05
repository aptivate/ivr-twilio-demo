from django.conf.urls import patterns, url

from .views import (
    say_words,
    gather,
    process_demo,
    LoopWithGather,
)

from .branching_demo import (
    gather_branch,
    gather_branch_a,
    gather_branch_b,
    process_branch,
    process_branch_a,
    process_branch_b,
)

urlpatterns = patterns('',
    url(r'^$', say_words, name='home'),
    url(r'^gather$', gather, name='gather'),
    url(r'^process_demo$', process_demo, name='process_demo'),
    url(r'^loop_gather$', LoopWithGather.as_view(), name='loop_gather'),

    url(r'^gather_branch$', gather_branch, name='gather_branch'),
    url(r'^gather_branch_a$', gather_branch_a, name='gather_branch_a'),
    url(r'^gather_branch_b$', gather_branch_b, name='gather_branch_b'),

    url(r'^process_branch$', process_branch, name='process_branch'),
    url(r'^process_branch_a$', process_branch_a, name='process_branch_a'),
    url(r'^process_branch_b$', process_branch_b, name='process_branch_b'),
)
