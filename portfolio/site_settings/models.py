from django.db import models
from wagtail.admin.panels import MultiFieldPanel, FieldPanel
from wagtail.contrib.settings.models import BaseSetting, register_setting
from wagtail.fields import RichTextField


@register_setting
class SiteSettings(BaseSetting):
    author_name = models.CharField(max_length=128)
    copyright_text = RichTextField()

    panels = [
        FieldPanel("author_name"),
        FieldPanel("copyright_text"),
    ]


@register_setting
class GoogleAnalyticsSettings(BaseSetting):
    analytics_code = models.TextField(blank=True, null=True, help_text='Your analytics tracking code')

    panels = [
        FieldPanel('analytics_code'),
    ]


@register_setting
class SocialMediaSettings(BaseSetting):
    linkedin = models.URLField(blank=True, null=True)
    github = models.URLField(blank=True, null=True)
    instagram = models.URLField(blank=True, null=True)
    skype = models.CharField(max_length=255, blank=True, null=True, help_text='Please, enter your skype name.')

    panels = [
        MultiFieldPanel([
            FieldPanel('linkedin'),
            FieldPanel('github'),
            FieldPanel('skype'),
            FieldPanel('instagram'),
        ], heading="Social Media Settings"),
    ]
