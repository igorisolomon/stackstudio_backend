from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser, \
    BaseUserManager, PermissionsMixin
from django.utils.translation import gettext_lazy as _
from django.template.defaultfilters import slugify


class Company(models.Model):
    name = models.CharField(_("company name"), max_length=50, blank=True)
    logo = models.ImageField(
        _("logo"), upload_to="images", blank=True, null=True)
    podcast_title = models.CharField(
        _("podcast title"), max_length=250, blank=True)
    google_podcast = models.URLField(
        _("google podcast"), max_length=200, blank=True)
    about = models.TextField(_("about"), blank=True)
    about_html = models.TextField(_("about html"), blank=True, default='')
    apple_podcast = models.URLField(
        _("apple podcast"), max_length=200, blank=True)
    spotify_podcast = models.URLField(
        _("spotify podcast"), max_length=200, blank=True)
    featured_podcast = models.ManyToManyField("Podcast", blank=True)
    intro_title = models.CharField(_("intro title"), max_length=50, blank=True)
    intro_description = models.TextField(_("intro description"), blank=True)
    intro_description_html = models.TextField(
        _("intro description html"), blank=True, default='')

    class Meta:
        verbose_name = _("company")
        verbose_name_plural = _("companies")

    def __str__(self):
        return self.name


class Podcast(models.Model):

    published_date = models.DateTimeField(
        _("published date"), auto_now=False, auto_now_add=False)
    title = models.CharField(_("title"), max_length=50, blank=True)
    is_published = models.BooleanField(_("is published"), default=False)
    body_html = models.TextField(_("rich text"), blank=True)
    body = models.TextField(_("plain text"), blank=True)
    published_link = models.URLField(
        _("published link"), blank=True, max_length=200)
    created_at = models.DateTimeField(
        _("created at"), auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(
        _("modified at"), auto_now=True, auto_now_add=False)
    slug = models.SlugField(null=False, unique=True)

    class Meta:
        verbose_name = _("podcast")
        verbose_name_plural = _("podcasts")
        ordering = ("-modified_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Blog(models.Model):

    published_date = models.DateTimeField(
        _("published date"), auto_now=False, auto_now_add=False)
    title = models.CharField(_("title"), max_length=50, blank=False)
    is_published = models.BooleanField(_("is published"), default=False)
    body_html = models.TextField(_("rich text"), blank=True)
    body = models.TextField(_("plain text"), blank=True)
    created_at = models.DateTimeField(
        _("created at"), auto_now=False, auto_now_add=True)
    modified_at = models.DateTimeField(
        _("modified at"), auto_now=True, auto_now_add=False)
    slug = models.SlugField(null=False, blank=True, unique=True)

    class Meta:
        verbose_name = _("blog")
        verbose_name_plural = _("blogs")
        ordering = ("-modified_at",)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)
