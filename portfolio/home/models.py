from django import forms
from django.db import models
from django.utils import timezone
from wagtail.contrib.forms.models import AbstractFormField, AbstractEmailForm
from wagtail.models import Orderable
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel, MultiFieldPanel, InlinePanel, PageChooserPanel, FieldRowPanel
from wagtail.images.edit_handlers import ImageChooserPanel
from wagtail.snippets.edit_handlers import SnippetChooserPanel
from wagtail.snippets.models import register_snippet
from modelcluster.fields import ParentalKey
from modelcluster.models import ClusterableModel
from colorfield.fields import ColorField


class HomePage(AbstractEmailForm):
    """
    HomePage model contains data for the main sections: Site Owner, About, Skills, Projects, and Contact Form.
    Inherited from AbstractEmailForm to be able to serve a Contact Form on the landing page instead of a separate page.
    """

    max_count = 1
    landing_page_template = "home/contact_page.html"

    full_name = models.CharField(max_length=64, null=True)
    professional_title = models.CharField(max_length=128, blank=True, null=True)
    photo = models.ForeignKey('wagtailimages.Image', null=True, on_delete=models.SET_NULL, related_name='+',
                              help_text="Please, upload a square photo (for example 300px x 300px).")
    about = RichTextField(blank=False, null=True)
    projects_note = RichTextField(blank=True, help_text="Short description of your projects.")
    thank_you_text = RichTextField(blank=False, null=True,
                                   help_text="Text that will be shown to the visitor after submitting the contact form")

    content_panels = AbstractEmailForm.content_panels + [
        MultiFieldPanel([
            FieldPanel('full_name'),
            FieldPanel('professional_title'),
            ImageChooserPanel('photo'),
        ], heading="Profile"),

        FieldPanel('about', classname="full"),

        InlinePanel('skills', label="Skills", min_num=1, max_num=30),

        MultiFieldPanel([
            FieldPanel('projects_note', classname="full"),
            InlinePanel('projects', label="Projects", min_num=1),
        ], heading="Projects"),

        MultiFieldPanel([
            InlinePanel('form_fields', label='Form Fields', heading="Form Fields"),
            FieldPanel('thank_you_text'),
            FieldRowPanel([
                FieldPanel('from_address', classname="col6"),
                FieldPanel('to_address', classname="col6"),
            ]),
            FieldPanel("subject"),
        ], heading="Contact Email Settings"),
    ]

    class Meta:
        verbose_name = "Home Page"
        verbose_name_plural = "Home Pages"


class Skill(Orderable):
    """Model stores libraries and frameworks that the user wants to showcase in the skills section."""

    page = ParentalKey('home.HomePage', related_name="skills")
    name = models.CharField(max_length=255)
    dev_icon = models.CharField(max_length=255, help_text="Name of a corresponding devicon icon.")

    class Meta(Orderable.Meta):
        unique_together = ('name', 'dev_icon')

    def __str__(self):
        return self.name


class Project(Orderable, ClusterableModel):
    """Model stores data about a project created by the user."""

    page = ParentalKey('home.HomePage', related_name="projects")
    title = models.CharField(max_length=64)
    description = RichTextField(blank=True, null=True)
    image = models.ForeignKey('wagtailimages.Image', on_delete=models.CASCADE, related_name="+",
                              help_text="Please, upload a landscape image (for example 900px x 650px).")
    url = models.URLField()
    finished_date = models.DateTimeField("Finished date")

    panels = [
        FieldPanel('title'),
        FieldPanel('description', classname="full"),
        ImageChooserPanel('image'),
        FieldPanel('url'),
        FieldPanel('finished_date'),
        InlinePanel('project_technologies', label="Project technologies", min_num=1, max_num=10),
    ]

    def clean(self):
        if self.finished_date > timezone.now():
            raise forms.ValidationError("Finished date cannot be in the future!")


class ProjectTechnologiesOrderable(Orderable):
    """"Model stores many-to-many relationships between Project and UsedTechnology"""

    project = ParentalKey('home.Project', on_delete=models.CASCADE, related_name="project_technologies")
    used_technology = models.ForeignKey('home.UsedTechnology', on_delete=models.CASCADE)

    panels = [
        SnippetChooserPanel('used_technology'),
    ]

    class Meta(Orderable.Meta):
        unique_together = ('project', 'used_technology')


@register_snippet
class UsedTechnology(models.Model):
    """Model stores libraries and frameworks that were used to create projects. Data will be shown as a colored badge"""

    name = models.CharField(max_length=255)
    color = ColorField(default='#FFFFFF')

    class Meta:
        unique_together = ('name', 'color')
        verbose_name = "Used project's technology"
        verbose_name_plural = "Used project's technologies"

    def __str__(self):
        return self.name


class FormField(AbstractFormField):
    page = ParentalKey('home.HomePage', on_delete=models.CASCADE, related_name='form_fields')
