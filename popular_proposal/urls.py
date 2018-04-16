from django.conf.urls import url
from popular_proposal.views.proposal_views import (ProposalCreationView,
                                                   ThanksForProposingView,
                                                   SubscriptionView,
                                                   HomeView,
                                                   PopularProposalDetailView,
                                                   PopularProposalUpdateView,
                                                   UnlikeProposalView,
                                                   ProposalsPerArea,
                                                   CommitView,
                                                   NotCommitView,
                                                   CommitmentDetailView,
                                                   PopularProposalOGImageView,
                                                   PopularProposalDetailRedirectView,
                                                   PopularProposalAyuranosView,
                                                   )
from popular_proposal.views.wizard import (ProposalWizard,
                                           ProposalWizardFull,
                                           ProposalWizardFullWithoutArea,)
from django.views.decorators.clickjacking import xframe_options_exempt
from django.utils.translation import ugettext_lazy as _


urlpatterns = [
    url(r'^$',
        HomeView.as_view(),
        name='home'),
    url(r'^embedded/?$',
        xframe_options_exempt(HomeView.as_view(is_embedded=True)),
        name='embedded_home'),
    url(r'^area_embedded/(?P<slug>[-\w]+)/?$',
        xframe_options_exempt(ProposalsPerArea.as_view(is_embedded=True)),
        name='area_embedded'),
    url(r'^create_wizard/(?P<slug>[-\w]+)/?$',
        ProposalWizard.as_view(),
        name='propose_wizard'),
    url(r'^create_wizard_full/?$',
        ProposalWizardFull.as_view(),
        name='propose_wizard_full'),
    url(_(r'^crear/?$'),
        ProposalWizardFullWithoutArea.as_view(),
        name='propose_wizard_full_without_area'),
    url(r'^detail/(?P<slug>[-\w]+)/?$',
        xframe_options_exempt(PopularProposalDetailView.as_view()),
        name='detail'),
    url(_(r'^ayudanos/(?P<slug>[-\w]+)/?$'),
        PopularProposalAyuranosView.as_view(),
        name='ayuranos'),
    url(r'^d/(?P<pk>\d+)/?$',
        PopularProposalDetailRedirectView.as_view(),
        name='short_detail'),
    url(r'^og_image/(?P<slug>[-\w]+).jpg$',
        PopularProposalOGImageView.as_view(),
        name='og_image'),
    url(_(r'^commitment/(?P<candidate_slug>[-\w]+)/(?P<proposal_slug>[-\w]+)/?$'),
        CommitmentDetailView.as_view(),
        name='commitment'),
    url(_(r'^commit/(?P<candidate_pk>[-\w]+)/(?P<proposal_pk>\d+)/?$'),
        CommitView.as_view(),
        name='commit_yes'),
    url(_(r'^not_commit/(?P<candidate_pk>[-\w]+)/(?P<proposal_pk>\d+)/?$'),
        NotCommitView.as_view(),
        name='commit_no'),
    url(r'^embedded_detail/(?P<slug>[-\w]+)/?$',
        xframe_options_exempt(PopularProposalDetailView.as_view(is_embedded=True)),
        name='embedded_detail'),
    url(_(r'^unlike/(?P<pk>\d+)/?$'),
        UnlikeProposalView.as_view(),
        name='unlike_proposal'),
    url(_(r'^actualizar/(?P<slug>[-\w]+)/?$'),
        PopularProposalUpdateView.as_view(),
        name='citizen_update'),
    url(r'^(?P<slug>[-\w]+)/?$',
        ProposalCreationView.as_view(),
        name='propose'),
    url(_(r'^(?P<pk>[-\w]+)/gracias/?$'),
        ThanksForProposingView.as_view(),
        name='thanks'),
    url(_(r'^(?P<pk>[-\w]+)/subscribe/?$'),
        SubscriptionView.as_view(),
        name='like_a_proposal'),
]
