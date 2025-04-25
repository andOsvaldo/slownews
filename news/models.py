from django.db import models
from wagtail.models import Page
from wagtail.fields import RichTextField
from wagtail.admin.panels import FieldPanel
from wagtail.api import APIField
from wagtail.fields import StreamField
from wagtail.blocks import RichTextBlock
from wagtail.images.blocks import ImageChooserBlock


class ArticlePage(Page):
    body = RichTextField()
    audio_url = models.URLField(blank=True, null=True)

    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("audio_url"),
    ]

    api_fields = [
        APIField("body"),
        APIField("audio_url"),
    ]

class StreamPage(Page):
    body = StreamField([
        ('paragraph', RichTextBlock()),
        ('image', ImageChooserBlock()),
    ], use_json_field=True)
    audio_url = models.URLField(blank=True, null=True)
    
    content_panels = Page.content_panels + [
        FieldPanel("body"),
        FieldPanel("audio_url"),
    ]

    api_fields = [
        APIField("body"),
        APIField("audio_url"),
    ]